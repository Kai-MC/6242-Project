# AccidentScope

**An Interactive Visualization Platform for Comprehensive Road Safety Analysis**

---

## Overview

AccidentScope is a web‑based dashboard and machine learning pipeline for exploring and predicting traffic accident severity across the United States. It combines:

- **Geospatial visualization** (D3.js + TopoJSON) for interactive exploration of accident hotspots and environmental conditions.
- **Gradient‑boosted models** (LightGBM) for multiclass severity classification.
- **Data parsing scripts** to preprocess raw accident data into analysis‑ready form.

This repository contains all code, assets, and documentation needed to reproduce the AccidentScope pipeline and launch the dashboard locally.

---

## Features

- **Interactive map**: Filter by time, weather, road conditions, and more.  
- **Real‑time updates**: Adjust controls to instantly see how filters affect accident patterns.  
- **Severity prediction**: Pretrained LightGBM model to score new accident records.  
- **Modular data pipeline**: Reusable CSV parsing, feature engineering, and modeling scripts.  

---

## Strctures
```
.
├── .gitignore
├── Prediction model.ipynb    # Jupyter notebook for training & evaluating the LightGBM model
├── README.md                 # (this file)
├── page.html                 # Static HTML & JavaScript (D3.js + TopoJSON) dashboard
├── parse_csv.py              # Data ingestion & preprocessing script
└── img/                      # Screenshots and example visuals used in the docs
```

---

## INSTALLATION

1. download data csv at:

`https://drive.google.com/file/d/1c0qDcE_5LGycpj9uBY3JVoRfY-_Kbiq0/view?usp=drive_link`

2. download code from zipfile or github 

`https://github.com/Kai-MC/6242-Project.git`


---
## EXECUTION

1. Serve `page.html` on a local HTTP server.
   ```bash
   # Python 3.x
   python -m http.server 8000
   ```
2. Open your browser to `http://localhost:8000/page.html`.
3. Use the left‑hand filters (sliders, dropdowns, checkboxes) to explore accident patterns on the map.


