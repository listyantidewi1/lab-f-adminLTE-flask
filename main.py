from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/chartSuhu')
def suhu():
    return render_template('chart.html')

@app.route('/lampu')
def lampu():
    return render_template('lampu.html')

if __name__ == "__main__":
    app.run(debug=True)