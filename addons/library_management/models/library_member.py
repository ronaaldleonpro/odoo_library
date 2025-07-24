from odoo import models, fields, api
from datetime import date

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(required=True)
    join_date = fields.Date(default=fields.Date.today)
    member_code = fields.Char(readonly=True, copy=False)

    @api.model
    def create(self, vals):
        if not vals.get('member_code'):
            vals['member_code'] = self.env['ir.sequence'].next_by_code('library.member') or 'NEW'
        return super(LibraryMember, self).create(vals)
