# 🚆 Transportation Exposure & Environmental Justice in Massachusetts

An environmental justice analysis using **ArcGIS Pro and EPA EJScreen data** to examine transportation-related exposure across Massachusetts and compare patterns among income and minority population groups.

## Project Overview

This project investigates whether transportation-related environmental burdens are distributed evenly across Massachusetts communities.

The analysis began with **PM₂.₅ concentrations** as a statewide air-quality indicator. Because PM₂.₅ showed very little variation among demographic groups, the project expanded to incorporate EPA EJScreen's **Traffic Proximity Index (PTRAF)** as a more localized measure of transportation exposure.

Using ArcGIS Pro, demographic and environmental indicators were analyzed alongside major transportation infrastructure, including highways, MBTA commuter rail, and the South Coast Rail corridor.

The project demonstrates how **GIS, demographic data, and environmental indicators can be combined to investigate environmental justice patterns that may not be visible through statewide averages alone.**

---

## Research Questions

- How does traffic proximity exposure vary across Massachusetts census tracts?
- Do traffic-proximity patterns differ among income groups?
- Do traffic-proximity patterns differ among minority population groups?
- How do major transportation corridors correspond with patterns of environmental burden?
- Does a localized transportation indicator reveal patterns that statewide PM₂.₅ averages do not?

---

## Tools & Skills

**ArcGIS Pro • Python • pandas • matplotlib • Microsoft Excel • EPA EJScreen • Spatial Analysis • Environmental Justice Analysis • Demographic Data • Summary Statistics • Data Visualization • Environmental Mapping**

- **ArcGIS Pro** — spatial data preparation, demographic classification, transportation overlays, summary statistics, and map development.
- **Python / pandas** — imported and worked with summary datasets generated during the analysis.
- **matplotlib** — created programmatic visualizations of environmental exposure patterns, including PM₂.₅ comparisons among demographic groups.
- **Microsoft Excel** — supported organization and review of summary outputs.
- **EPA EJScreen** — provided census-tract-level environmental and demographic indicators used in the environmental justice analysis.
- **GIS analysis** — integrated environmental exposure, demographic, and transportation datasets to examine spatial patterns across Massachusetts.

---

## Methodology

### 1. Data Preparation

EPA EJScreen data were imported into **ArcGIS Pro** and prepared for statewide analysis.

The workflow included:

- Clipping data to the Massachusetts state boundary.
- Removing null and geometry-only rows where appropriate.
- Creating demographic categories for comparative analysis.
- Classifying income groups as **Low, Mid, and High**.
- Classifying minority population groups as **Low, Mid, and High**.

### 2. Baseline PM₂.₅ Analysis

PM₂.₅ concentrations were initially analyzed across demographic groups to establish a statewide air-quality baseline.

Mean concentrations showed very little variation, ranging approximately from **6.78–6.82 μg/m³** among the groups examined.

Because this statewide indicator showed minimal demographic differentiation, the analysis was expanded to examine a more localized transportation-related exposure metric.

### 3. Traffic Proximity Analysis

EPA EJScreen's **Traffic Proximity Index (PTRAF)** was mapped across Massachusetts census tracts.

Transportation infrastructure was added for spatial context, including:

- I-90
- I-93
- I-95
- I-195
- Route 24
- MBTA commuter rail
- South Coast Rail

ArcGIS Pro Summary Statistics were then used to calculate:

- Mean PTRAF by income group.
- Mean PTRAF by minority population group.

These results were exported for additional visualization and comparison.

### 4. Visualization

The final project incorporated:

- Statewide PM₂.₅ mapping.
- Traffic-proximity exposure mapping.
- Transportation infrastructure overlays.
- Demographic exposure comparisons.
- Bar and line charts summarizing PTRAF patterns.
- A final project report integrating maps, charts, methods, and findings.

---

## Baseline Air Quality — PM₂.₅

🗺️ [View PM₂.₅ Across Massachusetts Map](maps/PM2.5_Across_Mass_2022_MapLayout.pdf)

The baseline analysis showed very little variation in mean PM₂.₅ concentration among the demographic groups examined.

This result suggested that statewide ambient PM₂.₅ averages alone were not sufficient to identify the more localized transportation-exposure patterns explored in the next stage of the project.

---

## Traffic Proximity Exposure

🗺️ [View Traffic Proximity Across Massachusetts Map](maps/TrafficProx_Across_Mass_2022_MapLayout.pdf)

The traffic-proximity analysis provided a more localized view of exposure around transportation networks and allowed demographic patterns to be compared at the census-tract level.

---

## Traffic Exposure by Demographic Group

📊 [View PTRAF Exposure Charts](outputs/PTRAF_charts.pdf)

The PTRAF comparison showed differences in traffic proximity among the demographic categories examined.

### Income Groups

