# 📊 Amazon Sales Data Analytics & EDA Dashboard

An intermediate-level exploratory data analysis (EDA) and web dashboard application built to extract insights from Amazon product listings, sales, ratings, and pricing metrics.

Live Application: [amazon-sales-data.streamlit.app](https://amazon-sales-data.streamlit.app)

---

## 🚀 Project Overview

This repository contains a data analytics and web-based visualization dashboard that parses, profiles, and breaks down Amazon Sales Data. The tool allows stakeholders to seamlessly filter through specific product categories, explore price versus discount distributions, and uncover patterns tied to consumer ratings.

### Key Metrics Tracked
* **Total Products Analyzed:** 1465+ entries
* **Average Product Rating:** 4.09 ⭐

---

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** [Streamlit](https://streamlit.io/)
* **Data Processing:** Pandas, NumPy
* **Visualization:**  Matplotlib / Seaborn

---

## 🧩 Features & Dashboard Structure

The multi-page or structured sidebar navigation breaks the analysis down into core sections:

1. **📋 Dataset Preview:** An interactive data explorer tracking essential unique keys such as `product_id`, `product_name`, and product `category`. 
2. **📉 Price & Discount Analysis:** Comprehensive evaluation of how manufacturers or merchants position prices against applied discount ratios.
3. **⭐ Ratings & Reviews:** Granular review scoring patterns to isolate high-performing inventory lines.

---


   streamlit run app.py
   ```
