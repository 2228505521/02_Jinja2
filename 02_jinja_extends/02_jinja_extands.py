from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/list/')
def my_list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run()
