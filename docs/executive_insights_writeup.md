# Executive Insight Writeup: Supply Chain Performance Analysis

## Executive Summary

This analysis reviewed 100 SKU-level supply-chain records across product category, supplier, location, shipping carrier, transportation mode, route, inventory position, lead time, revenue, cost, and quality outcomes. The dataset contains no missing values and represents `$577.6K` in total revenue and `46,099` units sold. Because the raw data does not include a formal accounting margin, the analysis uses a proxy total cost field equal to manufacturing cost, shipping cost, and logistics cost. Using that proxy, the portfolio produced about `$519.4K` in profit proxy, with an aggregate profit margin proxy of about `89.9%`.

The main executive takeaway is that the business has strong revenue concentration in a few category, supplier, and location segments, but quality and fulfillment risk are unevenly distributed. Skincare is the largest product category, contributing `$241.6K`, or `41.8%`, of total revenue. Haircare and cosmetics are smaller but still meaningful revenue pools at `$174.5K` and `$161.5K`, respectively. Cosmetics has the strongest category-level profile from a margin and quality perspective, with the highest average margin proxy and the lowest average defect rate. Haircare is the category most exposed to fulfillment delay, with the longest average end-to-end lead time at `41.4 days`.

Supplier performance is one of the clearest areas for action. Supplier 1 is the largest revenue contributor at `$157.5K` and appears comparatively stable, with a relatively low inspection fail rate of `22.2%`. Supplier 3 is also attractive from an economics perspective: it has the highest average margin proxy and a low fail rate of `20.0%`, though its average end-to-end lead time is longer than Supplier 1. Supplier 4 is the most concerning supplier. It contributes the least revenue among the five suppliers at `$86.5K`, has the lowest profit per SKU proxy, and shows a `66.7%` inspection fail rate. That combination suggests Supplier 4 should be prioritized for supplier quality review, process audit, renegotiation, or SKU rationalization.

Logistics performance shows meaningful tradeoffs between speed, cost, revenue coverage, and quality. Rail carries the most revenue by transportation mode at `$165.0K`, but it also has the longest end-to-end lead time at `41.7 days`. Air has a higher average shipping and logistics cost profile, but it has the shortest average end-to-end lead time among the major modes at `35.1 days` and the lowest average defect rate. Sea has the lowest average logistics cost at roughly `$417.82`, but it covers a smaller revenue base. These patterns suggest that transport mode decisions should not be evaluated on cost alone. For high-value, quality-sensitive, or stockout-prone SKUs, the faster and lower-defect profile of Air may justify its higher cost. For stable or lower-priority SKUs, Sea may remain a cost-efficient option.

Carrier performance also provides an actionable signal. Carrier B handles the largest revenue base at `$250.1K` and has the lowest inspection fail rate among carriers at `23.3%`. Carrier C generates `$184.9K` in revenue but has a much higher fail rate of `48.3%`, while Carrier A has a `42.9%` fail rate. If the operational team can validate that inspection failures are meaningfully linked to carrier handling or carrier-linked processes, Carrier B should be considered the benchmark carrier. Carrier C and Carrier A should be reviewed by lane, product type, and supplier before any broad volume shift is made.

At the location level, Mumbai and Kolkata are the two largest revenue locations, each around `$137K`. Mumbai has the stronger quality profile, with a lower inspection fail rate of `22.7%`, while Kolkata has a higher unit volume and more high stock-risk SKUs. Delhi and Chennai should be treated as operational watch areas. Delhi has the highest average demand-stock gap and a `53.3%` inspection fail rate. Chennai has the highest average defect rate and a `50.0%` fail rate. Bangalore stands out positively on lead time, with the shortest average end-to-end lead time at `33.3 days`, although it is a smaller revenue location.

The route analysis highlights a similar tradeoff. Route A produces the most revenue at `$253.2K`, but it also has the highest route-level fail rate at `41.9%`. Route B has the highest average logistics cost at about `$595.66`, but a lower fail rate than Route A. Route C has the smallest revenue base but a solid profit-per-SKU proxy. Route A deserves a quality deep dive because its importance to revenue makes its elevated fail rate more consequential. Route B deserves a cost review because its logistics cost is materially higher than the other routes.

