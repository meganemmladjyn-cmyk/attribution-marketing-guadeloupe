# Data sources

## attribution_data.csv

- Source: AjNavneet/MultiTouch-Attribution-Marketing-Spend-Optimization (GitHub), file `input/attribution_data.csv.zip`
- Download URL: https://raw.githubusercontent.com/AjNavneet/MultiTouch-Attribution-Marketing-Spend-Optimization/master/input/attribution_data.csv.zip
- Extraction: `python3 -m zipfile -e data/raw/attribution_data.csv.zip data/raw/`
- Licence: MIT (licence of the upstream repository)
- Size: 586,737 rows, 6 columns: cookie, time, interaction, conversion, conversion_value, channel
- Unique cookies (users): 240,108
- Channels (5): Facebook, Paid Search, Online Video, Instagram, Online Display
- Conversions: 17,639
- Ad spend: not in the file. The 50,000 EUR budget is a simulated scenario.
- The raw file is not versioned (see `.gitignore`).
