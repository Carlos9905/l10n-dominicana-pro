from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    l10n_do_tax_type = fields.Selection(
        selection=[
            ('itbis', 'ITBIS'),
            ('ritbis', 'ITBIS Withholding'),
            # TODO: investigate Subject to proportionality and ITBIS carried to cost
            #('prop', 'Subject to proportionality'),
            #('itbis_cost', 'ITBIS carried to cost'),
            ('isr', 'ISR Withholding'),
            ('isc', 'Selective Consumption Tax (SCT)'),
            ('other', 'Other taxes'),
            ('tip', 'Legal tip'),
            ('rext', 'Overseas payments (law 253-12)'),
            ('none', 'Non deductible')
        ],
        default="none",
        string="Tax DGII Type",
    )
    isr_retention_type = fields.Selection(
        selection=[
            ('01', 'Rentals'),
            ('02', 'Fees for Services'),
            ('03', 'Other Incomes'),
            ('04', 'Presumed Income'),
            ('05', 'Interest Paid to Legal Entities'),
            ('06', 'Interests Paid to Individuals'),
            ('07', 'Withholding by State Providers'),
            ('08', 'Mobile Games')
        ],
        string="ISR Withholding Type",
    )

    def _update_taxes_do(self):
        tax_data = [
            {"xml_id": "account.1_tax_18_sale", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_sale_incl", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_of_10", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_tip_sale", "l10n_do_tax_type": "tip", "tax_group_xml_id": "tax_group_tip"},
            {"xml_id": "account.1_ret_5_income_gov", "l10n_do_tax_type": "isr", "isr_retention_type": "07", "tax_group_xml_id": "group_isr"},
            {"xml_id": "account.1_tax_tip_purch", "l10n_do_tax_type": "tip", "tax_group_xml_id": "tax_group_tip"},
            {"xml_id": "account.1_tax_18_purch", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_purch_incl", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_16_purch", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_16_purch_incl", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_9_purch", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_9_purch_incl", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_8_purch", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_8_purch_incl", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_purch_serv", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_purch_serv_incl", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_10_total_mount", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_18_property_cost", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_ret_10_income_person", "l10n_do_tax_type": "isr", "isr_retention_type": "02", "tax_group_xml_id": "tax_group_retencion_10"},
            {"xml_id": "account.1_ret_100_tax_person", "l10n_do_tax_type": "ritbis", "tax_group_xml_id": "tax_group_retencion_18"},
            {"xml_id": "account.1_ret_100_tax_security", "l10n_do_tax_type": "ritbis", "tax_group_xml_id": "tax_group_retencion_18"},
            {"xml_id": "account.1_tax_18_serv_cost", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_ret_10_income_rent", "l10n_do_tax_type": "isr", "isr_retention_type": "01", "tax_group_xml_id": "tax_group_retencion_10"},
            {"xml_id": "account.1_ret_10_income_dividend", "l10n_do_tax_type": "isr", "isr_retention_type": "03", "tax_group_xml_id": "tax_group_retencion_10"},
            {"xml_id": "account.1_ret_2_income_person", "l10n_do_tax_type": "isr", "isr_retention_type": "03", "tax_group_xml_id": "tax_group_retencion_2"},
            {"xml_id": "account.1_ret_2_income_transfer", "l10n_do_tax_type": "isr", "isr_retention_type": "03", "tax_group_xml_id": "tax_group_retencion_2"},
            {"xml_id": "account.1_tax_18_importation", "l10n_do_tax_type": "itbis", "tax_group_xml_id": "tax_group_itbis_18"},
            {"xml_id": "account.1_tax_10_telco", "l10n_do_tax_type": "isc", "tax_group_xml_id": "tax_group_isc"},
            {"xml_id": "account.1_tax_2_telco", "l10n_do_tax_type": "other", "tax_group_xml_id": "group_tax"},
            {"xml_id": "account.1_tax_0015_bank", "l10n_do_tax_type": "other", "tax_group_xml_id": "tax_group_itbis_00015"},
            {"xml_id": "account.1_ret_100_tax_nonprofit", "l10n_do_tax_type": "ritbis", "tax_group_xml_id": "tax_group_retencion_18"},
            {"xml_id": "account.1_ret_30_tax_moral", "l10n_do_tax_type": "ritbis", "tax_group_xml_id": "tax_group_retencion_54"},
            {"xml_id": "account.1_ret_75_tax_nonformal", "l10n_do_tax_type": "ritbis", "tax_group_xml_id": "tax_group_ret"},
            {"xml_id": "account.1_ret_27_income_remittance", "l10n_do_tax_type": "isr", "isr_retention_type": "03", "tax_group_xml_id": "tax_group_retencion_27"},
        ]

        # Iterar y actualizar cada registro de impuestos
        for data in tax_data:
            tax_record = self.env.ref(data["xml_id"], raise_if_not_found=False)
            if tax_record:
                values = {
                    "l10n_do_tax_type": data.get("l10n_do_tax_type"),
                    "isr_retention_type": data.get("isr_retention_type"),
                    "tax_group_id": self.env.ref(data.get("tax_group_xml_id")).id if data.get("tax_group_xml_id") else None,
                }
                values = {k: v for k, v in values.items() if v is not None}
                tax_record.sudo().write(values)
