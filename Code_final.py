import streamlit as st

st.set_page_config(page_title="Marcador", layout="wide")

# CSS para compactar diseño
st.markdown("""
<style>
/* Forzar columnas horizontales en móvil */
.horizontal {
    display: flex !important;
    flex-wrap: nowrap !important;
    gap: 10px;
}
.horizontal > div[data-testid="column"] {
    flex: 1 1 0 !important;
}

/* Inputs más estrechos */
div[data-baseweb="input"] input {
    max-width: 80px !important;
    text-align: center;
}

/* Botones compactos y en fila */
.compact-buttons > div {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
}
.compact-buttons button {
    padding: 4px 8px !important;
    font-size: 0.85rem !important;
}
</style>
""", unsafe_allow_html=True)

# Inicialización del estado
for key in [
    'input_vos', 'input_nos', 
    'total_vos', 'total_nos', 
    'historial', 
    'rapido_vos', 'rapido_nos'
]:
    if key not in st.session_state:
        if key == 'historial':
            st.session_state[key] = []
        else:
            st.session_state[key] = 0

st.title("BOLOTE")

# Bloque de columnas forzado
st.markdown('<div class="horizontal">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Nos")
    input_nos = st.number_input("Puntuación", min_value=0, max_value=162, key="input_nos_col")
    if input_nos:
        st.session_state.input_nos = input_nos
        st.session_state.input_vos = 162 - input_nos

    # Botones rápidos Nos
    with st.container():
        st.markdown('<div class="compact-buttons">', unsafe_allow_html=True)
        if st.button("Tercera", key="tercera_nos"):
            st.session_state.rapido_nos += 20
        if st.button("Bolote", key="bolote_nos"):
            st.session_state.rapido_nos += 20
        for pts in [50, 100, 150, 200]:
            if st.button(f"{pts}", key=f"rapido_{pts}_nos"):
                st.session_state.rapido_nos += pts
        if st.button("Capote", key="capote_nos"):
            st.session_state.rapido_vos += 252
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("Vos")
    input_vos = st.number_input("Puntuación", min_value=0, max_value=162, key="input_vos_col")
    if input_vos:
        st.session_state.input_vos = input_vos
        st.session_state.input_nos = 162 - input_vos

    # Botones rápidos Vos
    with st.container():
        st.markdown('<div class="compact-buttons">', unsafe_allow_html=True)
        if st.button("Tercera", key="tercera_vos"):
            st.session_state.rapido_vos += 20
        if st.button("Bolote", key="bolote_vos"):
            st.session_state.rapido_vos += 20
        for pts in [50, 100, 150, 200]:
            if st.button(f"{pts}", key=f"rapido_{pts}_vos"):
                st.session_state.rapido_vos += pts
        if st.button("Capote", key="capote_vos"):
            st.session_state.rapido_vos += 252
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Botón siguiente ronda
if st.button("Siguiente ronda"):
    ronda_vos = st.session_state.input_vos
    ronda_nos = st.session_state.input_nos

    st.session_state.total_vos += ronda_vos + st.session_state.rapido_vos
    st.session_state.total_nos += ronda_nos + st.session_state.rapido_nos

    st.session_state.historial.append(
        (ronda_vos + st.session_state.rapido_vos, ronda_nos + st.session_state.rapido_nos)
    )

    st.session_state.input_vos = 0
    st.session_state.input_nos = 0
    st.session_state.rapido_vos = 0
    st.session_state.rapido_nos = 0

# Historial
st.markdown("### Marcador:")
for i, (vos, nos) in enumerate(st.session_state.historial, start=1):
    st.markdown(f"- **Ronda {i}**: Vos: `{vos}` – Nos: `{nos}` ")
st.markdown(f"{st.session_state.total_vos} - {st.session_state.total_nos}")
