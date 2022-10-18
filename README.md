# Projet_Embedded_IA_Mainix_Rabaud


Annotations pour dev: 
    trois fichiers h5 -< small large et medium -> lequel choisir pour le mettre sur le stm32. 
    
## Table des matières
* [Introduction](#Introduction)
* [Modèle et entrainement](#Modèle-et-entrainement)
* [Attaques](#Attaques)
* [Contraintes Embarquées](#Contraintes-Embarquées)
* [Implantation](#Implantation)

## Introduction

L'Esca est l'une des maladies les plus courantes qui peuvent gravement endommager la vigne. Cette maladie, si elle n'est pas traitée à temps, est la cause du stress végétatif ou de la mort de la plante attaquée, avec pour conséquence des pertes de production ainsi qu'un risque croissant de propagation aux vignes voisines. Aujourd'hui, la détection de l'Esca est effectuée manuellement par des enquêtes visuelles généralement réalisées par des agronomes, ce qui demande énormément de temps.

Récemment, les méthodes de traitement d'images, de vision par ordinateur et d'apprentissage automatique ont été largement adoptées pour la classification des maladies des plantes. Implémenter un réseau de neurones sur un système embarqué permettrait de rendre plus rapide et pratique l'identification de la maladie.

## Modèle et entrainement
* Description des données

Le jeu de données proposé consiste en une archive de 1770 images. Les images acquises ont une résolution de 1920x1080 pixels et 1280x720 pixels, avec une orientation aléatoire en portrait et en paysage.

* Data Augmentation

La Data augmentation consiste en une série de techniques visant à améliorer la taille et la qualité des ensembles de données d'entraînement, de manière à pouvoir construire des modèles d'apprentissage profond plus précis. On compte 13 transformation différentes appliqué sur chaque image ce qui permet d'augmenter drastiquement le nombres de données d'entrainement. 
Script des transformations : 

```python
transformation_array = [
                        "horizontalFlip",
                        "verticalFlip", 
                        "rotation", 
                        "widthShift", 
                        "heightShift",  
                        "shearRange",
                        "zoom", 
                        "blur",
                        "brightness", 
                        "contrast",
                        "saturation",
                        "hue",
                        "gamma"
                        ];  
```

* Modèles

* Entrainement


	
## Attaques
Les systèmes embarqués intégrant de l'intelligence artificielle sont des sysètmes très vulnérables : il est difficile de garantir leur sécurité face aux attaques. Avant de déployer un tel système et d'y rendre dépendant une exploitation agricole, il semble alors essentiel de connaître les différents types d'attaques possibles, et les risques encourus dans ce cas. Pour cela nous allons implémenter des scripts d'attaque, en nous basant sur les attaques les plus fréquentes et les mieux connus, et y soumettre notre système. Le but est donc de tester la sécurité de notre système face aux attaques, mais aussi de connaître la réaction de notre système dans ces situations.
* Adversarial
* Autres attaques
	
## Contraintes Embarquées 


## Implantation
```
$ cd ../lorem
$ npm install
$ npm start
```    
    
