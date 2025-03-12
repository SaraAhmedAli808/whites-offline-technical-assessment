from odoo import models, fields, api


class SalesPivotReport(models.Model):
    _name = "sales.pivot.report"
    _description = "Sales Pivot Report"
    _auto = False

    id = fields.Integer("ID", readonly=True)  # Required for Odoo models
    product_name = fields.Char("Product Name")
    month = fields.Char("Month")
    order_quantity = fields.Float("Order Quantity")
    total_order_amount = fields.Float("Total Order Amount")
    order_date = fields.Date("Order Date")



    @api.model
    def init(self):
        self.env.cr.execute("DROP VIEW IF EXISTS sales_pivot_report CASCADE;")

        query = """
        CREATE VIEW sales_pivot_report AS 
        SELECT 
            ROW_NUMBER() OVER() AS id,  -- Generate a unique ID
            pt.name AS product_name, 
            TO_CHAR(so.date_order, 'YYYY-MM') AS month,
            SUM(sol.product_uom_qty) AS order_quantity,
            SUM(sol.price_total) AS total_order_amount,
            so.date_order AS order_date
        FROM sale_order_line sol
        JOIN sale_order so ON sol.order_id = so.id
        JOIN product_product pp ON sol.product_id = pp.id
        JOIN product_template pt ON pp.product_tmpl_id = pt.id
        WHERE so.state IN ('sale', 'done')
        GROUP BY pt.name, month, so.date_order

        UNION ALL

        SELECT 
            ROW_NUMBER() OVER() AS id,  -- Generate a unique ID
            pt.name AS product_name, 
            TO_CHAR(po.date_order, 'YYYY-MM') AS month,
            SUM(pol.qty) AS order_quantity,
            SUM(pol.price_subtotal_incl) AS total_order_amount,
            po.date_order AS order_date
        FROM pos_order_line pol
        JOIN pos_order po ON pol.order_id = po.id
        JOIN product_product pp ON pol.product_id = pp.id
        JOIN product_template pt ON pp.product_tmpl_id = pt.id
        WHERE po.state IN ('paid', 'done', 'invoiced')  -- Only confirmed POS orders
        GROUP BY pt.name, month, po.date_order;
        """

        self.env.cr.execute(query)
