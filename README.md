# Big Data sous Python

Ce repository contient la matière pour le cours Big Data sous Python à
l'IAE.  Le cours comporte six séances en cours magistral ainsi que
trois en TD, deux heures chacune.  L'objectif du cours est de
présenter les techniques de machines à support vectoriel et des
réseaux de neurones avec applications en python.

Vous aurez des travaux à faire chez vous entre les cours qui ne seront
pas notées.  Il y aura ensuite des contrôles continus en début de
séance (5-10 minutes) qui seront généralement facile si vous avez fait
le travail demandé et impossible sinon.  Le dernier CM sera dédié à
une évaluation écrite.

Nous allons prendre comme hypothèse au moins les suppositions suivante
:

* Vous savez programmer.  Vous connaissez déjà au moins les bases de python
  (par exemple, de l'année dernière).
* Vous êtes suffisamment compétent en anglais pour lire des textes
  simples (surtout, tutoriels) en anglais.

# Github

Vous devez créer un repository github pour le cours afin de pouvoir
collaborer entre vous.  En outre, toute question que vous posez hors
cours doit impérativement passer par un github issue (sur votre repo,
vous me taguez).

Pour toute question en remote, les règles de bons sens suivants s'appliquent :

* C'est une question.  "Je ne comprends pas", par exemple, est un bon contre-exemple d'une question.
* Vous expliquez ce que vous avez compris, ce que vous avez essayé.
* Vous expliquez avec qui dans le cours vous avez consulté / collaboré afin d'essayer de comprendre.  Vous les taguez également.
* Sachez que le debugging est difficile pour tout le monde.  Si un point de debugging me paraît facile, je vous montrerez ce que je vois.  Mais souvent il faut passer du temps, qu'on soit débutant ou confirmé, afin de trouver un bug.

Les question en cours, bien évidemment, ne sont pas assujetties à cette déontologie sévère.  Vous êtes en cours pour l'interaction et vous devez poser vos questions réfléchies au fur et à mesure !


# Python

Il est bien évidemment impératif que vous puissiez écrire et essayer
des programs en python.  Avant la première séance, il convient donc de
télécharger et installer python sur votre ordinateur.  La bonne
nouvelle, c'est que c'est gratuit et (selon votre système
d'exploitation) relativement simple.

Les logiciels nécessaires seront également installés sur les machines
en salle 339.


## Linux

C'est un de rare cas dans la vie où tout est plus facile sur linux.
Afin, pour une certain définition de "facile".  Il suffit d'installer
python3 (attention : souvent python = python2) et virtualenv.
Virtualenv vous crée un environnement pour python largement
indépendant de ce qui est présent sur votre ordinateur.

Sur ubuntu, on peut taper

    $ sudo apt-get update
	$ sudo apt-get install python3-virtualenv virtualenv python python3
	$ sudo apt-get install gcc g++ python3-dev

Puis, dans votre répertoire de travail :

    $ virtualenv --python=python3 venv
	$ . venv/bin/activate                   # N'oubliez pas le "." au début.
	$ pip install -r requirements.txt

Le fichier `requirements.txt` se trouve [ici](requirements.txt).  Le
plus facile est de cloner ce repository.  Voir plus bas, "jour 1", sur
`git clone`.

Cela marche également sur MacOS si vous êtes à l'aise dans le terminal.

## MacOS, Windows

Apparemment l'usage de python sur Windows marche très bien sauf quand
ce n'est pas le cas.  Les systèmes MacOS et linux sont beaucoup plus
répandus dans le domaine de stat/ML/data science.  Ceci dit, un
produit commercial avec une très bonne offre gratuite existe :
[anaconda](https://www.anaconda.com/).  Il est téléchargeable
[ici](https://www.anaconda.com/download/).

## Tester

Vous avez sans doute le bon instinct de demander si vous avez bien
suivi cette démarche.  Vous pouvez lancer `ipython` (commandline:
ipython; sinon, il y a un icône quelque part).  Et puis vous devez
pouvoir faire le suivant :

	(venv) vagrant@ubuntu-bionic:~$ ipython
	Python 3.6.7 (default, Oct 22 2018, 11:32:17)
	Type 'copyright', 'credits' or 'license' for more information
	IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

	In [1]: import numpy as np

	In [2]: import scipy as sp

	In [3]: import sklearn

	In [4]: print("Hello, world!")
	Hello, world!

	In [5]: quit
	(venv) vagrant@ubuntu-bionic:~$

Il existe également une version du même logiciel qui vous présente un
éditeur dans votre browser : le Jupyter notebook.  Si vous l'essayez
sans browser, vous auriez ça :

	(venv) vagrant@ubuntu-bionic:~$ jupyter notebook

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
	(venv) vagrant@ubuntu-bionic:~$

Avec un browser, vous verrez ouvrir une fenêtre.
