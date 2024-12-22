# ML_classification_cats_dogs

## Overview

This repository contains machine learning scripts and datasets for classifying cats and dogs using different feature extraction techniques (CNN, HOG, PCA) and machine learning models (Naive Bayes, Decision Tree, k-NN). The repository is organized to facilitate reproducibility and understanding of the processes involved in building and evaluating models.

---

## Repository Structure

```
├── CNN_FeatureVector_done.ipynb       # Notebook for extracting CNN features
├── CNN_features_extracted_AVG.csv    # CNN features (average pooling)
├── CNN_features_extracted_MAX.csv    # CNN features (max pooling)
├── DTree_holdout_done.ipynb          # Decision Tree evaluation with holdout
├── DTree_kFold_done.ipynb            # Decision Tree evaluation with k-fold
├── HOG_16_PCA.csv                    # HOG features reduced using PCA
├── HOG_Transform_16.csv              # HOG features with 16 orientations
├── HOG_Transform_20.csv              # HOG features with 20 orientations
├── HOG_done.ipynb                    # HOG feature extraction notebook
├── NB_holdout_done.ipynb             # Naive Bayes evaluation with holdout
├── NB_kFold_done.ipynb               # Naive Bayes evaluation with k-fold
├── PCA_LDA_HOG16_done.ipynb          # PCA & LDA on HOG features
├── README.md                         # This file
├── Resultados Prática 1 - Douglas Felipe.pdf # Practical results for report 1
├── Resultados Prática 2 - Douglas Felipe.pdf # Practical results for report 2
├── Resultados.xlsx                   # Summary of results in Excel format
├── Resultados_NB_DT.xlsx             # Naive Bayes and Decision Tree results
├── kNN_fold.ipynb                    # k-NN evaluation with k-fold
├── kNN_holdout_done.ipynb            # k-NN evaluation with holdout
└── select_images.py                  # Script for image selection
```

---

## Notebooks and Features

### CNN Feature Extraction
- **`CNN_FeatureVector_done.ipynb`**:
  - Uses a pre-trained VGG16 model to extract CNN features for images.
  - Outputs features in CSV format for further analysis.

### HOG Feature Extraction
- **`HOG_done.ipynb`**:
  - Extracts HOG (Histogram of Oriented Gradients) features with different parameters.
  - Generates CSV files containing HOG descriptors.

### Dimensionality Reduction
- **`PCA_LDA_HOG16_done.ipynb`**:
  - Applies PCA to reduce the dimensionality of HOG features.
  - The results are saved in `HOG_16_PCA.csv`.

### Model Evaluations
- **Naive Bayes**:
  - `NB_holdout_done.ipynb`: Evaluates Naive Bayes classifier using holdout validation.
  - `NB_kFold_done.ipynb`: Evaluates Naive Bayes classifier using k-fold cross-validation.

- **Decision Tree**:
  - `DTree_holdout_done.ipynb`: Evaluates Decision Tree classifier with holdout validation.
  - `DTree_kFold_done.ipynb`: Evaluates Decision Tree classifier with k-fold cross-validation.

- **k-NN**:
  - `kNN_holdout_done.ipynb`: Evaluates k-NN classifier with holdout validation.
  - `kNN_fold.ipynb`: Evaluates k-NN classifier with k-fold cross-validation.

---

## Results and Reports
- **Results**:
  - `Resultados.xlsx`: Summary of experiment results in an Excel file.
  - `Resultados_NB_DT.xlsx`: Specific results for Naive Bayes and Decision Tree classifiers.
- **Reports**:
  - `Resultados Prática 1 - Douglas Felipe.pdf`: Documentation of Practical Report 1.
  - `Resultados Prática 2 - Douglas Felipe.pdf`: Documentation of Practical Report 2.

---

## How to Run the Code

1. **Setup**:
   - Install required libraries from the `requirements.txt` file (if available).
   - Ensure Python 3.8+ and Jupyter Notebook are installed.

2. **Run Notebooks**:
   - Open any `.ipynb` file in Jupyter Notebook or JupyterLab.
   - Follow the instructions and execute the cells sequentially.

3. **Custom Scripts**:
   - Use `select_images.py` for selecting specific images from a dataset.

---

## Contributions
Feel free to submit pull requests or report issues for improvements or fixes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
