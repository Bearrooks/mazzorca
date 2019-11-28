from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/portafolio/')
def portafolio():
    return render_template('portafolio.html')

@app.route('/servicios/')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto/')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
