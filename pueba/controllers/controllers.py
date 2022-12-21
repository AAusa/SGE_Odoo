# -*- coding: utf-8 -*-
# from odoo import http


# class Pueba(http.Controller):
#     @http.route('/pueba/pueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pueba/pueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pueba.listing', {
#             'root': '/pueba/pueba',
#             'objects': http.request.env['pueba.pueba'].search([]),
#         })

#     @http.route('/pueba/pueba/objects/<model("pueba.pueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pueba.object', {
#             'object': obj
#         })
