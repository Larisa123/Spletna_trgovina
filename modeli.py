import sqlite3
import datetime
import csv

baza = "spletna_trgovina.db"
conn = sqlite3.connect(baza)
cur = conn.cursor()


def dodajUporabnika(ime, priimek, email, geslo):
    """ Doda uporabnika v bazo uporabnikov, v bistvo je to registracija, tako, da se
     uporabnik lahko z temi podatki potem prijavi. """
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
    """ Doda sliko v tabelo slik. """
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
    """ Preveri ali obstaja uporabnik z tem emailom in geslom. """
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
    """ Vrne tabelo vseh uporabnikov. """
    cur.execute("""
        SELECT * FROM UPORABNIK
        """)
    return cur.fetchall()

def slikaNaVoljo(slika_id):
    """ Vrne logično vrednost, ki nam pove, ali je slika z id = slika_id še na voljo. """
    cur.execute("""
                   SELECT dosegljivost FROM SLIKA
                   WHERE id = ?
                   """, (slika_id, ))
    return cur.fetchone()[0] # dosegljivost slike z id = slika_id


def dodajSlikoVKosarico(uporabnik_id, slika_id):
    """ Doda izbrano sliko v košarico izbranega uporabnika, če je slika še na voljo. """
    if not slikaNaVoljo(slika_id):
        print(" Ta slika več ni na voljo. ")
        return

    try:
        datum_vstavljanja = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        cur.execute("""
               INSERT INTO KOSARICA (uporabnik_id, slika_id, datum_vstavljanja)
               VALUES (?,?,?)
               """, (uporabnik_id, slika_id, datum_vstavljanja))
        print("Uspešno dodana slika: " + str(slika_id) + " v košarico uporabnika " + str(uporabnik_id))
        conn.commit()

        spremeniDosegljivostSlike(slika_id, False)
    except:
        print("Vnos slike v košarico ni bil uspešen.")

def spremeniDosegljivostSlike(slika_id, dosegljivost):
    cur.execute("""
           UPDATE SLIKA
           SET dosegljivost = (?)
           WHERE id =  (?)
           """, (1 if dosegljivost else 0, slika_id))
    conn.commit()

def prikaziKosarico():
    cur.execute("""
        SELECT * FROM KOSARICA
        """)
    return cur.fetchall()
