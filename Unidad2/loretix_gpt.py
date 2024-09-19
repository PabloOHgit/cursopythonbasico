cartelera = [
    ("Forrest Gump","ficcion",142),
    ("Joker","drama",132),
    ("Gladiator II","accion",125),
    ("Dune","ficcion",166),
    ("Furiosa","aventuras",138)
]

while True:
    # Mostrar el menú y pedir una opción
    menu = int(input("Introduce la opción que desees (1-5): "))
    
    # Opción 1: Buscar una película por título
    if menu == 1:
        titulo_input = input("Elige la película a buscar por título: ")
        
        # Variable para controlar si se encontró o no la película
        pelicula_encontrada = False
        
        # Recorrer la cartelera para buscar la película
        for pelicula in cartelera: 
            if pelicula[0].lower() == titulo_input.lower():  # Comparación insensible a mayúsculas/minúsculas
                print(f"La película es, título: {pelicula[0]}, género: {pelicula[1]}, duración: {pelicula[2]} minutos.")
                pelicula_encontrada = True
                break  # Salir del bucle una vez encontrada la película
        
        # Si no se encontró ninguna película, mostrar un mensaje
        if not pelicula_encontrada:
            print("Película no encontrada en la cartelera.")
    
    # Salir del programa si se elige una opción fuera del rango (ejemplo opción 5)
    elif menu == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
