from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/art001/')
def art001():
    return render_template('art001.html')

@app.route('/art002/')
def art002():
    return render_template('art002.html')

@app.route('/art003/')
def art003():
    return render_template('art003.html')

@app.route('/art004/')
def art004():
    return render_template('art004.html')

@app.route('/art005/')
def art005():
    return render_template('art005.html')

@app.route('/art006/')
def art006():
    return render_template('art006.html')

@app.route('/art007/')
def art007():
    return render_template('art007.html')

@app.route('/art008/')
def art008():
    return render_template('art008.html')

@app.route('/art009/')
def art009():
    return render_template('art009.html')

@app.route('/art010/')
def art010():
    return render_template('art010.html')


if __name__ == "__main__":
    app.run(debug=True)