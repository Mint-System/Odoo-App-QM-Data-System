# -*- coding: utf-8 -*-

from odoo import models, fields, api


class qm_data_system(models.Model):
    _name = 'qm_data_system.finding'
    _description = 'Finding'

    title = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
