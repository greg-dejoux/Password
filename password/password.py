import re
import hashlib

def password():
    continuer = False
    while not continuer:
        mdp = input("Veuillez choisir votre nouveau mot de passe")
        if not len(mdp) > 8:
            print("Le mot de passe est trop court !")

        if not bool(re.search("[a-z]", mdp)):
            print("Le mot de passe ne contient pas de lettres en minuscule !")

        if not bool(re.search("[A-Z]", mdp)):
            print("Le mot de passe ne contient pas de lettres en majuscule !")

        if not bool(re.search("[0-9]", mdp)):
            print("Le mot de passe ne contient pas de chiffre !")

        if not bool(re.search("[!@#$%^&*]", mdp)):
            print("Le mot de passe ne contient pas de caractère spécial !")

        else:
            continuer = True
            print("Le mot de passe est correct !")
            # Si toutes ces conditions sont réunies, la boucle se fini et ça nous demande si on veut encrypter le mdp
            input("Voulez-vous crypter le mot de passe ?")
            if "oui":
                mdp = mdp.encode()
                crypt = hashlib.sha256(mdp)
                mdp = crypt.hexdigest()
                print("Voici votre mot de passe crypté :\n", mdp)

password()











