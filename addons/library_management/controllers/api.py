from odoo import http
from odoo.http import request

class LibraryAPI(http.Controller):

    @http.route('/library/book/<string:isbn>', type='json', auth='public')
    def get_book_by_isbn(self, isbn):
        book = request.env['library.book'].sudo().search([('isbn', '=', isbn)], limit=1)
        if book:
            return {'isbn': isbn, 'status': 'found'}
        else:
            return {'isbn': isbn, 'status': 'not found'}
