# Intro to Machine Learning

## Summary

> The first project of the introductory ML course covers binary and multiclass classification, regression, and clustering.  
> Model evaluation methods and overfitting prevention techniques are also explored.  
> All practice is based on real user activity data.

## Tools & Languages

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)

## Exercises

| Exercise | Task |
|---|---|
| **00** | Binary classifier: predict whether a commit was made on a working day or a weekend. |
| **01** | Compare 3 algorithms (logistic regression, SVM, and decision tree) and visualize their decision boundaries. |
| **02** | Multiclass classification: predict the day of the week for a commit. Adding categorical features via one-hot encoding. |
| **03** | Overfitting prevention: train/test split, cross-validation, and hyperparameter tuning. |
| **04** | Regression: predict the average delta between the deadline and the first commit for each user. |
| **05** | Clustering: split users into groups with similar behavior (K-means, DBSCAN, hierarchical) without labeled data. |

## Metrics

| # | Task type | Metric | Result |
|---|---|---|---|
| 00 | Binary classification | Accuracy | 74% |
| 01 | Algorithm comparison | Accuracy | 94% (decision tree) |
| 02 | Multiclass classification | Accuracy | ~93% (random forest) |
| 03 | Validation | Accuracy | 94% |
| 04 | Regression | MSE | ~53 units |
| 05 | Clustering | Silhouette score | 0.46 (hierarchical) |