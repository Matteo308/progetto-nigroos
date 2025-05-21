from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/concetti')
def concetti():
    return render_template('concetti.html')

@app.route('/thread')
def thread():
    return render_template('thread.html')

@app.route('/grafi')
def grafi():
    return render_template('grafi.html')

@app.route('/contatti')
def contatti():
    return render_template('contatti.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)