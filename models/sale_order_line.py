from odoo import models, fields, api

class SalesOrderLine(models.Model):

    _inherit = 'sale.order.line'

    warehouse_lines = fields.One2many('sale.order.line.warehouse', 'order_line_id', string='Warehouses')

    warehouse_name = fields.Selection(
        string="Warehouse",
        selection=lambda self: self._get_warehouse_selection(),
        required=True
    )

    @api.model
    def _get_warehouse_selection(self):
        warehouses = self.env['stock.warehouse'].search([])
        return [(w.name, w.name) for w in warehouses]
