# Sales Pivot Report

This module provides a **Sales Pivot Report** in Odoo, combining **Sales Orders** and **POS Orders** into a unified view for better sales analysis.

## Features
- Creates a **pivot table** for analyzing sales performance.
- Supports **Sales Orders** and **POS Orders**.
- Displays key sales metrics:
  - **Product Name**
  - **Order Date**
  - **Order Quantity**
  - **Total Order Amount**
- Provides **graphical** and **list views**.
- Allows **filtering by date range**.

## Setup

1. **Access the Report**
   - Navigate to **Sales > Reporting > Sales Pivot Report**.
   - Use **Pivot View** for detailed data analysis.
   - Use **Graph View** to visualize trends.

2. **Filter Data**
   - Apply date filters to view sales data for a specific period.
   - Group by **Product Name**, **Order Date**, or **Month**.

## Notes
- The report includes **confirmed sales orders** and **paid/invoiced POS orders**.
- Ensure that **sale_order_line** and **pos_order_line** contain valid data for accurate reports.

