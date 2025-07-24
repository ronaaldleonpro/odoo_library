from odoo import models, fields, api
from datetime import date

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    isbn = fields.Char()
    title = fields.Char(required=True)
    author = fields.Char(required=True)
    publication_date = fields.Date(required=True)
    years_since_publication = fields.Integer(compute='_compute_years_since_publication', store=True)

    @api.depends('publication_date')
    def _compute_years_since_publication(self):
        for record in self:
            if record.publication_date:
                record.years_since_publication = date.today().year - record.publication_date.year
            else:
                record.years_since_publication = 0
