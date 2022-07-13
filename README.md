<img src="https://img.freepik.com/vecteurs-premium/conception-modele-logo-photographie-appareil-photo-numerique-points_20029-1197.jpg" alt="drawing" width="200"/>


# Scrutoscope 1.0

Dispositif de surveillance passif ou actif, avec des périphériques paramétrables et une interface de gérance.

Scrutoscope permet, grâce à une interface web, de surveiller son domicile et les activités qui le concernent. Il permet, grâce à un serveur et un système de caméra et capteur infrarouge, de détecter des présences et d'en faire des photos, et les répertorier dans l'interface.

Le projet est encore au stade embryonnaire, il existe beaucoup de pistes d'améliorations, et de fonctionnalités à implémenté.

A l'heure actuelle, plusieurs fonctionnalités dîtes primordiale manquent encore à l'appel:
- L'ajout d'un front avec une petite tablette tactile sur le serveur, permettant de gérer les paramètres sans être nécessairement sur l'interface web, avec une identifcation avec RFID / NFC sur cet tablette.
- Les notifications mails, SMS et push lors d'une détection de présence. 
- La possibilité d'identifier la détection sur le mail via l'api: Un ami, un faux positif, un insecte, un intrus etc...
- La possibilité grâce à une analyse réseau et une intégration en fonction des constructeurs, d'intégrer des appareils dynamiquement. ex: nouvelle caméra IP, nous lançons notre scan réseau, identifions l'appareil, le modèle, et ensuite nous faisont une intégration pour rendre le système interactif et dynamique.
- Une vision de la caméra en direct sur l'interface web.
- Création d'un script rendant le système entièrement déployable à l'éxécution de celui-ci, ou lors du premier démarrage de l'appareil.
- Et bien d'autre....

## Partie Python serveur

Ce repository concerne la partie serveur / Python du projet. ce script python écoute en permanence et cherche une détection sur le capture infrarouge. Lors d'une détection, nous prenons un nombre de captures définies (en DB) et nous envoyons les statistiques sur le nombre de captures effectués, et à l'avenir, le type de detection (intrus, ami, faux positif...)

## Techologies Utilisées

**Server:** Python 3

## Auteurs

- [@bilel](https://github.com/Bilel69500) /dev
- [@théo](https://github.com/theoPARENTIT) /lead-dev
- [@mattéo](https://github.com/matvki) /dev
- [@jean-loup](https://github.com/hardkos77) /dev
- [@mohamed](https://github.com/MohamedZazou) /dev
- [@thibault](https://github.com/ThibautGr) /chef de projet
