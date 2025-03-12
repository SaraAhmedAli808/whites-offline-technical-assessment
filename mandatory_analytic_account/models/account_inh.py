# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountAccount(models.Model):
    _inherit = "account.account"

    mandatory_analytic_account = fields.Boolean(string="Require Analytic Account")
    mandatory_partner = fields.Boolean(string="Require Partner")
    bypass_users_ids = fields.Many2many(
        "res.users", string="Bypass Users",
        help="Users who can bypass mandatory validation checks."
    )

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        """ Override the post method to check validation before posting """
        for move in self:
            for line in move.line_ids:
                account = line.account_id

                # Skip validation if the user is in the bypass list
                if self.env.user in account.bypass_users_ids:
                    continue

                # Validate Analytic Account requirement
                if account.mandatory_analytic_account and not line.analytic_account_id:
                    raise ValidationError(_("An analytic account is required for the account '%s'." % account.name))

                # Validate Partner requirement
                if account.mandatory_partner and not line.partner_id:
                    raise ValidationError(_("A partner is required for the account '%s'." % account.name))

        return super(AccountMove, self).action_post()