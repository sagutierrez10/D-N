from flask import Flask, render_template, request, redirect, url_for

from ninja import Ninja
from dojo import Dojo
app = Flask(__name__)

@app.route("/")
def index():
    dojos= Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)

@app.route('/create', methods=['POST'])
def create():
    data = {
        'fn': request.form['fn'],
        'ln':request.form['ln'],
        'age':request.form['age'],
        'dojo':int(request.form['dojo'])
    }
    Ninja.save(data)
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos= Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/create/dojo', methods=['POST'])
def createDojo():
    data = {
        'fn': request.form['fn'],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def dojo(dojo_id):
    dojo_name = Dojo.get_dojo_name(dojo_id)
    if dojo_name == None: 
        return "Dojo Not Found"
    return render_template('results.html',dojo_name=dojo_name, ninjas=Ninja.get_ninjas_from_dojo(dojo_id))


if __name__ == "__main__":
    app.run(debug=True)