/** @odoo-module **/

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { TextInputPopup } from "@point_of_sale/app/utils/input_popups/text_input_popup";
import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";

patch(PaymentScreen.prototype, {
    setup() {
        super.setup();
        this.popup = useService("popup");
        this.state = useState({
            code: false,
        });
    },

    get currentOrder() {
        return this.env.services.pos.get_order();
    },

    get currentFiscalTypeName() {
        return this.currentOrder && this.currentOrder.fiscal_type
            ? this.currentOrder.fiscal_type.name
            : _t('Select Fiscal Type');
    },

   async onClick() {
        const currentFiscalType = this.currentOrder.fiscal_type;
        const fiscalPosList = [];

        for (let fiscalPos of this.env.pos.fiscal_types) {
            if (fiscalPos.type !== 'out_invoice') continue;
            fiscalPosList.push({
                id: fiscalPos.id,
                label: fiscalPos.name,
                isSelected: currentFiscalType
                    ? fiscalPos.id === currentFiscalType.id
                    : false,
                item: fiscalPos,
            });
        }

        let { confirmed, payload: selectedFiscalType } = await this.popup.add(SelectionPopup, {
            title: _t("Select Fiscal Type"),
            list: fiscalPosList,
        });

        if (confirmed) {
            var partner = this.currentOrder.get_partner();

            if (selectedFiscalType.requires_document && (!partner || !partner.vat))
                await this.open_vat_popup();
            
            this.currentOrder.set_fiscal_type(selectedFiscalType);
        }
   },

   async open_vat_popup() {

        let { confirmed, payload: vat } = await this.popup.add(TextInputPopup, {
            startingValue: '',
            title: _t('You need to select a customer with RNC or Cedula for this fiscal type.'),
            placeholder: _t('RNC or Cedula'),
        });
        
        if (confirmed) {
            if (!(vat.length === 9 || vat.length === 11) || Number.isNaN(Number(vat))) {
                this.popup.add(ErrorPopup, {
                    title: _t("This not RNC or Cedula"),
                    body: _t(
                        "Please ensure the RNC has exactly 9 digits or the Cedula has 11 digits"
                    ),
                });

            } else {
                // TODO: in future try optimize search partners like get_partner_by_id
                
                var partner = this.env.pos.db.get_partners_sorted().find(partner_obj => partner_obj.vat === vat);

                if (partner) {

                    this.currentOrder.set_partner(partner);

                } else {
                    // TODO: in future create automatic partner
                    //FIXME: Terminar de migrar este codigo
                    const { confirmed, payload: newPartner } = await this.showTempScreen(
                        'PartnerListScreen',
                        { partner: this.currentOrder.get_partner()}
                    );
                    if (confirmed) {
                        this.currentOrder.set_partner(newPartner);
                        this.currentOrder.updatePricelist(newPartner);
                    }
                }
            } 
        }
    }

//    async _finalizeValidation() {
//         await super._finalizeValidation(...arguments);
//         await this.env.services.rpc("/web/dataset/call_kw/pos.payment/get_payment_reference", {
//             model: 'pos.payment',
//             method: 'get_payment_reference',
//             args: [[],order_list],
//             kwargs: {}
//         });
//    }
});
