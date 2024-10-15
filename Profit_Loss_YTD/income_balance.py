    


####################### Income ####################

income_statement_label = {'04-Cost of Goods Sold':'02-1-Cost of Revenue',
'0401-DIRECT EXPENSES':'07-1-Other Operating Expenses, Total',
'0401-PURCHASE':'07-1-Other Operating Expenses, Total',
'0501-OTHERS DIRECT EXPENSES':'07-1-Other Operating Expenses, Total',
'0601-OTHERS DIRECT EXPENSES':'07-1-Other Operating Expenses, Total',
'0631- Development Expenses':'07-1-Other Operating Expenses, Total',
'06-Office & Administrative Expenses':'03-1-Office & Administrative Expenses',
'0625-Property Tax & Others':'09-1-Income Tax & VAT',
'0629- HMBR VAT & Tax Expenses':'09-1-Income Tax & VAT',
'0629-VAT & Tax Expenses':'09-1-Income Tax & VAT',
'0630- Bank Interest & Charges':'08-1-Interest Expense',
'0630-Bank Interest & Charges':'08-1-Interest Expense',
'0631-Other Expenses':'07-1-Other Operating Expenses, Total',
'0633-Interest-Loan':'08-1-Interest Expense',
'0636-Depreciation':'05-1-Depreciation/Amortization',
'07-Sales & Distribution Expenses':'04-1-Sales & Distribution Expenses',
'SALES & DISTRIBUTION EXPENSES':'04-1-Sales & Distribution Expenses',
'0701-MRP-Discount' : '04-2-MRP Discount',
'0702-Discount-Expense' : '04-3-Discount Expense',
'08-Revenue':'01-1-Revenue',
'14-Purchase Return':'06-1-Unusual Expenses (Income)',
'15-Sales Return':'06-1-Unusual Expenses (Income)',
'':'06-1-Unusual Expenses (Income)',
'Profit/Loss':'10-1-Net Income'}

income_label = pd.DataFrame(income_statement_label.items(),columns = ['xhrc4','Income Statement'])


####################### Balance ####################

balance_sheet_label = {
'0101-CASH & CASH EQUIVALENT':'01-3-Cash',
'0102-BANK BALANCE':'01-3-Cash',
'0103-ACCOUNTS RECEIVABLE':'02-1-Accounts Receivable',
'0104-PREPAID EXPENSES':'04-1-Prepaid Expenses',
'0105-ADVANCE ACCOUNTS':'04-1-Prepaid Expenses',
'0106-STOCK IN HAND':'03-1-Inventories',
'02-OTHER ASSET':'05-1-Other Assets',
'0201-DEFFERED CAPITAL EXPENDITURE':'05-1-Other Assets',
'0203-LOAN TO OTHERS CONCERN':'05-1-Other Assets',
'0204-SECURITY DEPOSIT':'05-1-Other Assets',
'0205-LOAN TO OTHERS CONCERN':'05-1-Other Assets',
'0206-Other Investment':'05-1-Other Assets',
'0301-Lab Equipment':'06-1-Property, Plant & Equipment',
'0301-Office Equipment':'06-1-Property, Plant & Equipment',
'0302-Corporate Office Equipments':'06-1-Property, Plant & Equipment',
'0303-Furniture & Fixture':'06-1-Property, Plant & Equipment',
'0303-Lab Decoration':'06-1-Property, Plant & Equipment',
'0304-Trading Vehicles':'06-1-Property, Plant & Equipment',
'0305-Private Vehicles':'06-1-Property, Plant & Equipment',
'0306- Plants & Machinery':'06-1-Property, Plant & Equipment',
'0307-Intangible Asset':'07-1-Goodwill & Intangible Asset',
'0308-Land & Building':'06-1-Property, Plant & Equipment',
'0901-Accrued Expenses':'09-1-Accrued Liabilities',
'0902-Income Tax Payable':'09-1-Accrued Liabilities',
'0903-Accounts Payable':'08-1-Accounts Payable',
'0904-Money Agent Liability':'10-1-Other Short Term Liabilities',
'0904-Reconciliation Liability':'10-1-Other Short Term Liabilities',
'0905-C & F Liability':'10-1-Other Short Term Liabilities',
'0906-Others Liability':'10-1-Other Short Term Liabilities',
'1001-Short Term Bank Loan':'11-1-Debt',
'1002-Short Term Loan':'11-1-Debt',
'11-Reserve & Fund':'12-1-Other Long Term Liabilities',
'1202-Long Term Bank Loan':'11-1-Debt',
'13-Owners Equity':'13-1-Total Shareholders Equity'}

balance_label = pd.DataFrame(balance_sheet_label.items(),columns = ['xhrc4','Balance Sheet'])