# -*- coding: utf-8 -*-
{
    'name': "Vazirmatn Typography",

    'summary': """
         Vazirmatn Typography""",

    'description': """
        Add Vazirmatn font on website and web modules.
    """,

    'author': "odooers.ir",
    'website': "https://odooers.ir",
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    "assets":  {
        "web.report_assets_common": [
            "/oe_vazirmatn_typography/static/src/scss/report.scss",
            ("remove", "/web/static/fonts/fonts.scss"),
        ],
        'web._assets_primary_variables': [
            ('prepend', 'oe_vazirmatn_typography/static/src/scss/primary_variables.scss'),
            
        ],
        #"web._assets_helpers": [
        #    (
        #        "after",
        #        "web/static/src/legacy/scss/utils.scss",
        #        "/oe_vazirmatn_typography/static/src/scss/utils.scss",
        #    ),
        #],
        "web.assets_frontend" : [
            '/oe_vazirmatn_typography/static/src/scss/fonts.scss',
            '/oe_vazirmatn_typography/static/src/scss/general.scss',
           # (
            #    "replace",
            #    "/website/static/src/scss/website.scss",
            #    "/oe_vazirmatn_typography/static/src/scss/website.scss",
           # ),
        ],
        "web.assets_backend": [
            "/oe_vazirmatn_typography/static/src/scss/fonts.scss",
            "/oe_vazirmatn_typography/static/src/scss/web.scss",
        ],

        "web._assets_common_styles": [
            ("remove", "/web/static/fonts/fonts.scss"),
        ],
        "website.assets_wysiwyg": [
            (
                "replace",
                "/website/static/src/scss/website.wysiwyg.scss",
                "/oe_vazirmatn_typography/static/src/scss/website.wysiwyg.scss",
            ),
        ],
        "website.website_configurator_assets_scss": [
            (
                "replace",
                "/website/static/src/scss/website.wysiwyg.scss",
                "/oe_vazirmatn_typography/static/src/scss/website.wysiwyg.scss",
            ),
        ],        
    },
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
