# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


from odoo import fields, models, _


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    sh_display_name = fields.Char(
        string=' Display Name', related='display_name', readonly=True, store=True)
