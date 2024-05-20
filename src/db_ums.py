import sqlite3
import json


"""
    db_init a pour but d'initialiser la base de donnée, de créer la table, cependant, si la table existe déja, l'éxecution de cette fonction sera passé.

    envoie_database : récupère la valeur entrante récupéré par le socket, une fois que le client lui a transmis ses valeurs de monitoring
"""


def db_init():
    try:
        db = sqlite3.connect("ums.db")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE monitoring (ip TEXT, cpu_usage REAL, ram_usage REAL, disque_usage REAL)")
        db.commit()
    except :
        print("DB deja initialisée")
    finally:
        cursor.close()
        db.close()





def envoi_database(valeur_entrant, ip_entrant):

    db = sqlite3.connect("ums.db")                                 # <=== Connection à la base et création du curseur
    cursor = db.cursor()

    valeur_entrant_dict = json.loads(valeur_entrant)               # <=== valeur_entrant est récupérer par le socket en variable, les valeurs sont repassé en json like 

    cpu = None
    ram = None
    disque = None
    ip = str(ip_entrant)

    for cle, valeur in valeur_entrant_dict.items():                # <== Itération dans le json recu pour en extraire les valeurs de monitoring, puis à l'aide d'un filtre elles sont stockées dans des variables avant d'être envoyé à la db

        if (cle == "cpu_usage"):
            cpu = valeur
        elif (cle == "ram_usage"): 
            ram = valeur
        elif (cle == "disque_usage"): 
            disque = valeur
        else :
            print("erreur eheh")


    cursor.execute("INSERT INTO monitoring (ip, cpu_usage, ram_usage, disque_usage) VALUES (?, ?, ?, ?)",(ip, cpu, ram, disque))    # <= les données sont mises dans la db

    db.commit()
    cursor.close()
    db.close()



# ===DEBUG===

#v = """{"cpu_usage": 0.0, "ram_usage": 18.5, "disque_usage": 6.0}"""
#i = "10.0.100.100"

#envoi_database(v,i)
        

