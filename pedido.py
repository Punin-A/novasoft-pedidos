def calcular_total(precio, cantidad):
    if precio < 0 or cantidad < 0:
        raise ValueError("El precio y la cantidad no pueden ser negativos")
    return round(precio * cantidad, 2)