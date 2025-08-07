from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        if not vals.get('default_code'):
            print('codigo automatico')
            vals['default_code'] = self.env['ir.sequence'].next_by_code('product.default_code_odoo')
        return super(ProductTemplate, self).create(vals)

    @api.constrains('list_price')
    def _check_price(self):
        for product in self:
            if product.list_price < 0:
                raise ValidationError('El precio de Venta debe ser mayor a 0.')

    partner_id = fields.Many2one('res.partner', string='Cliente')
    partner_country = fields.Char(related='partner_id.country_id.name', string='Pais del cliente')
    total_price_odoo = fields.Float(string='Total Odoo', compute='_compute_price')

    @api.depends('list_price')
    def _compute_price(self):
        for record in self:
            record.total_price_odoo = record.list_price * 3.8
