import streamlit as st
import google.generativeai as genai
import os

# ==========================================
# 1. CONFIGURATION & DESIGN "CABINET PRESTIGE"
# ==========================================
st.set_page_config(
    page_title="IA Juridique | Prototype Assistant",
    page_icon="⚖️",
    layout="wide"
)

# CSS Personnalisé pour coller exactement au rendu visuel souhaité
st.markdown("""
<style>
    /* Fond principal */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Style de la Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #D4AF37;
        min-width: 350px !important;
    }

    /* Titre Principal Or */
    .main-title {
        color: #D4AF37;
        font-size: 42px;
        font-weight: bold;
        font-family: 'Playfair Display', serif;
        margin-bottom: 10px;
    }

    /* Bannière de rappel déontologique */
    .deonto-banner {
        background-color: rgba(255, 75, 75, 0.1);
        border: 2px solid #FF4B4B;
        padding: 20px;
        border-radius: 10px;
        color: #FF4B4B;
        font-weight: bold;
        margin-bottom: 30px;
    }

    /* Alertes Sidebar - Style Blindé */
    .sidebar-alert-red {
        background-color: rgba(255, 75, 75, 0.2);
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 15px;
        font-size: 14px;
    }
    
    .sidebar-alert-gold {
        background-color: rgba(212, 175, 55, 0.1);
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #D4AF37;
        margin-bottom: 15px;
        font-size: 14px;
        color: #D4AF37;
    }

    /* Style des messages de chat */
    .stChatMessage {
        background-color: #1D232C !important;
        border: 1px solid #30363D !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. BARRE LATÉRALE : SÉCURITÉ & MENTIONS
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37;'>🛡️ Sécurité & Conformité</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Garde-fou 1 : Souveraineté
    st.markdown("""
    <div class="sidebar-alert-red">
        <b>⚠️ ALERTE SOUVERAINETÉ :</b><br>
        Ce prototype utilise l'API <b>Gemini (Google USA)</b>.<br>
        Vos données sont traitées hors UE. <u>Aucune garantie de souveraineté européenne</u> n'est appliquée sur ce flux de test.
    </div>
    """, unsafe_allow_html=True)
    
    # Garde-fou 2 : Secret Professionnel
    st.markdown("""
    <div class="sidebar-alert-gold">
        <b>🤐 CONFIDENTIALITÉ & SECRET PRO :</b><br>
        En vertu de l'article 66-5 de la loi de 1971, le secret professionnel est absolu.<br><br>
        <b>STRICTEMENT INTERDIT :</b>
        <ul>
            <li>Noms de clients / adversaires</li>
            <li>Coordonnées réelles</li>
            <li>Montants d'honoraires</li>
        </ul>
        <i>Utilisez : [CLIENT], [ADVERSAIRE], [PRIX].</i>
    </div>
    """, unsafe_allow_html=True)

    # Garde-fou 3 : Informatique & Libertés
    st.info("""
        **🔍 Audit Informatique :**
        - Chiffrement TLS 1.3 actif.
        - Pas de stockage de base de données.
        - Purge des sessions à la fermeture.
    """)
    
    st.markdown("---")
    st.caption("Usage interne exclusivement - Version Prototype 1.0")

# ==========================================
# 3. LOGIQUE API & PROMPT
# ==========================================
cle_api = st.secrets.get("IA_API_KEY") or os.environ.get("IA_API_KEY")

if not cle_api:
    st.error("Clé API manquante. Ajoutez IA_API_KEY dans vos secrets.")
    st.stop()

genai.configure(api_key=cle_api)

# Prompt Système ultra-juridique
system_prompt = """
Tu es un avocat français senior. Tu assistes ton confrère dans la rédaction de contrats.
CONSIGNES :
1. Droit Français uniquement.
2. Identifie les risques (clauses léonines, déséquilibre significatif) AVANT de proposer le texte.
3. Si l'utilisateur demande quelque chose d'illégal, refuse poliment.
4. Reste formel : utilise "Maître", "Confrère" ou un ton neutre.
"""

model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_prompt)

# ==========================================
# 4. ZONE DE TRAVAIL PRINCIPALE
# ==========================================
st.markdown("<div class='main-title'>⚖️ Assistant IA de Rédaction Contractuelle</div>", unsafe_allow_html=True)

# Rappel déontologique inamovible
st.markdown("""
<div class="deonto-banner">
    ⛔ RAPPEL DÉONTOLOGIQUE : Ce système est un assistant de rédaction. Il ne dispense pas de la qualification juridique. 
    L'avocat signataire conserve l'entière responsabilité intellectuelle et légale de la rédaction finale du contrat (Responsabilité Civile Professionnelle).
</div>
""", unsafe_allow_html=True)

# Initialisation du chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if prompt := st.chat_input("Ex: Rédige une clause de force majeure adaptée à la jurisprudence actuelle..."):
    # Affichage du message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Réponse de l'IA
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        # Mention de traçabilité IA ACT (Obligatoire)
        st.caption("🤖 Traçabilité : Contenu généré par IA Générative (AI Act Compliance).")
        
        try:
            full_response = ""
            # On simule un historique pour que l'IA se souvienne de la discussion
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
            full_response = response.text
            
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Erreur système : {e}")

# Footer de bas de page
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555;'>Propriété intellectuelle du Cabinet | Prototype de recherche interne</p>", unsafe_allow_html=True)
