# -*- coding: utf-8 -*-
{
    'name': "QDES: additional fields",
    'description': """Adding fields, changing views""",
    'version': '14.0.1.1.0',
    'author': 'Borovlev AS',
    'company': 'BIKO',
    "depends": ['base', 'contacts'],
    "data": [
        'views/biko_software_views.xml',
        'views/biko_source_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    "sequence": -1,
}
