from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    prioridad_interna = fields.Selection([('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')],
                                         string='Prioridad Interna', tracking=True)
