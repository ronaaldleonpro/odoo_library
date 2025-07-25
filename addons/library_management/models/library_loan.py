from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'

    member_id = fields.Many2one(
        'library.member',
        required=True,
        help="Select the member borrowing the book"
    )
    book_id = fields.Many2one(
        'library.book', 
        required=True,
        help="Select the book being borrowed"
    )
    loan_date = fields.Date(
        string='Loan Date',
        default=fields.Date.today,
        help="Use today's date as default"
    )
    returned = fields.Boolean(
        string='Returned',
        default=False,
        help="Check manually if the book has been returned"
    )

    @api.model
    def create(self, vals):
        member_id = vals.get('member_id')
        if member_id:
            active_loans = self.search_count([
                ('member_id', '=', member_id),
                ('returned', '=', False)
            ])
            if active_loans >= 5:
                raise ValidationError("This member already has 5 active loans.")
        return super(LibraryLoan, self).create(vals)

    @api.constrains('member_id')
    def _check_max_loans(self):
        for record in self:
            count = self.search_count([('member_id', '=', record.member_id.id), ('returned', '=', False)])
            if count > 5:
                raise ValidationError('A member cannot have more than 5 active loans.')
