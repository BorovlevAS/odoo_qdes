from odoo import fields, models

class BikoSource(models.Model):

    _name = 'biko.source'
    _description = 'BIKO: sources'
    _order = 'name'

    name = fields.Char(string = 'Name', required = True)