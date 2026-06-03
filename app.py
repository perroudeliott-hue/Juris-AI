import streamlit as st
import google.generativeai as genai
import os

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="IA Juridique | Prototype Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Un CSS minimaliste uniquement pour marquer la traçabilité IA des textes
st.markdown("""
<style>
    .ai-watermark {
        font-size: 0.85rem;
        color: #7f8c8d;
        font-style: italic;
        border-left: 3px solid #bdc3c7;
        padding-left: 10px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. BARRE LATÉRALE : MENTIONS LÉGALES (AI ACT & RGPD)
# ==========================================
with st.sidebar:
    st.header("⚖️ Conformité & Sécurité")
    st.markdown("---")
    
    # Mention AI Act & Responsabilité
    st.warning("**Règlement (UE) 2024/1689 (AI Act)**")
    st.markdown("""
    **Qualification :** Ce prototype est qualifié de système d'IA à risque limité (Art. 50). 
    
    **Transparence :** L'utilisateur est expressément informé qu'il interagit avec un système d'intelligence artificielle générative (LLM).
    
    **Responsabilité de la Structure :** L'outil est fourni "en l'état" pour assistance à la rédaction. La structure décline toute responsabilité quant à l'exactitude juridique des textes générés. La supervision, la qualification juridique et la validation finale incombent exclusivement à l'avocat signataire, sous couvert de son assurance RCP.
    """)
    
    # Mention RGPD & Transfert de données
    st.error("**RGPD & Transferts hors UE**")
    st.markdown("""
    **Sous-traitant :** L'API Gemini (Google LLC) opère comme sous-traitant ultérieur.
    
    **Transfert de données :** Les prompts transitent vers des serveurs situés aux États-Unis (sujet au *Data Privacy Framework*).
    
    **Mesures de sauvegarde :** Le traitement de Données à Caractère Personnel (DCP) est **strictement interdit** sur cette interface. Le principe de minimisation (Art. 5c RGPD) impose une pseudonymisation absolue avant soumission.
    """)

    # Mention Secret Professionnel
    st.info("**Secret Professionnel (Loi de 1971)**")
    st.markdown("""
    L'avocat utilisateur est garant du secret professionnel (Art. 66-5). 
    Les entités, montants, et éléments permettant l'identification d'une affaire doivent impérativement être remplacés par des variables alphanumériques (ex: `[PARTIE_A]`).
    """)
    
    st.markdown("---")
    st.caption("Démo Interne - Prototype non destiné à la production.")

# ==========================================
# 2.5 GESTION DES DOCUMENTS LÉGAUX
# ==========================================
with st.sidebar:
    st.markdown("---")
    st.subheader("📚 Documentation")
    
    # Création des deux boutons
    col1, col2 = st.columns(2)
    with col1:
        btn_mentions = st.button("Mentions")
    with col2:
        btn_cgu = st.button("CGU")

    # Logique d'affichage
    if btn_mentions:
        st.session_state.active_doc = "mentions_legales.md"
    if btn_cgu:
        st.session_state.active_doc = "cgu.md"

    # Affichage du document si un bouton a été cliqué
    if "active_doc" in st.session_state:
        doc_path = st.session_state.active_doc
        if os.path.exists(doc_path):
            with open(doc_path, "r", encoding="utf-8") as f:
                contenu = f.read()
            
            with st.expander(f"Visualisation : {doc_path.replace('.md', '').upper()}", expanded=True):
                st.markdown(contenu)
                if st.button("Fermer le document"):
                    del st.session_state.active_doc
                    st.rerun()
        else:
            st.error(f"Fichier {doc_path} introuvable.")
            
# ==========================================
# 3. INITIALISATION DE L'API ET DE LA MÉMOIRE
# ==========================================
# Récupération de la clé API
cle_api = os.environ.get("IA_API_KEY")

if not cle_api:
    st.error("🚨 Clé API introuvable. Veuillez configurer la variable d'environnement IA_API_KEY.")
    st.stop()

genai.configure(api_key=cle_api)

# Prompt Système rigoureux
system_prompt = """
Tu es un avocat français au Barreau de Paris. Tu assistes un confrère dans la rédaction de contrats.
CONSIGNES STRICTES :
1. Fonde tes analyses exclusivement sur le droit français (Code civil, Code de commerce) et le droit européen (RGPD, etc.).
2. Identifie systématiquement les risques juridiques (déséquilibre significatif, non-conformité) avant de rédiger une clause.
3. Conserve les balises d'anonymisation (ex: [PARTIE_A]) sans jamais inventer de données fictives.
4. Ton ton doit être neutre, objectif et confraternel ("Maître").
"""

model = genai.GenerativeModel('gemini-3.5-flash', system_instruction=system_prompt)

# Correction du bug de mémoire : Initialisation d'une vraie session de chat persistante
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Bonjour Maître. Quel contrat ou clause analysons-nous aujourd'hui ?"}]

# ==========================================
# 4. INTERFACE PRINCIPALE DU CHATBOT
# ==========================================
st.title("Assistant IA de Rédaction Contractuelle")
st.markdown("*Prototype de conformité et d'assistance juridique.*")
st.divider()

# Affichage de l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Saisie utilisateur
if prompt := st.chat_input("Insérez vos directives ou la clause à réviser ici..."):
    
    # 1. Affichage immédiat de la question de l'utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# 2. Appel à l'API et affichage de la réponse
    with st.chat_message("assistant"):
        with st.spinner("Analyse de la conformité et rédaction en cours..."):
            try:
                # Utilisation de la session de chat existante pour garder le contexte
                response = st.session_state.chat_session.send_message(prompt)
                
                # Affichage du texte généré
                st.markdown(response.text)
                
                # Ajout du filigrane de traçabilité (AI Act) sous le message
                st.markdown('<div class="ai-watermark">Contenu généré par un système d\'IA (Gemini 1.5). Une vérification humaine par un professionnel du droit est obligatoire.</div>', unsafe_allow_html=True)
                
                # Sauvegarde dans l'historique
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                st.error(f"Une erreur est survenue lors du traitement : {e}")
