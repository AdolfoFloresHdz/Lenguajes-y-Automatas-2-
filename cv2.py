import cv2
import numpy as np

# Cargar la imagen desde un archivo JPG
imagen = cv2.imread('tu_imagen.jpg')

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print('No se pudo cargar la imagen')
else:
    # Obtener las dimensiones de la imagen
    alto, ancho, canales = imagen.shape

    # Mostrar información sobre la imagen
    print(f'Dimensiones de la imagen: {ancho} x {alto}')
    print(f'Número de canales: {canales}')

    # Convertir la imagen a una matriz NumPy
    matriz = np.array(imagen)

    # Ahora tienes la imagen en forma de matriz NumPy y puedes realizar operaciones en ella
    # Por ejemplo, puedes acceder al valor de un píxel en las coordenadas (x, y)
    x = 100
    y = 50
    pixel = matriz[y, x]
    print(f'Valor del píxel en ({x}, {y}): {pixel}')

    # También puedes guardar la matriz como una nueva imagen si lo deseas
    # cv2.imwrite('nueva_imagen.jpg', matriz)