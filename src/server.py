# Configuration de l'adresse IP du serveur ainsi que du port
import socket
from db_ums import db_init, envoi_database

HOST = ""              # L'ip doit être un str (ne pas set d'ip pour écouter sur toutes les interfaces)
PORT = 55000           # Le port est un int
MaxConnection = 10     # Nombre maximum de connexion simultanée (INT) (utilisé dans la méthode serveur.listen())

def run_serveur(): 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:


        try:

            serveur.bind((HOST, PORT))                                                                  # Je set l'IP ainsi que le port
            serveur.listen(MaxConnection)                                                               # Nombre maximum de connexions simultanées
            print(f"Serveur en attente de connexions sur le port {PORT}")                               # Message de statut

            while True:

                connection, adresse_client = serveur.accept()                                           # Accepter la connexion entrante
                print(f"Connexion reçue de {adresse_client}")

                with connection:

                    while True:

                        data = connection.recv(1024)                                                    # Réception des données du client

                        if not data:
                            print("Connexion fermée par le client.")
                            break

                        data_recu = data.decode('utf-8')                                                # Décodage des données reçues
                        print(f"Données reçues : {data_recu}")
                        print(type(data_recu))
                        envoi_database(data_recu,adresse_client) 


        except Exception as erreur:
            print(f"""
            
            Une erreur s'est produite : 

            {erreur}
            
            """)



db_init()
run_serveur()
