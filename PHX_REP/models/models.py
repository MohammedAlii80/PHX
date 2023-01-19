from odoo import api, fields, models
from num2words import num2words





class accountbankstatement(models.Model):
    _inherit = 'account.bank.statement'

    text_amount = fields.Char(string="Amount in letters", required=False, compute="amount_to_text")
    state_st = fields.Selection(string="State", selection=[('receipt', 'Receipt'), ('send', 'Send'), ],required=True )
    sum_amount = fields.Integer(string="Sum Amout", required=False,compute='test_meth' )

    def test_meth(self):
        for rec in self:
            if rec.line_ids:
                for line in rec.line_ids:
                    rec.sum_amount += line.amount
            else:
                rec.sum_amount=0

    # @api.multi
    @api.depends('balance_end')
    def amount_to_text(self):
        for line in self:
            lang = self.env.user.lang
            print(lang)
            line.text_amount = num2words(abs(line.balance_end), lang='ar_001')
