import streamlit as st

# Inicializar variables en sesión
if "total_vos" not in st.session_state:
    st.session_state.total_vos = 0
if "total_nos" not in st.session_state:
    st.session_state.total_nos = 0

st.set_page_config(page_title="Puntos Vos y Nos", layout="centered")

st.title("🎯 Puntos Vos y Nos")

col1, col2 = st.columns(2)

# --- Columna Vos ---
with col1:
    st.subheader("Vos")
    puntos_vos = st.number_input("Puntos ronda (Vos)", min_value=0, step=1, key="puntos_vos_input")
    if st.button("➕ Otra ronda Vos"):
        st.session_state.total_vos += puntos_vos
    st.markdown(f"**Total acumulado: {st.session_state.total_vos} puntos**")

    st.markdown("### Sumar rápido:")
    if st.button("Tercera (20)", key="vos_tercera"):
        st.session_state.total_vos += 20
    if st.button("Bolote_Rebolote (20)", key="vos_bolote"):
        st.session_state.total_vos += 20
    if st.button("+50", key="vos_50"):
        st.session_state.total_vos += 50
    if st.button("+100", key="vos_100"):
        st.session_state.total_vos += 100
    if st.button("+150", key="vos_150"):
        st.session_state.total_vos += 150
    if st.button("+200", key="vos_200"):
        st.session_state.total_vos += 200

# --- Columna Nos ---
with col2:
    st.subheader("Nos")
    puntos_nos = st.number_input("Puntos ronda (Nos)", min_value=0, step=1, key="puntos_nos_input")
    if st.button("➕ Otra ronda Nos"):
        st.session_state.total_nos += puntos_nos
    st.markdown(f"**Total acumulado: {st.session_state.total_nos} puntos**")

    st.markdown("### Sumar rápido:")
    if st.button("Tercera (20)", key="nos_tercera"):
        st.session_state.total_nos += 20
    if st.button("Bolote_Rebolote (20)", key="nos_bolote"):
        st.session_state.total_nos += 20
    if st.button("+50", key="nos_50"):
        st.session_state.total_nos += 50
    if st.button("+100", key="nos_100"):
        st.session_state.total_nos += 100
    if st.button("+150", key="nos_150"):
        st.session_state.total_nos += 150
    if st.button("+200", key="nos_200"):
        st.session_state.total_nos += 200

# Botón de reset
st.markdown("---")
if st.button("🔁 Reiniciar totales"):
    st.session_state.total_vos = 0
    st.session_state.total_nos = 0
    st.experimental_rerun()
