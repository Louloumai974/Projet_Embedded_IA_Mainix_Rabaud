# Projet_Embedded_IA_Mainix_Rabaud
    
## Table des matières
* [Introduction](#Introduction)
* [Modèle et entrainement](#Modèle-et-entrainement)
* [Attaques](#Attaques)
* [Contraintes Embarquées](#Contraintes-Embarquées)
* [Implantation](#Implantation)
* [Résultats](#Résultats)
* [Conclusion](#Conclusion)

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

On propose trois modèles différents un small, un medium et un long. On présente ici le modèle small, qui sera celui implanté sur la carte (pour les raisons expliqué plus bas).
```
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 80, 45, 32)        896

 activation (Activation)     (None, 80, 45, 32)        0

 max_pooling2d (MaxPooling2D  (None, 40, 22, 32)       0
 )

 conv2d_1 (Conv2D)           (None, 40, 22, 32)        9248

 activation_1 (Activation)   (None, 40, 22, 32)        0

 max_pooling2d_1 (MaxPooling  (None, 20, 11, 32)       0
 2D)

 conv2d_2 (Conv2D)           (None, 20, 11, 64)        18496

 activation_2 (Activation)   (None, 20, 11, 64)        0

 max_pooling2d_2 (MaxPooling  (None, 10, 5, 64)        0
 2D)

 conv2d_3 (Conv2D)           (None, 10, 5, 64)         36928

 activation_3 (Activation)   (None, 10, 5, 64)         0

 max_pooling2d_3 (MaxPooling  (None, 5, 2, 64)         0
 2D)

 conv2d_4 (Conv2D)           (None, 5, 2, 32)          18464

 activation_4 (Activation)   (None, 5, 2, 32)          0

 max_pooling2d_4 (MaxPooling  (None, 2, 1, 32)         0
 2D)

 flatten (Flatten)           (None, 64)                0

 dense (Dense)               (None, 64)                4160

 activation_5 (Activation)   (None, 64)                0

 dropout (Dropout)           (None, 64)                0

 dense_1 (Dense)             (None, 2)                 130

 activation_6 (Activation)   (None, 2)                 0

=================================================================
```

* Entrainement

On converti nos images en arrays .npy pour pouvoir faciliter l'entrainement du modèles. Cette conversion s'effectue avec le script ConvertNPY.py

![Alt text](/images/small_accuracy_loss.png?raw=true "")

On obtient une accuracy de 0.97, ce qui est une bonne chose. Cependant, on remarque que notre modèle à une tendance à overfiter, en essayant plusieurs changements de parmètres nous n'avons pas résussi à diminuer ce chiffre, nous aurons donc un modèle assez faible. 
	
## Attaques

Les systèmes embarqués intégrant de l'intelligence artificielle sont des sysètmes très vulnérables : il est difficile de garantir leur sécurité face aux attaques. Avant de déployer un tel système et d'y rendre dépendant une exploitation agricole, il semble alors essentiel de connaître les différents types d'attaques possibles, et les risques encourus dans ce cas. Pour cela nous allons implémenter des scripts d'attaque, en nous basant sur les attaques les plus fréquentes et les mieux connus, et y soumettre notre système. 
Le but est donc de tester la sécurité de notre système face aux attaques, mais aussi de connaître la réaction de notre système dans ces situations. En effet, l'un des concepts de base de la sécurité est de prendre en compte le pire scénario possible, en attaquant nous même notre système, nous allons pouvoir nous mettre dans la situation d'un attaquant ayant par exemple un accès total aux données, et ainsi mesurer les risques encourus en cas d'un scénario "catastrophe".

* Adversarial

Une attaque adversariale, qui peut se traduire par attaque par exemples contradictoires, est un type d'attaque qui permet à l'attaquant de mettre à mal l'intelligence artificielle par corruption des données en entrée. D'une part, l'attaque peut viser les données d'entraînement. Si les données d'entraînements sont modifiées de manière imperceptible par l'homme, l'utilisateur du système pensera alors que son système est correctement entraîné, alors que les images vus par le système lors de l'entraînement ne correspondront pas aux étiquettes associées. D'autre part, l'attaque peut viser les données pendant l'utilisation du système : par exemple une légère modification du caractère d'un panneau pourrait tromper l'IA d'une voiture autonome. 
	
## Contraintes Embarquées 

Nous utlisierons le modèle small car le modèle medium demande plus de RAM que la carte SMT32 peut en fournir. 

![Alt text](/images/small_embedded.png?raw=true "")

On remarque que l'accuracy à grandement diminué, ce qui s'explique par l'overtiffing remarqué plus haut.


## Implantation

On utilise CubeMx et le pack X_Cube_AI pour générer un nouveau projet à partir de notre modèle de carte. Cela nous permet ensuite d'avoir un projet déjà configuré et de travailler uniquement sur le fichier app_x_cube_ai.c qui est notre fichier d'application. 

On crée un fichier CommunicationSTM32.py qui va communiquer avec la carte via l'UART2. On va envoyer des images et recevoir en retour une prédiction. 
La fonction MX_X_CUBE_AI_Init est la fonction appelée dans le main(), c'est le coeur de l'application car elle contient la partie de synchronisation avec le script python et c'est aussi dans cette fonction que sont appelées les focntion acquire_and_process_data et post_process qui permettent d'acquérir, traiter et renvoyer les données. 

```C
	    // Synchronisation loop
	      while(sync == 0){
	    	  while(ack_received != 1){
	    		  HAL_UART_Receive(&huart2, (uint8_t *) ack, sizeof(ack), 100);
	    		  if ((ack[0] == 's') && (ack[1] == 'y') && (ack[2] == 'n') && (ack[3] == 'c')){
	    			  ack_received = 1;
	    		  }
	    		  HAL_UART_Transmit(&huart2, (uint8_t *) return_ack, sizeof(return_ack), 100);
	    		  sync = 1;
	    	  }
	      }
	      /* 1 - acquire and pre-process input data */
	      res = acquire_and_process_data(in_data);
	      /* 2 - process the data - call inference engine */
	      if (res == 0)
	        res = ai_run();
	      /* 3- post-process the predictions */
	      if (res == 0)
	        res = post_process(out_data);
	
```
 Pour réaliser l'inference on utilise le script CommunicationSTM32.py dans lequel se trouve une boucle pour envoyer les images pixel par pixel 
```python
    while(input_sent == False):
        for i in range(85):
            for j in range(45):
                ser.write(tmp[i,j])

```
 
 
## Résultats 
Quand le modèle termine son inférence, il nous renvoie son résultat et on la compare avec le label pour voir la performence de notre modèle

![Alt text](/images/resultats.PNG?raw=true "")

Comme prévu, les predictions sont parfois fausses. Cela était prévisible compte tenu de notre accuracy qui était assez basse.
Nous n'avons pas utilisé d'attaques sur notre modèle car il produit des erreurs sans attaques, l'attaquer n'est donc pas révélateur de l'efficacité de l'attaque. 

## Conclusion

Nous avons réussi à implanter notre modèle sur la carte et à établir une communication permettant d'envoyer une image et de récuperer une prédiction. Cependant, notre modèle n'est pas assez bien élaboré et limite nos résultats, un nouveau model est donc un axe important d'amélioration de notre projet. 
