from odoo import models, fields, api
from datetime import   datetime
class ProdutoUpdate(models.Model):
    _name = 'product.update.jobs'

    @api.model
    def actualizar_produtos(self):
        lista_productos = self.env['product.product'].search([])
        for producto in lista_productos:
            producto.write({'description':f'Actualizado el {datetime.now()} - PERU'})
