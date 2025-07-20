from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivered_value = fields.Monetary(
        string="Delivered Value", compute="_compute_delivered_value", store=True
    )
    downpayment_total = fields.Monetary(
        string="Downpayment", compute="_compute_downpayment_total", store=True
    )
    over_delivery_warning = fields.Boolean(
        string="Over Delivered?", compute="_compute_delivery_warning"
    )
    warning_message = fields.Char(
        string="Warning", compute="_compute_warning_message"
    )

    @api.depends('order_line.qty_delivered', 'order_line.price_unit')
    def _compute_delivered_value(self):
        for order in self:
            total = 0.0
            for line in order.order_line:
                total += line.qty_delivered * line.price_unit
            order.delivered_value = total

    @api.depends('invoice_ids.invoice_line_ids')
    def _compute_downpayment_total(self):
        for order in self:
            total = 0.0
            for invoice in order.invoice_ids.filtered(lambda inv: inv.state != 'cancel'):
                for line in invoice.invoice_line_ids:
                    if line.is_downpayment:
                        total += line.price_total
            order.downpayment_total = total

    @api.depends('downpayment_total', 'delivered_value')
    def _compute_delivery_warning(self):
        for order in self:
            if order.downpayment_total > 0:
                order.over_delivery_warning = order.delivered_value > order.downpayment_total
            else:
                order.over_delivery_warning = False

    @api.depends('over_delivery_warning')
    def _compute_warning_message(self):
        for order in self:
            if order.over_delivery_warning:
                order.warning_message = "⚠️ Delivered value exceeds total downpayment."
            else:
                order.warning_message = ""
