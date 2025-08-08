/** @odoo-module */

import {Dialog} from "@web/core/dialog/dialog";
import { _t } from '@web/core/l10n/translation';
import { useChildRef, useOwnedDialogs, useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";
import {Component} from "@odoo/owl";
import {session} from "@web/session";
import {registry} from '@web/core/registry';

export class PreviewDialog extends Dialog {
    setup() {
        super.setup();
        let self = this;
        self.env.dialogData.close = () => this._cancel();
        self.modalRef = useChildRef();
        // 调整高度
        setTimeout(function ()  {
            var $dl = $('#' + self.id + ' .modal-dialog .modal-content');
            if ($dl)    {
                let h = $(document.body).height() - 120;
                if (h >= 300)
                    $dl.attr({"style": "height: " + h.toString() + 'px;'});
            }
        }, 800);
    }

    render() {
        super.render();
    }

    async _cancel() {
        this.disableButtons();
        if (this.props.cancel) {
            try {
                await this.props.cancel();
            } catch (e) {
                this.props.close();
                throw e;
            }
        }
        this.props.close();
    }

    disableButtons() {
        if (!this.modalRef.el) {
            return; // safety belt for stable versions
        }
        for (const button of [...this.modalRef.el.querySelectorAll(".modal-footer button")]) {
            button.disabled = true;
        }
    }
}

PreviewDialog.template = "app_report_direct_print.PreviewDialog";
PreviewDialog.components = {Dialog};
PreviewDialog.props = {
    close: Function,
    title: {
        validate: (m) => {
            return (
                typeof m === "string" || (typeof m === "object" && typeof m.toString === "function")
            );
        },
        optional: true,
    },
    url: String,
    size: {type: String, optional: true},
    confirm: {type: Function, optional: true},
    confirmLabel: {type: String, optional: true},
    cancel: {type: Function, optional: true},
    cancelLabel: {type: String, optional: true},
};
PreviewDialog.defaultProps = {
    confirmLabel: _t("Ok"),
    cancelLabel: _t("Cancel"),
    title: _t("Preview"),
};


function _getReportUrl(action, type) {
    let url = `/report/${type}/${action.report_name}`;
    const actionContext = action.context || {};
    if (action.data && JSON.stringify(action.data) !== "{}") {
        // build a query string with `action.data` (it's the place where reports
        // using a wizard to customize the output traditionally put their options)
        const options = encodeURIComponent(JSON.stringify(action.data));
        const context = encodeURIComponent(JSON.stringify(actionContext));
        url += `?options=${options}&context=${context}`;
    } else {
        if (actionContext.active_ids) {
            url += `/${actionContext.active_ids.join(",")}`;
        }
        if (type === "html") {
            const context = encodeURIComponent(JSON.stringify(env.services.user.context));
            url += `?context=${context}`;
        }
    }
    return url;
}

registry.category("ir.actions.report handlers").add("app_preview", async (action, options, env) => {
    //处理 report 的 hook
    let wkhtmltopdfStateProm;
    if (session.app_print_pdf_mode === 'preview' && action.report_type === 'qweb-pdf') {
        if (!wkhtmltopdfStateProm) {
            wkhtmltopdfStateProm = await rpc("/report/check_wkhtmltopdf");
        }
        const state = await wkhtmltopdfStateProm;
        if (state === "upgrade" || state === "ok") {
            // todo: 此处后续返回 preview，渲染弹出窗口
            var active_ids_path = '/' + action.context.active_ids.join(',');
            var url = _getReportUrl(action, 'pdf');

            var title = action.display_name;
            var printUrl = decodeURIComponent('/app_report_direct_print/static/lib/PDFjs/web/viewer.html?print_auto=1&file=' + url);
            if (session.app_print_auto) {
                window.open(printUrl, '_blank');
                return true;
            } else {
                //处理弹出窗口
                env.services.dialog.add(PreviewDialog, {
                    title: title,
                    size: 'lg',
                    url: url,
                });
                return true;
            }
            return false;
        } else
            return false;

    }
});
