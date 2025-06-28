"""
  Implemente la función reemplazar_palabras(mensaje, palabras) que recibe un mensaje y una lista de
 strings donde cada string tiene el formato "palabra_vieja|palabra_nueva". Para cada string en la lista, la
 función debe reemplazar todas las ocurrencias exactas de la palabra vieja por la palabra nueva. La función
 retorna el nuevo mensaje.
 Asuma que todas las palabras en el mensaje están en minúsculas, separadas por un espacio en blanco
 y que el mensaje no contiene signos de puntuación.
 Note que en el ejemplo, la palabra "lleno" en "relleno" no se reemplaza por "repleto" por no ser una
 ocurrencia exacta. Ejemplo de entrada:
 mensaje = "comer relleno me dejó muy lleno y cuando estoy lleno no me siento 
bien"
 palabras = ["lleno|repleto", "comer|cenar", "bien|alegre"]
Ejemplo de salida:
 "cenar relleno me dejó muy repleto y cuando estoy repleto no me siento alegre"
"""