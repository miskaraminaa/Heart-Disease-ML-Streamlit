import streamlit as st
import joblib
import numpy as np

# Chargement du modèle
model = joblib.load('model_heart_disease.pkl')

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Maladie Cardiaque",
    page_icon="Heart",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS - Style pastel, doux, moderne, centré
st.markdown("""
<style>
    .main { 
        font-family: sans-serif; 
        background-color: #f9f9fc;
        max-width: 100%;
        margin: 1px auto;

    }
    .card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
        border: 1px solid #e8ecf4;
        margin: 1px auto;
        max-width: 100%;
        text-align: center;
    }
    .card-header {
        font-size: 1.7em;
        font-weight: 700;
        color: #4a7bc7;
        margin-bottom: 18px;
        padding-bottom: 10px;
        border-bottom: 2px solid #a8c6fa;
        text-align: center;
        max-width: 100%;

    }
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #6a9ef0 0%, #a8c6fa 100%);
        color: white;
        padding: 36px 20px;
        border-radius: 18px;
        margin: 0 auto 32px;
        max-width: 1000px;
        box-shadow: 0 8px 24px rgba(106, 158, 240, 0.2);
    }
    .main-header h1 {
        font-size: 2.9em;
        font-weight: 800;
        margin: 0 0 14px 0;
    }
    .main-header p {
        font-size: 1.3em;
        font-style: italic;
        opacity: 0.95;
        margin: 0;
    }
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #f0f4ff;
        padding: 16px 0;
        border-radius: 14px;
        margin: 0 auto 32px;
        max-width: 800px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
        flex-wrap: wrap;
        gap: 20px;
    }
    .navbar a {
        color: #e86b9e;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1em;
        padding: 10px 18px;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .navbar a:hover {
        background-color: #e0eafc;
        color: #4a7bc7;
    }
    .stButton > button {
        background-color: #6a9ef0;
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        font-size: 1.1em;
        transition: 0.3s;
        box-shadow: 0 2px 8px rgba(106, 158, 240, 0.3);
        margin: 0 auto;
        display: block;
    }
    .stButton > button:hover {
        background-color: #4a7bc7;
        transform: translateY(-2px);
    }

    /* === RÉSULTATS MODERNES & DOUX === */
    .result-card {
        padding: 20px 28px;
        border-radius: 14px;
        font-size: 1.35em;
        font-weight: 600;
        text-align: center;
        margin: 26px auto 0;
        max-width: 600px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
    }
    .success-card {
        background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
        color: #2e7d32;
        border: 1px solid #a5d6a7;
        box-shadow: 0 4px 12px rgba(129, 199, 132, 0.15);
    }
    .success-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(129, 199, 132, 0.22);
    }
    .error-card {
        background: linear-gradient(135deg, #ffebee 0%, #fff5f5 100%);
        color: #c62828;
        border: 1px solid #ef9a9a;
        box-shadow: 0 4px 12px rgba(239, 154, 154, 0.15);
    }
    .error-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(239, 154, 154, 0.22);
    }

</style>
""", unsafe_allow_html=True)

# En-tête principal
st.markdown("""
<div class="main-header">
    <h1>Prédiction de la Maladie Cardiaque</h1>
    <p>Prendre soin de son cœur, c'est investir dans l'avenir.</p>
</div>
""", unsafe_allow_html=True)

# Barre de navigation
st.markdown("""
<div class="navbar">
    <a href="#accueil">Accueil</a>
    <a href="#prediction">Prédiction</a>
    <a href="#informations">Variables</a>
    <a href="#a-propos">À propos</a>
</div>
""", unsafe_allow_html=True)

# CARD 1 : Accueil
with st.container():
    st.markdown('<div id="accueil"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Accueil</div>', unsafe_allow_html=True)
    st.markdown("""
    Bienvenue dans cet outil de **prédiction du risque cardiaque**.  
    Basé sur un modèle de **régression logistique**, il analyse 13 paramètres médicaux pour estimer la probabilité de maladie cardiaque.
    """)
    st.info("Passez à la section **Prédiction** pour évaluer un cas.")
    st.markdown('</div>', unsafe_allow_html=True)

