# Muk IT , muk_web_preview
# 山西清水欧度信息技术有限公司, Report Pdf Preview
# odooai.cn
# -*- coding: utf-8 -*-

# Created on 2019-09-02
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# Odoo13在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/13.0/zh_CN/index.html

# Odoo13在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/13.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    "name": "Report Direct Print and Preview. PoS direct print to local printer. Silent Print without Download",
    'version': '18.0.24.12.10',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'OPL-1',
    'sequence': 2,
    'price': 68.00,
    'currency': 'EUR',
    'images': ['static/description/banner.gif'],
    'depends': [
        'web',
        'base_setup',
    ],
    'summary': """
    Report direct print, pdf preview without download. Pdf direct print. html direct print Preview.
    POS auto print support. All odoo app like sale, purchase support.
    Notice!  Direct print only support chrome browser.
    """,
    'description': """
    Support Odoo 18,17,16, Enterprise and Community Edition
    1. odoo Report direct print to any local printer(usb,wifi,network,bluetooth).
    2. Install then use. Easy setup without 3rd Software. No need subscription like PrintNode or any Cloud service. No need for odoo iot box.
    3. Silent Print. Just 1 click to print in chrome or Windows edge browser. Kiosk Mode.
    4. Pos, point of sale support. All odoo report support like sale, purchase, stock.
    5. Easy setup for download or preview report before print.
    6. Multi-language Support.
    7. Multi-Company Support.
    8. Support Odoo 18,17,16,15,14,13,14,15,16. Enterprise and Community Edition
    ==========
    1. 直接报表打印，静默打印，打印至本地打印机。
    2. 即装即用。无需其它第三方软件支持。无需使用打印云服务（如PrintNode, Google Print)。
    3. 静默打印。在Chrome 及 Windows Edge浏览器中支持1键打印。
    4. 支持收银POS打印，支持所有odoo 报表打印。
    5. 可配置。支持配置下载打印或预览打印报表。
    6. 多语言支持
    7. 多公司支持
    8. Odoo 18,17,16,15,14,13,14,15,16支持。企业版，社区版，多版本支持
    """,
    'data': [
        # 'views/assets.xml',
        'views/res_config_settings_views.xml',
        'data/ir_config_parameter.xml',
    ],
    'assets': {
        'web.assets_qweb': [
        ],
        'web.assets_backend': [
            'app_report_direct_print/static/src/scss/preview_dialog.scss',
            'app_report_direct_print/static/src/scss/preview_content.scss',
            # 'app_report_direct_print/static/src/js/preview_handler.js',
            # 'app_report_direct_print/static/src/js/preview_generator.js',
            'app_report_direct_print/static/src/js/preview_dialog.js',
            # 'app_report_direct_print/static/src/js/web_pdf_preview.js',
            # 'app_report_direct_print/static/lib/printThis/printThis.js',
            'app_report_direct_print/static/src/xml/preview_dialog.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
