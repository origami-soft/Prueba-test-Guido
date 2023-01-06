# -*- coding: utf-8 -*-
# from odoo import http


# class TestGuido(http.Controller):
#     @http.route('/test_guido/test_guido', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_guido/test_guido/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_guido.listing', {
#             'root': '/test_guido/test_guido',
#             'objects': http.request.env['test_guido.test_guido'].search([]),
#         })

#     @http.route('/test_guido/test_guido/objects/<model("test_guido.test_guido"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_guido.object', {
#             'object': obj
#         })
