import time
import random
import os
import math
from pyfiglet import figlet_format

# ==============================
# MENÚ PRINCIPAL
# ==============================

def mostrar_menu_principal():
    """
    Muestra el menú de la galería de arte ASCII
    """
    print("\n" + "="*60)
    print("꒰ᐢ. .ᐢ꒱₊˚⊹   GALERÍA DE ARTE ASCII v1.0  ⊹˚₊꒰ᐢ. .ᐢ꒱")
    print("Creado por: \n [Mariana Fabiola Cisneros García\n Jennifer Atzhiri Mariscal Magaña\n Elena Yaretzi Ochoa Jarillo\n Esthela Naomi Orozco Leal]")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de Banner")
    print("3. Marcos Decorativos")
    print("4. Animaciones")
    print("5. Tabla de Multiplicar Visual")
    print("6. Salir")
    print("-"*60)
    
    seleccion = (int(input("Selecciona un número: ")))
    
    if seleccion == "1":
        menu_patrones()
        
    
# ==============================
# MENÚ PATRONES
# ==============================
def menu_patrones():
    print("\n" + "="*60)
    print("𑣲₍ ᐢ. .ᐢ₎ PATRONES GEOMÉTRICOS ₍ ᐢ. .ᐢ₎")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Pirámide")
    print("4. Volver al menú principal")
    
    seleccion = (int(input("Selecciona un número: ")))
    if seleccion == "1":
        triangulo()
    if seleccion == "2":
        cuadrado()
    if seleccion == "3":
        piramide()
    if seleccion == "4":
        mostrar_menu_principal()
        
# ==============================
# PATRONES GEOMÉTRICOS
# ==============================
def triangulo(altura):
    """
    Genera un triángulo de asteriscos de altura especificada
    """
    altura = (int(input("Ingresa la altura del triángulo: ")))
    
    for i in range(1, altura + 1):
        print("*" * i)
        return
    
def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado
    """
    lado = (int(input("Ingresa el largo del cuadrado: ")))
    
    for i in range(lado):
        print("*" * lado)
        return 

def piramide(altura):
    """
    Genera una pirámide de asteriscos de altura especificada
    """
    altura = (int(input("Ingresa la altura de la pirámide: ")))
    
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        asteriscos = "*" * (2 * i)
        print(espacios + asteriscos)
        return

# ==============================
# TEXTO ARTÍSTICO
# ==============================
def generar_banner(texto):
    """
    Genera un banner con el texto ingresado
    """
    texto = (int(input("Inserta una frase: ")))
    
    