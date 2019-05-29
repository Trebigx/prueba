from flask import Flask, render_template


app = Flask (__name__)


@app.route('/r')
def registro():
    return render_template('registro_page.html')

@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/salir')
def about():
    return render_template('about_page.html')

if  __name__ == '__main__':
    app.run (debug=True)