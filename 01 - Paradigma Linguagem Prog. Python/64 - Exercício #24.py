from flask import Flask
app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    instr = '<p>Emtre com, dois números</p>'
    return boas_vindas + instr

@app.route('/somar/')
@app.route('/somar/<num1>/<num2>')

def soma(num1 = 0, num2 = 0):
    resultado = float(num1) + float(num2)
    return str(resultado)

if __name__ == '__main__':
    app.run(debug = True)