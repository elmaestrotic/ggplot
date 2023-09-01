import pandas as pd
from plotnine import *

# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 8, 12, 6, 9]
})

def print_points():
    # Crear la gráfica utilizando ggplot con marcadores de punto en diferentes colores
    p = (
            ggplot(data) +
            aes(x='x', y='y') +
            geom_point(shape='o', size=4, color='blue') +  # Cambiar el color y forma de los puntos
            labs(title='Gráfico de Puntos', x='Eje X', y='Eje Y')
    )
    print(p)

def generar_grafica_barras():
    # Crear un DataFrame de ejemplo
    data = pd.DataFrame({
        'Periodo': ['Periodo 1', 'Periodo 2', 'Periodo 3', 'Periodo 4'],
        'Rendimiento': [80, 55, 90, 75]
    })

    # Crear la gráfica de barras utilizando Plotnine
    p = (
        ggplot(data, aes(x='Periodo', y='Rendimiento', fill='Periodo')) +
        geom_bar(stat='identity') +
        labs(title='Comparativa de Rendimiento Académico por Periodo', x='Período', y='Rendimiento') +
        theme_minimal() +
        scale_fill_manual(values=['blue', 'red', 'green', 'purple'])
    )

    print(p)

# Función principal
if __name__ == '__main__':
    generar_grafica_barras()
