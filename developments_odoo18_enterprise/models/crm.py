from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    tipo_cliente = fields.Selection([('new', 'Nuevo'), ('recurrent', 'Recurrente')], string='Tipo de Cliente',
                                    tracking=True, required=False)

    visitado = fields.Boolean(string='Visitado', default=False)

    def action_marcar_true(self):
        for lead in self:
            lead.visitado = True




