# Mandatory Analytic Account & Partner Validation

## Features
- Adds a **Require Analytic Account** and **Require Partner** option in Chart of Accounts.
- Allows selected users to **bypass validation**.
- Prevents posting journal entries if required fields are missing.
- Displays **error messages** for missing data.

## Setup
1. **Enable Validation in Chart of Accounts**
   - Go to **Accounting > Configuration > Chart of Accounts**.
   - Open or create an account and enable:
     - **Require Analytic Account** if an analytic account is mandatory.
     - **Require Partner** if a partner is mandatory.
     - **Bypass Users** to select users who can skip validation.

2. **Post a Journal Entry**
   - Create a **Journal Entry** in **Accounting > Journal Entries**.
   - Try posting it:
     - If required fields are missing, an error message will appear.
     - If a user is in **Bypass Users**, they can post without restrictions.




