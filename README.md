# Heart-Disease-ML-Streamlit
**Prédiction des Maladies Cardiaques par Machine Learning**  
**Application Web Interactive Streamlit**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red)
![License](https://img.shields.io/badge/License-MIT-yellow)



## Description
Projet académique (2ITE – 3ème année, 2025-2026)  


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
- 
### Comparaison détaillée des 7 modèles (accuracy sur test set)

| Modèle                  | Accuracy | Precision | Recall | F1-score | ROC-AUC | Points forts                              |
|-------------------------|----------|-----------|--------|----------|---------|-------------------------------------------|
| **Régression Logistique** | **86.2 %** | 0.88      | 0.85   | **0.86** | **0.92** | Interprétable, rapide, meilleur équilibre |
| Random Forest           | 85.1 %   | 0.87      | 0.84   | 0.85     | 0.91    | Robuste, feature importance claire        |
| XGBoost                 | 84.8 %   | 0.86      | 0.84   | 0.85     | 0.91    | Très bon sur données déséquilibrées       |
| SVM (RBF)               | 83.5 %   | 0.85      | 0.83   | 0.84     | 0.89    | Frontière non linéaire efficace           |
| Arbre de Décision       | 82.0 %   | 0.83      | 0.82   | 0.82     | 0.87    | Très interprétable                        |
| KNN (k=5)               | 80.5 %   | 0.82      | 0.80   | 0.81     | 0.86    | Sensible au scaling                       |
| Naïve Bayes             | 79.0 %   | 0.80      | 0.79   | 0.79     | 0.85    | Rapide mais suppose indépendance          |

**Choix final** : **Régression Logistique** → meilleur compromis **performance + interprétabilité** pour une application clinique.

### Visualisations clés
- Heatmap des corrélations  
- Pairplot (séparation visuelle des classes)  
- Coordonnées parallèles (profils sains vs malades)  
- Frontière de décision SVM (âge vs thalach)  
- Feature importance (Random Forest & XGBoost)

### Performances
- Accuracy : 86 %
- F1-score équilibré
- ROC-AUC > 0.92
- Visualisations : Heatmap, Pairplot, Parallel Coordinates, Decision Boundary

## Déploiement Streamlit
```bash
streamlit run app.py
