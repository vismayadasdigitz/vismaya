from email.policy import default

from odoo import models,fields,api
from odoo.addons.test_convert.tests.test_env import field
from odoo.api import returns


class Salesorderinherit(models.Model):
    _inherit = "sale.order"


    payment_mode=fields.Char(string="payment_mode", readonly=True)
    is_paid=fields.Boolean(string="hu",default=False)

    def test(self):
        pass
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'test',
        #     'view_mode': 'sale.view_order_form',
        #     'res_model': 'sale.order',
        #
        # }
    def toggle_active(self):
        for record in self:
            record.is_paid=not record.is_paid


