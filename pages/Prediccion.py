import joblib  # o import pickle si tu modelo está con pickle
import streamlit as st
import pandas as pd
import joblib  # Para cargar el modelo guardado
import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import pytz
from datetime import datetime
import matplotlib.pyplot as plt

# Función para cargar el archivo CSS de fondo
with open("assets/background.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
try:
    modelo_data = joblib.load("Algorit/modelo_con_todo.pkl")
    modelo = modelo_data["modelo"]
    label_encoder = modelo_data["label_encoder"]
#    Ya es el modelo directamente


except Exception as e:
    st.error(f"⚠️ Error: No se pudo cargar el modelo. Detalles: {str(e)}")
    st.stop()

# ESTETICA TITULO
st.markdown("""
    <style>
        .title {
            font-family: 'Segoe UI Black', 'Times New Roman', sans-serif; 
            font-size: 63px;
            color: #1b5e20;
            text-align: center;
            margin-top: 1px;
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite;
        }

        @keyframes colorChange {
            0% { color: #1b5e20; }
            50% { color: #255d27; }
            100% { color: #1b5e20; }
        }

        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(27, 94, 32, 0.3), 0 0 10px rgba(27, 94, 32, 0.2); }
            50% { text-shadow: 0 0 8px rgba(27, 94, 32, 0.3), 0 0 16px rgba(27, 94, 32, 0.2); }
            100% { text-shadow: 0 0 5px rgba(27, 94, 32, 0.3), 0 0 10px rgba(27, 94, 32, 0.2); }
        }
    </style>
    <div class="title">🩺 PREDICCIÓN DEL TIPO DE ANEMIA CON STACKING ENSEMBLE</div>
""", unsafe_allow_html=True)


# Carga del modelo previamente entrenado


# Interfaz de entrada"Algorit/modelo_con_todo.pkl"
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="custom-header">🔴 Glóbulos Rojos</div>',
                unsafe_allow_html=True)
    with st.expander("Por favor Ingrese los valores", expanded=True):
        rbc = st.number_input("RBC (×10⁶/µL)", min_value=1.36,
                              max_value=90.80, value=5.0, step=0.1)
        hgb = st.number_input("HGB (g/dL)", min_value=0.00,
                              max_value=87.10, value=14.0, step=0.1)
        hct = st.number_input("HCT (%)", min_value=2.00,
                              max_value=3715.00, value=42.0, step=0.1)

with col2:
    st.markdown('<div class="custom-header">⚪ Glóbulos Blancos</div>',
                unsafe_allow_html=True)
    with st.expander("Por favor Ingrese los valores", expanded=True):
        wbc = st.number_input("WBC (×10³/µL)", min_value=0.80,
                              max_value=45.70, value=7.0, step=0.1)
        lymp = st.number_input("LYM% (%)", min_value=6.20,
                               max_value=91.40, value=30.0, step=0.1)
        neutp = st.number_input(
            "NEUT% (%)", min_value=0.70, max_value=5317.00, value=60.0, step=0.1)
        lymn = st.number_input(
            "LYM# (×10³/µL)", min_value=0.20, max_value=41.80, value=2.0, step=0.1)
        neutn = st.number_input(
            "NEUT# (×10³/µL)", min_value=0.50, max_value=44.00, value=4.0, step=0.1)

st.markdown('<div class="custom-header">🧪 Índices Eritrocitarios y Parámetros Plaquetarios </div>',
            unsafe_allow_html=True)
with st.expander("Por favor Ingrese los valores", expanded=True):
    col3, col4 = st.columns(2)
    with col3:
        mcv = st.number_input("MCV (fL)", min_value=0.0,
                              max_value=122.10, value=90.0, step=0.1)
        mch = st.number_input("MCH (pg)", min_value=11.40,
                              max_value=3117.00, value=30.0, step=0.1)
        mchc = st.number_input(
            "MCHC (g/dL)", min_value=11.50, max_value=92.80, value=33.0, step=0.1)
    with col4:
        plt = st.number_input("PLT (miles/µL)", min_value=11.30,
                              max_value=660.00, value=250.0, step=1.0)
        pdw = st.number_input("PDW (%)", min_value=8.40,
                              max_value=29.20, value=14.0, step=0.1)
        pct = st.number_input("PCT (%)", min_value=0.01,
                              max_value=13.60, value=2.0, step=0.1)

