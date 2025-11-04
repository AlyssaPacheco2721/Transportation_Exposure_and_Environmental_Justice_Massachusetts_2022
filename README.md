# Environmental Justice and Air Quality in Massachusetts

This project examines whether fine particulate matter (PM2.5) pollution disproportionately affects low-income and minority communities across Massachusetts. The analysis integrates EPA Air Quality data, EPA EJScreen demographic indicators, and U.S. Census tract boundaries to explore relationships between pollution exposure and socioeconomic variables.

---

### Project Contents
- **/AQI_map_layout.jpg/** → Spatial map showing PM2.5 concentrations by census tract.  
- **/correlation_plot.png/** → Bar chart of average PM2.5 by income group.  
- **/summary_table.csv/** → SQL summary table of mean pollution values.  
- **/analysis.sql/** → SQL script containing data cleaning, joins, and aggregation queries.  
- **/air_quality_trends.py/** → Python script used for data visualization.

---

### Methodology
1. Imported EPA AQS PM2.5 data (2022) as point features and joined to census tracts using spatial join in ArcGIS Pro.  
2. Combined tract-level pollution averages with demographic indicators from EPA EJScreen and Census ACS.  
3. Categorized income groups as:
   - *Low Income* (< $50,000)  
   - *Middle Income* ($50,000–$100,000)  
   - *High Income* (> $100,000)
4. Calculated average PM2.5 concentrations for each income group using SQL queries.  
5. Visualized results through both spatial mapping and a summary bar chart generated in Python.

---

### Key Findings (Preliminary)
- Low-income tracts displayed slightly higher mean PM2.5 concentrations than high-income tracts.  
- Areas with elevated PM2.5 exposure generally overlapped with dense urban corridors and major transportation routes.  
- The analysis supports continued monitoring of how socioeconomic and spatial factors intersect to influence air quality exposure.

---

### Tools Used
ArcGIS Pro | QGIS | SQLite | Python | Pandas | Matplotlib

---
### Data Sources
- **EPA Air Quality System (AQS) – Annual Summary Data (2022)**  
  [https://aqs.epa.gov/aqsweb/airdata/download_files.html](https://aqs.epa.gov/aqsweb/airdata/download_files.html)  
  Contains annual mean PM2.5 concentrations by monitoring site.

- **EPA EJScreen 2023 Dataset**  
  [https://www.epa.gov/ejscreen/download-ejscreen-data](https://www.epa.gov/ejscreen/download-ejscreen-data)  
  Provides census-tract-level demographic and environmental indicators, including low-income population percentage and particulate exposure indexes.

- **U.S. Census Bureau TIGER/ACS 2022**  
  [https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)  
  Supplies tract boundaries and demographic data (median household income, population counts, etc.).

---

### Data Year Justification
The EPA Air Quality System (AQS) updates particulate (PM2.5) data twice annually, in **May** and **November**, and allows up to six months for reporting from local agencies. Data are published in multiple formats, including raw, daily, and annual summary files. Only after full quality assurance review are annual summaries considered complete and nationally consistent.  

For this project, the **2022 Annual Summary** dataset was selected as it represents the **most recent fully validated and quality-assured data** available at the time of analysis.  
The 2023 and 2024 datasets are still provisional and may contain incomplete or uncertified records.  
Using 2022 ensures consistency with both **EPA EJScreen** and **U.S. Census ACS 2022** data, providing a reliable, methodologically aligned baseline for analysis.

---

### Future Improvements
- Incorporate 2023–2024 AQS data once fully validated for time-series trend analysis.  
- Integrate additional indicators (ozone, NO₂, or traffic proximity).  
- Build an interactive dashboard using ArcGIS Online or Power BI to visualize results by community.

---

### Citation
Pacheco, A. (2025). *Environmental Justice and Air Quality in Massachusetts: An exploratory analysis of PM2.5 exposure and socioeconomic inequality using GIS, SQL, and Python.* GitHub Repository.  

---

### Author
**Alyssa Pacheco**  
Environmental Science | GIS & Data Science 

