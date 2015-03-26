# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from datetime import datetime
import openerp.tools
import werkzeug

class website_gordonramsay(http.Controller):
    @http.route(['/henriksmatbod'], type='http', auth="public", website=True)
    def matbod_header(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            }
        return request.render('theme_gordonramsay.main', ctx)   

    @http.route(['/henriksmatbod','/henriksmatbod/bilder'], type='http', auth="public", website=True)
    def matbod_madia(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            }
        return request.render('theme_gordonramsay.bilder', ctx)

    @http.route(['/henriksmatbod/video'], type='http', auth="public", website=True)
    def matbod_kontakt(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            }
        return request.render('theme_gordonramsay.video', ctx)           
        
    @http.route(['/henriksmatbod/kurser'], type='http', auth="public", website=True)
    def matbod_kurser(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            }
        return request.render('theme_gordonramsay.kurser', ctx)  
         
    @http.route(['/henriksmatbod/webshop'], type='http', auth="public", website=True)
    def matbod_webshop(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            }
        return request.render('theme_gordonramsay.webshop', ctx) 
          
    @http.route(['/henriksmatbod/kontakt'], type='http', auth="public", website=True)
    def matbod_kontakt(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
           
        ctx = {
            }
        return request.render('theme_gordonramsay.kontakt', ctx)   
        