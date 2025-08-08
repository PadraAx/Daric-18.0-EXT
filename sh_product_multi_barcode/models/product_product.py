# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.osv import expression


class ShProduct(models.Model):
    _inherit = 'product.product'

    barcode_line_ids = fields.One2many(
        'product.template.barcode', 'product_id', 'Barcode Lines', ondelete="cascade")

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if not name:
            return super().name_search(name, args, operator, limit)

        domain = args or []

        match_domain = [('barcode_line_ids', operator, name)]

        products = self.search_fetch(expression.AND([domain, match_domain]), [
                                     'display_name'], limit=limit)
        if not products:
            products = self.search_fetch(expression.AND(
                [domain, [('name', operator, name)]]), ['display_name'], limit=limit)
        if not products:
            products = self.search_fetch(expression.AND(
                [domain, [('default_code', '=', name)]]), ['display_name'], limit=limit)

        return [(product.id, product.display_name) for product in products.sudo()]

    @api.model
    def _search_display_name(self, operator, value):
        is_positive = operator not in expression.NEGATIVE_TERM_OPERATORS
        combine = expression.OR if is_positive else expression.AND
        domains = [
            [('name', operator, value)],
            [('default_code', operator, value)],
            [('barcode_line_ids', operator, value)],
        ]
        if operator in ('=', 'in') or (operator.endswith('like') and is_positive):
            barcode_values = [value] if operator != 'in' else value
            domains.append([('barcode', 'in', barcode_values)])
        if operator == '=' and isinstance(value, str) and (m := re.search(r'(\[(.*?)\])', value)):
            domains.append([('default_code', '=', m.group(2))])
        if partner_id := self.env.context.get('partner_id'):
            supplier_domain = [
                ('partner_id', '=', partner_id),
                '|',
                ('product_code', operator, value),
                ('product_name', operator, value),
            ]
            domains.append([('product_tmpl_id.seller_ids', 'any', supplier_domain)])
        return combine(domains)

    @api.constrains('barcode', 'barcode_line_ids')
    def check_uniqe_name(self):
        for rec in self:
            if self.env.company and self.env.company.sh_multi_barcode_unique:
                multi_barcode_id = self.env['product.template.barcode'].search(
                    [('name', '=', rec.barcode)])
                if multi_barcode_id:
                    raise ValidationError(_(
                        'Barcode must be unique!'))

    def _valid_field_parameter(self, field, name):
        return name in ['ondelete'] or super()._valid_field_parameter(field, name)
