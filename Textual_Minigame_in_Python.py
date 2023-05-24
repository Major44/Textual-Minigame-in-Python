"""Ce module permet de generer des valeurs aleatoires"""
import random  





"""Permet de verifier si la chaine de caracteres est un entier valide."""
def is_integer(chaineCaractere):               
    if chaineCaractere.strip() == '':
        return False
    return chaineCaractere.strip().isdigit()

motSecret = ["Secret", "Soleil", "Terre", "Mars", "Paris"]
motJoueur = ""
indice = "Si vous lavez, vous voulez le partager. Si vous le partagez, vous ne l'avez plus "
nbTentatives = 0
maxTentatives = 5
scoreJoueur = 0
niveauJoueur = 1
nomJoueur = ""
ageJoueur = ""
meilleurJoueur = "Personne"
meilleurScore = 0
lettresTrouvees = [' '] * 26
tresorTrouve = False
positionTresor = random.randint(1, 10)

print("== Mini jeu : DEVINE LE MOT SECRET ==")
print("Un mot secret est enregistre dans la base. Maintenant, vous allez essayez de le DEVINER ")
print("*** Pour vous aider, voici un indice :", indice, "***")

nomJoueur = input("Entrez votre nom : ")

while True:
    ageJoueur = input("Entrez votre Age : ")
    if not is_integer(ageJoueur):
        print("L'age saisi n'est pas un entier valide.")
        continue
    break

age = int(ageJoueur)

while True:
    motJoueur = input("Devinez le mot : ")

    motTrouve = False
    for mot in motSecret:
        if motJoueur.lower() == mot.lower():
            motTrouve = True
            break

    if motTrouve:
        print("FELICITATIONS, vous avez trouve le mot ")
        print("Relancez le JEU pour jouer a nouveau ")

        scoreJoueur += 10
        if scoreJoueur > meilleurScore:
            meilleurScore = scoreJoueur
            meilleurJoueur = nomJoueur

        print("Votre score actuel :", scoreJoueur)
        print("Meilleur score :", meilleurScore, "(Joueur :", meilleurJoueur, ")")

        break
    else:
        print("Ce n'est pas le mot secret. Essayez encore.")

        nbTentatives += 1
        if nbTentatives >= maxTentatives:
            print("Nombre maximum de tentatives atteint.")
            print("Relancez le JEU pour jouer a nouveau ")
            break

if nbTentatives < maxTentatives:
    print("Vous avez une chance de trouver un tresor ")
    positionDevinee = int(input("Essayez de deviner la position du tresor (entre 1 et 10) : "))

    if positionDevinee == positionTresor:
        print("FELICITATIONS, vous avez trouve le tresor ")
        scoreJoueur += 20
        print("Votre score actuel :", scoreJoueur)
        tresorTrouve = True
    else:
        print("Dommage, vous n'avez pas trouver le tresor.")

if tresorTrouve:
    print("Bravo ! Vous avez atteint un nouveau niveau.")
    niveauJoueur += 1
    print("Votre niveau actuel :", niveauJoueur)
