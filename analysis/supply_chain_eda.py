from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "supply_chain_data.csv"
OUTPUT = ROOT / "outputs"


DIMENSIONS = [
    "Product type",
    "Customer demographics",
    "Shipping carriers",
    "Supplier name",
    "Location",
    "Inspection results",
    "Transportation modes",
    "Routes",
]

NUMERIC_COLUMNS = [
    "Price",
    "Availability",
    "Number of products sold",
    "Revenue generated",
    "Stock levels",
    "Lead times",
    "Order quantities",
    "Shipping times",
    "Shipping costs",
    "Lead time",
    "Production volumes",
    "Manufacturing lead time",
    "Manufacturing costs",
    "Defect rates",
    "Costs",
]


def dollars(value: float) -> str:
    return f"${value:,.0f}"


def pct(value: float) -> str:
    return f"{value:.1%}"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(SOURCE)
    df = df.rename(
        columns={
            "Revenue generated": "Revenue",
            "Number of products sold": "Units sold",
            "Product type": "Product type",
            "Costs": "Logistics cost",
        }
    )

    # These are analytical proxies for EDA/dashboarding. The source data does not
    # define a fully burdened margin field, so keep every source cost column too.
    df["Total cost proxy"] = (
        df["Manufacturing costs"] + df["Shipping costs"] + df["Logistics cost"]
    )
    df["Profit proxy"] = df["Revenue"] - df["Total cost proxy"]
    df["Profit margin proxy"] = np.where(
        df["Revenue"] != 0, df["Profit proxy"] / df["Revenue"], np.nan
    )
    df["Revenue per unit"] = np.where(
        df["Units sold"] != 0, df["Revenue"] / df["Units sold"], np.nan
    )
    df["Cost per unit proxy"] = np.where(
        df["Units sold"] != 0, df["Total cost proxy"] / df["Units sold"], np.nan
    )
    df["Inventory coverage ratio"] = np.where(
        df["Units sold"] != 0, df["Stock levels"] / df["Units sold"], np.nan
    )
    df["Demand-stock gap"] = df["Units sold"] - df["Stock levels"]
    df["Fulfillment lead time"] = df["Lead times"] + df["Shipping times"]
    df["End-to-end lead time"] = (
        df["Lead time"] + df["Manufacturing lead time"] + df["Shipping times"]
    )
    df["Quality risk flag"] = np.where(df["Defect rates"] >= 3.5, "High", "Normal")
    df["Stock risk flag"] = np.where(df["Demand-stock gap"] > 500, "High", "Normal")
    df["Margin risk flag"] = np.where(df["Profit margin proxy"] < 0.85, "High", "Normal")
    return df