# Botón para predecir
if st.button("🔍 Realizar Predicción"):
    try:
        datos_entrada = pd.DataFrame({
            'WBC': [wbc],
            'LYMp': [lymp],
            'NEUTp': [neutp],
            'LYMn': [lymn],
            'NEUTn': [neutn],
            'RBC': [rbc],
            'HGB': [hgb],
            'HCT': [hct],
            'MCV': [mcv],
            'MCH': [mch],
            'MCHC': [mchc],
            'PLT': [plt],
            'PDW': [pdw],
            'PCT': [pct]
        })

        clases = [
            'Healthy',
            'Iron deficiency anemia',
            'Macrocytic anemia',
            'Normocytic hypochromic anemia',
            'Normocytic normochromic anemia',
            'Other microcytic anemia'
        ]

        prediccion_codificada = modelo.predict(datos_entrada)
        prediccion = label_encoder.inverse_transform(prediccion_codificada)[0]


        fecha_hora_actual = datetime.now(pytz.timezone(
            'America/Lima')).strftime("%d/%m/%Y %H:%M:%S")

        def crear_pdf(fecha_hora_actual):
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            c.setFont("Helvetica", 14)
            y = 750
            for label, val in [
                ("WBC", wbc), ("LYM%", lymp), ("NEUT%", neutp), ("LYM#", lymn),
                ("NEUT#", neutn), ("RBC", rbc), ("HGB", hgb), ("HCT", hct),
                ("MCV", mcv), ("MCH", mch), ("MCHC", mchc), ("PLT", plt),
                ("PDW", pdw), ("PCT", pct), ("Diagnóstico", prediccion),
                ("Fecha y hora", fecha_hora_actual)
            ]:
                c.drawString(100, y, f"{label}: {val}")
                y -= 15
            c.save()
            buffer.seek(0)
            return buffer

        pdf_buffer = crear_pdf(fecha_hora_actual)
        pdf_base64 = base64.b64encode(pdf_buffer.read()).decode()

        if prediccion == "Healthy":
            st.markdown(f"""<div style="background-color:#E6FFE6;color:#1E8449;padding:1rem;border-radius:8px;
            border:2px solid #468c27;text-align:center;font-size:20px;">✅ Diagnóstico: {prediccion}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style="background-color:#FDEDEC;color:#B03A2E;padding:1rem;border-radius:8px;
            border:2px solid #E74C3C;text-align:center;font-size:20px;">⚠️ Diagnóstico: {prediccion}</div>""", unsafe_allow_html=True)

        st.markdown("""
            <style>
                .custom-btn {
                    font-size: 18px;
                    background-color: #ff8167 !important;
                    color: black;
                    padding: 10px 100px;
                    border-radius: 8px;
                    border: none;
                    cursor: pointer;
                    margin-top: 5px;
                }
                .custom-btn:hover {
                    background-color: #C70039;
                }
            </style>
        """, unsafe_allow_html=True)

        col_pred, col_descarga = st.columns([2.3, 1])
        with col_descarga:
            st.markdown(f"""
                <a href="data:application/pdf;base64,{pdf_base64}" download="resultado_prediccion.pdf">
                    <button class="custom-btn">📥 Descargar informe</button>
                </a>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error al realizar la predicción: {e}")


# TODOOO LO DE ABAJO ES PURO ESTETICA!!!
# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
        background-color: #ff4b4b;
        color: white;
    }
.stButton>button {
    width: 100%;
    margin-top: 1rem;
    background-color: #ff4b4b !important;
    color: white !important;
    transition: background-color 0.3s ease !important; /* Añadimos !important */
}

.stButton>button:hover {
    background-color: #b21414 !important; /* Color con !important */
}

}

    }
    .css-1d391kg {
        padding: 2rem;
        border-radius: 0.5rem;
        background-color: #f7f7f7;
    }
    h1 {
        color: #ff4b4b !important;
        margin-bottom: 2rem;
    }
    .stExpander {
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    /* Animación para los cuadros de entrada */
    .stSlider, .stNumberInput, .stSelectbox, .stExpander, .stButton>button {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .stSlider:hover, .stNumberInput:hover, .stSelectbox:hover, .stExpander:hover, .stButton>button:hover {
        transform: translateY(-5px); /* Movimiento sutil hacia arriba */
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); /* Efecto sombra al pasar el puntero */
    }

    </style>
""", unsafe_allow_html=True)


# Insertar CSS personalizado
st.markdown(
    """
    <style>
    /* Borde negro grueso en los expanders y cuadros de entrada */
    .stExpander, .stSlider, .stNumberInput, .stSelectbox {
        border: 3px solid black;
        border-radius: 8px;
        margin-top: 15px; /* Ajusta la separación hacia abajo */
        padding: 10px; /* Ajusta el espacio interno */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Sombra para efecto visual */
    }

    /* Margen inferior para los expanders */
    .stExpander {
        margin-bottom: 20px; /* Espacio extra entre secciones */
    }

    /* Estilo de los textos de las secciones */
    .custom-header {
        font-family: 'Times New Roman', serif;  /* Cambiado a Times New Roman */
        font-size: 35px;  /* Tamaño mayor */
        font-weight: bold;
        color: #2C3E50;
        padding: 1px 0;
        margin-bottom: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
