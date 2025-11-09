# Heart-Disease-ML-Streamlit
**Prédiction des Maladies Cardiaques par Machine Learning**  
**Application Web Interactive Streamlit**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red)
![License](https://img.shields.io/badge/License-MIT-yellow)



## Description
Projet académique (2ITE – 3ème année, 2025-2026)  
**Supervisé par** Pr. SKITTOU Mustapha  
**Réalisé par** Miskar Amina & Aziz Mohammed

**Objectif** : Prédire la présence d’une maladie cardiaque (classification binaire) à partir de 13 variables cliniques sur **1025 patients**.  
**Meilleur modèle** : **Régression Logistique** → **86 % accuracy**  
**Déploiement** : Application web interactive **Streamlit** pour prédiction en temps réel.


## Détails Machine Learning
### Dataset
- Source : UCI Heart Disease (1025 patients, 14 colonnes)
- Variables : `age`, `sex`, `cp`, `trestbps`, `chol`, `thalach`, `oldpeak`, ...

### Feature Engineering
- Création du `risk_score` (score de risque composite)
- Gestion des outliers, valeurs manquantes, doublons

### 7 Modèles testés
- Régression Logistique (vainqueur)
- Naïve Bayes • KNN • SVM • Arbre de Décision • Random Forest • XGBoost

### Performances
- Accuracy : 86 %
- F1-score équilibré
- ROC-AUC > 0.92
- Visualisations : Heatmap, Pairplot, Parallel Coordinates, Decision Boundary

## Déploiement Streamlit
```bash
streamlit run app.py
