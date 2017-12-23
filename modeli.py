import sqlite3
import datetime
import csv

baza = "spletna_trgovina.db"
conn = sqlite3.connect(baza)
cur = conn.cursor()


def dodajUporabnika(ime, priimek, email, geslo):
    try:
        cur.execute("""
               INSERT INTO UPORABNIK (ime, priimek, email, geslo)
               VALUES (?,?,?,?)
               """, (ime, priimek, email, geslo))
        print("Uspešno dodan uporabnik: " + ime + " " + priimek)

        conn.commit()
    except:
        print("Uporabnik z email naslovom " + email + " je že vnešen.")


def dodajSliko(naslov, vrsta, cena):
    try:
        dosegljivost = True # če jo vnesemo, je dosegljiva
        cur.execute("""
               INSERT INTO SLIKA (dosegljivost, naslov, vrsta, cena)
               VALUES (?,?,?,?)
               """, (dosegljivost, naslov, vrsta, cena))
        print("Uspešno dodana slika: " + naslov)

        conn.commit()
    except:
        print("Slika z naslovom " + naslov + " je že vnešena.")


def prijavaUporabnika(email, geslo):
    try:
        cur.execute("""
               SELECT geslo FROM UPORABNIK
               WHERE email = ?
               """, (email, ))
        pravoGeslo = cur.fetchone()
        if pravoGeslo[0] == geslo:
            print("Prijava uporabnika z naslovom " + email + " uspešna.")
            return True

        conn.commit()

        print("Geslo uporabnika: " + email + " ni pravilno.")
    except:
        print("Uporabnik z email naslovom " + email + " še ni registriran.")


def uporabniki():
    cur.execute("""
        SELECT * FROM UPORABNIK
        """)
    return cur.fetchall()

def dodajSlikoVKosarico(uporabnik_id, slika_id):
    try:
        datum_vstavljanja = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        cur.execute("""
               INSERT INTO KOSARICA (uporabnik_id, slika_id, datum_vstavljanja)
               VALUES (?,?,?)
               """, (uporabnik_id, slika_id, datum_vstavljanja))
        print("Uspešno dodana slika: " + str(slika_id) + " v košarico uporabnika " + str(uporabnik_id))
        conn.commit()
    except:
        print("Vnos slike v košarico ni bil uspešen.")


