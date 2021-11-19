c'est un  d’un module qui peut etre  intégré dans les systèmes bancaires et qui permet d'obtenir les mouvements pendant une période donnée.
*Les étapes de préparation d’environnement
 -Installation du python (configurer la variable d’environnement)
 -Taper la commande pip install virtualenvwrapper-win pour installer un environnement virtuel qui servira à lancer le projet.
 -Taper la commande mkvirtualenv nom_environnementVirtuel pour créer un environnement virtuel
 -Taper la commande workon nom_environnementVirtuel pour travailler dans l’environnement virtuel déjà créé
 - Se placer dans le dossier du projet
 * Déploiement
 -Taper la commande python manage.py runserver pour lancer l’application. (on peut modifier le port s’il est déjà utilisé en tapant la commande python manage.py runserver 
 nouveauPort )
 -S’il y a des bibliothèques additionnelles à importer, la cmd les affichera. Il suffit de taper la commande pip install nom_biblio pour les installer.
