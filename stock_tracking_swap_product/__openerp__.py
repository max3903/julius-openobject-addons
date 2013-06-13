# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Julius Network Solutions SARL <contact@julius.fr>
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
#################################################################################

{
    "name" : "Stock tracking swap product",
    "version" : "1.0",
    "author" : "Julius Network Solutions",
    "description" : """Presentation:

This module add a wizard to swap product in packaging.
This wizard is used to replace an object from a package.
Adding to the historical movements and parent objects

""",
    "website" : "http://www.julius.fr",
    "depends" : [
        "stock_tracking_swap_pack",
        "stock_tracking_add_product",
    ],
    "category" : "Customs/Stock",
    "init_xml" : [],
    "demo_xml" : [],
    "images" : [],
    "update_xml" : [
        "wizard/swap_product_view.xml",
        'stock_view.xml',
    ],
    'test': [],
    'installable': True,
    'active': False,
}