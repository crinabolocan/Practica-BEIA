from flask import Flask, render_template

app = Flask(__name__)

# Definirea rutei pentru pagina de resurse
@app.route('/')
def resources():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
