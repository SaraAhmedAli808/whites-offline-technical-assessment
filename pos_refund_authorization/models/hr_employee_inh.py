import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    pos_refund_password = fields.Char(
        string="POS Refund Password",
        help="Password required to authorize refunds in POS."
    )

    @api.onchange('pos_refund_password')
    def _onchange_numeric_password(self):
        if self.pos_refund_password and not re.match(r'^\d+$', self.pos_refund_password):
            raise UserError(_("The POS refund password must contain only numbers."))

    @api.model
    def validate_refund_password(self, password):
        manager = self.env.user.employee_id
        return manager and manager.pos_refund_password == password
