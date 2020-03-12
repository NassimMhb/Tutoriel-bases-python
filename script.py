#coding:utf-8

# Ceci est un commentaire

""" Ceci est un long commentaire
sur plusieurs lignes, il faut pour cela
mettre 3 doubles cotes """

print("Bonjour tout le monde, j'utilise des simples cotes")
print("Une autre ligne")


# Passer à la ligne avec \n 
print("Test de passage à la ligne\n avec le n ")

# Mettre une tabulation avec \t
print("\tTest de tabulation avec le t ")


"""
Nommer une variable : 	doit commencer par une lettre
						ne doit pas contenir de caractères spéciaux
						ne pas contenir d'espaces
						utiliser des underscores (_)

Types standards :	entier numérique (int)
					nombre flottant (float)
					chaine de caractères (str)
					booléen (bool)
					autres (listes, dictionnaires, tuples, etc.)

Fonctions vues : 	print() -> afficher à l'écran
					input() -> lire au clavier
					type() -> retourne le type d'une donnée, variable, etc.
					int(), float(), str(), bool() -> caster une donnée, la convertir
					str.format() -> formater une chaîne

Opérateurs en Python : 	+ (addition)
						- (soustraction)
						* (multiplication)
						/ (division)
						% (modulo) -> reste d'une division Euclidienne
"""

"""
print("Cours de python sur les bases")

agePersonne = 14
prixHT = 120.46
agePersonne2 = "25"
continuer_partie = True

print(type(agePersonne))
print(type(agePersonne2))

texte = "L'âge de la personne est {} et le prix HT est de {}euros."
print(texte.format(agePersonne, prixHT))

print("Deuxième méthode : L'âge de la personne est {} et le prix HT est de {}euros.".format(agePersonne, prixHT))

#Lire clavier
nomJoueur = input("Entrez un nom de joueur :")
print("Bienvenue, ", nomJoueur)

#caster
prixHT = input("Entrez un prix HT : ")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT * 20 / 100)
print("Prix TTC =", prixTTC)

# Opérateurs en python

calcul = 5 / 2
calcul2 = 5 / 2
calcul = int(calcul)
calcul2 = float(calcul2)

print("Résultat en int =", calcul)
print("Résultat en float =", calcul2)


niveauPersonnage = input("Niveau de départ ?")
niveauPersonnage = int(niveauPersonnage)

print("Niveau du personnage", niveauPersonnage)

print("Combat réussi, tu gagnes un niveau !")
niveauPersonnage = niveauPersonnage + 1

print("Niveau du personnage", niveauPersonnage)

"""

""" Cours sur les conditions 

Conditions multiples :	and (ET)
						or (OU)
						in / not in (DANS / PAS DANS)


"""


print("Cours de python sur les conditions")

identifiant = "Nassim"
mot_de_passe ="password123"

print("Interface de connexion")

user_id = input("Entrez votre identifiant :")
user_password= input("Entrez votre mot de passe :")

if user_id == identifiant and user_password == mot_de_passe:
	print("Vous êtes connectés, bienvenue", user_id)

print("Je ne suis plus dans le if")



print("***************************Cours sur IN / NOT IN***********************************")
lettre_hasard = "b"
lettre_hasard2 = "a"

if lettre_hasard not in "aeiouy":
	print("la lettre n'est pas présente")


if lettre_hasard2 in "aeiouy":
	print("la lettre est présente")
else:
	print("La lettre n'est pas présente")

print("-----------------------------Fin de cours sur IN / NOT IN------------------------")


print("**************************Cours sur IF / ELIF / ELSE*****************************")
ageMajeur = 22

if age == 18
	print("Tu viens d'être majeur")
elif age == 50:
	print("Tu viens d'avoir 50 ans")
elif age == 60:
	print("Tu viens d'avoir 60 ans")
else:
	print("Tu as", age, "ans")

print("-----------------------------Fin de cours sur IF / ELIF / ELSE------------------------")


print("**************************Cours sur les booléens*****************************")


print("-----------------------------Fin de cours sur les booléens------------------------")