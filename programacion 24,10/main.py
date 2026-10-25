# Importar la clase Mensaje desde el módulo modelos
from modelos import Mensaje

# Crear (instanciar) un objeto de la clase Mensaje con datos de prueba
mi_correo = Mensaje("Victor Collazo", "Avance 2 del Proyecto")

# Imprimir en consola el resultado del método de la clase
print(mi_correo.resumen())