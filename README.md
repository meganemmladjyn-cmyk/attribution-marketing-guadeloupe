# Attribution Marketing Guadeloupe

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/-SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white)
![Power BI](https://img.shields.io/badge/-Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/status-in--progress-yellow.svg)

## Problem

KaribStyle, a fictional e-commerce retailer in the French Caribbean, spreads its marketing budget across several channels. It does not know which channels actually drive conversions.

## Solution

This project compares four attribution models (first-click, last-click, linear, time-decay) on public customer-journey data. A budget optimizer then suggests how to reallocate a simulated 50,000 EUR budget across channels.

## Data

- **Source:** AjNavneet/MultiTouch-Attribution-Marketing-Spend-Optimization (GitHub), file `attribution_data.csv`.
- **Size:** 586,737 rows, 6 columns. Each row is one interaction, not one customer journey.
- **Customer journeys (unique users):** TBD
- **Channels:** TBD
- **Ad spend:** TBD. If the file has no spend column, the 50,000 EUR budget is a simulated scenario and is labeled as such everywhere.
- **Licence of the source data:** TBD
- The raw file is not versioned. See `data/sources.md` for the download steps.

## Results

| Metric | Value |
| --- | --- |
| Attribution models compared | 4 |
| Largest gap between two models (channel credit) | TBD |
| ROAS per channel and per model | TBD |
| Simulated reallocation impact | TBD |

No figure is published until a notebook computes it.

## Demo

Dashboard screenshots and a short GIF will be added here.

## Quick Start

```bash
git clone https://github.com/meganemmladjyn-cmyk/attribution-marketing-guadeloupe.git
cd attribution-marketing-guadeloupe
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then place `attribution_data.csv` in `data/raw/`.

## Stack

| Layer | Technology |
| --- | --- |
| Data processing | Python, pandas |
| Attribution models | Custom Python modules |
| Budget optimization | SciPy (`scipy.optimize`) |
| Dashboard | Power BI, DAX |

## Next Steps

- [ ] Build the journeys table
- [ ] Write the four attribution models
- [ ] Compare the models and validate totals
- [ ] Add the budget optimizer
- [ ] Build the Power BI dashboard
- [ ] Add screenshots and final results

## Contact

Built by Mégane Ladjyn, Data Marketing Analyst based in Guadeloupe.
Open to freelance and remote opportunities: [LinkedIn](https://linkedin.com/in/megane-ladjyn)
