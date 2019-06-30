from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
import datetime as dt



db = Database()
print("Radim ")


db.bind(provider='sqlite', filename='backend--Antunovic.sqlite', create_db=True)


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
    ocjene = Set("Ocjene_studenata")


class Projekt(db.Entity):
    id = PrimaryKey(str)
    link= Required(str)
    opis= Required(str)
    grupe = Required(Grupa)


class Ocjene_studenata(db.Entity):
    id = PrimaryKey(str)
    seminar=Optional(int)
    kolokvij1=Optional(int)
    kolokvij2=Optional(int)
    bodoviProjekt=Optional(int)
    brojBodova = Required(float)
    student = Required(Student)
    obrazlozenje=Optional(str)


db.generate_mapping(check_tables=True, create_tables=True)


