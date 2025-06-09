import streamlit as st
from streamlit_sortables import sort_items
import math

st.set_page_config(page_title="Karteikarten Generator", layout="wide")
st.title("📇 Karteikarten aus Stichpunkten")

# Eingabefeld für komplette Stichpunktliste
st.subheader("✍️ Stichpunkte eingeben (ein Stichpunkt pro Zeile)")
text_input = st.text_area("Jeder Stichpunkt wird zu einer Karteikarte:", height=300)

# Karteikarten erzeugen
if st.button("🎴 Karteikarten generieren"):
    st.session_state.karten = [line.strip() for line in text_input.split("\n") if line.strip()]

# Karten anzeigen und sortieren
if "karten" in st.session_state and st.session_state.karten:
    st.markdown("---")
    st.subheader("📇 Deine Karteikarten (per Drag & Drop sortierbar)")

    # Karten in Grid umwandeln
    def chunk_list(lst, n):
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    # Format für Anzeige
    formatted_cards = [f"{i+1}. {k}" for i, k in enumerate(st.session_state.karten)]
    sortiertes = sort_items(formatted_cards)


    if sortiertes != formatted_cards:
        st.session_state.karten = [s.split(". ", 1)[1] for s in sortiertes]

    # Visuelle Anzeige der Karten im Grid-Stil
    cols = st.columns(5)
    for i, card in enumerate(st.session_state.karten):
        with cols[i % 5]:
            st.markdown(
                f"""
                <div style='border:1px solid #ccc; border-radius:8px; padding:12px; margin:8px 0; 
                     background-color:#f9f9f9; text-align:center; min-height:80px;'>
                    {card}
                </div>
                """,
                unsafe_allow_html=True
            )
