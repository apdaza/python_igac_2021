from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('carga.html')


@app.route('/cargador', methods=['POST'])
def cargador():
    archivo = request.files['file']
    nuevo_nombre = secure_filename(archivo.filename)
    archivo.save(nuevo_nombre)
    df = pd.read_csv(nuevo_nombre)
    df2 = pd.read_csv(nuevo_nombre)

    shape_original = df.shape

    df = df.groupby('ciudades')['mascotas','hijos','edades'].median().reset_index()
    print(df.head())
    shape_agrupado = df.shape
    
    df.plot(figsize = (10, 10),
            title = 'Resumen',
            kind = 'bar',
            stacked=False,
            x='ciudades')
    
    img = io.BytesIO()
    
    plt.legend()
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    df2 = df2.groupby('generos')['mascotas','hijos','edades'].median().reset_index()
    
    shape_agrupado2 = df2.shape
    
    df2.plot(figsize = (5, 5),
            title = 'Resumen',
            kind = 'bar',
            stacked=False,
            x='generos')
    
    img2 = io.BytesIO()
    
    plt.legend()
    plt.savefig(img2, format='png')
    img2.seek(0)

    plot_url2 = base64.b64encode(img2.getvalue()).decode()


    return render_template('resultados.html', plot_img = [plot_url, plot_url2],
                           formas = (shape_original, shape_agrupado, shape_agrupado2),
                           tablas=[df.to_html(classes='data', header=True, index=False),
                                   df2.to_html(classes='data', header=True, index=False)])


if __name__ == '__main__':
    app.run()
