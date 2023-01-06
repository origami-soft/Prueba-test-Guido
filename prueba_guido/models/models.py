# -*- coding: utf-8 -*-

from odoo import models, fields, api

class prueba_prueba(models.Model):
    _name = 'prueba.prueba'

    name = fields.Char(string='Nombre')


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    prueba = fields.Char(string='Prueba')
    selecction = fields.Char(string='Selection')


class sale_order(models.Model):
    _inherit = 'sale.order'

    prueba = fields.Char(string='Prueba')

