"""
Módulo que define el Tipo de Dato Abstracto (ADT) Fracción.

Contiene la lógica matemática pura para representar, simplificar
y operar con números racionales, aislando esta responsabilidad
del resto de la aplicación web.
"""

import math

class Fraccion:
    """
    Representa un número racional con numerador y denominador.
    Simplifica automáticamente la fracción al instanciarse.
    """

    def __init__(self, numerador: int, denominador: int):
        """
        Inicializa la fracción y valida que el denominador no sea cero.
        """
        if denominador == 0:
            raise ZeroDivisionError("Error Matemático: El denominador no puede ser cero.")
        
        # Guardamos el estado original para mostrar el cálculo crudo en la vista
        self.num_original = numerador
        self.den_original = denominador
        
        self.numerador = numerador
        self.denominador = denominador
        self._simplificar()

    def valor_crudo(self) -> str:
        """
        Devuelve la representación en cadena de la fracción original sin simplificar.
        """
        if self.den_original == 1:
            return str(self.num_original)
        if self.num_original == 0:
            return "0"
        return f"{self.num_original}/{self.den_original}"
    
    def _simplificar(self) -> None:
        """
        Método privado que simplifica la fracción usando el algoritmo de Euclides (MCD).
        """
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd
        
        # Normalizamos el signo para que siempre esté en el numerador
        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador

    def sumar(self, otra: 'Fraccion') -> 'Fraccion':
        """Suma dos fracciones y devuelve una nueva instancia."""
        nuevo_num = (self.numerador * otra.denominador) + (otra.numerador * self.denominador)
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def restar(self, otra: 'Fraccion') -> 'Fraccion':
        """Resta dos fracciones y devuelve una nueva instancia."""
        nuevo_num = (self.numerador * otra.denominador) - (otra.numerador * self.denominador)
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def multiplicar(self, otra: 'Fraccion') -> 'Fraccion':
        """Multiplica dos fracciones y devuelve una nueva instancia."""
        return Fraccion(self.numerador * otra.numerador, self.denominador * otra.denominador)

    def dividir(self, otra: 'Fraccion') -> 'Fraccion':
        """Divide dos fracciones y devuelve una nueva instancia."""
        if otra.numerador == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return Fraccion(self.numerador * otra.denominador, self.denominador * otra.numerador)

    def valor_decimal(self) -> float:
        """Convierte la fracción a su valor decimal equivalente."""
        return self.numerador / self.denominador

    def __lt__(self, otra: 'Fraccion') -> bool:
        """Sobrecarga del operador '<' para permitir el uso de .sort() en listas."""
        return self.valor_decimal() < otra.valor_decimal()

    def __eq__(self, otra: object) -> bool:
        """Sobrecarga del operador '==' para comparar igualdades aritméticas."""
        if not isinstance(otra, Fraccion):
            return False
        return self.numerador == otra.numerador and self.denominador == otra.denominador

    def __str__(self) -> str:
        """Representación en cadena de la fracción simplificada."""
        if self.denominador == 1:
            return str(self.numerador)
        if self.numerador == 0:
            return "0"
        return f"{self.numerador}/{self.denominador}"