def summarize_dimension(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    grouped = (
        df.groupby(dimension, dropna=False)
        .agg(
            sku_count=("SKU", "count"),
            revenue=("Revenue", "sum"),
            units_sold=("Units sold", "sum"),
            profit_proxy=("Profit proxy", "sum"),
            total_cost_proxy=("Total cost proxy", "sum"),
            avg_margin_proxy=("Profit margin proxy", "mean"),
            avg_defect_rate=("Defect rates", "mean"),
            fail_count=("Inspection results", lambda s: (s == "Fail").sum()),
            avg_fulfillment_lead_time=("Fulfillment lead time", "mean"),
            avg_end_to_end_lead_time=("End-to-end lead time", "mean"),
            avg_shipping_cost=("Shipping costs", "mean"),
            avg_logistics_cost=("Logistics cost", "mean"),
            avg_stock_level=("Stock levels", "mean"),
            avg_demand_stock_gap=("Demand-stock gap", "mean"),
            high_stock_risk_skus=("Stock risk flag", lambda s: (s == "High").sum()),
            high_quality_risk_skus=("Quality risk flag", lambda s: (s == "High").sum()),
        )
        .reset_index()
    )
    grouped["revenue_share"] = grouped["revenue"] / grouped["revenue"].sum()
    grouped["inspection_fail_rate"] = grouped["fail_count"] / grouped["sku_count"]
    grouped["profit_per_sku_proxy"] = grouped["profit_proxy"] / grouped["sku_count"]
    return grouped.sort_values("revenue", ascending=False)


def top_bottom_skus(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "SKU",
        "Product type",
        "Supplier name",
        "Location",
        "Revenue",
        "Units sold",
        "Profit proxy",
        "Profit margin proxy",
        "Defect rates",
        "Demand-stock gap",
        "End-to-end lead time",
        "Transportation modes",
        "Routes",
    ]
    top_revenue = df.nlargest(10, "Revenue")[cols].assign(list_name="Top revenue")
    high_defect = df.nlargest(10, "Defect rates")[cols].assign(list_name="Highest defect")
    high_gap = df.nlargest(10, "Demand-stock gap")[cols].assign(list_name="Highest stock risk")
    low_margin = df.nsmallest(10, "Profit margin proxy")[cols].assign(list_name="Lowest margin")
    return pd.concat([top_revenue, high_defect, high_gap, low_margin], ignore_index=True)


def correlation_table(df: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "Revenue",
        "Units sold",
        "Profit proxy",
        "Profit margin proxy",
        "Defect rates",
        "Fulfillment lead time",
        "End-to-end lead time",
        "Manufacturing costs",
        "Shipping costs",
        "Logistics cost",
        "Stock levels",
        "Availability",
        "Production volumes",
    ]
    corr = df[metrics].corr(numeric_only=True)
    pairs = []
    for i, left in enumerate(metrics):
        for right in metrics[i + 1 :]:
            pairs.append(
                {
                    "metric_1": left,
                    "metric_2": right,
                    "correlation": corr.loc[left, right],
                    "abs_correlation": abs(corr.loc[left, right]),
                }
            )
    return pd.DataFrame(pairs).sort_values("abs_correlation", ascending=False)


def write_markdown_summary(df: pd.DataFrame, dimension_tables: dict[str, pd.DataFrame]) -> None:
    product = dimension_tables["Product type"]
    supplier = dimension_tables["Supplier name"]
    mode = dimension_tables["Transportation modes"]
    location = dimension_tables["Location"]
    carrier = dimension_tables["Shipping carriers"]
    route = dimension_tables["Routes"]

    def format_value(value):
        if pd.isna(value):
            return ""
        if isinstance(value, (float, np.floating)):
            return f"{value:.3f}"
        return str(value)

    def md_table(frame: pd.DataFrame, cols: list[str], n: int = 10) -> str:
        rows = frame[cols].head(n)
        header = "| " + " | ".join(cols) + " |"
        divider = "| " + " | ".join(["---"] * len(cols)) + " |"
        body = [
            "| " + " | ".join(format_value(value) for value in row) + " |"
            for row in rows.to_numpy()
        ]
        return "\n".join([header, divider, *body])

    lines = [
        "# Supply Chain EDA Summary",
        "",
        "## Dataset Profile",
        f"- Source rows: {len(df):,}",
        f"- Unique SKUs: {df['SKU'].nunique():,}",
        f"- Product categories: {df['Product type'].nunique():,}",
        f"- Suppliers: {df['Supplier name'].nunique():,}",
        f"- Locations: {df['Location'].nunique():,}",
        f"- Missing values: {int(df.isna().sum().sum()):,}",
        "",
        "## Core KPIs",
        f"- Total revenue: {dollars(df['Revenue'].sum())}",
        f"- Units sold: {df['Units sold'].sum():,}",
        f"- Total cost proxy: {dollars(df['Total cost proxy'].sum())}",
        f"- Profit proxy: {dollars(df['Profit proxy'].sum())}",
        f"- Average profit margin proxy: {pct(df['Profit margin proxy'].mean())}",
        f"- Average defect rate: {df['Defect rates'].mean():.2f}%",
        f"- Inspection fail rate: {pct((df['Inspection results'] == 'Fail').mean())}",
        f"- Average fulfillment lead time: {df['Fulfillment lead time'].mean():.1f} days",
        f"- Average end-to-end lead time: {df['End-to-end lead time'].mean():.1f} days",
        "",
        "## Product Summary",
        md_table(
            product,
            [
                "Product type",
                "sku_count",
                "revenue",
                "revenue_share",
                "units_sold",
                "avg_margin_proxy",
                "avg_defect_rate",
                "inspection_fail_rate",
                "avg_end_to_end_lead_time",
            ],
        ),
        "",
        "## Supplier Summary",
        md_table(
            supplier,
            [
                "Supplier name",
                "sku_count",
                "revenue",
                "units_sold",
                "avg_margin_proxy",
                "avg_defect_rate",
                "inspection_fail_rate",
                "avg_end_to_end_lead_time",
                "high_stock_risk_skus",
            ],
        ),
        "",
        "## Logistics Summary",
        "### Transportation Modes",
        md_table(
            mode,
            [
                "Transportation modes",
                "sku_count",
                "revenue",
                "avg_shipping_cost",
                "avg_logistics_cost",
                "avg_end_to_end_lead_time",
                "avg_defect_rate",
            ],
        ),
        "",
        "### Routes",
        md_table(
            route,
            [
                "Routes",
                "sku_count",
                "revenue",
                "avg_logistics_cost",
                "avg_end_to_end_lead_time",
                "inspection_fail_rate",
            ],
        ),
        "",
        "### Carriers",
        md_table(
            carrier,
            [
                "Shipping carriers",
                "sku_count",
                "revenue",
                "avg_shipping_cost",
                "avg_fulfillment_lead_time",
                "inspection_fail_rate",
            ],
        ),
        "",
        "## Location Summary",
        md_table(
            location,
            [
                "Location",
                "sku_count",
                "revenue",
                "units_sold",
                "avg_margin_proxy",
                "avg_defect_rate",
                "avg_end_to_end_lead_time",
                "high_stock_risk_skus",
            ],
        ),
        "",
    ]
    (OUTPUT / "eda_summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    df = load_data()

    df.to_csv(OUTPUT / "tableau_supply_chain_enriched.csv", index=False)

    dimension_tables = {}
    for dimension in [
        "Product type",
        "Customer demographics",
        "Shipping carriers",
        "Supplier name",
        "Location",
        "Inspection results",
        "Transportation modes",
        "Routes",
    ]:
        table = summarize_dimension(df, dimension)
        dimension_tables[dimension] = table
        filename = dimension.lower().replace(" ", "_") + "_summary.csv"
        table.to_csv(OUTPUT / filename, index=False)

    top_bottom_skus(df).to_csv(OUTPUT / "sku_priority_lists.csv", index=False)
    correlation_table(df).to_csv(OUTPUT / "metric_correlations.csv", index=False)
    pd.DataFrame(
        {
            "column": df.columns,
            "dtype": [str(dtype) for dtype in df.dtypes],
            "missing_count": df.isna().sum().values,
            "unique_count": [df[col].nunique(dropna=False) for col in df.columns],
        }
    ).to_csv(OUTPUT / "data_dictionary_profile.csv", index=False)

    write_markdown_summary(df, dimension_tables)


if __name__ == "__main__":
    main()
