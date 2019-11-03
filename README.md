# SVN et réseaux de neurones

Ce repository contient la matière pour le cours _SVN et réseaux de
neurones_ à l'IAE de l'Université de Nantes.  Vous y trouverez
également les notes pour le prof qui serait peut-être, par un joli
hasard, compréhensibles en lecture simple.  Le cours comporte neuf
séances de deux heures en CM dont la dernière sera l'examen final.
L'objectif du cours est de comprendre les techniques de machines à
support vectoriel (SVM) et des réseaux de neurones (ANN) avec
applications en python.

Vous aurez des travaux à faire chez vous entre les cours qui ne seront
pas notées.  En général, si vous faites les travail au fur et à
mesure, vous réussirez.  Et si vous ne le faites pas, vous trouverez
vite que la matière est impossible.

Nous allons prendre comme hypothèses au moins les suppositions suivantes :

* Vous savez programmer.  Vous connaissez déjà au moins les bases de python
  (par exemple, de l'année dernière).
* Vous connaissez des moteurs de recherche, Stack Overflow, etc.
* Vous êtes suffisamment compétent en anglais pour lire des textes
  simples (surtout, tutoriels) en anglais.  Ou que vous avez découvert
  que les moteurs de traduction marchent suffisamment bien pour s'en
  sortir.

Lors des cours magistraux, vous n'aurez pas besoin de vos
ordinateurs.  D'ailleurs, il est fortement recommandé d'avoir du papier
et de pouvoir écrire, car les présentations seront souvent visuelles.

Un élément intentionné du cours est l'usage des outils d'industrie.
Je vous encourage à les maîtriser.  Le cours sera plus facile ainsi
que votre vie professionnelle après.

# Évaluation

* Projet final en binôme
  * *(0 points)* Vous composer en binôme (maximum un groupe de 3)
  * *(2 points)* Choisir une compétition kaggle (kaggle.com),
    idéalement non-clôturée, pas la même qu'une autre équipe, et pas
    un "getting started competition".  Communiquer un repo github (en
    mode public) sur lequel vous allez collaborer et communiquer votre
    projet.  Communiquer la composition de votre équipe.  Le tout par
    _issue_ sur **ce** repo (du cours).  (date butoir : deuxième
    cours)
  * *(2 points)* Communiquer l'achèvement de votre projet (date butoir : avant
    06h00 le jour de la huitième (N-1) séance, par issue ici
  * *(2 points, extra)_ Communiquer l'achèvement de votre projet une semaine avant la date
    butoir
  * *(10 points)* Rapport écrit (dans votre repo github, en format pdf) qui explique
    ce que vous avez fait, ce que vous avez essayé, ce qui a marché,
    ce qui n'a pas marché, et quels sont vos résultats - en français
    ou en anglais comme vous voulez
  * *(5 points)* Votre projet peut tourner dans une machine vagrant dont vous
    fournissez le Vagrantfile, tout le code source est présent avec
    mode d'emploi
  * *(5 points)* Le résultat que donne votre code est cohérent avec votre rapport
  * *(20 points)* Examen écrit et individuel lors de la dernière séance dont les questions
    ciblerons votre projet

# Github

Vous êtes en train de préparer une carrière en économétrie ou data
science, qui sont plus proches qu'ils pourraient vous sembler à cet
instant.  Dans ces domaines, vous trouverez que deux points sont
beaucoup plus importants à votre réussite que les algorithmes :
pouvoir bien formuler une question et pouvoir bien expliquer les
résultats.  Aussi, une partie importante de votre note dans ce cours
serait basée sur la clarté de vos communications (y compris votre code).

Vous devez chaque groupe créer un repository github pour le cours afin de
pouvoir collaborer entre vous.  Git et github sont des outils que vous
allez très probablement rencontrer dans vos vies professionnelles.  En
tant qu'étudiant en M2 EKAP, vous avez la capacité d'apprendre un
outil informatique en autonomie.  Aussi, le sujet du cours ne sera pas
"comment se servir de git".  Il existe des milliers de tutoriels
là-dessus dans des styles variés pour accommoder tout goût.

L'attente est que vous utilisez git comme outil de travail.
Recherchez comment faire un bon message de commit, comment décider
commenter votre code ou le commit ou les deux.  Git n'est pas
simplement un outil pour télécharger votre code, et une manque
d'histoire cohérente de développement serait vu comme de la mauvaise
communication (comme dans la vraie vie).

# Questions hors séance

Toute question que vous posez hors cours doit passer par un github
issue -- sur le repo du cours s'il est général, sur votre repo s'il
est spécifique à votre projet.  (Vous devez me taguer pour que je le vois.)

Pour toute question en remote, les règles suivants de bons sens s'appliquent :

* C'est une question.  Un bon contre-exemple serait la phrase "je ne comprends pas X".
* Vous expliquez d'abord ce que vous avez compris, ce que vous avez essayé.
* Vous expliquez avec qui dans le cours vous avez consulté / collaboré
  afin d'essayer de comprendre.  Vous les taguez également.  Consulter
  sans réfléchir est une erreur (très commune).  Ne
  consulter personne est généralement une très mauvaise stratégie.
* Sachez que le debugging est difficile pour tout le monde.  Si un
  point de debugging me paraît facile, je vous montrerez ce que je
  vois.  Mais souvent il faut passer du temps, qu'on soit débutant ou
  confirmé, afin de trouver un bug.  C'est d'ailleurs comment on
  apprend.

Les question en cours, bien évidemment, ne sont pas assujetties à
cette déontologie (peut-être un peu sévère).  Vous êtes en cours pour
l'interaction et vous devez poser vos questions réfléchies au fur et à
mesure !


# Python

Il est bien évidemment impératif que vous puissiez écrire et essayer
des programs en python.  Avant la première séance, il convient donc de
télécharger et installer python sur votre ordinateur.  (Les salles
informatiques sont à votre disposition dans la limite des règles de
l'IAE, surtout si vous n'avez pas de matériel vous-même.)  La bonne
nouvelle, c'est que les logiciels requis sont gratuits et (selon votre
système d'exploitation) relativement simple.

Les logiciels nécessaires seront également installés sur les machines
des salles informatiques.


## Linux

C'est un de rare cas dans la vie où tout est plus facile sur linux
(pour une certain définition de "facile").  Il suffit d'installer
python3 et virtualenv.  Virtualenv vous crée un environnement pour
python largement indépendant de ce qui est présent sur votre
ordinateur.

Sur ubuntu, on peut taper

    $ sudo apt-get update
	$ sudo apt-get install python3-virtualenv python3
	$ sudo apt-get install gcc g++ python3-dev

Puis, dans votre répertoire de travail :

    $ virtualenv --python=python3 venv
	$ . venv/bin/activate                   # N'oubliez pas le "." au début.
	$ pip install -r requirements.txt

Le fichier `requirements.txt` se trouve [ici](requirements.txt).  Le
plus facile est de cloner ce repository.  Voir plus bas, "jour 1", sur
`git clone`.

Cela marche également sur MacOS si vous êtes à l'aise dans le
terminal.

Les machines virtuelles "vagrant" peuvent être très utiles.  Le fichier
[Vagrantfile](Vagrantfile) définit une machine virtuelle dont le
professeur se sert pour ses testes et pour évaluer votre code.
N'hésitez pas à vous en servir également.  Le web a beaucoup de
tutoriels sur vagrant.


## MacOS, Windows

Apparemment l'usage de python sur Windows marche très bien sauf quand
ce n'est pas le cas.  Les systèmes MacOS et linux sont beaucoup plus
répandus dans le domaine de stat/ML/data science.  Ceci dit, un
produit commercial avec une très bonne offre gratuite existe :
[anaconda](https://www.anaconda.com/).  Il est téléchargeable
[ici](https://www.anaconda.com/download/).  Il est également
disponible pour linux.


## Tester

Vous avez sans doute le bon instinct de se poser la question "est-ce
que j'ai bien suivi cette démarche ?".  Vous pouvez lancer `ipython3`
(commandline: ipython3; sinon, il y a un icône quelque part).  Et puis
vous devez pouvoir faire le suivant comme teste de base :

	(venv) vagrant@ubuntu-focal:/vagrant$ ipython
	Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
	Type 'copyright', 'credits' or 'license' for more information
	IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

	In [1]: import numpy as np

	In [2]: import scipy as sp

	In [3]: import sklearn

	In [4]: print("Hello, world!")
	Hello, world!

	In [5]: quit
	(venv) vagrant@ubuntu-focal:/vagrant$ 

Il existe également une version du même logiciel qui vous présente un
éditeur dans votre browser : le Jupyter notebook.  Si vous l'essayez
sans browser, vous auriez ça :

	(venv) vagrant@ubuntu-focal:~$ jupyter notebook

	[I 13:15:41.693 NotebookApp] Serving notebooks from local directory: /home/vagrant
	[I 13:15:41.693 NotebookApp] The Jupyter Notebook is running at:
	[I 13:15:41.693 NotebookApp] http://localhost:8888/?token=f949d83075275b57602064d7dc91c31b449009bd09a26f9e
	[I 13:15:41.693 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
	[W 13:15:41.697 NotebookApp] No web browser found: could not locate runnable browser.
	[C 13:15:41.697 NotebookApp]

		To access the notebook, open this file in a browser:
			file:///run/user/1000/jupyter/nbserver-8273-open.html
		Or copy and paste one of these URLs:
			http://localhost:8888/?token=f949d83075275b57602064d7dc91c31b449009bd09a26f9e
	^C[I 13:15:42.734 NotebookApp] interrupted
	Serving notebooks from local directory: /home/vagrant
	0 active kernels
	The Jupyter Notebook is running at:
	http://localhost:8888/?token=f949d83075275b57602064d7dc91c31b449009bd09a26f9e
	Shutdown this notebook server (y/[n])? ^C[C 13:15:42.890 NotebookApp] received signal 2, stopping
	[I 13:15:42.892 NotebookApp] Shutting down 0 kernels
	(venv) vagrant@ubuntu-focal:~$

Avec un browser, vous verrez ouvrir une fenêtre.
