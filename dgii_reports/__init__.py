# Part of Domincana Premium.
# See LICENSE file for full copyright and licensing details.
# © 2018 José López <jlopez@indexa.do>

from . import controllers
from . import models
from . import wizard

from odoo import api, SUPERUSER_ID

def update_taxes(env):
    """ Actualiza los registros de impuestos con los datos correctos """
    env['account.tax'].search([])._update_taxes_do()
