from flask import Flask, Response, jsonify, request
from domain import Studenti, Projekti, Grupe

app = Flask(__name__)

@app.route("/studenti", methods=["GET"])
def handle_studenti():
    studenti = Studenti.listaj()
    return jsonify({"STUDENT": studenti})

@app.route("/studenti", methods=["POST"])
def handle_studenti_dodaj():
    status, greske = Studenti.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/projekti", methods=["GET"])
def handle_projekti():
    projekti = Projekti.listaj()
    return jsonify({"Studentov projekt": projekti})

@app.route("/projekti", methods=["POST"])
def handle_projekti_dodaj():
    status, greske = Projekti.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/grupe", methods=["GET"])
def handle_grupe():
    grupe = Grupe.listaj()
    return jsonify({"Studentova grupa": grupe})

@app.route("/grupe", methods=["POST"])
def handle_grupe_dodaj():
    status, greske = Grupe.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

if __name__ == '__main__':
    app.debug = True
    app.run()