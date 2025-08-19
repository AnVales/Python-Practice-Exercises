"""
Ejemplo de uso de diccionarios: obtener el valor (capital) de una clave (país) usando el método get().
"""
dic = {
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín"
}

pais = "Francia"
capital = dic.get(pais, "Capital no encontrada")
print(capital)