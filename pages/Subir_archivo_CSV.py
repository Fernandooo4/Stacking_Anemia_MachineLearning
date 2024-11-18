import streamlit as st
import pandas as pd
import joblib  # Para cargar el modelo guardado
import pickle

st.markdown("""
    <style>
        /* Modificar la tipografía del título con efecto llamativo */
        .title {
            font-family: 'Segoe UI Black', 'Times New Roman', sans-serif; 
            font-size: 103px; /* Tamaño del título */
            color: #4CAF50; /* Color verde claro del texto */
            text-align: center; /* Centrar el título */
            margin-top: 1px; /* Mover el título un poco más arriba */
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite; /* Animación */
        }

        /* Efecto de cambio de color en el título */
        @keyframes colorChange {
            0% { color: #4CAF50; } /* Verde claro */
            50% { color: #388E3C; } /* Verde más oscuro */
            100% { color: #4CAF50; } /* Verde claro */
        }

        /* Efecto de sombra en el título */
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title">Sube tu archivo aqui!</div>
    </div>
""", unsafe_allow_html=True)



# Sección de predicción
st.header("Predicción de Anemia usando un archivo .csv ")
st.write("Sube un archivo CSV para realizar una predicción de anemia utilizando el algoritmo random forest.")

# Función para cargar el archivo CSS de fondo
with open("assets/fondo_csv.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carga el modelo de predicción
with open("Algorit/rf_hp.pkl", 'rb') as file:
    modelo_anemia = pickle.load(file)

# Carga del archivo CSV
archivo = st.file_uploader("Subir archivo CSV 🗂️", type="csv")

if archivo is not None:
    # Leer los datos del archivo CSV con separador ';'
    datos = pd.read_csv(archivo, sep=';')

    # Verificar y renombrar columnas si es necesario
    columnas_correctas = ['Age', 'Sex', 'RBC', 'PCV', 'MCV', 'MCH', 'MCHC', 'RDW', 'TLC', 'PLT/mm3', 'HGB']
    if list(datos.columns) != columnas_correctas:
        datos.columns = columnas_correctas

    # Mostrar una vista previa de los datos subidos
    st.write("Datos subidos:")
    st.write(datos.head())

    # Realizar las predicciones
    predicciones = modelo_anemia.predict(datos)

    # Añadir la columna 'Test' con los resultados de las predicciones (0 o 1)
    datos['Test'] = predicciones

    # Mostrar los resultados de la predicción
    st.write("Resultados de la Predicción:")
    st.write(datos[['Age', 'Sex', 'RBC', 'PCV', 'MCV', 'MCH', 'MCHC', 'RDW', 'TLC', 'PLT/mm3', 'HGB', 'Test']])

    # Guardar el nuevo archivo CSV con la columna 'Test' añadida
    archivo_actualizado = "archivo_actualizado.csv"
    datos.to_csv(archivo_actualizado, sep=';', index=False)

    # Proveer un enlace para que el usuario descargue el archivo actualizado
    st.download_button(
        label="Descargar archivo con resultados ",
        data=datos.to_csv(sep=';', index=False).encode('utf-8'),
        file_name=archivo_actualizado,
        mime="text/csv"
    )