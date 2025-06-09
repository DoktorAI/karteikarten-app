import streamlit as st
from streamlit_sortable import sortable

st.set_page_config(page_title="Karteikarten Generator", layout="wide")
st.title("📇 Karteikarten aus Stichpunkten")

if "karten" not in st.session_state:
    st.session_state.karten = []

with st.form("neue_karte"):
    neuer_text = st.text_area("Stichpunkt eingeben", height=100)
    col1, col2 = st.columns([3, 1])
    with col2:
        absenden = st.form_submit_button("➕ Hinzufügen")
    if absenden and neuer_text.strip():
        st.session_state.karten.append(neuer_text.strip())

st.markdown("---")
st.subheader("🧩 Karteikarten Übersicht (Drag & Drop)")
karten_liste = [f"{i+1}. {k}" for i, k in enumerate(st.session_state.karten)]
neue_reihenfolge = sortable(karten_liste, direction="vertical", show_order=True)
if neue_reihenfolge != karten_liste:
    st.session_state.karten = [k.split(". ", 1)[1] for k in neue_reihenfolge]

st.markdown("---")
st.subheader("📌 Neue Karte zwischenkartieren")
if len(st.session_state.karten) >= 2:
    zwischen_index = st.selectbox(
        "Nach welcher Karte soll eingefügt werden?",
        [f"{i+1}. {text}" for i, text in enumerate(st.session_state.karten)]
    )
    zwischen_text = st.text_area("Neuer Stichpunkt", key="zwischen_text")
    if st.button("Einfügen") and zwischen_text.strip():
        idx = int(zwischen_index.split(".")[0])
        st.session_state.karten.insert(idx, zwischen_text.strip())

st.markdown("---")
st.subheader("📋 Aktuelle Karteikarten")
for i, karte in enumerate(st.session_state.karten):
    st.markdown(f"**{i+1}.** {karte}")
