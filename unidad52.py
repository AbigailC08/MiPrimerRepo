from flask import Flask, request, redirect, url_for
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Lista de preguntas y respuestas correctas
preguntas = [
    {
        "pregunta": "¿Qué librería se usa en este código para graficar funciones?",
        "opciones": ["matplotlib", "seaborn", "plotly", "bokeh"],
        "respuesta": "matplotlib"
    },
    {
        "pregunta": "¿Cuál es la función de numpy para calcular el valor absoluto?",
        "opciones": ["np.abs", "np.absval", "np.absvalue", "np.absfunc"],
        "respuesta": "np.abs"
    },
    {
        "pregunta": "¿Cuál es el rango por defecto para la evaluación de funciones de Fourier en el código?",
        "opciones": ["(-10, 10)", "(-π, π)", "(-1, 1)", "(-5, 5)"],
        "respuesta": "(-π, π)"
    },
    {
        "pregunta": "¿Qué método se usa para evaluar la función ingresada por el usuario?",
        "opciones": ["eval", "exec", "compile", "lambda"],
        "respuesta": "eval"
    },
    {
        "pregunta": "¿Qué función en numpy se usa para calcular el logaritmo natural?",
        "opciones": ["np.log", "np.log10", "np.log2", "np.logn"],
        "respuesta": "np.log"
    },
    {
        "pregunta": "¿Cuál de estos es una función trigonométrica en numpy?",
        "opciones": ["np.tan", "np.tangent", "np.sine", "np.cosine"],
        "respuesta": "np.tan"
    },
    {
        "pregunta": "¿Qué función en matplotlib se usa para guardar la gráfica en memoria?",
        "opciones": ["savefig", "save", "write", "export"],
        "respuesta": "savefig"
    },
    {
        "pregunta": "¿Qué método en numpy se usa para verificar NaN?",
        "opciones": ["np.isnan", "np.isnan", "np.nan", "np.checknan"],
        "respuesta": "np.isnan"
    },
    {
        "pregunta": "¿Qué función en numpy se usa para crear un array de valores lineales?",
        "opciones": ["np.linspace", "np.array", "np.arange", "np.range"],
        "respuesta": "np.linspace"
    },
    {
        "pregunta": "¿Qué valor de umbral de aciertos define un resultado favorable en este código?",
        "opciones": ["50%", "60%", "70%", "80%"],
        "respuesta": "60%"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        respuestas_usuario = [request.form.get(f"pregunta_{i}", "") for i in range(len(preguntas))]
        respuestas_incorrectas = sum(1 for i in range(len(preguntas)) if respuestas_usuario[i] != preguntas[i]["respuesta"])

        # Si más de 6 respuestas incorrectas, reiniciar
        if respuestas_incorrectas > 6:
            return render_reiniciar("Has respondido incorrectamente más de 6 preguntas. Intenta de nuevo.")
        # Si todas correctas, avanzar a graficar
        elif respuestas_incorrectas == 0:
            return redirect(url_for('graficar'))
        # Si respuestas correctas pero no todas, reiniciar
        else:
            return render_reiniciar("No alcanzaste el mínimo de respuestas correctas para avanzar. Intenta de nuevo.")
    
    return render_preguntas()

def render_preguntas():
    preguntas_html = "<h2>Test de conocimientos</h2><form method='POST'>"
    for i, p in enumerate(preguntas):
        opciones_html = ""
        for opcion in p["opciones"]:
            opciones_html += f"<label><input type='radio' name='pregunta_{i}' value='{opcion}'> {opcion}</label><br>"
        preguntas_html += f"<p><strong>{p['pregunta']}</strong><br>{opciones_html}</p>"
    preguntas_html += "<button type='submit'>Enviar Respuestas</button></form>"

    return f"""
    <html>
    <head>
        <title>Cuestionario</title>
        <style>
            body {{ font-family: Arial, sans-serif; background:#f0f4f8; margin:0; padding:20px; }}
            .container {{ max-width:800px; margin:auto; background:#fff; padding:20px; border-radius:8px; }}
            h2 {{ text-align:center; }}
            .error {{ color:red; text-align:center; margin-top:10px; }}
            button {{ display:block; margin:20px auto; padding:10px 20px; font-size:16px; background:#007bff; color:#fff; border:none; border-radius:5px; cursor:pointer; }}
            button:hover {{ background:#0069d9; }}
        </style>
    </head>
    <body>
        <div class="container">
            {preguntas_html}
        </div>
    </body>
    </html>
    """

def render_reiniciar(mensaje):
    return f"""
    <html>
    <head>
        <title>Respuesta Incorrecta</title>
        <style>
            body {{ font-family: Arial, sans-serif; background:#f0f4f8; margin:0; padding:20px; }}
            .container {{ max-width:800px; margin:auto; background:#fff; padding:20px; border-radius:8px; text-align:center; }}
            p {{ color:red; font-weight:bold; }}
            a {{ display:block; margin-top:20px; text-decoration:none; color:#007bff; }}
            a:hover {{ text-decoration:underline; }}
        </style>
    </head>
    <body>
        <div class="container">
            <p>{mensaje}</p>
            <a href="/">Reiniciar Cuestionario</a>
        </div>
    </body>
    </html>
    """

@app.route('/graficar', methods=['GET', 'POST'])
def graficar():
    grafica = ""
    error_msg = ""
    funcion_input = ""

    if request.method == 'POST':
        # Obtener función del formulario
        ejemplo = request.form.get('ejemplo', '')
        if ejemplo and ejemplo != 'ninguno':
            funcion_input = ejemplo
        else:
            funcion_input = request.form.get('funcion', '')

        try:
            x = np.linspace(-np.pi, np.pi, 400)
            allowed_names = {
                "x": x,
                "abs": np.abs,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "exp": np.exp,
                "log": np.log,
                "sqrt": np.sqrt,
                "pi": np.pi,
                "e": np.e
            }
            y = eval(funcion_input, {"__builtins__": None}, allowed_names)
            if not hasattr(y, "__len__") or len(y) != len(x):
                raise ValueError("La función no devuelve un array válido.")
            if np.any(np.isnan(y)) or np.any(np.isinf(y)):
                raise ValueError("La función contiene valores inválidos (NaN o inf).")
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, linewidth=2, color='dodgerblue')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.title("f(x) = " + funcion_input, fontsize=16)
            plt.xlabel("x", fontsize=14)
            plt.ylabel("f(x)", fontsize=14)
            img = io.BytesIO()
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            grafica = base64.b64encode(img.getvalue()).decode()
        except Exception as e:
            error_msg = f"Error en la función: {str(e)}. Usa funciones y operaciones permitidas."

    # Página de graficar, incluyendo ejemplos
    ejemplos = [
        "sin(x)", "cos(x)", "x**2", "log(abs(x))",
        "np.sin(x)", "np.cos(x)", "np.tan(x)", "np.exp(x)",
        "np.abs(x)", "np.sin(x)+0.5*np.sin(3*x)"
    ]
    ejemplos_html = "<h3>Ejemplos de funciones:</h3>"
    for e in ejemplos:
        ejemplos_html += f"<button name='ejemplo' value='{e}'> {e} </button> "

    return f"""
    <html>
    <head>
        <title>Graficar función</title>
        <style>
            body {{ font-family: Arial, sans-serif; background:#f0f4f8; margin:0; padding:20px; }}
            .container {{ max-width:800px; margin:auto; background:#fff; padding:20px; border-radius:8px; }}
            h2 {{ text-align:center; }}
            form {{ display:flex; flex-direction:column; align-items:center; }}
            input[type=text] {{ width:80%; padding:10px; font-size:16px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px; }}
            button {{ padding:10px 20px; font-size:16px; background:#007bff; color:#fff; border:none; border-radius:5px; margin:5px; cursor:pointer; }}
            button:hover {{ background:#0069d9; }}
            img {{ display:block; margin:20px auto; max-width:100%; border-radius:8px; }}
            .error {{ color:red; text-align:center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Ingrese una función para graficar</h2>
            {f"<div class='error'>{error_msg}</div>" if error_msg else ""}
            <form method='POST'>
                <input type='text' name='funcion' placeholder='Ejemplo: sin(x), cos(x), x**2, log(abs(x))' value="{funcion_input}">
                <input type='hidden' name='ejemplo' value=''>
                {ejemplos_html}
                <button type='submit'>Graficar</button>
            </form>
            {f'<img src="data:image/png;base64,{grafica}" alt="Gráfica">' if grafica else ''}
        </div>
        <script>
            document.querySelectorAll("button[name='ejemplo']").forEach(btn => {{
                btn.onclick = function() {{
                    document.querySelector("input[name='funcion']").value = this.value;
                }};
            }});
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)