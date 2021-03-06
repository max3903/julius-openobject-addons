# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-Today Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api


class res_partner(models.Model):
    _inherit = "res.partner"

    property_payment_type = fields.Many2one('payment.type', 'Payment type',
                                            company_dependent=True)

    @api.model
    def _commercial_fields(self):
        res = super(res_partner, self)._commercial_fields()
        res += ['property_payment_type']
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
