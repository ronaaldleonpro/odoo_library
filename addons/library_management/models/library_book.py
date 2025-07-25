from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import re

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    isbn = fields.Char(
        string='ISBN',
        required=True,
        size=17,
        help="Format: 978-XXXXX-X-XXX-X (13 digits)"
    )
    title = fields.Char(
        string='Title',
        required=True,
        help="Title of the book")
    author = fields.Char(
        string='Author',
        required=True,
        help="Author's name"
    )
    publication_date = fields.Date(
        string='Years Since Publication',
        required=True,
        help="Select any date. Only gets the year." 
        
    )
    years_since_publication = fields.Integer(
        compute='_compute_years_since_publication', 
        store=True,
        help="Automatically calculated based on publication year"
    )
    available = fields.Boolean(
        string='Available',
        default=True,
        help="Check if the book is currently available for loan"
    )
    available_display = fields.Char(
        string='Available Status',
        compute='_compute_available_display',
        store=False
    )

    @api.depends('publication_date')
    def _compute_years_since_publication(self):
        for record in self:
            if record.publication_date:
                record.years_since_publication = date.today().year - record.publication_date.year
            else:
                record.years_since_publication = 0

    @api.constrains('isbn')
    def _validate_isbn_format(self):
        for book in self:
            if book.isbn:
                if len(book.isbn) != 17:
                    raise ValidationError(
                        "ISBN must have 17 characters. Ejemplo: 978-99923-1-234-5"
                    )
                
                if not re.match(r'^\d{3}-\d{5}-\d{1}-\d{3}-\d{1}$', book.isbn):
                    raise ValidationError(
                        "Invalid ISBN format. Use: 978-XXXXX-X-XXX-X (13 digits with hyphens)"
                    )
    
    @api.depends('available')
    def _compute_available_display(self):
        for book in self:
            book.available_display = 'Available' if book.available else 'Unavailable'