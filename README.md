<p align="center">
  <img src="https://github.com/user-attachments/assets/500f3ce0-5fa6-4158-9e11-0f624e20f879" width="150" />
</p>

# Industrial Internship Report.

**Author:** Avgustin Chynarbekov  
**Co-authors:** Mekia Shigute Gaso, Burul Shambetova  
**Affiliation:** Ala-Too International University, Bishkek, Kyrgyzstan  

This repository supports the Data Science internship work that led to a published preprint on global temperature anomalies and visualization. It holds the data pipeline, scripts, figures, and documentation required to reproduce the analysis.

---

## Pre-preprint work and reproducibility

The research problem is the communication of long-term global temperature change through a reproducible visualization pipeline based on HadCRUT5 global summary data.

**Contents of this repository**

- Raw input data under `metoffice_dataset/`
- Preprocessing: `converted_dataset/convert_hadcrut5.py` → `converted_dataset/temperature_data.csv`
- Figures: `graphs/visualizations.py` and outputs under `graphs/` (including `FIGURES.zip` where packaged)
- Manuscript drafts: `research_article_avgustin_chynarbekov.pdf`, `research_article_avgustin_chynarbekov.docx`

**Reproduction**

1. Install Python 3 with `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scipy` as used in the scripts.
2. Run `convert_hadcrut5.py` from `converted_dataset/` if rebuilding the processed CSV from the raw file.
3. Run `visualizations.py` from `graphs/` to regenerate the figures from the processed data.

Literature context, research gap, exploratory choices, and evaluation of the visual narrative are aligned with the internship report submitted for the course.

**Repository URL:** [https://github.com/NpAvgust/Pre-print-31.03.2026](https://github.com/NpAvgust/Pre-print-31.03.2026)

---

## Published preprint

**Title:** Visualizing Global Climate Change Trends: A Data-Driven Analysis of Temperature Anomalies and Regional Patterns  

**Authors:** Avgustin Chynarbekov, Mekia Shigute Gaso, Burul Shambetova  

**Platform:** Research Square  

**Article:** [https://www.researchsquare.com/article/rs-8662602/v1](https://www.researchsquare.com/article/rs-8662602/v1)  

**DOI:** [https://doi.org/10.21203/rs.3.rs-8662602/v1](https://doi.org/10.21203/rs.3.rs-8662602/v1)  

**Abstract (summary):** The study analyses global temperature anomalies from 1880 to 2024 using public HadCRUT-related data, applies multiple visualization methods (time series, heatmaps, grouped bar charts, regional comparisons), and reports long-term warming, recent acceleration, and hemispheric and land–ocean contrasts. Implementation uses Python (Matplotlib, Seaborn, Pandas).

**Posting confirmation:** Email from Research Square confirming the preprint is live and the DOI is assigned — see `preprint-publication-yes.pdf` in this folder.

---

## Peer review process

Structured feedback was collected using a single review instrument sent to two external readers: one from industry(researchsquare.com) and one from a university.

**Review instrument (questions)**

1. Does the paper clearly state the research problem and its relevance to the field?  
2. Is the proposed method or approach technically sound and well-justified?  
3. Are the experiments and evaluation metrics appropriate for the claims made?  
4. Are the results reproducible based on the description provided?  
5. How does this work compare to the most relevant prior work cited?  
6. Are there any significant limitations or threats to validity that are not acknowledged?  
7. Is the writing clear, structured, and accessible to a reader familiar with data science?  
8. What is the single most important change you would recommend before journal or conference submission?  

Written responses to all items were obtained from both readers and are retained with the full internship submission package.

---

## Post-review refinement

A revision record links each major comment to the change made in the manuscript or figures and the location (section, figure, or paragraph). Where a suggestion was not incorporated, a short written justification was recorded. The updated manuscript files in this repository reflect those edits.

---

## Journal or conference channel

The manuscript has been submitted to PLOS Climate for journal consideration. Submission evidence (confirmation and the current status in the PLOS submission system) is kept with the official internship dossier alongside this repository. 
https://plos.org/ https://www.ariessys.com/

---

## Optional demonstration

No separate Streamlit or other hosted demo is linked here; the analytical artefact is the scripts and figures above.

---

## Licence and citation

The preprint on Research Square is published under the licence stated on the article page (CC BY 4.0 as indicated there). Cite using the DOI above.
