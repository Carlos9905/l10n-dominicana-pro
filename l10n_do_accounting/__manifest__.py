{
    "name": "Fiscal Accounting (Rep. Dominicana)",
    "summary": """
        Este módulo implementa la administración y gestión de los números de
        comprobantes fiscales para el cumplimento de la norma 06-18 de la
        Dirección de Impuestos Internos en la República Dominicana.
    """,
    "author": "Marcos, Guavana, Indexa, Iterativo SRL, Neotec",
    "license": "LGPL-3",
    "website": "https://github.com/odoo-dominicana",
    "category": "Localization",
    "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "web",
        "account",
        "l10n_do",
    ],
    # always loaded
    "data": [
        "data/ir_config_parameters.xml",
        "data/ir_cron_data.xml",
        "data/account_fiscal_type_data.xml",

        "security/ir.model.access.csv",
        "security/res_groups.xml",

        "wizard/account_fiscal_sequence_validate_wizard_views.xml",
        "wizard/account_invoice_refund_views.xml",
        
        "views/account_move_views.xml",
        "views/account_journal_views.xml",
        "views/res_partner_views.xml",
        "views/account_fiscal_sequence_views.xml",
        'views/res_company_views.xml',
        'views/account_move_cancel_views.xml',
        "views/report_templates.xml",
        "views/report_invoice.xml",
        "views/layouts.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/res_partner_demo.xml",
        "demo/account_fiscal_sequence_demo.xml",
    ],
}
