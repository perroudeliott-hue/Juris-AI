import streamlit as st
import google.generativeai as genai
import os

# 1. Récupération ultra-rapide de la clé (on la passera dans le terminal)
cle_api = os.environ.get("IA_API_KEY")

if not cle_api:
    st.error("🚨 Clé API introuvable. Tapez 'export IA_API_KEY=\"votre_clé\"' dans le terminal.")
    st.stop()

genai.configure(api_key=cle_api)

# 2. Master-Prompt (Orienté Droit du Numérique & Contrats)
master_prompt = """
Tu es un avocat français au Barreau de Paris, spécialisé en droit du numérique et révision contractuelle. 
Ton objectif est d'assister un professionnel du droit. Ton ton est institutionnel, clair et précis.
Base-toi EXCLUSIVEMENT sur le droit français (RGPD, Code civil). 
Identifie les risques juridiques puis propose une rédaction sécurisée. Ne donne pas de conseils génériques, sois concret.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=master_prompt
)

# 3. Interface Utilisateur
st.set_page_config(page_title="Assistant Juridique IA", page_icon="⚖️", layout="centered")
st.title("⚖️ Assistant Contrats IA")
st.warning("⚠️ **Rappel Déontologique :** Outil de démonstration. La validation finale des clauses incombe à l'avocat.")

# 4. Mémoire du Chatbot
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Bonjour Maître. Quel contrat (NDA, DPA, prestation IT) révisons-nous pour cette démonstration ?"}]

# 5. Affichage de l'historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. Moteur de discussion
if prompt := st.chat_input("Ex: Rédige une clause de réversibilité stricte..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyse juridique en cours..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erreur technique : {e}")
