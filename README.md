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

La Data augmentation consiste en une série de techniques visant à améliorer la taille et la qualité des ensembles de données d'entraînement, de manière à pouvoir construire des modèles d'apprentissage profond plus précis. 

```python
for transformation in transformation_array:
        if transformation == "horizontalFlip":
              #datagen = ImageDataGenerator(horizontal_flip = True)                 # for random flip
              datagen = ImageDataGenerator(preprocessing_function=horizontal_flip)  # all imgs flipped
        elif transformation == "verticalFlip":
              #datagen = ImageDataGenerator(vertical_flip = True)                   # for random flip
              datagen = ImageDataGenerator(preprocessing_function=vertical_flip)    # all imgs flipped
        elif transformation == "rotation":
              datagen = ImageDataGenerator(rotation_range = 40, fill_mode='nearest') 
        elif transformation == "widthShift":
              datagen = ImageDataGenerator(width_shift_range = 0.2, fill_mode='nearest')
        elif transformation == "heightShift":
              datagen = ImageDataGenerator(height_shift_range = 0.2, fill_mode='nearest')         
        elif transformation == "shearRange":
              datagen = ImageDataGenerator(shear_range = 0.2)   
        elif transformation == "zoom":
              datagen = ImageDataGenerator(zoom_range = [0.5, 1.0])
        elif transformation == "blur":
              datagen = ImageDataGenerator(preprocessing_function=blur)        
        elif transformation == "brightness":
              #Values less than 1.0 darken the image, e.g. [0.5, 1.0], 
              #whereas values larger than 1.0 brighten the image, e.g. [1.0, 1.5], 
              #where 1.0 has no effect on brightness.
              datagen = ImageDataGenerator(brightness_range = [1.1, 1.5])
        elif transformation == "contrast": 
              datagen = ImageDataGenerator(preprocessing_function=contrast)
        elif transformation == "saturation": 
              datagen = ImageDataGenerator(preprocessing_function=saturation)      
        elif transformation == "hue": 
              datagen = ImageDataGenerator(preprocessing_function=hue)    
        elif transformation == "gamma": 
              datagen = ImageDataGenerator(preprocessing_function=gamma)      
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
    
