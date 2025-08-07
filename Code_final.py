import streamlit as st

# Inicializar estado
if 'total_vos' not in st.session_state:
    st.session_state.total_vos = 0
if 'total_nos' not in st.session_state:
    st.session_state.total_nos = 0
if 'historial_vos' not in st.session_state:
    st.session_state.historial_vos = []
if 'historial_nos' not in st.session_state:
    st.session_state.historial_nos = []
if 'input_vos' not in st.session_state:
    st.session_state.input_vos = ""
if 'input_nos' not in st.session_state:
    st.session_state.input_nos = ""

# Estilo visual
st.markdown("""
    <style>
        .historial {
            font-size: 0.85rem;
            color: gray;
            margin-top: 0.5rem;
        }
        .puntos-totales {
            font-weight: bold;
            font-size: 1.2rem;
            margin-top: 0.5rem;
        }
        .stTextInput input {
            text-align: center;
        }
        .row-container {
            display: flex;
            justify-content: space-between;
        }
        .column {
            flex: 1;
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Marcador Truco")

# Crear columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vos")
    input_vos = st.text_input("Puntos ronda (Vos)", key="input_vos", label_visibility="collapsed")
    st.markdown(f"<div class='puntos-totales'>Puntos totales: {st.session_state.total_vos}</div>", unsafe_allow_html=True)
    st.markdown("<div class='historial'>" + "<br>".join(map(str, st.session_state.historial_vos[::-1])) + "</div>", unsafe_allow_html=True)

    if st.button("Tercera (20)", key="t_vos"):
        st.session_state.total_vos += 20
        st.session_state.historial_vos.append(3)

    if st.button("Bolete / Rebolote (20)", key="b_vos"):
        st.session_state.total_vos += 20
        st.session_state.historial_vos.append(20)

    for val in [50, 100, 150, 200]:
        if st.button(f"{val}", key=f"{val}_vos"):
            st.session_state.total_vos += val
            st.session_state.historial_vos.append(val)

with col2:
    st.subheader("Nos")
    input_nos = st.text_input("Puntos ronda (Nos)", key="input_nos", label_visibility="collapsed")
    st.markdown(f"<div class='puntos-totales'>Puntos totales: {st.session_state.total_nos}</div>", unsafe_allow_html=True)
    st.markdown("<div class='historial'>" + "<br>".join(map(str, st.session_state.historial_nos[::-1])) + "</div>", unsafe_allow_html=True)

    if st.button("Tercera (20)", key="t_nos"):
        st.session_state.total_nos += 20
        st.session_state.historial_nos.append(3)

    if st.button("Bolete / Rebolote (20)", key="b_nos"):
        st.session_state.total_nos += 20
        st.session_state.historial_nos.append(20)

    for val in [50, 100, 150, 200]:
        if st.button(f"{val}", key=f"{val}_nos"):
            st.session_state.total_nos += val
            st.session_state.historial_nos.append(val)

# Botón siguiente ronda
if st.button("Siguiente ronda"):
    try:
        if input_vos and not input_nos:
            puntos = int(input_vos)
            st.session_state.total_vos += puntos
            st.session_state.total_nos += 162 - puntos
            st.session_state.historial_vos.append(puntos)
            st.session_state.historial_nos.append(162 - puntos)
        elif input_nos and not input_vos:
            puntos = int(input_nos)
            st.session_state.total_nos += puntos
            st.session_state.total_vos += 162 - puntos
            st.session_state.historial_nos.append(puntos)
            st.session_state.historial_vos.append(162 - puntos)

        if "input_vos" not in st.session_state:
            st.session_state.input_vos = ""
        if "input_nos" not in st.session_state:
            st.session_state.input_nos = ""
    except ValueError:
        st.error("Introduce un número válido.")
