import sqlite3
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
    except:
        print("Uporabnik z email naslovom " + email + " je že vnešen.")

    conn.commit()

def dodajSliko(naslov, vrsta, cena):
    try:
        dosegljivost = True # če jo vnesemo, je dosegljiva
        cur.execute("""
               INSERT INTO SLIKA (dosegljivost, naslov, vrsta, cena)
               VALUES (?,?,?,?)
               """, (dosegljivost, naslov, vrsta, cena))
        print("Uspešno dodana slika: " + naslov)
    except:
        print("Slika z naslovom " + naslov + " je že vnešena.")

    conn.commit()

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

        print("Geslo uporabnika: " + email + " ni pravilno.")
    except:
        print("Uporabnik z email naslovom " + email + " še ni registriran.")

    conn.commit()

def uporabniki():
    cur.execute("""
        SELECT * FROM UPORABNIK
        """)
    return cur.fetchall()


