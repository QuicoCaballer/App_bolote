import streamlit as st

PUNTOS_TOTALES = 162

# Inicializar estado
if "total_vos" not in st.session_state:
    st.session_state.total_vos = 0
    st.session_state.total_nos = 0
    st.session_state.historial_vos = []
    st.session_state.historial_nos = []
    st.session_state.input_vos = 0
    st.session_state.input_nos = 0
    st.session_state.rapidos_vos = 0
    st.session_state.rapidos_nos = 0

# Función para autocompletar input contrario
def actualizar_inputs():
    vos = st.session_state.input_vos
    nos = st.session_state.input_nos
    if vos and not nos:
        st.session_state.input_nos = max(0, PUNTOS_TOTALES - vos)
    elif nos and not vos:
        st.session_state.input_vos = max(0, PUNTOS_TOTALES - nos)

# Función para sumar puntos rápidos
def sumar_rapidos(equipo, puntos):
    if equipo == "vos":
        st.session_state.total_vos += puntos
        st.session_state.rapidos_vos += puntos
    else:
        st.session_state.total_nos += puntos
        st.session_state.rapidos_nos += puntos

# Título
st.title("🎯 Puntos Vos y Nos")

# Columnas principales
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟡 Vos")
    st.number_input("Puntos ronda", key="input_vos", min_value=0, max_value=162, step=1, on_change=actualizar_inputs)
    st.markdown(f"**Total acumulado:** {st.session_state.total_vos} _(+{st.session_state.rapidos_vos} rápidos)_")
    
    st.text("Puntuaciones rápidas:")
    if st.button("Tercera (20)", key="tercera_vos"):
        sumar_rapidos("vos", 20)
    if st.button("Bolete_Rebolote (20)", key="bolete_vos"):
        sumar_rapidos("vos", 20)
    if st.button("+50", key="50_vos"):
        sumar_rapidos("vos", 50)
    if st.button("+100", key="100_vos"):
        sumar_rapidos("vos", 100)
    if st.button("+150", key="150_vos"):
        sumar_rapidos("vos", 150)
    if st.button("+200", key="200_vos"):
        sumar_rapidos("vos", 200)

with col2:
    st.subheader("🔵 Nos")
    st.number_input("Puntos ronda", key="input_nos", min_value=0, max_value=162, step=1, on_change=actualizar_inputs)
    st.markdown(f"**Total acumulado:** {st.session_state.total_nos} _(+{st.session_state.rapidos_nos} rápidos)_")

    st.text("Puntuaciones rápidas:")
    if st.button("Tercera (20)", key="tercera_nos"):
        sumar_rapidos("nos", 20)
    if st.button("Bolete_Rebolote (20)", key="bolete_nos"):
        sumar_rapidos("nos", 20)
    if st.button("+50", key="50_nos"):
        sumar_rapidos("nos", 50)
    if st.button("+100", key="100_nos"):
        sumar_rapidos("nos", 100)
    if st.button("+150", key="150_nos"):
        sumar_rapidos("nos", 150)
    if st.button("+200", key="200_nos"):
        sumar_rapidos("nos", 200)

# Botón de ronda
st.markdown("---")
if st.button("➕ Siguiente ronda"):
    puntos_vos = st.session_state.input_vos
    puntos_nos = st.session_state.input_nos

    if puntos_vos + puntos_nos != PUNTOS_TOTALES:
        st.error("La suma de puntos debe ser exactamente 162.")
    else:
        st.session_state.total_vos += puntos_vos
        st.session_state.total_nos += puntos_nos
        st.session_state.historial_vos.append(puntos_vos)
        st.session_state.historial_nos.append(puntos_nos)
        st.session_state.input_vos = 0
        st.session_state.input_nos = 0
        st.experimental_rerun()

# Historial
st.markdown("---")
st.subheader("📜 Historial de rondas (normales)")

col1_hist, col2_hist = st.columns(2)
with col1_hist:
    st.markdown("**Vos**")
    for i, val in enumerate(st.session_state.historial_vos, 1):
        st.markdown(f"- Ronda {i}: {val}")

with col2_hist:
    st.markdown("**Nos**")
    for i, val in enumerate(st.session_state.historial_nos, 1):
        st.markdown(f"- Ronda {i}: {val}")

# Botón de reinicio
st.markdown("---")
if st.button("🔁 Reiniciar todo"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()
