# POS Refund Authorization

This module adds **manager authorization** for refunds in Odoo POS using a numeric password.

##  Features
- Adds a **POS Refund Password** field in Employee records.
- Ensures passwords **contain only numbers**.
- Requires **manager approval** before processing refunds in POS.
- Displays errors for invalid or missing passwords.

##  Setup
1. **Set a Manager's Refund Password**
   - Go to **HR > Employees**, open a manager’s record, and enter a numeric password in
    **"POS Refund Password"** after Company field.

2. **Authorize Refunds in POS**
   - On refund, the system prompts for a **manager’s password**.
   - Enter the correct password to proceed.

##  Notes
- Refunds ( won’t work )if no manager has a password.
