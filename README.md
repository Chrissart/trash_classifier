# Clasificador de Basura
El clasificador de basura es un sistema diseñado para ayudar a los alumnos de nuestra facultad a separar los residuos en los cestos públicos de manera adecuada. Este sistema utiliza técnicas de aprendizaje automático para identificar el tipo de residuo basado en imágenes y proporcionar una clasificación precisa.

## Características
- Clasifica diferentes tipos de residuos, incluyendo cartón, vidrio, metal, papel, plástico y basura miscelánea.
- Utiliza una arquitectura de red neuronal convolucional (CNN) preentrenada (ResNet101V2) para aprovechar el aprendizaje de un gran conjunto de datos (ImageNet).
- Incluye capas personalizadas para adaptar el modelo a los datos de residuos específicos de nuestra facultad.
- Utiliza técnicas como el aumento de datos, la regularización y el afinamiento para mejorar el rendimiento y la generalización del modelo.
- Proporciona una función para predecir la clase de un residuo dado una imagen.

## Instalación
1. Clona este repositorio en tu máquina local.
2. Instala las dependencias requeridas mediante el siguiente comando:
```Copy code
pip install -r requirements.txt
```
## Uso
1. Prepara tus datos de entrenamiento y validación según la estructura de carpetas requerida (consultar documentación interna).
2. Ejecuta el script de entrenamiento para entrenar el modelo utilizando los datos de entrenamiento. Esto generará un modelo entrenado guardado en un archivo .h5.
Utiliza el modelo entrenado para clasificar nuevas imágenes ejecutando el script de predicción y proporcionando la ruta de la imagen a clasificar.
3. Observa los resultados de la clasificación y la precisión obtenida.