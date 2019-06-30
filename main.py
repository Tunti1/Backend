from flask import Flask, Response, jsonify, request
from domain import Studenti, Projekti, Grupe,Ocjene
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/studenti', methods=['GET', 'POST'])
def handle_studenti():
    if request.method == 'GET':
        studenti = Studenti.listaj()
        return jsonify({"studenti": studenti})
    elif request.method == 'POST':
        status, greske = Studenti.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r


@app.route("/projekti", methods=['GET', 'POST'])
def handle_projekti():
    if request.method == 'GET':
        projekti = Projekti.listaj()
        return jsonify({"Studentov_projekt": projekti})
    elif request.method == 'POST':
        status, greske = Projekti.dodaj(request.get_json())
        if status:
         return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/grupe", methods=['GET', 'POST','PUT'])
def handle_grupe():
    if request.method == 'GET':
        grupe = Grupe.listaj()
        return jsonify({"Studentova_grupa":grupe})
    elif request.method == 'POST':
        status, greske = Grupe.dodaj(request.get_json())
        print(status)
        print(greske)
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r
    elif request.method == 'PUT':
        status, greske = Grupe.update(request.get_json())
        print(status)
        print(greske)
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r



@app.route("/ocjene", methods=['GET', 'POST','put'])
def handle_ocjene():
    if request.method == 'GET':
        ocjene=Ocjene.listaj()
        return jsonify({"Ocjene":ocjene})

    elif request.method == 'POST':
        status, greske = Ocjene.dodaj(request.get_json())
        print(status)
        print(greske)
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r
    elif request.method == 'PUT':
        status, greske = Ocjene.update(request.get_json())
        print(status)
        print(greske)
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r


if __name__ == '__main__':
    app.debug = True
    app.run()