/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

class DgiiReportsUrlWidget extends Component {
    static props = { ...standardFieldProps };

    setup() {
        super.setup();
        this.action = useService("action");
    }

    async openDgiiReport(ev) {
        this.action.doAction({
            type: "ir.actions.act_url",
            url: "dgii_reports/" + this.props.value,
            target: "_blank",
        });
    }
}

DgiiReportsUrlWidget.template = "dgii_reports.DgiiReportsUrlWidget";
registry.category("fields").add("dgii_reports_url", {
    component: DgiiReportsUrlWidget,
});
