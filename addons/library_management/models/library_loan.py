from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'
    _order = 'loan_date desc'

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
        help="Date when the book was borrowed. Default is today's date"
    )
    return_date = fields.Date(
        string='Return Date',
        help="Date when the book was returned"
    )
    returned = fields.Boolean(
        string='Returned',
        default=False,
        help="Indicates if the book has been returned"
    )
    returned_display = fields.Char(
        string='Return Status',
        compute='_compute_returned_display',
        store=True
    )
    book_available = fields.Boolean(
        related='book_id.available', 
        string="Book Available Status",
        store=True
    )

    @api.model
    def create(self, vals):
        book = self.env['library.book'].browse(vals.get('book_id'))
        member = self.env['library.member'].browse(vals.get('member_id'))
        
        # Book availability validation
        if not book.available:
            raise ValidationError('This book is already on loan and is not available.')
        
        # Loan limit validation
        if member:
            active_loans = self.search_count([
                ('member_id', '=', member.id),
                ('returned', '=', False)
            ])
            if active_loans >= 5:
                raise ValidationError("Member '%s' already has 5 active loans!" % member.name)
        
        # Create the loan
        loan = super().create(vals)
        # Update book availability
        book.write({'available': False})
        return loan

    def write(self, vals):
        # If marked as returned, update book and return date
        if 'returned' in vals and vals['returned']:
            vals['return_date'] = fields.Date.today()
            for loan in self:
                loan.book_id.write({'available': True})
        return super().write(vals)

    @api.constrains('member_id', 'returned')
    def _check_max_loans(self):
        for loan in self:
            if not loan.returned and loan.member_id:
                active_loans = self.search_count([
                    ('member_id', '=', loan.member_id.id),
                    ('returned', '=', False),
                    ('id', '!=', loan.id)
                ])
                if active_loans >= 5:
                    raise ValidationError("Member '%s' cannot have more than 5 active loans!" % member.name)

    @api.depends('returned')
    def _compute_returned_display(self):
        for loan in self:
            loan.returned_display = 'Returned' if loan.returned else 'On Loan'

    def action_return_book(self):
        self.ensure_one()
        if self.returned:
            raise ValidationError('Book "%s" has already been returned!' % self.book_id.title)
        
        self.write({
            'returned': True,
            'return_date': fields.Date.today()
        })
        self.book_id.write({'available': True})
        
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Book "%s" returned successfully!' % self.book_id.title,
                'type': 'rainbow_man',
            }
        }