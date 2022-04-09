from odoo import api, fields, models

class ResPartner(models.Model):

    _inherit = 'res.partner'

    inner_name = fields.Char(string = 'Inner name')
    software_ids = fields.Many2many(comodel_name = 'biko.software', column1 = 'partner_id', column2 = 'software_ids',
                                    string = 'Software')