The SKU-level view is important because some risks are hidden when looking only at averages. For example, `SKU51` is the top revenue SKU at about `$9.9K` and has a strong margin proxy, but it has a long end-to-end lead time. `SKU38` is another high-revenue SKU with strong margin, but it has a high demand-stock gap, indicating replenishment pressure. On the risk side, `SKU42` has the highest defect rate and a low margin proxy, making it a strong candidate for quality review or SKU-level intervention. `SKU84` combines high defect rate with long lead time, which makes it a meaningful operational risk even if its revenue contribution is not the largest.

Overall, the recommended executive actions are to prioritize a Supplier 4 quality review, audit Carrier C and Carrier A performance by route and product, review Route A for quality failures, investigate Route B for logistics cost reduction, and build SKU-level replenishment monitoring around high demand-stock gaps. The strongest dashboard design for this project should help leaders move from portfolio-level KPIs to specific suppliers, carriers, routes, locations, and SKUs requiring action.

## Deep Dive Insights

### Product Type

Skincare is the core revenue engine. It represents `40` of the `100` SKUs and generates `$241.6K`, equal to `41.8%` of total revenue. It also has the largest unit volume at `20,731` units. Its inspection fail rate of `32.5%` is lower than haircare and cosmetics, but it still contains `18` high stock-risk SKUs, the most of any category.

Haircare contributes `$174.5K` in revenue and has the longest end-to-end lead time at `41.4 days`. Its average defect rate is also the highest among product types at `2.48%`. This suggests haircare should be monitored for fulfillment delay and quality consistency.

Cosmetics contributes `$161.5K` in revenue and has the best category-level economics in this analysis. It has the highest average margin proxy, the lowest average defect rate at `1.92%`, and the shortest average end-to-end lead time at `33.4 days`. It may be a good category to protect and expand if market demand supports it.

### Supplier

Supplier 1 is the largest revenue source and has a comparatively strong fail-rate profile. Supplier 3 is economically attractive because it has the highest average margin proxy and low inspection fail rate, but its longer lead time should be watched. Supplier 4 is the major exception: it has a `66.7%` inspection fail rate, the lowest revenue, and the weakest profit-per-SKU proxy. Supplier 4 should be the first supplier selected for quality improvement conversations.

### Location

Mumbai and Kolkata lead revenue, but they have different risk profiles. Mumbai combines high revenue with the lowest location-level fail rate, making it a comparatively healthy location. Kolkata has similar revenue and the highest unit volume, but more high stock-risk SKUs. Delhi and Chennai are the most concerning locations. Delhi has the highest demand-stock gap and the highest fail rate. Chennai has the highest defect rate and a high fail rate. Bangalore is smaller but operationally faster.

### Logistics

Rail carries the most revenue but is slowest. Air is faster and has lower average defects, but it is more expensive. Sea is cheapest by average logistics cost but covers less revenue. Route A is important because it has the highest revenue and highest fail rate. Route B is important because it has the highest logistics cost. Carrier B is the strongest carrier candidate based on revenue coverage and lower fail rate.

### Inventory And SKU Prioritization

The portfolio has `41` high stock-risk SKUs using the Python-defined demand-stock gap threshold. This makes replenishment one of the most important dashboard views. The best SKU-level dashboard should combine revenue, margin proxy, defect rate, demand-stock gap, supplier, route, and carrier in one scatterplot. This makes it easier to separate SKUs that are high-value and worth protecting from SKUs that are low-margin, high-defect, or operationally expensive.

## Recommended Next Steps

1. Validate the cost definition with the business owner before presenting profit or margin as final financial performance.
2. Review Supplier 4 quality outcomes by SKU, product type, location, route, and carrier.
3. Review Route A failure patterns and Route B logistics costs.
4. Use Carrier B as a benchmark and compare Carrier A and Carrier C by lane before shifting volume.
5. Build a replenishment watchlist for high-revenue SKUs with high demand-stock gaps.
6. Track dashboard KPIs over time if future extracts include dates, because trend analysis would make the operational recommendations much stronger.

