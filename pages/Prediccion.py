import streamlit as st
import pandas as pd
import joblib  # Para cargar el modelo guardado
import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Función para cargar el archivo CSS de fondo
with open("assets/background.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Cargar el fondo
#cargar_fondo() podria faltar eso capaz, pero lo dudo a la firmexD
# Cargar el modelo (asegúrate de que el archivo .pkl del modelo esté en el mismo directorio o especifica la ruta)
modelo = joblib.load("Algorit/rf_hp.pkl") 



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

# Load the model
try:
    modelo = joblib.load("Algorit/rf_hp.pkl")
except:
    st.error("⚠️ Error: No se pudo cargar el modelo. Verifique que el archivo 'rf_hp.pkl' existe en la carpeta 'algoritmos'.")
    st.stop()

# estetica del titulo
st.markdown("""
    <style>
        /* Modificar la tipografía del título con efecto llamativo */
        .title {
            font-family: 'Segoe UI Black', 'Times New Roman', sans-serif; 
            font-size: 63px; /* Tamaño del título */
            color: #713232; /* Color del texto */
            text-align: center; /* Centrar el título */
            margin-top: 1px; /* Mover el título un poco más arriba */
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite; /* Animación */
        }

        /* Efecto de cambio de color en el título */
        @keyframes colorChange {
            0% { color: #713232; }
            50% { color: #b13131; }
            100% { color: #713232; }
        }

        /* Efecto de sombra en el título */
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title">🩺 PREDICCIÓN DE ANEMIA USANDO EL ALGORITMO RANDOM FOREST</div>
    </div>
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

# Layout en columnas
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="custom-header">📋 Datos Personales</div>', unsafe_allow_html=True)
    with st.expander("Completa tus datos personales", expanded=True):
        age = st.slider("Edad", min_value=0, max_value=110, value=30, step=1)
        sex = st.selectbox("Género", ["Masculino", "Femenino"])

# Sección de parámetros hematológicos
with col2:
    st.markdown('<div class="custom-header">🔬 Parámetros Hematológicos</div>', unsafe_allow_html=True)
    with st.expander("Introduce los datos hematológicos", expanded=True):
        rbc = st.number_input("Conteo de glóbulos rojos (RBC), millones/µL", min_value=0.0, max_value=10.0, value=4.5, step=0.1)
        hgb = st.number_input("Hemoglobina (HGB), g/dL", min_value=0.0, max_value=18.0, value=13.5, step=0.1)
        pcv = st.number_input("Hematocrito (PCV), %", min_value=0.0, max_value=100.0, value=45.0, step=0.1)

# Parámetros adicionales (Este se desplegará por defecto)
st.markdown('<div class="custom-header">📊 Parámetros Adicionales</div>', unsafe_allow_html=True)
with st.expander("Introduce otros parámetros relacionados", expanded=True):
    col3, col4 = st.columns(2)

    with col3:
        mcv = st.number_input("Volumen corpuscular medio (MCV), fL", min_value=0.0, max_value=200.0, value=90.0, step=0.1)
        mch = st.number_input("Hemoglobina corpuscular media (MCH), pg", min_value=0.0, max_value=50.0, value=30.0, step=0.1)
        mchc = st.number_input("Concentración de hemoglobina corpuscular media (MCHC), g/dL", min_value=0.0, max_value=40.0, value=33.0, step=0.1)

    with col4:
        rdw = st.number_input("Ancho de distribución de glóbulos rojos (RDW), %", min_value=0.0, max_value=100.0, value=14.0, step=0.1)
        tlc = st.number_input("Conteo total de leucocitos (TLC), células/mm³", min_value=0.0, max_value=30.0, value=6.0, step=0.1)
        plt = st.number_input("Plaquetas (PLT), miles/µL", min_value=0.0, max_value=500.0, value=250.0, step=1.0)

sex_value = 1 if sex == "Masculino" else 0

# Botón predecir
if st.button("🔍 Realizar Predicción"):
    try:
        # Crear DataFrame de entrada
        datos_entrada = pd.DataFrame({
            'Age': [age],
            'Sex': [sex_value],
            'RBC': [rbc],
            'PCV': [pcv],
            'MCV': [mcv],
            'MCH': [mch],
            'MCHC': [mchc],
            'RDW': [rdw],
            'TLC': [tlc],
            'PLT/mm3': [plt],
            'HGB': [hgb]
        })

        # Predicción (aquí debes incluir tu modelo de predicción)
        prediccion = modelo.predict(datos_entrada)[0]

        # Función para crear PDF
        def crear_pdf():
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, f"Edad: {age}")
            c.drawString(100, 735, f"Género: {'Masculino' if sex_value == 1 else 'Femenino'}")
            c.drawString(100, 720, f"RBC: {rbc}")
            c.drawString(100, 705, f"HGB: {hgb}")
            c.drawString(100, 690, f"PCV: {pcv}")
            c.drawString(100, 675, f"MCV: {mcv}")
            c.drawString(100, 660, f"MCH: {mch}")
            c.drawString(100, 645, f"MCHC: {mchc}")
            c.drawString(100, 630, f"RDW: {rdw}")
            c.drawString(100, 615, f"TLC: {tlc}")
            c.drawString(100, 600, f"PLT: {plt}")
            c.drawString(100, 585, f"Resultado de Predicción: {'Riesgo de Anemia' if prediccion == 1 else 'No hay Riesgo de Anemia'}")

            c.save()
            buffer.seek(0)
            return buffer

        # Crear PDF
        pdf_buffer = crear_pdf()

        # Convertir el PDF a base64
        pdf_base64 = base64.b64encode(pdf_buffer.read()).decode()

        # Mostrar resultado de la predicción con un estilo animado
        if prediccion == 1:
            st.markdown("""<div class="zoom-bounce" style="background-color: #ea9999; color: #B03A2E; font-weight: bold; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem; border: 2px solid #E74C3C; text-align: center; font-size: 20px; font-family: 'Times New Roman', Times New Roman; width: 100%; display: inline-block;">⚠️ El modelo predice que hay riesgo de anemia.</div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="zoom-bounce" style="background-color: #E6FFE6; color: #1E8449; font-weight: bold; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem; border: 2px solid #468c27; text-align: center; font-size: 20px; font-family: 'Times New Roman', Times New Roman; width: 100%; display: inline-block;">✅ El modelo predice que no hay riesgo de anemia.</div>""", unsafe_allow_html=True)

        # Estilos CSS personalizados para el botón de descarga
        st.markdown(""" 
            <style>
                .custom-btn {
                    font-size: 18px;
                    background-color: #ff8167 !important ;
                    color: black;
                    padding: 10px 100px;
                    border-radius: 8px;
                    border: none;
                    cursor: pointer;
                    text-align: center;
                    display: inline-block;
                    margin: 10px;
                    margin-top: 5px;  /* Ajusta esta propiedad para mover el botón en el eje Y */
                }
                .custom-btn:hover {
                    background-color: #C70039;
                }
            </style>
        """, unsafe_allow_html=True)

        # Columnas para disposición
        col_pred, col_descarga = st.columns([2.3, 1])
        with col_descarga:
            st.markdown(""" 
                <a href="data:application/pdf;base64,{}" download="resultado_prediccion.pdf">
                    <button class="custom-btn">📥 Descargar informe </button>
                </a>
            """.format(pdf_base64), unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error al realizar la predicción: {str(e)}")
