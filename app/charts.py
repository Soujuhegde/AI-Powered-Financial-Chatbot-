import plotly.express as px


def revenue_chart(df):

    fig = px.line(
        df,
        x="Fiscal Year",
        y="Total Revenue",
        color="Company Name",
        markers=True,
        title="Revenue Trend",
        template="plotly_white"
    )

    return fig


def net_income_chart(df):

    fig = px.bar(
        df,
        x="Fiscal Year",
        y="Net Income",
        color="Company Name",
        title="Net Income Comparison",
        template="plotly_white"
    )

    return fig