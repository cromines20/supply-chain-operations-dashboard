# Supply Chain EDA Summary

## Dataset Profile
- Source rows: 100
- Unique SKUs: 100
- Product categories: 3
- Suppliers: 5
- Locations: 5
- Missing values: 0

## Core KPIs
- Total revenue: $577,605
- Units sold: 46,099
- Total cost proxy: $58,206
- Profit proxy: $519,399
- Average profit margin proxy: 86.1%
- Average defect rate: 2.28%
- Inspection fail rate: 36.0%
- Average fulfillment lead time: 21.7 days
- Average end-to-end lead time: 37.6 days

## Product Summary
| Product type | sku_count | revenue | revenue_share | units_sold | avg_margin_proxy | avg_defect_rate | inspection_fail_rate | avg_end_to_end_lead_time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| skincare | 40 | 241628.162 | 0.418 | 20731 | 0.860 | 2.335 | 0.325 | 37.100 |
| haircare | 34 | 174455.391 | 0.302 | 13611 | 0.853 | 2.483 | 0.382 | 41.382 |
| cosmetics | 26 | 161521.266 | 0.280 | 11757 | 0.873 | 1.919 | 0.385 | 33.423 |

## Supplier Summary
| Supplier name | sku_count | revenue | units_sold | avg_margin_proxy | avg_defect_rate | inspection_fail_rate | avg_end_to_end_lead_time | high_stock_risk_skus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Supplier 1 | 27 | 157528.995 | 11080 | 0.842 | 1.804 | 0.222 | 33.444 | 9 |
| Supplier 2 | 22 | 125467.419 | 11068 | 0.872 | 2.363 | 0.364 | 39.636 | 11 |
| Supplier 5 | 18 | 110343.464 | 8662 | 0.853 | 2.665 | 0.389 | 40.611 | 9 |
| Supplier 3 | 15 | 97795.980 | 8083 | 0.911 | 2.466 | 0.200 | 40.267 | 8 |
| Supplier 4 | 18 | 86468.962 | 7206 | 0.841 | 2.337 | 0.667 | 36.111 | 4 |

## Logistics Summary
### Transportation Modes
| Transportation modes | sku_count | revenue | avg_shipping_cost | avg_logistics_cost | avg_end_to_end_lead_time | avg_defect_rate |
| --- | --- | --- | --- | --- | --- | --- |
| Rail | 28 | 164990.418 | 5.469 | 541.748 | 41.679 | 2.319 |
| Road | 29 | 159315.232 | 5.542 | 553.386 | 37.241 | 2.621 |
| Air | 26 | 155735.350 | 6.018 | 561.713 | 35.077 | 1.824 |
| Sea | 17 | 97563.819 | 4.970 | 417.819 | 35.353 | 2.315 |

### Routes
| Routes | sku_count | revenue | avg_logistics_cost | avg_end_to_end_lead_time | inspection_fail_rate |
| --- | --- | --- | --- | --- | --- |
| Route A | 43 | 253198.852 | 485.483 | 37.791 | 0.419 |
| Route B | 37 | 204484.008 | 595.659 | 37.378 | 0.297 |
| Route C | 20 | 119921.958 | 500.471 | 37.600 | 0.350 |

### Carriers
| Shipping carriers | sku_count | revenue | avg_shipping_cost | avg_fulfillment_lead_time | inspection_fail_rate |
| --- | --- | --- | --- | --- | --- |
| Carrier B | 43 | 250094.647 | 5.509 | 21.209 | 0.233 |
| Carrier C | 29 | 184880.177 | 5.599 | 23.034 | 0.483 |
| Carrier A | 28 | 142629.995 | 5.555 | 21.107 | 0.429 |

## Location Summary
| Location | sku_count | revenue | units_sold | avg_margin_proxy | avg_defect_rate | avg_end_to_end_lead_time | high_stock_risk_skus |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mumbai | 22 | 137755.027 | 9426 | 0.889 | 2.122 | 40.591 | 9 |
| Kolkata | 25 | 137077.551 | 12770 | 0.857 | 2.286 | 40.400 | 11 |
| Chennai | 20 | 119142.816 | 8768 | 0.851 | 2.638 | 37.300 | 9 |
| Bangalore | 18 | 102601.724 | 5420 | 0.854 | 2.094 | 33.333 | 2 |
| Delhi | 15 | 81027.701 | 9715 | 0.846 | 2.229 | 34.067 | 10 |
