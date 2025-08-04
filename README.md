📌 Descripción del Proyecto
Aplicación web para la predicción del nivel de anemia mediante técnicas de Stacking Ensemble con múltiples clasificadores. Desarrollada con Streamlit y entrenada con modelos optimizados, 
esta herramienta permite un análisis automatizado a partir de datos clínicos.

🚀 Demo en línea
Accede a la aplicación aquí:
🔗 https://machinelearning-deteccion-anemia.streamlit.app/

🧪 Repositorio de experimentos
Los notebooks, análisis exploratorios, y pruebas de modelos se encuentran en el repositorio complementario:
📂 https://github.com/Fernandooo4/AnemiaEnsemblePipeline

🧠 Modelos incluidos
- Random Forest  
- LightGBM  
- SVM  
- Decision Tree  
- TabNet  
- CatBoost  

📁 Estructura del repositorio
```
.
├── .devcontainer/                  # Configuración para el entorno de desarrollo.
├── .streamlit/                     # Archivos de configuración para la aplicación Streamlit.
├── Algorit/                        # Contiene los modelos entrenados en formato .pkl.
│   ├── kart_hp.pkl                  
│   ├── lightgbm_hp.pkl              
│   ├── modelo_con_todo.pkl          
│   ├── rf_hp.pkl                    
│   ├── stacking_meta_model.pkl      
│   ├── svm_hp.pkl                   
│   └── tabnet_model.pkl             # Modelo TabNet elegido para la pagina.
├── assets/                         # Recursos para la interfaz de la aplicación.
│   ├── background.css               # Hojas de estilo CSS.
│   ├── fondo_*.css                  # Hojas de estilo específicas.
│   └── imagenes/                    # Contiene todas las imágenes usadas en la aplicación.
├── pages/                          # Páginas de la aplicación Streamlit.
│   └── principal.py                 # Código de la página principal.
├── .gitignore                      # Archivo de configuración de Git para ignorar archivos.
└── requirements.txt                # Lista de librerías y dependencias necesarias.
```
