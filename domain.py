from model import Student, Projekt, Komponenta, Grupa
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID


class Grupe:
    @db_session()
    def listaj():
        # ORM upit
        q = select(s for s in Grupa)

        def dohvati_veze(x):
            if "studenti" in x:
                x["studenti"] = [Student[y].to_dict() for y in x["studenti"]]
            return x
        grupe = [dohvati_veze(s.to_dict(with_collections=True)) for s in q]
        return grupe

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            if "studenti" in s:
                studenti_zbirno = s["studenti"]
                svi_studenti = list(Student[x] for x in studenti_zbirno)
                s["studenti"] = svi_studenti
            kreirana_grupa = Grupa(**s)
            return True, kreirana_grupa.id
        except Exception as e:
            return False, str(e)

class Studenti:
    @db_session()
    def listaj():
        q = select(s for s in Student)
        data = [x.to_dict() for x in q]
        return data,

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Student(**s)
            return True, None
        except Exception as e:
            return False, str(e)
        
class Projekti:
    @db_session()
    def listaj():
        q = select(i for i in Projekt)
        data = [x.to_dict(with_collections=True) for x in q]
        for d in data:
            komponente = d["komponente"]
         
            d["komponente"] = Projekti.dohvati_komponentu(komponente)
        return data 

    @db_session
    def dohvati_komponentu(ids):
        q = select(s for s in Komponenta if s.id in ids)
        data = [x.to_dict("ocjena student brojBodova") for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            komponente = s["komponente"]
            del s["komponente"]  
            s = Projekt(**s)
            for komponenta in komponente:
                komponenta["id"] = str(gid())
                komponenta["ispit"] = s
                st = Komponenta(**komponenta)
            return True, None

        except Exception as e:
            return False, str(e)


if __name__ == "__main__":
    studenti = Studenti.listaj()
    print(studenti)
    print("Kod studenata")
    grupe=Grupe.listaj()
    print(grupe)
    print("kod grupa sam")
    projekti=Projekti.listaj()
    print(projekti)
    print("Prosao projekte")
  
    
