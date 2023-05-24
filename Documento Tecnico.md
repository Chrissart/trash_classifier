# Clasificador de Basura
El clasificador de basura es un sistema diseñado para ayudar a los alumnos de tu facultad a separar los residuos en los cestos públicos de manera adecuada. Este sistema utiliza técnicas de aprendizaje automático para identificar el tipo de residuo basado en imágenes y proporcionar una clasificación precisa.

## Funcionamiento
El sistema de clasificación de basura consta de varios componentes clave:

1. **Preprocesamiento de Datos**: El sistema comienza con un conjunto de datos etiquetados que consiste en imágenes de diferentes tipos de residuos (cartón, vidrio, metal, papel, plástico y basura miscelánea). Estas imágenes se dividen en conjuntos de entrenamiento y validación.

2. **Transferencia de Aprendizaje**: El sistema utiliza una arquitectura de red neuronal convolucional (CNN) preentrenada llamada ResNet101V2. Esta arquitectura se utiliza como modelo base y se carga con pesos preentrenados utilizando el conjunto de datos de ImageNet. Se congela la mayoría de las capas del modelo base para evitar que se modifiquen durante el entrenamiento posterior.

3. **Afinamiento (Fine-Tuning)**: Después de agregar capas personalizadas encima del modelo base, se descongelan las últimas capas del modelo base para permitir que se ajusten durante el entrenamiento. Esto permite que el modelo se adapte específicamente a los datos de residuos utilizados en tu facultad.

4. **Entrenamiento y Validación**: El modelo se entrena utilizando el generador de datos que carga y aumenta las imágenes de entrenamiento. Se utilizan técnicas como el aumento de datos y la regularización para mejorar la generalización del modelo. El proceso de entrenamiento se detiene tempranamente si no se observa una mejora en la pérdida de validación después de cierto número de épocas consecutivas.

5. **Evaluación y Predicción**: Después de entrenar el modelo, se evalúa su rendimiento utilizando el generador de datos de validación. Se calcula la precisión y se muestra una matriz de confusión para evaluar las clasificaciones correctas e incorrectas. Además, se proporciona una función predecir_imagen que permite ingresar una imagen nueva y obtener la clase predicha y la probabilidad asociada.

## Razones detrás del diseño
El diseño del clasificador de basura se basa en varias consideraciones:

1. **Transferencia de Aprendizaje**: Se utiliza una red neuronal preentrenada (ResNet101V2) para aprovechar el conocimiento aprendido en un gran conjunto de datos (ImageNet). Esto ayuda a mejorar el rendimiento y la eficiencia del modelo, ya que no es necesario entrenarlo desde cero.

2. **Agregación de Capas Personalizadas**: Se agregan capas personalizadas encima del modelo base para adaptar el modelo a los datos de residuos específicos de tu facultad. Estas capas adicionales permiten aprender representaciones más específicas y complejas de los residuos en el contexto de tu entorno.
    
    1. **Capa de Promedio Global (Global Average Pooling)**: Se agrega una capa de promedio global después del modelo base para reducir la dimensionalidad de las características extraídas y capturar información global sobre las imágenes de residuos. Esto ayuda a generar una representación compacta y significativa de las características de las imágenes.

    2. **Capas Totalmente Conectadas y Capas de Dropout**: Se agregan capas totalmente conectadas con funciones de activación ReLU para capturar relaciones no lineales más complejas entre las características extraídas y las etiquetas de las clases. Además, se agregan capas de dropout para evitar el sobreajuste y mejorar la generalización del modelo.

    3. **Regularización**: Se utilizan técnicas de regularización, como la regularización L2, para evitar el sobreajuste del modelo y mejorar su capacidad de generalización.

    El diseño de las capas adicionales y la arquitectura del modelo se basa en un equilibrio entre la complejidad del modelo y la cantidad de datos disponibles. Se realizaron ajustes y experimentos iterativos para encontrar una configuración óptima que logre un buen rendimiento y generalización aunque el conjunto de datos flaquee por no ser de uso especifico para entornos abiertos cómo en la facultad.

2. **Afinamiento**: Se descongelan y se ajustan las últimas capas del modelo base para adaptarlo específicamente a los datos de residuos utilizados en tu facultad. Esto permite que el modelo capture características más específicas de los residuos relevantes para el contexto de tu facultad.

3. **Regularización**: Se utilizan técnicas de regularización, como la regularización L2, para evitar el sobreajuste del modelo y mejorar su capacidad de generalización.

4. **Aumento de Datos**: Se aplica aumento de datos durante el entrenamiento para aumentar la diversidad de los datos de entrenamiento y mejorar la capacidad del modelo para manejar diferentes variaciones en las imágenes de residuos.

5. **Evaluación y Visualización**: Se evalúa el rendimiento del modelo utilizando métricas como la precisión y se muestra una matriz de confusión para proporcionar una comprensión más detallada de las clasificaciones correctas e incorrectas. Esto ayuda a evaluar y comprender la efectividad del clasificador de basura.

## Uso en la Separación de Residuos
El clasificador de basura diseñado con este sistema proporciona una herramienta útil para los alumnos de tu facultad al separar los residuos en los cestos públicos. Los usuarios pueden capturar una imagen del residuo y utilizar la función predecir_imagen para obtener la clasificación predicha y la probabilidad asociada. Esto les permite determinar en qué cesto colocar correctamente el residuo y contribuir a una separación adecuada de los residuos.

ESpero que este clasificador de basura ayude a los alumnos a tomar decisiones informadas sobre la separación de residuos y contribuya a promover prácticas sostenibles en el entorno de tu facultad.