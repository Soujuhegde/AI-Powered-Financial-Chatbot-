import pandas as pd


class FinancialEngine:

    def __init__(self, file_path):
        self.df = pd.read_excel(file_path, sheet_name="Extracted Data")

    def get_company_data(self, company):
        return self.df[
            self.df["Company Name"] == company
        ]

    def get_metric(self, company, year, metric):
        row = self.df[
            (self.df["Company Name"] == company)
            &
            (self.df["Fiscal Year"] == year)
        ]

        if row.empty:
            return 0

        return row.iloc[0][metric]

    def compare_metric(
        self,
        company1,
        company2,
        year,
        metric
    ):

        val1 = self.get_metric(
            company1,
            year,
            metric
        )

        val2 = self.get_metric(
            company2,
            year,
            metric
        )

        return val1, val2

    def highest_revenue(self, year):

        data = self.df[
            self.df["Fiscal Year"] == year
        ]

        idx = data["Total Revenue"].idxmax()

        return data.loc[idx]

    def get_growth_metrics(self, company):

        return self.df[
            self.df["Company Name"] == company
        ][[
            "Fiscal Year",
            "Revenue Growth (%)",
            "Net Income Growth (%)",
            "Operating Cash Flow Growth (%)"
        ]]