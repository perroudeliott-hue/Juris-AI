import streamlit as st
import google.generativeai as genai
import os

# ==========================================
# 1. CONFIGURATION DE LA PAGE ET STYLE CSS
# ==========================================
st.set_page_config(
    page_title="Assistance Contrats IA | Cabinet d'Avocats",
    page_icon="⚖️",
    layout="wide", # Layout large pour un look pro
    initial_sidebar_state="expanded"
)

# Injection de CSS personnalisé pour "pimper" l'interface
st.markdown("""
<style>
    /* Modification du fond et des polices */
    .stApp {
        background-color: #1A1D21;
        color: #ECF0F1;
    }
    
    /* Titre principal */
    h1 {
        color: #D4AF37 !important; /* Couleur dorée */
        font-family: 'Times New Roman', Times, serif;
    }
    
    /* Bulles de chat */
    .stChatMessage {
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Bulle Assistant (Gemini) */
    .stChatMessage[data-testid="stChatMessageAssistant"] {
        background-color: #2C3E50;
        border: 1px solid #34495E;
    }
    
    /* Bulle Utilisateur */
    .stChatMessage[data-testid="stChatMessageUser"] {
        background-color: #21618C;
        border: 1px solid #2E86C1;
    }
    
    /* Personnalisation de la barre latérale */
    [data-testid="stSidebar"] {
        background-color: #141619;
        border-right: 2px solid #D4AF37;
    }
    
    /* Mention légale dans les réponses IA */
    .ai-tracer {
        font-size: 0.8rem;
        color: #95A5A6;
        font-style: italic;
        margin-top: -10px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INTÉGRATION DES GARDE-FOUS (Sidebar)
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/lawyer.png", width=70) # Un petit logo par défaut
    st.markdown("# 🛡️ Sécurité & Conformité")
    st.markdown("---")
    
    # 2.1 Garde-fou Informatique (Souveraineté des données)
    with st.expander("☁️ Hébergement & Flux de Données", expanded=True):
        st.error("**ALERTE SOUVERAINETÉ :**")
        st.write("""
            Le modèle LLM utilisé (Gemini) est hébergé sur des serveurs de Google situés aux **États-Unis**.
            Les données saisies dans le chat transitent hors de l'Union Européenne.
        """)
        
    # 2.2 Garde-fou Secret Professionnel (Anonymisation obligatoire)
    with st.expander("🤐 Confidentialité & Secret Pro.", expanded=True):
        st.warning("**REGLE D'OR (Prototype) :**")
        st.write("""
            Il est **strictement interdit** de saisir :
            - Des noms réels de clients physiques ou moraux.
            - Des données financières spécifiques.
            - Des détails d'affaires permettant l'identification.
            *Utilisez des balises de type [PARTIE_A] ou [MONTANT].*
        """)

    # 2.3 Garde-fou Réglementaire (RGPD & AI Act awareness)
    with st.expander("🇪🇺 Conformité Européenne", expanded=False):
        st.info("**Cadre Légal :**")
        st.write("""
            - **RGPD :** Aucune Donnée à Caractère Personnel (DCP) ne doit être traitée ici.
            - **EU AI Act :** Ce prototype est classé comme un système d'IA à risque limité. Sa traçabilité est assurée par la mention générique intégrée aux réponses.
        """)
    
    st.markdown("---")
    st.markdown("v0.9-beta | Démo Interne")

# ==========================================
# 3. CONFIGURATION API & PROMPT SYSTEM
# ==========================================
# Récupération de la clé depuis les secrets de déploiement (Streamlit Cloud ou variable d'env)
cle_api = os.environ.get("IA_API_KEY")

if not cle_api:
    st.error("🚨 ERREUR CRITIQUE : Clé API introuvable dans les secrets de déploiement.")
    st.stop()

genai.configure(api_key=cle_api)

# Master-Prompt Juridique Strict
master_prompt = """
Tu es un avocat français au Barreau de Paris, spécialisé en droit des obligations, droit commercial et conformité RGPD. 
Ton objectif est d'assister un confrère dans la rédaction et la révision de contrats d'affaires. 
Ton ton est institutionnel, hautement précis et neutre.

TES CONSIGNES STRICTES DE TRAVAIL :
1. DROIT APPLICABLE : Base-toi EXCLUSIVEMENT sur le droit français (Code civil, Code de commerce) et le RGPD. Refuse toute référence au droit anglo-saxon (Common Law) sauf demande explicite.
2. SÉCURITÉ JURIDIQUE : Analyse systématiquement les risques de déséquilibre significatif (clauses abusives) dans tes propositions.
3. ANTI-HALLUCINATION : Ne cite JAMAIS un article de loi ou une jurisprudence dont tu n'es pas absolument certain. En cas de doute, écris "[Point à vérifier par l'avocat]".
4. FORMATAGE : Pour chaque demande, fournis d'abord une brève note d'analyse des risques (3 points clés), puis la proposition de rédaction juridique.
5. RESPECT DE L'ANONYMISATION : Si l'utilisateur utilise des balises comme [PARTIE_A], conserve-les scrupuleusement.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Rapide et performant pour un chatbot
    system_instruction=master_prompt
)

# ==========================================
# 4. INTERFACE DE CHAT & BANNIÈRE FIXE
# ==========================================
st.markdown("# ⚖️ Assistant IA de Rédaction Contractuelle")

# Bannière Déontologique Fixe (Inamovible)
st.warning("""
    **⛔ RAPPEL DÉONTOLOGIQUE :** Ce système est un prototype d'assistance. Il ne dispense pas de la qualification juridique. 
    L'avocat signataire conserve l'entière responsabilité intellectuelle et légale de la rédaction finale du contrat.
""")

st.markdown("---")

# Gestion de l'historique de chat en mémoire session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Bonjour Maître. Sur quel type de clause ou de contrat (NDA, Contrat SaaS, CGV) souhaitez-vous travailler ?"}]

# Affichage de l'historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Zone de saisie utilisateur
if prompt := st.chat_input("Ex: Rédige une clause de limitation de responsabilité plafonnée au montant du contrat..."):
    # Enregistrement du message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Génération de la réponse Gemini
    with st.chat_message("assistant"):
        # Ajout systématique de la mention de traçabilité AI Act
        st.markdown('<div class="ai-tracer">Texte généré par une intelligence artificielle (Gemini 1.5 Flash). Vérification humaine requise.</div>', unsafe_allow_html=True)
        
        with st.spinner("Analyse du contexte juridique..."):
            try:
                # Envoi du message dans la session de chat pour garder le contexte
                response = st.session_state.chat_session.send_message(prompt)
                st.markdown(response.text)
                # Sauvegarde pour l'affichage de l'historique
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erreur lors de la communication avec l'API. Vérifiez votre connexion. Détails : {e}")
