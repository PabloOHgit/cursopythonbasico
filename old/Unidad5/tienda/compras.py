class Producto:
    
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"El precio de {self.nombre} es {self.precio}"
    
    def mostrar(self):
        print(self.precio)
        
class Compra:
    
    def __init__(self,productos):
        self.productos = productos
        
    def totalCompra(self):
        suma = 0
        for producto in self.productos:
            suma += producto.precio
        return round(suma,2)
        # return round(sum(producto.precio for producto in self.productos), 2)
            




