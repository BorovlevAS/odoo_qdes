from random import randint
from odoo import fields, models

class BikoSoftware(models.Model):

    _name = 'biko.software'
    _description = 'BIKO: software'
    _order = 'name'

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer(string='Color Index', default=_get_default_color)
    name = fields.Char(string = 'Name', required = True)