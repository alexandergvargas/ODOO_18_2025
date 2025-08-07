# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Developements Odoo 18 Enterprise',
    'category': 'Sale',
    'description': """  Este modulo sirve para crear pequeñas personalizaciones dentro de Odoo 18
""",
    'version': '1.1',
    'depends': [
        'crm', 'project', 'documents_project', 'product'
    ],
    'data': [
        'views/crm.xml',
        'views/project.xml',
        'views/jobs_atomatic.xml',
        'views/sequence.xml',
        'views/product_template.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
