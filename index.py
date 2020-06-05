import random


listemots =["angle" , "armoire" , "banc" , "bureau" , "cabinet" , "carreau" , "chaise" , "classe" , "clé" , "coin" , "couloir" , "dossier" , "eau" , "école" , "écriture" , "entrée" , "escalier" , "étagère" , "étude" , "extérieur" , "fenêtre" , "intérieur" , "lavabo" , "lecture" , "lit" , "marche" , "matelas" , "maternelle" , "meuble" , "mousse" , "mur" , "peluche" , "placard" , "plafond" , "porte" , "portemanteau" , "poubelle" , "radiateur" , "rampe" , "récréation" , "rentrée" , "rideau" , "robinet" , "salle" , "savon" , "serrure" , "serviette" , "siège" , "sieste" , "silence" , "sol" , "sommeil" , "sonnette" , "sortie" , "table" , "tableau" , "tabouret" , "tapis" , "tiroir" , "toilette" , "vitre" , "wc","aller","amener","apporter","appuyer","s’asseoir","attendre","bâiller","bosser","se","coucher","dormir","éclairer","écrire","emmener","emporter","s’endormir","s’ennuyer","entrer","étudier","fermer","frapper","s’installer","se","lever","lire","ouvrir","se","presser","se","réchauffer","rentrer","se,""reposer","rester","se","réveiller","sonner","sortir","tricher","venir","absent","assis","bas","couché","haut","présent""à", "côté","à","droite","à","gauche","au","milieu","au-delà","au-dessous","au-dessus","debout","dedans","dehors","en","bas","en","face","en","haut","loin","près","tard","tôt","à","après","au","avant","contre","dans","de","derrière","devant","du","sous","sur","crayon","stylo","feutre","taille-crayon","pointe","mine","gomme","dessin","coloriage","rayure","peinture","pinceau","couleur","craie","papier","feuille","cahier","carnet","carton","ciseaux","découpage","pliage","pli","colle","affaire","boîte","casier","caisse","trousse","cartable","jouet","jeu","pion","dé","domino","puzzle","cube","perle","chose","forme","carré","rond","pâte","à","modeler","tampon","livre","histoire","bibliothèque","image","album","titre","bande","dessinée","conte","dictionnaire","magazine","catalogue","page","ligne","mot","enveloppe","étiquette","carte","d’appel","affiche","alphabet","appareil","caméscope","cassette","cédé","cédérom","chaîne","chanson","chiffre","contraire","différence","doigt","écran","écriture","film","fois","idée","instrument","intrus","lettre","liste","magnétoscope","main","micro","modèle","musique","nom","nombre","orchestre","ordinateur","photo","point","poster","pouce","prénom","question","radio","sens","tambour","télécommande","téléphone","télévision","trait","trompette","voix","xylophone","zéro","chanter","chercher","choisir","chuchoter","coller","colorier","commencer","comparer","compter","construire","continuer","copier","couper","déchirer","décoller","décorer","découper","demander","démolir","se","dépêcher","dessiner","dire","discuter","écouter","écrire","effacer","entendre","entourer","envoyer","faire","finir","fouiller","goûter","imiter","laisser","lire","mettre","montrer","ouvrir","un","livre","parler","peindre","plier","poser","prendre","préparer","ranger","réciter","recommencer","regarder","remettre","répéter","répondre","sentir","souligner","tailler","se","taire","tenir","terminer","toucher","travailler","trier","ami","attention","camarade","colère","copain","coquin","dame","directeur","directrice","droit","effort","élève","enfant","fatigue","faute","fille","garçon","gardien","madame","maître","maîtresse","mensonge","ordre","personne","retard","sourire","travail","aider","défendre","désobéir","distribuer","échanger","s’excuser","expliquer","se","fâcher","gronder","obéir","obliger","partager","prêter","priver","promettre","punir","se", "quitter","raconter","refuser","séparer"]
#nombres = random.randint(0, 20)

a=listemots[random.randint(0, 300)]
print(a)
b=listemots[random.randint(0, 300)]
print(a+" "+b)
c=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c)
d=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d)
e=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e)
f=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e+" "+f)
g=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g)
h=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h)
i=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i)
j=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i+" "+j)
k=listemots[random.randint(0, 300)]
print(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i+" "+j+" "+k)

final=[a+b+c+d+e+f+g+h+i+j+k]

fichier = open("data.txt", "a")
fichier.write(a)
fichier.write("\n")
fichier.write(a+" "+b)
fichier.write("\n")
fichier.write(a+" "+b+" "+c)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i+" "+j)
fichier.write("\n")
fichier.write(a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h+" "+i+" "+j+" "+k)
fichier.write("\n")
fichier.write("\n") 

fichier.close()