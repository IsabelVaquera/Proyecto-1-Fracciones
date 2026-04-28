"""
Módulo de enrutamiento (Controlador) para la Calculadora de Fracciones.

Recibe las peticiones HTTP (GET y POST) desde la vista (index.html),
gestiona la lógica del negocio orquestando los modelos y servicios,
y retorna la plantilla renderizada.
"""

from flask import Blueprint, render_template, request
from models.fraccion import Fraccion
from services.historial_service import cargar_historial, guardar_historial, limpiar_historial

calculadora_bp = Blueprint("calculadora", __name__)

# Carga en memoria el historial al iniciar el módulo
historial_operaciones = cargar_historial()

@calculadora_bp.route("/", methods=["GET", "POST"])
def calculadora():
    """
    Ruta principal que procesa todos los formularios de la aplicación.
    Maneja tres acciones principales: Ordenar múltiples, Limpiar historial,
    y Operaciones aritméticas básicas/Comparación.
    """
    resultado = None
    comparacion = None
    lista_ordenada = None
    error = None

    if request.method == "POST":

        # ---------------------------------------------------------
        # BLOQUE 1: Acción de limpiar el historial
        # ---------------------------------------------------------
        if "limpiar_historial" in request.form:
            limpiar_historial()
            historial_operaciones.clear()

        # ---------------------------------------------------------
        # BLOQUE 2: Acción del Ordenador Dinámico de múltiples fracciones
        # ---------------------------------------------------------
        elif "ordenar" in request.form:
            try:
                # Flask atrapa arreglos de inputs con el mismo nombre usando getlist()
                nums = request.form.getlist("nums_orden[]")
                dens = request.form.getlist("dens_orden[]")

                # Comprensión de listas para instanciar objetos Fraccion válidos
                fracciones_obj = [
                    Fraccion(int(n), int(d))
                    for n, d in zip(nums, dens)
                    if n.strip() and d.strip()
                ]

                # Python usa el método mágico __lt__ de la clase Fraccion para ordenar
                fracciones_obj.sort()
                lista_ordenada = " < ".join([f.valor_crudo() for f in fracciones_obj])
                historial_operaciones.insert(0, f"Ordenadas: {lista_ordenada}")

            except Exception:
                error = "Error en el formato de las fracciones a ordenar."

        # ---------------------------------------------------------
        # BLOQUE 3: Acción de la Calculadora Básica y el Comparador
        # ---------------------------------------------------------
        else:
            try:
                f1 = Fraccion(int(request.form["num1"]), int(request.form["den1"]))
                f2 = Fraccion(int(request.form["num2"]), int(request.form["den2"]))
                operacion = request.form.get("operacion")

                if operacion == "comparar":
                    if f1 == f2:
                        comparacion = f"{f1.valor_crudo()} es IGUAL a {f2.valor_crudo()}"
                    elif f1 < f2:
                        comparacion = f"{f1.valor_crudo()} es MENOR que {f2.valor_crudo()}"
                    else:
                        comparacion = f"{f1.valor_crudo()} es MAYOR que {f2.valor_crudo()}"

                    historial_operaciones.insert(0, f"Comparación: {comparacion}")

                else:
                    # Diccionario para mapear la operación seleccionada a su método correspondiente
                    operaciones = {
                        "sumar": ("+", f1.sumar(f2)),
                        "restar": ("-", f1.restar(f2)),
                        "multiplicar": ("x", f1.multiplicar(f2)),
                        "dividir": ("÷", f1.dividir(f2)),
                    }

                    simbolo, resultado = operaciones.get(operacion, ("", None))

                    if resultado:
                        historial_operaciones.insert(
                            0,
                            f"{f1.valor_crudo()} {simbolo} {f2.valor_crudo()} = {resultado}"
                        )

            except ZeroDivisionError as e:
                error = str(e)
            except ValueError:
                error = "Ingresa números válidos."

        # ---------------------------------------------------------
        # BLOQUE FINAL: Mantenimiento de la persistencia
        # ---------------------------------------------------------
        if not error:
            # Mantenemos la cola de historial a un máximo de 5 elementos
            if len(historial_operaciones) > 5:
                historial_operaciones.pop()

            guardar_historial(historial_operaciones)

    # Renderiza la plantilla inyectando las variables de estado actualizadas
    return render_template(
        "index.html",
        resultado=resultado,
        comparacion=comparacion,
        lista_ordenada=lista_ordenada,
        error=error,
        historial=historial_operaciones
    )