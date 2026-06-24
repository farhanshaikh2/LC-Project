import pandas as pd

LC_Issuance = pd.read_excel("Trade_Finance_Main.xlsm",skiprows=3,header=0,engine="openpyxl",usecols=['LC Number', 'Issue Date.', 'Project Director', 'Status', 'Bank', 'Facility Space', 'Beneficiary', 'Group Company', 'Project', 'Project Code', 'Curr', 'LC Amt(FCY)', 'Rate', 'LC Amt(SAR)', 'Expiry Date', 'Last Ship Date', 'Lines', 'Payment Terms', 'Cash Margin', 'Cash-Fund Utilized', 'Cash-Recovered', 'Increase Amount in SAR', 'Remarks', 'Active/Cancelled',]
).astype(
    {
        "Project Director":"category",
        "Status":"category",        
        "Bank":"category",
        "Facility Space":"category",
        "Beneficiary":"category",
        "Group Company":"category",
        "Project":"category",
        "Project Code":"Int32",
        "Curr":"category",
        "Lines":"category",
        
    }
)
LC_Issuance["Last Ship Date"] = pd.to_datetime(LC_Issuance["Last Ship Date"]).dt.date
LC_Issuance["Issue Date."] = pd.to_datetime(LC_Issuance["Issue Date."]).dt.date
LC_Issuance["Expiry Date"] = pd.to_datetime(LC_Issuance["Expiry Date"]).dt.date

