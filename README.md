# Transportation Exposure & Environmental Justice in Massachusetts 2022
Exploring the intersection of transportation infrastructure, air quality, and community demographics using GIS & EPA EJScreen data

This project investigates whether transportation-related air pollution and traffic exposure vary across different income and minority populations in Massachusetts.

The analysis expands upon an earlier PM₂.₅ air-quality assessment, which found relatively uniform pollution levels statewide. By incorporating additional indicators from the EPA’s EJScreen dataset—specifically Diesel Particulate Matter (DSLPM) and Traffic Proximity (PTRAF)—this project explores whether transportation corridors such as major highways and the South Coast Rail expansion correspond with higher environmental burdens in vulnerable communities.

---
### Objective
- Evaluate traffic proximity (PTRAF) and diesel particulate matter (DSLPM) exposure across census tracts.
- Compare results by income and minority composition to identify possible environmental justice disparities.
- Map and visualize results to highlight localized transportation-related exposure patterns.
- Frame findings within the context of Massachusetts’ transportation development, particularly the South Coast Rail project.

---

### Project Contents
- **/maps/PM25_map_layout.jpg/** → Baseline air quality map
- **/maps/PTRAF_map_layout.jpg/** → Traffic proximity exposure
- **/maps/DSLPM_map_layout.jpg/** → Diesel PM exposure
- **/outputs/summary_table_PTRAF.csv/** → Mean traffic proximity by group
- **/outputs/summary_table_DSLPM.csv/** → Mean diesel PM by group
- **/outputs/ptraf_by_income_chart.png/** → Bar chart – PTRAF vs Income
- **/outputs/dslpm_by_minority_chart.png/** → Bar chart – DSLPM vs Minority
- **/Environmental_Justice_AirQuality_Mass.aprx** → ArcGIS Pro project file
- /**StoryMap_Link.txt** → ADD URL
---

### Methodology
1. Data Preparation
- Unzipped and imported EJScreen 2022 data into ArcGIS Pro.
- Clipped data to Massachusetts boundary.
- Removed null or geometry-only records.
- Created two categorical variables:
   - Income_Group: High / Mid / Low based on LOWINCPCT
   - Minority_Group: High / Mid / Low based on MINORPCT

2. Baseline Analysis
- Examined PM₂.₅ concentrations by income group.
- Found minimal variation (6.78–6.82 µg/m³), suggesting uniform air quality statewide.
- Created baseline map layout and summary bar chart.

3. Transportation Exposure Analysis
- Mapped Traffic Proximity (PTRAF) and Diesel PM (DSLPM) to identify regional patterns.
- Overlaid commuter rail lines and major highways (I-195, Route 24, South Coast Rail corridor).
- Used Summary Statistics to calculate mean PTRAF and DSLPM by both Income and Minority Groups.
- Exported summary tables to Excel for bar chart visualization.

4. Visualization & StoryMap Integration
- Designed multiple map layouts:
   - PM₂.₅ baseline map
   - PTRAF exposure map
   - DSLPM exposure map
- Created bar charts illustrating exposure differences across demographic groups.
- Combined spatial and chart outputs in an ArcGIS StoryMap to narrate findings.
  
---

### Key Findings (Preliminary)
- Uniform statewide PM₂.₅: Modeled concentrations were consistent across income groups, suggesting equitable ambient air quality.
- Localized transportation disparities: PTRAF and DSLPM values were higher in high-minority and low-income tracts near urban centers, major highways, and commuter rail expansion zones.
- These results highlight the importance of integrating transportation exposure metrics into environmental justice assessments, even in regions with generally clean air.

---

### Tools Used
ArcGIS Pro | ArcGIS Online StoryMaps | Excel | Python |

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

### Future Improvements


---

### Citation


---

### Author
**Alyssa Pacheco**
Environmental Data Scientist | GIS & Analytics for Ecology & Conservation
📍 New Bedford, Massachusetts
🌐 alyssapacheco.com
🐙 github.com/alyssapacheco2721

