# Supply Chain Operations Analysis

This is a portfolio-style analytics project focused on supply-chain performance across SKUs, suppliers, locations, product categories, transportation modes, routes, carriers, inventory risk, and quality outcomes.

The project uses Python for data preparation and exploratory analysis, then Tableau for the final dashboard design.

## Tableau Dashboard

I used `outputs/tableau_supply_chain_enriched.csv` as the primary Tableau data source.
View the Tableau dashboard here:

[Supply Chain Performance Dashboard](https://public.tableau.com/app/profile/colton.romines/viz/Dashboard_17827118009200/SupplyChainOverview?publish=yes)

### Dashboard Highlights

- Revenue concentration by product category
- Supplier quality and inspection analysis
- Logistics cost vs lead time tradeoffs
- Route and carrier performance heatmap
- SKU-level profitability and risk prioritization

## Business Questions

- Which product categories and locations contribute the most revenue?
- Which suppliers have the strongest combination of revenue, margin, quality, and lead-time performance?
- Which transportation modes, carriers, and routes show the best cost, quality, and speed tradeoffs?
- Which SKUs should be prioritized for replenishment, quality review, or cost review?

## Tools

- Python: data cleaning, feature engineering, exploratory analysis, and summary tables
- Tableau: interactive dashboard design and stakeholder-facing visualization
- CSV/Markdown: reproducible project outputs and written analysis

## Project Files

- `supply_chain_data.csv`: raw SKU-level dataset
- `analysis/supply_chain_eda.py`: Python analysis script
- `outputs/tableau_supply_chain_enriched.csv`: main Tableau data source
- `outputs/eda_summary.md`: concise EDA summary
- `outputs/*_summary.csv`: summary tables by product, supplier, location, carrier, route, transportation mode, customer segment, and inspection result
- `outputs/sku_priority_lists.csv`: SKU-level watchlists for revenue, defects, stock risk, and margin risk
- `outputs/metric_correlations.csv`: correlation scan across key metrics
- `docs/executive_insights_writeup.md`: executive-facing insights memo

## Analysis Notes

The source data includes revenue, manufacturing cost, shipping cost, and a separate logistics-style cost column. The analysis uses a proxy total cost field:

```text
Total cost proxy = Manufacturing costs + Shipping costs + Logistics cost
```

Profit and margin fields are therefore analytical proxies rather than audited accounting measures.