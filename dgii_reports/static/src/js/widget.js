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

// odoo.define('dgii_report.dgii_report_widget', function (require) {
//     "use strict";

//     var field_registry = require('web.field_registry');
//     var basic_fields = require('web.basic_fields');

//     var UrlDgiiReportsWidget = basic_fields.UrlWidget.extend({
//         _renderReadonly: function () {
//             this.$el.text(this.attrs.text || this.value)
//                 .addClass('o_form_uri o_text_overflow')
//                 .attr('target', '_blank')
//                 .attr('href', "dgii_reports/"+this.value);
//         },
//     });

//     field_registry.add('dgii_reports_url', UrlDgiiReportsWidget);

//     return {
//         UrlDgiiReportsWidget: UrlDgiiReportsWidget,
//     };

// });
