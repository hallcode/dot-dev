from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photography')
def photos():
    return render_template('photography.html')

@app.route('/travel')
def travel():
    return render_template('travel-map.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
