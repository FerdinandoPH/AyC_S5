import sys
import mylib
import doctest

def main():
    """
    Programa principal que ejecuta funciones de mylib según argumentos recibidos.
    
    Uso:
    python main.py <nombre_funcion> <parametros>

    Para correr los tests:
    python main.py --test

    Ejemplo:
    python main.py T 5
    """
    if '--test' in sys.argv:
        doctest.testmod(mylib, verbose=True)  # Corre los tests de mylib.py
        return
    
    if len(sys.argv) < 3:
        print("Uso: python main.py <nombre_funcion> <parametros>")
        return

    funcion = sys.argv[1]  # Nombre de la función
    parametros = [int(arg) for arg in sys.argv[2:]]  # Convierte parámetros a enteros

    # Verifica si la función existe en mylib
    if hasattr(mylib, funcion):
        funcion_a_ejecutar = getattr(mylib, funcion)  # Obtiene referencia a la función
        resultado = funcion_a_ejecutar(*parametros)  # Llama a la función con los parámetros
        print(f"{funcion}({', '.join(map(str, parametros))}) = {resultado}")
    else:
        print(f"Error: la función '{funcion}' no está definida en mylib.")

if __name__ == "__main__":
    main()
