from odoo import http
from odoo.http import request, Response
import json

class LibraryAPI(http.Controller):

    @http.route('/api/library/book/<string:isbn>', auth='public', methods=['GET'], type='http')
    def get_book_info(self, isbn, **kwargs):
        try:
            book = request.env['library.book'].sudo().search([('isbn', '=', isbn)], limit=1)
            
            if not book:
                return Response(
                    json.dumps({'error': 'Book not found'}),
                    status=404,
                    mimetype='application/json'
                )
            
            data = {
                'book_id': book.id,
                'title': book.title,
                'author': book.author,
                'isbn': book.isbn,
                'available': book.available,
                'available_display': book.available_display,
                'publication_year': book.publication_date.year if book.publication_date else None
            }
            
            return Response(
                json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            
        except Exception as e:
            return Response(
                json.dumps({'error': str(e)}),
                status=500,
                mimetype='application/json'
            )
