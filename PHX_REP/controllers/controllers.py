# -*- coding: utf-8 -*-
# from odoo import http


# class ReportAtlasco(http.Controller):
#     @http.route('/report_atlasco/report_atlasco', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_atlasco/report_atlasco/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_atlasco.listing', {
#             'root': '/report_atlasco/report_atlasco',
#             'objects': http.request.env['report_atlasco.report_atlasco'].search([]),
#         })

#     @http.route('/report_atlasco/report_atlasco/objects/<model("report_atlasco.report_atlasco"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_atlasco.object', {
#             'object': obj
#         })
