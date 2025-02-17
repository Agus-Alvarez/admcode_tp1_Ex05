# calculator_package/test/test_complex_calculator.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from calculator_package.calculator.complex_calculator import SimpleComplexCalculator

def test_calculadora():
    """
    Función principal de pruebas para la calculadora de números complejos.
    Incluye pruebas de validación de tipos y manejo de errores.
    """
    calc = SimpleComplexCalculator()
    
    print("=== Pruebas de la Calculadora de Números Complejos ===")
    
    # 1. Pruebas de operaciones básicas con números válidos
    print("\n1. Pruebas con números válidos:")
    complejo1 = [4, 5]  # Números enteros
    complejo2 = [2, 3]
    complejo3 = [4.67, 5.89]  # Números flotantes
    complejo4 = [2.0, 3.0]
    
    print("\n1.1 Suma con enteros:")
    resultado = calc.sumar(complejo1, complejo2)
    print(f"Resultado: {calc.formato_complejo(resultado)}")
    
    print("\n1.2 Suma con flotantes:")
    resultado = calc.sumar(complejo3, complejo4)
    print(f"Resultado: {calc.formato_complejo(resultado)}")
    
    # 2. Pruebas de validación de tipos
    print("\n2. Pruebas de validación de tipos:")
    
    print("\n2.1 Lista con elementos no numéricos:")
    resultado = calc.sumar([1, "a"], complejo1)
    print(f"Resultado esperado: ERROR")
    print(f"Resultado obtenido: {resultado}")
    
    print("\n2.2 Lista con longitud incorrecta:")
    resultado = calc.sumar([1], complejo1)
    print(f"Resultado esperado: ERROR")
    print(f"Resultado obtenido: {resultado}")
    
    # 3. Pruebas de división por cero
    print("\n3. Pruebas de división por cero:")
    try:
        resultado = calc.dividir(complejo1, [0, 0])
        print("Prueba fallida: No se detectó el error de división por cero")
    except ZeroDivisionError as e:
        print(f"Prueba exitosa: {e}")
    
    # 4. Pruebas de formato con entradas inválidas
    print("\n4. Pruebas de formato con entradas inválidas:")
    
    print("\n4.1 Formato con entrada no numérica:")
    resultado = calc.formato_complejo([1, "a"])
    print(f"Resultado esperado: ERROR")
    print(f"Resultado obtenido: {resultado}")
    
    print("\n4.2 Formato con lista incorrecta:")
    resultado = calc.formato_complejo([1])
    print(f"Resultado esperado: ERROR")
    print(f"Resultado obtenido: {resultado}")
    
    # 5. Pruebas de operaciones con mezcla de tipos
    print("\n5. Pruebas con mezcla de tipos (enteros y flotantes):")
    complejo_mixto1 = [1, 2.5]
    complejo_mixto2 = [3.5, 4]
    
    print("\n5.1 Suma con tipos mixtos:")
    resultado = calc.sumar(complejo_mixto1, complejo_mixto2)
    print(f"Resultado: {calc.formato_complejo(resultado)}")
    
    print("\n5.2 Multiplicación con tipos mixtos:")
    resultado = calc.multiplicar(complejo_mixto1, complejo_mixto2)
    print(f"Resultado: {calc.formato_complejo(resultado)}")

if __name__ == '__main__':
    test_calculadora()