# CARD 2 : Prédiction
with st.container():
    st.markdown('<div id="prediction"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Évaluation du Risque</div>', unsafe_allow_html=True)

    st.markdown('<div class="prediction-form">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Âge (années)", 1, 120, 50)
        sex = st.selectbox("Sexe", [0, 1], format_func=lambda x: "Homme" if x == 1 else "Femme")
        cp = st.selectbox("Type de douleur thoracique", [0, 1, 2, 3])
        trestbps = st.number_input("Pression artérielle au repos (mmHg)", 80, 200, 120)
        chol = st.number_input("Cholestérol sérique (mg/dl)", 100, 600, 200)

    with col2:
        fbs = st.selectbox("Glycémie à jeun > 120 mg/dl", [0, 1], format_func=lambda x: "Oui" if x == 1 else "Non")
        restecg = st.selectbox("Résultat ECG au repos", [0, 1, 2])
        thalach = st.number_input("Fréquence cardiaque maximale", 60, 220, 150)
        exang = st.selectbox("Angine à l'effort", [0, 1], format_func=lambda x: "Oui" if x == 1 else "Non")
        oldpeak = st.number_input("Dépression ST à l'effort", 0.0, 10.0, 1.0, step=0.1)

    with col3:
        slope = st.selectbox("Pente du segment ST", [0, 1, 2])
        ca = st.selectbox("Nombre de vaisseaux majeurs (fluoroscopie)", [0, 1, 2, 3, 4])
        thal = st.selectbox("Thalassémie", [1, 2, 3])
        st.write(" ")
        st.write(" ")

        if st.button("Lancer la prédiction"):
            input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                    thalach, exang, oldpeak, slope, ca, thal]])
            prediction = model.predict(input_data)[0]

            st.markdown("---")
            if prediction == 1:
                st.markdown("""
                <div class="result-card error-card">
                    <span style="font-size: 1.6em;">Warning</span>
                    <span>Risque élevé de <strong>maladie cardiaque</strong> détecté.</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="result-card success-card">
                    <span style="font-size: 1.6em;">Check</span>
                    <span>Aucun signe de <strong>maladie cardiaque</strong> détecté.</span>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# CARD 3 : Description des Variables — LISTE CENTRÉE, EN DUR
with st.container():
    st.markdown('<div id="informations"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-header">Description des Variables</div>
        <div style="text-align: center; color: #4a5568; font-size: 0.98em; line-height: 1.8;">
            <p><strong>Voici la signification de chaque paramètre utilisé par le modèle :</strong></p>
            <ul style="display: inline-block; text-align: left; margin: 20px 0; padding-left: 20px; max-width: 700px;">
                <li><strong style="color: #6a9ef0;">age</strong> : Âge du patient (années)</li>
                <li><strong style="color: #6a9ef0;">sex</strong> : Sexe (1 = Homme, 0 = Femme)</li>
                <li><strong style="color: #6a9ef0;">cp</strong> : Type de douleur thoracique (0 = typique, 1 = atypique, 2 = non-angineuse, 3 = asymptomatique)</li>
                <li><strong style="color: #6a9ef0;">trestbps</strong> : Pression artérielle au repos (mmHg)</li>
                <li><strong style="color: #6a9ef0;">chol</strong> : Cholestérol sérique (mg/dl)</li>
                <li><strong style="color: #6a9ef0;">fbs</strong> : Glycémie à jeun > 120 mg/dl (1 = oui, 0 = non)</li>
                <li><strong style="color: #6a9ef0;">restecg</strong> : Résultat ECG au repos (0 = normal, 1 = anomalie ST-T, 2 = hypertrophie VG)</li>
                <li><strong style="color: #6a9ef0;">thalach</strong> : Fréquence cardiaque maximale atteinte</li>
                <li><strong style="color: #6a9ef0;">exang</strong> : Angine induite par l'exercice (1 = oui, 0 = non)</li>
                <li><strong style="color: #6a9ef0;">oldpeak</strong> : Dépression ST à l'effort</li>
                <li><strong style="color: #6a9ef0;">slope</strong> : Pente du segment ST (0 = descendante, 1 = plate, 2 = montante)</li>
                <li><strong style="color: #6a9ef0;">ca</strong> : Nombre de vaisseaux majeurs (0 à 4)</li>
                <li><strong style="color: #6a9ef0;">thal</strong> : Thalassémie (1 = normal, 2 = défaut fixe, 3 = défaut réversible)</li>
                <li><strong style="color: #6a9ef0;">target</strong> : Présence de maladie cardiaque (1 = oui, 0 = non)</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# CARD 4 : À propos
with st.container():
    st.markdown('<div id="a-propos"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-header">À propos</div>
        <div style="text-align: center; color: #4a5568; line-height: 1.8; font-size: 1.02em;">
            <p>
                Cette application a été développée dans le cadre d’un <strong>projet de Data Mining et Visualisation des Big Data</strong>.<br>
                Elle illustre l’application pratique d’un modèle de Machine Learning en santé.
            </p>
            <p style="margin: 20px 0; font-weight: 600; color: #2d3748;">
                <strong>Auteurs :</strong> MISKAR Amina & AZIZ Mohammed<br>
                <strong>Modèle :</strong> Régression Logistique<br>
                <strong>Précision :</strong> 86.2 % (jeu de validation)<br>
                <strong>Données :</strong> UCI Heart Disease Dataset
            </p>
            <p style="color: #718096; font-size: 0.9em; margin-top: 28px;">
                © 2025 — Projet académique | ENSAJ, Université Chouaib Doukkali
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)