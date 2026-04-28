# 🧮 Calculadora de Fracciones Racionales

Aplicación web desarrollada en Python con Flask para la gestión, cálculo, comparación y ordenamiento de fracciones matemáticas, implementando el **Algoritmo de Euclides**.

## 🚀 Características Principales
* **Aritmética Exacta:** Suma, resta, multiplicación y división de números racionales.
* **Simplificación Automática:** Reducción de fracciones a su mínima expresión usando Máximo Común Divisor (MCD).
* **Comparador Lógico:** Evaluación mediante sobrecarga de operadores matemáticos (`<`, `>`, `==`).
* **Ordenador Dinámico:** Interfaz responsiva que permite añadir múltiples fracciones y ordenarlas con `.sort()`.
* **Persistencia JSON:** Sistema de almacenamiento local para guardar el historial de operaciones.

## 🏗️ Arquitectura de Software (MVC)
El proyecto sigue principios SOLID y el patrón **Modelo-Vista-Controlador**, estructurado en:
* `/models`: Tipo de Dato Abstracto (ADT) `Fraccion`. Aislado de la web.
* `/routes`: Blueprints de Flask que actúan como controladores HTTP.
* `/services`: Lógica de persistencia de datos (`historial_service.py`).
* `/templates`: UI minimalista estilo "Dashboard" usando CSS puro con paleta de colores pastel.

## 💻 Instalación y Ejecución Local

1. Clonar este repositorio:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>