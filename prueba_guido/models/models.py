# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crm_lead(models.Model):
    _inherit = 'crm.lead'

    prueba = fields.Char(string='Prueba')
    selecction = fields.Char(string='Selection')

class sale_order(models.Model):
    _inherit = 'sale.order'
    
    sale_team = fields.Many2one('crm.team',string='SALES')