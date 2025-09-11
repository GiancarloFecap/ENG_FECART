from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/teste')
def test():
    return render_template('teste.html')


if __name__ == '__main__':
    app.run(debug=True)