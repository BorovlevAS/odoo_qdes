from odoo import api, fields, models

class ResPartner(models.Model):

    _inherit = 'res.partner'

    inner_name = fields.Char(string = 'Inner name')
    software_ids = fields.Many2many(comodel_name = 'biko.software', column1 = 'partner_id', column2 = 'software_ids',
                                    string = 'Software')

    source_id = fields.Many2one(comodel_name = 'biko.source', string = 'Source')
    recomendator_id = fields.Many2one(comodel_name = 'res.partner', string = 'Recommendator')

    email2 = fields.Char()
    email2_formatted = fields.Char(
        'Additional Email', compute='_compute_email_formatted',
        help='Format email address "Name <email@domain>"')

    telegram = fields.Char(string = 'Telegram')
    skype = fields.Char(string='Skype')
