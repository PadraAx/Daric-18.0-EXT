# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_print_pdf_mode = fields.Selection([
        ('preview', 'Preview then Print or Download'),
        ('download', 'Download(odoo Default)'),
    ], string="Print Mode", default='preview', config_parameter='app_print_pdf_mode')
    app_print_auto = fields.Boolean('Direct Print',
                                    config_parameter='app_print_auto',
                                    help="When enable, the report would auto print to default printer.")
