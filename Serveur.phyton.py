''' BIBLIOTHÈQUE '''

import mysql.connector # importer la librerie

''' CONNECTION A LA BASE DE DONNEE '''

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="eric",
    database="viroulaud_anna_db"
)

''' AFFICHAGE CONSOLE '''

with mydb.cursor() as mycursor: # Utilisation de "with" pour garantir la fermeture automatique du curseur après son utilisation

    ''' OPTIONS POUR L'UTILISATEUR '''
    
    print("1 - Afficher l'enregistrement d'une team")
    print("2 - Afficher tous les joueurs d'une team")
    print("3 - Afficher tous les jeux joués par une team")
    print("4 - Afficher toutes les origines des joueurs d'une team")
    print("5 - Afficher toutes les dates d'arrivée d'une team")
    print("6 - Afficher les joueurs avec la date de sortie de leur jeux")
    print("7 - Afficher tout le classement de tous les membres d'une team")

    ''' Demande à l'utilisateur de choisir une option '''
    numero = input("Rentrez le numéro de la requête que vous voulez effectuer:")
    
    '''CONDITION NUMERO 1'''
    
    if int(numero) == 1: # si le numero sectionné egal 1
    
        # Affiche l'enregistrement complet de la team spécifiée
        
        nomTeam = input("-Rentrez le nom d'une Team : ") # le nom donnée par l'utilisateur
        mycursor.execute("SELECT * FROM Team WHERE nomTeam = %s", (nomTeam,)) # requete sql %s corespond a tout l'enregistrement
        result = mycursor.fetchall() # résultats de la requête SQL exécutée stockez dans la variable result
        for row in result:
            print(row)  # Afficher les résultats
            
    elif int(numero) == 2:
    
        # Affiche les noms des joueurs d'une team spécifiée
        
        nomTeam = input("-Rentrez le nom d'une Team : ")
        mycursor.execute("SELECT nomJoueur FROM Joueur JOIN TEAM ON Team.idTeam = JOUEUR.idTeam WHERE Team.nomTeam = %s", (nomTeam,))
        result = mycursor.fetchall() 
        for row in result:
            print(row)

    elif int(numero) == 3:
    
        # Affiche les personnages joués par les joueurs d'une team spécifiée
        
        nomTeam = input("-Rentrez le nom d'une Team : ")
        mycursor.execute("SELECT DISTINCT personnage_joueur FROM Joueur JOIN TEAM ON Team.idTeam = JOUEUR.idTeam WHERE Team.nomTeam = %s ", (nomTeam,))
        result = mycursor.fetchall()
        for row in result:
            print(row)
            
    elif int(numero) == 4:
    
        # Affiche les origines des joueurs d'une team spécifiée avec le nombre de joueurs par origine
        
        nomTeam = input("-Rentrez le nom d'une Team : ")
        mycursor.execute("SELECT origine, COUNT(*) AS nombre_joueurs FROM Joueur JOIN Team ON Team.idTeam = Joueur.idTeam WHERE Team.nomTeam = %s GROUP BY origine", (nomTeam,))
        result = mycursor.fetchall()
        for row in result:
            print(row)
            
    elif int(numero) == 5:
    
        # Affiche les dates d'arrivée des joueurs dans une team spécifiée avec le nombre de joueurs par date
        
        nomTeam = input("-Rentrez le nom d'une Team : ")
        mycursor.execute("SELECT Joueur.date_arriver, COUNT(*) AS date_entrer FROM Joueur JOIN Team ON Team.idTeam = Joueur.idTeam WHERE Team.nomTeam = %s GROUP BY Joueur.date_arriver", (nomTeam,))
        result = mycursor.fetchall()
        for row in result:
            print(row)
            
    elif int(numero) == 6:
    
        # Affiche les noms des joueurs avec la date de sortie de leur jeu dans une team spécifiée
        
        nomTeam = input("-Rentrez le nom d'une Team : ")
        mycursor.execute("SELECT Joueur.nomJoueur, JEU_JOUEUR.datedesortie FROM Joueur JOIN Team ON Team.idTeam = Joueur.idTeam JOIN JEU_JOUEUR ON Joueur.personnage_joueur = JEU_JOUEUR.personnage_joueur WHERE Team.nomTeam = %s ", (nomTeam,))
        result = mycursor.fetchall()
        for row in result:
            print(row)
            
    elif int(numero) == 7:
    
        # Affiche les noms des joueurs avec leur classement dans une team spécifiée
        
        nomTeam = input("-Rentrez le nom d'une Team : ")
        mycursor.execute("SELECT Joueur.nomJoueur, Classement.classement FROM Joueur JOIN Team ON Team.idTeam = Joueur.idTeam JOIN Classement ON Team.nomTeam = Classement.nomTeam WHERE Team.nomTeam = %s", (nomTeam,))
        result = mycursor.fetchall()
        for row in result:
            print(row)

  