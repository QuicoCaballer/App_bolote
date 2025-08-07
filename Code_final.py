import streamlit as st

st.set_page_config(page_title="Marcador", layout="wide")

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

# Columnas para vos y nos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vos")
    input_vos = st.number_input("Puntuación", min_value=0, max_value=162, key="input_vos_col")
    if input_vos:
        st.session_state.input_vos = input_vos
        st.session_state.input_nos = 162 - input_vos

    # Botones rápidos solo afectan a Vos
    if st.button("Tercera", key="tercera_vos"):
        st.session_state.rapido_vos += 20
    if st.button("Bolote_Rebolote", key="bolote_vos"):
        st.session_state.rapido_vos += 20
    for pts in [50, 100, 150, 200]:
        if st.button(f"{pts} puntos", key=f"rapido_{pts}_vos"):
            st.session_state.rapido_vos += pts

with col2:
    st.subheader("Nos")
    input_nos = st.number_input("Puntuación", min_value=0, max_value=162, key="input_nos_col")
    if input_nos:
        st.session_state.input_nos = input_nos
        st.session_state.input_vos = 162 - input_nos

    # Botones rápidos solo afectan a Nos
    if st.button("Tercera", key="tercera_nos"):
        st.session_state.rapido_nos += 20
    if st.button("Bolote_Rebolote", key="bolote_nos"):
        st.session_state.rapido_nos += 20
    for pts in [50, 100, 150, 200]:
        if st.button(f"{pts} puntos", key=f"rapido_{pts}_nos"):
            st.session_state.rapido_nos += pts

# Botón para pasar a la siguiente ronda
if st.button("Siguiente ronda"):
    ronda_vos = st.session_state.input_vos
    ronda_nos = st.session_state.input_nos

    st.session_state.total_vos += ronda_vos + st.session_state.rapido_vos
    st.session_state.total_nos += ronda_nos + st.session_state.rapido_nos

    st.session_state.historial.append(
        (ronda_vos + st.session_state.rapido_vos, ronda_nos + st.session_state.rapido_nos)
    )

    # Reset inputs y puntos rápidos
    st.session_state.input_vos = 0
    st.session_state.input_nos = 0
    st.session_state.rapido_vos = 0
    st.session_state.rapido_nos = 0

# Historial en sombreado
st.markdown("---")
st.markdown("### Marcador:")
for i, (vos, nos) in enumerate(st.session_state.historial, start=1):
    st.markdown(f"- **Ronda {i}**: Vos: `{vos}` – Nos: `{nos}` ")
st.markdown(f"{st.session_state.total_vos} - {st.session_state.total_nos}")
