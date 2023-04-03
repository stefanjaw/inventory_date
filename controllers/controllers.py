# -*- coding: utf-8 -*-
from odoo import http

# class InventoryDate(http.Controller):
#     @http.route('/inventory_date/inventory_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_date/inventory_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_date.listing', {
#             'root': '/inventory_date/inventory_date',
#             'objects': http.request.env['inventory_date.inventory_date'].search([]),
#         })

#     @http.route('/inventory_date/inventory_date/objects/<model("inventory_date.inventory_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_date.object', {
#             'object': obj
#         })