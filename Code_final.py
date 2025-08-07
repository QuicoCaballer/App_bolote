import streamlit as st

# Constante
PUNTOS_TOTALES = 162

# Inicializar estado si es la primera vez
if "total_vos" not in st.session_state:
    st.session_state.total_vos = 0
    st.session_state.total_nos = 0
    st.session_state.historial_vos = []
    st.session_state.historial_nos = []
    st.session_state.input_vos = 0
    st.session_state.input_nos = 0

# Función: calcular el otro input automáticamente
def actualizar_inputs():
    vos = st.session_state.input_vos
    nos = st.session_state.input_nos
    # Si solo se ha rellenado Vos
    if vos and not nos:
        st.session_state.input_nos = max(0, PUNTOS_TOTALES - vos)
    # Si solo se ha rellenado Nos
    elif nos and not vos:
        st.session_state.input_vos = max(0, PUNTOS_TOTALES - nos)

# Título
st.title("🎯 Puntos Vos y Nos")

# Entradas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vos")
    st.number_input("Puntos ronda", key="input_vos", min_value=0, max_value=162, step=1, on_change=actualizar_inputs)
    st.markdown(f"**Total acumulado:** {st.session_state.total_vos}")

with col2:
    st.subheader("Nos")
    st.number_input("Puntos ronda", key="input_nos", min_value=0, max_value=162, step=1, on_change=actualizar_inputs)
    st.markdown(f"**Total acumulado:** {st.session_state.total_nos}")

# Botón único
if st.button("➕ Siguiente ronda"):
    puntos_vos = st.session_state.input_vos
    puntos_nos = st.session_state.input_nos

    # Validar que suman 162
    if puntos_vos + puntos_nos != PUNTOS_TOTALES:
        st.error("La suma de puntos debe ser exactamente 162.")
    else:
        # Acumular totales
        st.session_state.total_vos += puntos_vos
        st.session_state.total_nos += puntos_nos

        # Guardar en historial
        st.session_state.historial_vos.append(puntos_vos)
        st.session_state.historial_nos.append(puntos_nos)

        # Reset inputs
        st.session_state.input_vos = 0
        st.session_state.input_nos = 0
        st.experimental_rerun()

# Historial
st.markdown("---")
st.subheader("📜 Historial de rondas")

col1_hist, col2_hist = st.columns(2)
with col1_hist:
    st.markdown("**Vos**")
    for i, val in enumerate(st.session_state.historial_vos, 1):
        st.markdown(f"- Ronda {i}: {val}", help="Puntos de Vos")

with col2_hist:
    st.markdown("**Nos**")
    for i, val in enumerate(st.session_state.historial_nos, 1):
        st.markdown(f"- Ronda {i}: {val}", help="Puntos de Nos")

# Botón de reinicio
st.markdown("---")
if st.button("🔁 Reiniciar todo"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()
