import os

# Liste des adresses à bloquer
sites_a_bloquer = ['www.instagram.com', 'www.snapchat.com']

# Adresse IP locale (pouvant être utilisée pour rediriger les adresses)
adresse_locale = '127.0.0.1'

# Emplacement du fichier hosts sur votre système d'exploitation (peut varier selon le système d'exploitation)
fichier_hosts = r'/private/etc/hosts'

# Ouvre le fichier hosts en mode écriture
with open(fichier_hosts, 'a') as fichier:
    # Itère à travers chaque adresse à bloquer et ajoute une ligne au fichier hosts pour rediriger l'adresse vers l'adresse IP locale
    for site in sites_a_bloquer:
        ligne = f"\n{adresse_locale} {site}"
        fichier.write(ligne)

# Rafraîchit le cache DNS pour prendre en compte les changements dans le fichier hosts
os.system('ipconfig /flushdns')