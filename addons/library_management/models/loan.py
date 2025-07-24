from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'

    member_id = fields.Many2one('library.member', required=True)
    book_id = fields.Many2one('library.book', required=True)
    loan_date = fields.Date(default=fields.Date.today)
    returned = fields.Boolean(default=False)

    @api.constrains('member_id')
    def _check_max_loans(self):
        for record in self:
            count = self.search_count([('member_id', '=', record.member_id.id), ('returned', '=', False)])
            if count > 5:
                raise ValidationError('A member cannot have more than 5 active loans.')
