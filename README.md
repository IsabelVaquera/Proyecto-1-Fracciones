# 🧮 Calculadora de Fracciones Web (MVC)

Una aplicación web desarrollada en **Python** con **Flask**, diseñada para realizar operaciones con fracciones de forma sencilla, rápida y muy visual.
Permite sumar, restar, multiplicar, dividir, comparar y ordenar fracciones, mostrando los resultados en su formato real, simplificado y decimal.

## ✨ Descripción

La **Calculadora de Fracciones** es un proyecto académico enfocado en el manejo de números racionales y la implementación de Arquitectura de Software.
La aplicación permite ingresar fracciones mediante casillas separadas para:
`Numerador` y `Denominador`

Además, simplifica automáticamente los resultados utilizando el Algoritmo de Euclides (MCD) y muestra el valor decimal equivalente para una mejor comprensión.

## 🚀 Funcionalidades

### 🧮 Operaciones básicas
La aplicación permite realizar:
* Suma (+)
* Resta (-)
* Multiplicación (x)
* División (÷)

**Ejemplos de cálculos lógicos:**
* 1/2 + 3/4 = 5/4
* 5/6 - 1/3 = 1/2
* 2/5 * 4/7 = 8/35
* 8/9 ÷ 2/3 = 4/3

### 🔍 Comparación de fracciones
Permite evaluar dos fracciones ingresadas y determinar mediante operadores lógicos cuál es la relación entre ellas.
**Ejemplo:**
`1/2` y `3/4`
**Resultado:**
`1/2 es MENOR que 3/4`

### 📊 Ordenamiento de fracciones dinámico
Permite ingresar múltiples fracciones añadiendo casillas dinámicamente y ordenarlas de menor a mayor.
**Ejemplo de entrada:**
`3/4`, `1/2`, `5/6`, `2/3`
**Resultado ordenado:**
`1/2 < 2/3 < 3/4 < 5/6`

### 🧾 Historial de operaciones (Persistente)
La aplicación incluye un historial donde se guardan las últimas operaciones realizadas.
A diferencia de calculadoras básicas, este proyecto incluye **Persistencia de Datos en JSON**, lo que significa que el historial sobrevive incluso si se apaga el servidor, permitiendo además limpiar los datos con un solo clic.

### 🖥️ Vista general de la aplicación
La interfaz es un *Dashboard* responsivo de dos columnas en tonos pastel que incluye:
* Entradas separadas para fracciones.
* Botones de operaciones aritméticas y comparación.
* Módulo de generador dinámico de cajas para ordenar.
* Resultados visuales divididos en: Valor Real, Valor Simplificado y Valor Decimal.
* Historial de operaciones persistente.
* Alertas dinámicas de error.

## 📌 Formato de entrada

La aplicación acepta números enteros en sus respectivas casillas de `Num` y `Den`.

**Ejemplos válidos:**
* Num: `1`, Den: `2`
* Num: `-5`, Den: `6`
* Num: `0`, Den: `3`

**Ejemplos inválidos:**
* Dejar casillas vacías.
* Ingresar letras o caracteres especiales.
* Num: `4`, Den: `0`

## ⚠️ Manejo de errores

La aplicación controla errores comunes en el backend, por ejemplo:
* **Denominador igual a cero:**
  * *Resultado:* `Error Matemático: El denominador no puede ser cero.`
* **División entre cero:**
  * *Resultado:* `Error: No se puede dividir por cero.`
* **Campos incompletos:**
  * *Resultado:* `Por favor llena las 4 cajas de la calculadora.`

## 🛠️ Tecnologías utilizadas

Este proyecto fue desarrollado bajo el patrón de diseño **MVC** con:
* **Python 3** (Lógica de Modelos)
* **Flask** (Framework Web y Controladores)
* **HTML5 / CSS3 Puro** (Vistas y diseño UI/UX)
* **JavaScript** (Manipulación del DOM para el ordenador múltiple)
* **JSON** (Base de datos local para persistencia)

## 📥 Descargar el proyecto

Puedes obtener el proyecto de dos formas:

**Opción 1: Descargar ZIP**
En GitHub:
`Code → Download ZIP`
Luego descomprime el archivo y entra a la carpeta del proyecto.

**Opción 2: Clonar con Git**
Ejecuta en tu terminal:
```bash
git clone <TU_ENLACE_DE_GITHUB_AQUI>

````markdown

Luego entra a la carpeta:

```bash
cd Proyecto-1-Fracciones
````

---

## 💻 Ejecución del Proyecto (Windows / Linux)

### 1. Activar el Entorno Virtual

Es recomendable ejecutar el proyecto en su propio entorno para evitar conflictos de librerías.

**En Windows:**

```bash
env\Scripts\activate
```

**En Linux / Mac:**

```bash
source env/bin/activate
```

---

### 2. Instalar Dependencias

Instala el framework web necesario para correr la aplicación:

```bash
pip install -r requirements.txt
```

---

### 3. Ejecutar el Servidor

Una vez instaladas las dependencias, levanta el servidor local:

```bash
python app.py
```

Se mostrará un mensaje indicando que el servidor está corriendo.
Abre tu navegador web y visita:

```
http://127.0.0.1:5000
```

---

## 🏗️ Arquitectura del Proyecto (MVC)

A diferencia de scripts planos, este proyecto está dividido profesionalmente:

* `models/fraccion.py`
  Lógica matemática pura (MCD, simplificación, operaciones)

* `services/historial_service.py`
  Lógica de conexión a la "base de datos" (JSON)

* `routes/calculadora_routes.py`
  Controladores (Blueprints) que dirigen el tráfico

* `templates/index.html`
  La vista renderizada al usuario final

---

## 📦 requirements.txt

El archivo `requirements.txt` indica que el proyecto necesita el framework web Flask.

Contenido principal:

```txt
Flask==3.0.0
Werkzeug<3.0.0
```

---

## 🎯 Objetivo del Proyecto

El objetivo principal de este proyecto es aplicar operaciones con fracciones usando programación estructurada y desarrollo web en Python.

También permite demostrar el dominio en:

* Patrón de Diseño MVC (Modelo-Vista-Controlador)
* Enrutamiento web con Flask (Blueprints)
* Manejo de persistencia de datos (JSON)
* Algoritmo de Euclides
* Diseño UI/UX y manipulación del DOM

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica académica de Estructura de Datos I y programación en Python.

---

## ✅ Estado del Proyecto

* 🟢 Arquitectura MVC implementada
* 🟢 Interfaz web responsiva y estilizada
* 🟢 Operaciones aritméticas completadas
* 🟢 Comparador matemático implementado
* 🟢 Ordenador de listas dinámico implementado
* 🟢 Persistencia de datos en JSON funcional

---

## 🌟 Conclusión

La Calculadora de Fracciones Web trasciende el alcance de una calculadora de consola tradicional, ofreciendo una experiencia visual limpia, modular y persistente.

Cumple con los estándares de ingeniería de software mediante su correcta separación en capas y aplicación del patrón MVC.

```
```
