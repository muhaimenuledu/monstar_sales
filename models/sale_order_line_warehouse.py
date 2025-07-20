from odoo import models, fields, api

class SaleOrderLineWarehouse(models.Model):
    _name = 'sale.order.line.warehouse'
    _description = 'Sale Order Line Warehouse'

    order_line_id = fields.Many2one('sale.order.line', string='Order Line', required=True, ondelete='cascade')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    warehouse_name = fields.Selection(
        string="Warehouse",
        selection=lambda self: self._get_warehouse_selection(),
        required=True
    )

    @api.model
    def _get_warehouse_selection(self):
        warehouses = self.env['stock.warehouse'].search([])
        return [(w.name, w.name) for w in warehouses]