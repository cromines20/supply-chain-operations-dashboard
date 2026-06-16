# Supply Chain Operations Analysis

This is a portfolio-style analytics project focused on supply-chain performance across SKUs, suppliers, locations, product categories, transportation modes, routes, carriers, inventory risk, and quality outcomes.

The project uses Python for data preparation and exploratory analysis, then Tableau for the final dashboard design.

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
- `docs/tableau_dashboard_build_guide.md`: Tableau dashboard build instructions and resume bullet options
- `docs/executive_insights_writeup.md`: executive-facing insights memo

Install dependencies and run the analysis with:

```bash
pip install -r requirements.txt
python3 analysis/supply_chain_eda.py
```

## Analysis Notes

The source data includes revenue, manufacturing cost, shipping cost, and a separate logistics-style cost column. The analysis uses a proxy total cost field:

```text
Total cost proxy = Manufacturing costs + Shipping costs + Logistics cost
```

Profit and margin fields are therefore analytical proxies rather than audited accounting measures.

## Tableau Dashboard

I used `outputs/tableau_supply_chain_enriched.csv` as the primary Tableau data source. The recommended dashboard includes:

- KPI cards for revenue, units sold, margin, inspection fail rate, lead time, and stock-risk SKUs
- Product revenue and margin view
- Supplier performance matrix
- Supplier and inspection quality heatmap
- Transportation mode cost, speed, and quality scatterplot
- Route and carrier heatmap
- Location performance view
- SKU priority scatterplot

Detailed build instructions are in `docs/tableau_dashboard_build_guide.md`.
