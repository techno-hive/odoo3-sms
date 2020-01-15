# -*- coding: utf-8 -*-
from odoo import http

# class Josphat(http.Controller):
#     @http.route('/josphat/josphat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/josphat/josphat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('josphat.listing', {
#             'root': '/josphat/josphat',
#             'objects': http.request.env['josphat.josphat'].search([]),
#         })

#     @http.route('/josphat/josphat/objects/<model("josphat.josphat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('josphat.object', {
#             'object': obj
#         })