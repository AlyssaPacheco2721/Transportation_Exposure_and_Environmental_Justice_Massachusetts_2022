# Transportation Exposure and Environmental Justice in Massachusetts 2022

This project examines transportation-related environmental burdens across Massachusetts, focusing on how traffic exposure varies among income and minority populations. Building on an initial PM₂.₅ analysis that showed minimal statewide variation, this expanded study incorporates EPA EJScreen’s Traffic Proximity Index (PTRAF) to evaluate more localized disparities along highway corridors and urban transportation networks.

---
### Objective
- Assess traffic proximity exposure (PTRAF) across Massachusetts census tracts.
- Compare PTRAF levels across income groups and minority population groups.
- Identify how transportation corridors (interstates, MBTA lines, South Coast Rail) influence environmental burdens.
- Visualize results using GIS maps and charts to highlight environmental justice patterns.

---

### Project Contents
- **/maps/PM25_map_layout.jpg/** → Baseline air quality map
- **/maps/PTRAF_map_layout.jpg/** → Traffic proximity exposure
- **/maps/DSLPM_map_layout.jpg/** → Diesel PM exposure
  
- **/outputs/summary_table_PTRAF.csv/** → Mean traffic proximity by group
- **/outputs/summary_table_DSLPM.csv/** → Mean diesel PM by group
- **/outputs/ptraf_by_income_chart.png/** → Bar chart – PTRAF vs Income
- **/outputs/dslpm_by_minority_chart.png/** → Bar chart – DSLPM vs Minority
- **/outputs/Project_Summary.pdf**  → Final project summary PDF
---

### Methodology
1. Data Preparation
   - Imported EPA EJScreen 2022 data into ArcGIS Pro
   - Clipped to Massachusetts state boundary
   - Removed null and geometry-only rows
   - Created demographic categories:
   - Income_Group: Low / Mid / High
   - Minority_Group: Low / Mid / High

2. Baseline Air Quality (PM₂.₅)
   - PM₂.₅ concentrations were nearly identical across groups (6.78–6.82 μg/m³)
   - Indicates uniform statewide ambient air quality
   - Exported baseline map + summary table

3. Traffic Proximity (PTRAF) Analysis
   - Mapped PTRAF statewide
   - Overlaid transportation infrastructure:
   - Major highways (I-90, I-93, I-95, I-195, Route 24)
   - MBTA commuter rail
   - South Coast Rail expansion
   - Used Summary Statistics to calculate:
   - Mean PTRAF by Income Group
   - Mean PTRAF by Minority Group
   - Exported results to Excel for chart creation

4. Visualization
   - PM₂.₅ baseline map
   - PTRAF exposure map
   - Bar + line charts comparing exposure across groups
   - Final Project Summary PDF integrating maps, charts, and narrative results

---

### Key Findings
1. Air quality (PM₂.₅) is uniform statewide
   - Little to no disparity across income groups, confirming ambient pollution is relatively consistent across Massachusetts.

2. Traffic exposure is NOT uniform
   - PTRAF reveals clear disparities:
   - Low-income communities = highest traffic exposure
   - High-income communities = lowest exposure
   - Mid-minority tracts = highest exposure due to their presence in dense urban transportation corridors

3. Income and minority indicators diverge geographically
   - Massachusetts has two contrasting demographic landscapes:
   - Western/Central MA → rural, low-income, low-minority, low traffic
   - Eastern MA (Boston metro, Gateway Cities) → racially diverse, mid-income, high traffic
   - This explains why income-based and minority-based exposure patterns differ.

4. Transportation infrastructure drives EJ disparities
   - Highways, interchanges, and high-density transit corridors create localized exposures invisible in statewide PM₂.₅ averages.

---

### Tools Used
ArcGIS Pro | Excel 

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

  -**MBTA / MassGIS Transportation Data**
  ADD URL
  Rail lines and highway corridors for context

---

### Data Year Justification
The EPA Air Quality System (AQS) updates particulate (PM2.5) data twice annually, in **May** and **November**, and allows up to six months for reporting from local agencies. Data are published in multiple formats, including raw, daily, and annual summary files. Only after full quality assurance review are annual summaries considered complete and nationally consistent.  

For this project, the **2022 Annual Summary** dataset was selected as it represents the **most recent fully validated and quality-assured data** available at the time of analysis.  
The 2023 and 2024 datasets are still provisional and may contain incomplete or uncertified records.  
Using 2022 ensures consistency with both **EPA EJScreen** and **U.S. Census ACS 2022** data, providing a reliable, methodologically aligned baseline for analysis.

---

### Data Limitations
The PTRAF field (Traffic Proximity Index) contained nine null values in the EPA EJScreen 2022 dataset for Massachusetts, including one tract in central Massachusetts. These gaps represent missing modeled data, not zero traffic exposure. Null tracts were excluded from summary calculations but retained in maps as “No Data” for transparency.

---

### Future Improvements
- Add DSLPM (diesel exhaust) analysis
- Incorporate population-weighted exposure
- Add Boston metro zoom-in chapter in StoryMap
- Analyze transportation change post–South Coast Rail

---

### Author
**Alyssa Pacheco**

Environmental Data Scientist | GIS & Analytics for Ecology & Conservation

📍 Massachusetts

🌐 alyssapacheco.com

🐙 github.com/alyssapacheco2721

