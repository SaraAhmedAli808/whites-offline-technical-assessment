odoo.define('pos_refund_authorization.RefundPasswordButton', function (require) {
    'use strict';

    const TicketScreen = require('point_of_sale.TicketScreen');
    const Registries = require('point_of_sale.Registries');
    const rpc = require("web.rpc");

    const PosResTicketScreen = (TicketScreen) => class extends TicketScreen {
        async _onDoRefund() {
            let managers = await rpc.query({
                model: 'hr.employee',
                method: 'search_read',
                args: [[['pos_refund_password', '!=', false]], ['name', 'pos_refund_password']],
            });
            if (!managers.length) {
                this.showPopup('ErrorPopup', {
                    title: this.env._t('Refund Authorization Failed'),
                    body: this.env._t('No manager has set a refund password.'),
                });
                return;
            }

            const { confirmed, payload } = await this.showPopup('NumberPopup', {
                title: this.env._t('Manager Authorization'),
                body: this.env._t('Enter the manager\'s refund password'),
                confirmText: this.env._t('Confirm'),
                isPassword: true,
            });

            if (!confirmed) return;

            const isAuthorized = managers.some(manager => {
                console.log(`Checking manager ${manager.name} with password: ${manager.pos_refund_password}`);
                return manager.pos_refund_password === payload;
            });

            if (isAuthorized) {
                console.log("Authorization Successful!");
                super._onDoRefund();
            } else {
                console.log("Authorization Failed! Invalid password.");
                this.showPopup('ErrorPopup', {
                    title: this.env._t('Refund Denied'),
                    body: this.env._t('Invalid manager password.'),
                });
            }
        }
    };

    Registries.Component.extend(TicketScreen, PosResTicketScreen);
});
