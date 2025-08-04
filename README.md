.
├── .devcontainer/                  # Configuración para el entorno de desarrollo.
├── .streamlit/                     # Archivos de configuración para la aplicación Streamlit.
├── Algorit/                        # Contiene los modelos entrenados en formato .pkl.
│   ├── kart_hp.pkl                  # Modelo de regresión lineal.
│   ├── lightgbm_hp.pkl              # Modelo LightGBM optimizado.
│   ├── modelo_con_todo.pkl          # Modelo final de stacking con todos los modelos base.
│   ├── rf_hp.pkl                    # Modelo Random Forest optimizado.
│   ├── stacking_meta_model.pkl      # Meta-modelo para el stacking.
│   ├── svm_hp.pkl                   # Modelo SVM optimizado.
│   └── tabnet_model.pkl             # Modelo TabNet entrenado.
├── assets/                         # Recursos para la interfaz de la aplicación.
│   ├── background.css               # Hojas de estilo CSS.
│   ├── fondo_*.css                  # Hojas de estilo específicas.
│   └── imagenes/                    # Contiene todas las imágenes usadas en la aplicación.
├── pages/                          # Páginas de la aplicación Streamlit.
│   └── principal.py                 # Código de la página principal.
├── .gitignore                      # Archivo de configuración de Git para ignorar archivos.
└── requirements.txt                # Lista de librerías y dependencias necesarias.
