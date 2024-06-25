from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photography')
def photos():  # put application's code here
    return render_template('photography.html')

@app.route('/travel')
def travel():  # put application's code here
    return render_template('travel-map.html')


if __name__ == '__main__':
    app.run()
