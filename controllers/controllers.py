# -*- coding: utf-8 -*-
from odoo import http


class QmDataSystem(http.Controller):
    @http.route('/qm_data_system/finding/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/qm_data_system/finding/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('qm_data_system.listing', {
            'root': '/qm_data_system/finding',
            'objects': http.request.env['qm_data_system.finding'].search([]),
        })

    @http.route('/qm_data_system/finding/objects/<model("qm_data_system.finding"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('qm_data_system.object', {
            'object': obj
        })
