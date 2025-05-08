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
modelo = joblib.load("Algorit/kart_hp.pkl") 


#  Cargando el MODELO ENTRENADOO
try:
    modelo = joblib.load("Algorit/kart_hp.pkl")
except:
    st.error("⚠️ Error: No se pudo cargar el modelo. Verifique que el archivo 'kart_hp.pkl' existe en la carpeta 'algoritmos'.")
    st.stop()

##TITULO 
# ESTETICA TITULO
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
    <div class="title">🩺 PREDICCIÓN DE ANEMIA USANDO EL ALGORITMO DECISION TREE</div>
    </div>
""", unsafe_allow_html=True)


# Seccion de GLOBULOS ROJOS
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="custom-header">🔴 Glóbulos Rojos</div>', unsafe_allow_html=True)
    with st.expander("Por favor Ingrese los valores", expanded=True):
        rbc = st.number_input(
            "RBC (Glóbulos rojos) [×10⁶/µL]",
            min_value=1.36, max_value=90.80, value=5.0, step=0.1, format="%.2f"
        )
        
        hgb = st.number_input(
            "HGB (Hemoglobina) [g/dL]",
            min_value=-10.00, max_value=87.10, value=14.0, step=0.1, format="%.2f"
        )
        
        hct = st.number_input(
            "HCT (Hematocrito) [%]",
            min_value=2.00, max_value=3715.00, value=42.0, step=0.1, format="%.2f"
        )


# Sección de GLOBULOS BLANCOS
with col2:
    st.markdown('<div class="custom-header">⚪ Glóbulos Blancos</div>', unsafe_allow_html=True)
    with st.expander("Por favor Ingrese los valores", expanded=True):
        wbc = st.number_input(
            "WBC (Glóbulos blancos) [×10³/µL]",
            min_value=0.80, max_value=45.70, value=7.0, step=0.1, format="%.2f"
        )
        
        lymp = st.number_input(
            "LYM% (Porcentaje de linfocitos) [%]",
            min_value=6.20, max_value=91.40, value=30.0, step=0.1, format="%.2f"
        )
        
        neutp = st.number_input(
            "NEUT% (Porcentaje de neutrófilos) [%]",
            min_value=0.70, max_value=5317.00, value=60.0, step=0.1, format="%.2f"
        )
        
        lymn = st.number_input(
            "LYM# (Linfocitos absolutos) [×10³/µL]",
            min_value=0.20, max_value=41.80, value=2.0, step=0.1, format="%.2f"
        )
        
        neutn = st.number_input(
            "NEUT# (Neutrófilos absolutos) [×10³/µL]",
            min_value=0.50, max_value=44.00, value=4.0, step=0.1, format="%.2f"
        )


# Parámetros Índices Eritrocitarios y Parámetros Plaquetarios 
st.markdown('<div class="custom-header">🧪 Índices Eritrocitarios y Parámetros Plaquetarios </div>', unsafe_allow_html=True)
with st.expander("Por favor Ingrese los valores", expanded=True):
    col3, col4 = st.columns(2)

    with col3:
        mcv = st.number_input("Volumen corpuscular medio (MCV), fL", min_value=-79.30, max_value=122.10, value=90.0, step=0.1)
        mch = st.number_input("Hemoglobina corpuscular media (MCH), pg", min_value=11.40, max_value=3117.00, value=30.0, step=0.1)
        mchc = st.number_input("Concentración de hemoglobina corpuscular media (MCHC), g/dL", min_value=11.50, max_value=92.80, value=33.0, step=0.1)

    with col4:
        plt = st.number_input("Plaquetas (PLT), miles/µL", min_value=11.30, max_value=660.00, value=250.0, step=1.0)
        pdw = st.number_input("Distribución plaquetaria (PDW), %", min_value=8.40, max_value=29.20, value=14.0, step=0.1)
        pct = st.number_input("Plaquetocrito (PCT), %", min_value=0.01, max_value=13.60, value=2.0, step=0.1)


import pytz
from datetime import datetime

if st.button("🔍 Realizar Predicción"):
    try:
        # Crear DataFrame de entrada con los parámetros correctos
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

        # Definir las clases en el orden correcto
        clases = [
            'Healthy',
            'Iron deficiency anemia',
            'Macrocytic anemia',
            'Normocytic hypochromic anemia',
            'Normocytic normochromic anemia',
            'Other microcytic anemia'
        ]

        # Predicción
        prediccion = modelo.predict(datos_entrada)[0]

        # Obtener la fecha y hora actual en la zona horaria de Perú (GMT-5)
        peru_tz = pytz.timezone('America/Lima')
        fecha_hora_actual = datetime.now(peru_tz).strftime("%d/%m/%Y %H:%M:%S")

        # Función para crear PDF
        def crear_pdf(fecha_hora_actual):
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            c.setFont("Helvetica", 14)
            c.drawString(100, 750, f"Glóbulos Blancos (WBC): {wbc} [×10³/µL]")
            c.drawString(100, 735, f"Linfocitos (%): {lymp} [%]")
            c.drawString(100, 720, f"Neutrófilos (%): {neutp} [%]")
            c.drawString(100, 705, f"Linfocitos Absolutos (LYM#): {lymn} [×10³/µL]")
            c.drawString(100, 690, f"Neutrófilos Absolutos (NEUT#): {neutn} [×10³/µL]")
            c.drawString(100, 675, f"RBC: {rbc}")
            c.drawString(100, 660, f"Hemoglobina (HGB): {hgb}")
            c.drawString(100, 645, f"HCT: {hct}")  
            c.drawString(100, 630, f"MCV: {mcv}")
            c.drawString(100, 615, f"MCH: {mch}")
            c.drawString(100, 600, f"MCHC: {mchc}")
            c.drawString(100, 585, f"PLT: {plt}")
            c.drawString(100, 570, f"PDW: {pdw}")  
            c.drawString(100, 555, f"PCT: {pct}")
            c.drawString(100, 540, f"Resultado de Predicción: {prediccion}")
            c.drawString(100, 520, f"Fecha y hora del diagnóstico: {fecha_hora_actual}")
            c.save()
            buffer.seek(0)
            return buffer

        # Crear PDF
        pdf_buffer = crear_pdf(fecha_hora_actual)

        # Convertir el PDF a base64
        pdf_base64 = base64.b64encode(pdf_buffer.read()).decode()

        # Mostrar resultado personalizado
        if prediccion == "Healthy":
            st.markdown(f"""<div class="zoom-bounce" style="background-color: #E6FFE6; color: #1E8449; font-weight: bold; 
                            padding: 1rem; border-radius: 0.5rem; margin-top: 1rem; border: 2px solid #468c27; text-align: center; font-size: 
                            20px; font-family: 'Times New Roman', Times New Roman; width: 100%; display: inline-block;">✅ Diagnóstico: {prediccion}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="zoom-bounce" style="background-color: #ea9999; color: #B03A2E; font-weight: 
                            bold; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem; border: 2px solid #E74C3C; text-align: 
                            center; font-size: 20px; font-family: 'Times New Roman', Times New Roman; width: 100%; display: inline-block;">
                            ⚠️ Diagnóstico: {prediccion}</div>""", unsafe_allow_html=True)

        # Estilos CSS personalizados para el botón de descarga
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
                    text-align: center;
                    display: inline-block;
                    margin: 10px;
                    margin-top: 5px;
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