- Low-income communities showed the highest mean traffic proximity exposure.
- High-income communities showed the lowest mean exposure.

### Minority Population Groups

- Mid-minority census tracts showed the highest mean traffic proximity in this analysis.
- The geographic distribution of income and minority populations produced different exposure patterns across Massachusetts.

---

## Key Findings

### 1. Statewide PM₂.₅ showed little demographic variation

Mean PM₂.₅ concentrations were approximately **6.78–6.82 μg/m³** across the demographic groups analyzed.

This provided a relatively uniform statewide baseline within this analysis.

### 2. Traffic proximity showed greater variation

Unlike the PM₂.₅ results, PTRAF revealed differences in transportation exposure among demographic groups.

Low-income communities showed the highest mean traffic proximity exposure, while high-income communities showed the lowest.

### 3. Income and minority indicators showed different geographic patterns

The analysis identified contrasting demographic and transportation landscapes across Massachusetts.

Western and Central Massachusetts included more rural areas with lower traffic exposure, while Eastern Massachusetts contained denser urban and transportation networks.

These geographic differences helped explain why income-based and minority-population comparisons did not produce identical exposure patterns.

### 4. Localized indicators revealed patterns obscured by statewide averages

The comparison between PM₂.₅ and PTRAF demonstrated the importance of indicator selection in environmental justice analysis.

A statewide pollution average may show relatively little variation while a more spatially specific transportation indicator reveals localized differences in exposure.

---

## Project Outputs

- 🗺️ [PM₂.₅ Across Massachusetts — 2022](maps/PM2.5_Across_Mass_2022_MapLayout.pdf)
- 🗺️ [Traffic Proximity Across Massachusetts — 2022](maps/TrafficProx_Across_Mass_2022_MapLayout.pdf)
- 📊 [PM₂.₅ Summary Table](outputs/summary_table_PM25.csv)
- 📊 [PTRAF Summary Table](outputs/summary_table_PTRAF.csv)
- 📈 [PTRAF Exposure Charts](outputs/PTRAF_charts.pdf)
- 🐍 [`scripts/ej_analysis.py`](scripts/ej_analysis.py) — Python analysis and visualization script using pandas and matplotlib
- 📄 [Final Project Summary](outputs/EJ_Transportation_Project_Summary2.pdf)
- 🗺️ `EJ_AirQuality_Mass.aprx` — ArcGIS Pro project file

---

## Data Sources

### EPA Air Quality System (AQS) — Annual Summary Data

PM₂.₅ annual summary data were used to establish the baseline air-quality analysis.

**Source:** EPA Air Quality System (AQS)

https://aqs.epa.gov/aqsweb/airdata/download_files.html

### EPA EJScreen

EPA EJScreen provided census-tract-level environmental and demographic indicators used in the environmental justice analysis, including traffic proximity and demographic variables.

**Source:** EPA EJScreen

https://www.epa.gov/ejscreen/download-ejscreen-data

### U.S. Census Bureau TIGER/ACS

Census geographic and demographic data provided additional tract-level context for the analysis.

**Source:** U.S. Census Bureau

https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html

### MBTA / MassGIS Transportation Data

Transportation datasets were used to provide spatial context for rail and transportation infrastructure.

**Source:** MassGIS — MBTA Rapid Transit

https://www.mass.gov/info-details/massgis-data-mbta-rapid-transit

---

## Data Year Selection

The **2022 annual PM₂.₅ summary dataset** was selected to provide a quality-assured annual baseline and maintain temporal consistency with the demographic and environmental datasets used in the analysis.

Using a common analysis period reduced temporal mismatch when comparing air quality, demographic characteristics, and transportation-related environmental indicators.

---

## Data Limitations

The PTRAF field contained **nine null values** within the Massachusetts data used for this project.

These records represent missing modeled values rather than zero traffic exposure.

Null records were excluded from summary calculations but retained in the spatial visualization as **No Data** to distinguish missing information from measured exposure.

The project is an exploratory statewide analysis and does not establish that transportation infrastructure causes the demographic exposure patterns observed.

---

## Future Development

Future versions of this project could extend the analysis through:

- Diesel particulate matter analysis.
- Population-weighted exposure calculations.
- Statistical testing of differences among demographic groups.
- Spatial regression or other quantitative environmental justice methods.
- A detailed Boston metropolitan-area analysis.
- Evaluation of transportation exposure following the South Coast Rail expansion.
- Development of an interactive GIS StoryMap or dashboard.

---

## Data & Citation

This project uses publicly available environmental, demographic, and transportation data from the **U.S. Environmental Protection Agency, U.S. Census Bureau, MBTA, and MassGIS**.

**Project Citation**

Pacheco, A. *Transportation Exposure and Environmental Justice in Massachusetts.*

---

## Author

**Alyssa Pacheco**

Environmental Scientist | Coastal & Marine Science | GIS & Environmental Data Analysis
