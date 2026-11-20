<div align="center">

# 🔒 Lightweight ML for IoT Intrusion Detection

### An Extended Study on the IoTID20 Dataset

**Accuracy · Efficiency · Robustness · Adversarial · Multi-Seed · Cross-Dataset**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![pandas](https://img.shields.io/badge/pandas-3.1.1-orange.svg)](https://pandas.pydata.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.15-red.svg)](https://pytorch.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.4.1-green.svg)](https://xgboost.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 English | 📖 فارسی

---

# English

## Overview

This repository contains the complete reproducible research code for a comprehensive evaluation of three lightweight machine-learning models — **Logistic Regression**, **XGBoost**, and a small **PyTorch MLP** — for binary intrusion detection on the [IoTID20 dataset](https://www.kaggle.com/datasets/rohulaminlabid/iotid20-dataset).

The study goes beyond a simple train/test comparison by including:

- **Triple-method duplicate verification** (hash, value-based, per-class)
- **Multi-seed stability** (10 seeds, mean ± std with bootstrap CIs)
- **Adversarial robustness** (FGSM, PGD on MLP; feature perturbation on XGBoost)
- **Noise robustness with proper methodology** (raw-feature vs scaled-feature noise)
- **Concept drift / temporal split analysis**
- **Per-attack-family deep dive** (feature separation and confusion analysis)
- **Cross-dataset validation** support (TON_IoT, BoT_IoT, Edge-IIoTset)
- **Statistical significance tests** (McNemar, Wilcoxon, bootstrap 95% CI)

## Key Results

| Metric | Logistic Regression | XGBoost | Neural Network |
|--------|---------------------|---------|----------------|
| **MCC** | 0.8127 | **0.9356** | 0.8896 |
| **PR-AUC** | 0.9959 | **0.9994** | 0.9986 |
| **Latency (μs)** | 105 | 384 | **103** |
| **Model size (KB)** | **1** | 825 | 67 |
| **Multi-seed MCC (10 seeds)** | 0.808±0.003 | **0.935±0.002** | 0.880±0.012 |

### Critical Findings

1. **75.2% of IoTID20 rows are exact duplicates** — confirmed by three independent methods. Scan traffic has the highest duplicate rate (84.7%), Normal the lowest (33.1%).

2. **Temporal split collapses performance to MCC=0.000** — the model completely fails when evaluated chronologically. Random splits are massively optimistic (0.936 optimism).

3. **XGBoost is catastrophically fragile to noise** — MCC drops from 0.936 to 0.168 at σ=0.1 (raw-feature noise). Neural Network degrades gracefully (0.890→0.835). This is a real finding, not a methodology artifact.

4. **5 features are sufficient** — using only the top-5 SHAP features, MCC drops by less than 1% (0.927 vs 0.936).

5. **Cost-sensitive thresholding reduces expected alert cost by 88%** without retraining.

## Repository Structure

```
├── notebook/
│   └── IoTIDS20-V3.ipynb       # Main analysis notebook (60 cells, 20 sections)
├── figures/                     # 21 publication-ready PNG figures (300 DPI)
├── results/                     # 28 CSV result tables + key_findings.txt
├── models/                      # Trained model artifacts (gitignored)
├── data/                        # Dataset files (gitignored)
├── requirements.txt
├── run_study.py
├── LICENSE
└── README.md
```

## Quick Start

```bash
# 1. Clone
git clone https://github.com/hannah8877h-dev/iotid20-ids-study.git
cd iotid20-ids-study

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download IoTID20
#    https://www.kaggle.com/datasets/rohulaminlabid/iotid20-dataset
#    Place "IoT Network Intrusion Dataset.csv" inside data/

# 4. Run
jupyter notebook notebook/IoTIDS20-V3.ipynb
```

### Fast mode (smoke test, ~10 min)

```bash
FAST_MODE=1 jupyter notebook notebook/IoTIDS20-V3.ipynb
```

### Full run (~30-50 min)

```bash
jupyter notebook notebook/IoTIDS20-V3.ipynb
```

## Optional: Cross-Dataset Validation

Place any of these inside `data/` for Section 14:

| Dataset | Kaggle Link |
|---------|-------------|
| TON_IoT | `gwdaraktle/toniot-datasets` |
| BoT_IoT | `aldostronsky/botiot` |
| Edge-IIoTset | `mohamedaminebouzid/edge-iiotset-iotiot-cyber-security-dataset` |

## Citation

If you use this code, please cite:

```bibtex
@misc{shabestani2026iotid20,
  title={Lightweight Machine Learning for IoT Intrusion Detection:
         An Extended Accuracy, Efficiency, Robustness, and Adversarial Study},
  author={Shabestani, Hannaneh},
  year={2026},
  url={https://github.com/hannah8877h-dev/iotid20-ids-study}
}
```

And the original dataset:

```bibtex
@inproceedings{ullah2020iotid20,
  title={A Scheme for Generating a Dataset for Anomalous Activity Detection in IoT Networks},
  author={Ullah, I. and Mahmoud, Q.H.},
  booktitle={Canadian AI 2020, LNCS 12109},
  year={2020},
  publisher={Springer}
}
```

---

# فارسی

## نمای کلی

این ریپازیتوری حاوی کد کامل و قابل بازتولید پژوهشی برای ارزیابی جامع سه مدل یادگیری ماشین سبک — **رگرسیون لجستیک**، **XGBoost**، و یک **شبکه عصبی PyTorch** — برای تشخیص نفوذ دودویی روی [دیتاست IoTID20](https://www.kaggle.com/datasets/rohulaminlabid/iotid20-dataset) است.

این مطالعه فراتر از یک مقایسه ساده train/test شامل موارد زیر است:

- **اعتبارسنجی سه‌روشی رکوردهای تکراری** (hash، value-based، per-class)
- **پایداری چند-seed** (۱۰ seed، میانگین ± انحراف معیار با bootstrap CI)
- **مقاومت در برابر حملات تخاصمی** (FGSM، PGD روی MLP؛ feature perturbation روی XGBoost)
- **مقاومت در برابر نویز با روش‌شناسی صحیح** (نویز روی ویژگی‌های خام vs استانداردشده)
- **تحلیل رانش مفهومی / تقسیم زمانی**
- **تحلیل عمیق هر خانواده حمله** (جداسازی و اشتباه ویژگی‌ها)
- **اعتبارسنجی متقابل** (پشتیبانی TON_IoT، BoT_IoT، Edge-IIoTset)
- **آزمون معناداری آماری** (McNemar، Wilcoxon، bootstrap 95% CI)

## نتایج کلیدی

| معیار | رگرسیون لجستیک | XGBoost | شبکه عصبی |
|--------|---------------------|---------|----------------|
| **MCC** | 0.8127 | **0.9356** | 0.8896 |
| **PR-AUC** | 0.9959 | **0.9994** | 0.9986 |
| **تأخیر (μs)** | 105 | 384 | **103** |
| **حجم مدل (KB)** | **1** | 825 | 67 |
| **MCC چند-seed (۱۰ seed)** | 0.808±0.003 | **0.935±0.002** | 0.880±0.012 |

### یافته‌های حیاتی

1. **۷۵٫۲٪ رکوردهای IoTID20 تکراری دقیق هستند** — با سه روش مستقل تأیید شد. ترافیک Scan بیشترین نرخ تکرار را دارد (۸۴٫۷٪)، Normal کمترین (۳۳٫۱٪).

2. **تقسیم زمانی، عملکرد را به MCC=0.000 می‌رساند** — مدل در ارزیابی زمانی کاملاً شکست می‌خورد. تقسیم تصادفی به‌شدت خوش‌بینانه است (۰٫۹۳۶ optimism).

3. **XGBoost در برابر نویز به‌شدت شکننده است** — MCC از ۰٫۹۳۶ به ۰٫۱۶۸ در σ=0.1 افت می‌کند. شبکه عصنی ملایم‌تر افت می‌کند (۰٫۸۹۰→۰٫۸۳۵). این یافته واقعی است، نه خطای روش‌شناسی.

4. **۵ ویژگی کافی است** — با تنها ۵ ویژگی برتر SHAP، MCC کمتر از ۱٪ افت می‌کند (۰٫۹۲۷ در مقابل ۰٫۹۳۶).

5. **آستانه‌گذاری هزینه‌محور، هزینه هشدار را ۸۸٪ کاهش می‌دهد** — بدون نیاز به بازآموزی.

## ساختار ریپازیتوری

```
├── notebook/
│   └── IoTIDS20-V3.ipynb       # نوت‌بوک اصلی (۶۰ سلول، ۲۰ بخش)
├── figures/                     # ۲۱ نمودار PNG با کیفیت انتشار (۳۰۰ DPI)
├── results/                     # ۲۸ جدول CSV + key_findings.txt
├── models/                      # مدل‌های آموزش‌دیده (gitignored)
├── data/                        # فایل‌های دیتاست (gitignored)
├── requirements.txt
├── run_study.py
├── LICENSE
└── README.md
```

## شروع سریع

```bash
# 1. کلون کنید
git clone https://github.com/hannah8877h-dev/iotid20-ids-study.git
cd iotid20-ids-study

# 2. وابستگی‌ها را نصب کنید
pip install -r requirements.txt

# 3. دیتاست IoTID20 را دانلود کنید
#    https://www.kaggle.com/datasets/rohulaminlabid/iotid20-dataset
#    فایل "IoT Network Intrusion Dataset.csv" را در data/ قرار دهید

# 4. اجرا
jupyter notebook notebook/IoTIDS20-V3.ipynb
```

### حالت سریع (تست سریع، ~۱۰ دقیقه)

```bash
FAST_MODE=1 jupyter notebook notebook/IoTIDS20-V3.ipynb
```

### اجرای کامل (~۳۰-۵۰ دقیقه)

```bash
jupyter notebook notebook/IoTIDS20-V3.ipynb
```

## اختیاری: اعتبارسنجی متقابل

هر یک از این‌ها را در `data/` قرار دهید برای بخش ۱۴:

| دیتاست | لینک Kaggle |
|---------|-------------|
| TON_IoT | `gwdaraktle/toniot-datasets` |
| BoT_IoT | `aldostronsky/botiot` |
| Edge-IIoTset | `mohamedaminebouzid/edge-iiotset-iotiot-cyber-security-dataset` |

## ارجاع

اگر از این کد استفاده می‌کنید، لطفاً ارجاع دهید:

```bibtex
@misc{shabestani2026iotid20,
  title={Lightweight Machine Learning for IoT Intrusion Detection:
         An Extended Accuracy, Efficiency, Robustness, and Adversarial Study},
  author={Shabestani, Hannaneh},
  year={2026},
  url={https://github.com/hannah8877h-dev/iotid20-ids-study}
}
```

---

## 👩‍💻 Author / نویسنده

**Hannaneh Shabestani**

- University: Hamedan University of Technology
- GitHub: [@hannah8877h-dev](https://github.com/hannah8877h-dev)

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE).

این پروژه تحت مجوز MIT منتشر شده است — به [LICENSE](LICENSE) مراجعه کنید.
