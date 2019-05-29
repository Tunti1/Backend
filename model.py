from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
import datetime as dt



db = Database()
print("Radim ")


db.bind(provider='sqlite', filename='backend-Antunovic.sqlite', create_db=True)


class Grupa(db.Entity):
    id = PrimaryKey(str)
    naziv = Required(str)
    studenti = Set("Student")
    projekt_ = Set("Projekt")


class Student(db.Entity):
    id = PrimaryKey(str)
    jmbag = Required(str)
    ime = Required(str)
    Prezime = Required(str)
    grupe = Set(Grupa)
    komponente = Set("Komponenta")


class Projekt(db.Entity):
    id = PrimaryKey(str)
    link= Required(str)
    maxBodova = Optional(int)
    komponente = Set("Komponenta")
    grupe = Required(Grupa)


class Komponenta(db.Entity):
    id = PrimaryKey(int)
    brojBodova = Required(float)
    ocjena = Optional(int)
    projekt = Required(Projekt)
    student = Required(Student)


db.generate_mapping(check_tables=True, create_tables=True)


