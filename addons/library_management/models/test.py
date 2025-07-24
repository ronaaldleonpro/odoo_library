from odoo import models, api

class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Test Model'
    
    @api.model
    def test_method(self):
        print("¡Los modelos se están cargando correctamente!")