import streamlit as st
import pandas as pd
import joblib  # Para cargar el modelo guardado
import pickle
import random
import time


# Función para cargar el archivo CSS de fondo
with open("assets/fondo_FAQ.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("""
    <style>
        /* Modificar la tipografía del título con efecto llamativo */
        .title {
            font-family: 'Segoe UI Black', 'Times New Roman', sans-serif; 
            font-size: 94px; /* Tamaño del título */
            color: #3a7ca5; /* Color azul claro del texto */
            text-align: center; /* Centrar el título */
            margin-top: 1px; /* Mover el título un poco más arriba */
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite; /* Animación */
        }

        /* Efecto de cambio de color en el título */
        @keyframes colorChange {
            0% { color: #3a7ca5; } /* Azul claro */
            50% { color: #1f4e6c; } /* Azul más oscuro */
            100% { color: #3a7ca5; } /* Azul claro */
        }

        /* Efecto de sombra en el título */
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title">PREGUNTAS🔎⬇️</div>
    </div>
""", unsafe_allow_html=True)


# CSS personalizado
st.markdown("""
    <style>
        /* Estilos generales */
        .main {
            background: linear-gradient(to bottom, #c9e3ff, #e1f0ff);
        }
        
        body {
            background-color: #aed2f8 !important ; 
        }

        .stApp {
            background: linear-gradient(to bottom, #c9e3ff, #e1f0ff);
        }
        
        /* Título principal */
        .title-container {
            background: linear-gradient(45deg, #3498db, #2ecc71);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
            /* Se eliminó la animación */
        }
        
        .main-title {
            color: white;
            font-size: 2.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Contenedor de preguntas */
        .qa-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .qa-container:hover {
            transform: translateY(-5px);
        }
        
        /* Estilos para preguntas */
        .question {
            color: #2c3e50;
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 10px;
            border-left: 5px solid #3498db;
            padding-left: 10px;
        }
        
        /* Estilos para respuestas */
        .answer {
            color: #34495e;
            font-size: 1.1em;
            line-height: 1.6;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 5px;
        }
        
        /* Título de categoría */
        .category-title {
            color: #2c3e50;
            font-size: 1.8em;
            margin: 30px 0;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 2px;
            background: linear-gradient(45deg, #3498db, #2ecc71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Estilos para listas */
        .answer ul {
            list-style-type: none;
            padding-left: 20px;
        }
        
        .answer ul li:before {
            content: "•";
            color: #3498db;
            font-weight: bold;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }
    </style>
""", unsafe_allow_html=True)

# Datos de preguntas y respuestas
qa_data = {
    "Conceptos Básicos de la Anemia": [
        {
            "pregunta": "¿Qué es exactamente la anemia y cómo afecta al cuerpo humano?",
            "respuesta": "La anemia es una condición médica en la que el cuerpo no tiene suficientes glóbulos rojos saludables para transportar el oxígeno adecuadamente a los tejidos del cuerpo. Esto resulta en fatiga, debilidad y otros síntomas porque los órganos no reciben el oxígeno necesario para funcionar correctamente."
        },
        {
            "pregunta": "¿Cuáles son los principales parámetros que se utilizan para diagnosticar la anemia?",
            "respuesta": """Los parámetros clave incluyen:
            • Hemoglobina (Hb): Normal 12-16 g/dL en mujeres, 13-17 g/dL en hombres
            • Hematocrito (Hct): 36-46% en mujeres, 41-53% en hombres
            • Volumen Corpuscular Medio (VCM): 80-96 femtolitros
            • Hierro sérico: 60-170 μg/dL"""
        },
        {
            "pregunta": "¿Cuáles son las causas comunes de la anemia?",
            "respuesta": "Las causas comunes incluyen deficiencia de hierro, deficiencia de vitamina B12, pérdida crónica de sangre (como en úlceras o menstruación abundante), trastornos de la médula ósea y enfermedades crónicas."
        },
        {
            "pregunta": "¿Qué efectos secundarios pueden surgir si no se trata la anemia?",
            "respuesta": "Si no se trata, la anemia puede causar problemas graves como daño a los órganos, insuficiencia cardíaca, y en casos extremos, puede ser mortal."
        },
        {
            "pregunta": "¿Cómo puede la anemia afectar a los niños y mujeres embarazadas?",
            "respuesta": "En los niños, la anemia puede afectar el desarrollo cognitivo y físico. En mujeres embarazadas, puede aumentar el riesgo de parto prematuro, bajo peso al nacer y complicaciones postparto."
        }
    ],
    "Machine Learning en la Detección de Anemia": [
        {
            "pregunta": "¿Cómo se aplica el Machine Learning en la detección de anemia?",
            "respuesta": """El Machine Learning se utiliza para:
            • Analizar hemogramas completos automáticamente
            • Predecir la probabilidad de anemia basada en múltiples parámetros
            • Clasificar el tipo de anemia (ferropénica, megaloblástica, etc.)
            • Monitorear la evolución del tratamiento"""
        },
        {
            "pregunta": "¿Qué tan preciso es el Machine Learning en la detección de anemia?",
            "respuesta": "Los modelos de ML actuales pueden alcanzar una precisión del 85-95% en la detección de anemia, dependiendo del algoritmo utilizado y la calidad de los datos. Los algoritmos más exitosos son Random Forest y Redes Neuronales Profundas."
        },
        {
            "pregunta": "¿Qué tipos de datos son necesarios para entrenar un modelo de Machine Learning para detectar anemia?",
            "respuesta": """Los datos necesarios incluyen:
            • Resultados de hemogramas
            • Información sobre antecedentes médicos
            • Factores como la edad, el sexo y la dieta
            • Datos sobre la frecuencia de visitas médicas y tratamientos anteriores"""
        },
        {
            "pregunta": "¿Qué algoritmos de Machine Learning se usan más en la detección de anemia?",
            "respuesta": """Algunos algoritmos comunes son:
            • Random Forest
            • Support Vector Machines (SVM)
            • Redes Neuronales Artificiales
            • K-Nearest Neighbors (KNN)"""
        }
    ],
    "Aplicación Clínica": [
        {
            "pregunta": "¿Qué herramientas de ML se utilizan en la práctica clínica?",
            "respuesta": """Se emplean:
            • Aplicaciones móviles para análisis de palidez
            • Sistemas de soporte de decisiones clínicas
            • Algoritmos de predicción de respuesta al tratamiento
            • Plataformas de monitoreo continuo"""
        },
        {
            "pregunta": "¿Cómo beneficia el ML a los profesionales de la salud en el manejo de la anemia?",
            "respuesta": """Los beneficios incluyen:
            • Diagnóstico más rápido y preciso
            • Reducción de errores humanos
            • Seguimiento más eficiente del tratamiento
            • Personalización de los tratamientos según características del paciente"""
        }
    ]
}

# Visualización de preguntas y respuestas
for category, questions in qa_data.items():
    st.markdown(f"<div class='category-title'>{category}</div>", unsafe_allow_html=True)
    for qa in questions:
        st.markdown(f"<div class='qa-container'><div class='question'>{qa['pregunta']}</div><div class='answer'>{qa['respuesta']}</div></div>", unsafe_allow_html=True)
        time.sleep(0.)  # Pequeña pausa para mejorar la experiencia visual
