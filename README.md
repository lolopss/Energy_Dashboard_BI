# Mini-projet BI : PostgreSQL & Power BI

## Description

Ce projet est une démonstration simple d'un workflow BI : extraction, modélisation et visualisation de données. L'objectif était de créer un mini-jeu de données réaliste dans PostgreSQL, puis de construire un rapport interactif dans Power BI afin de me familiariser avec ces **outils techniques**.

## Contenu du projet

- **Base de données PostgreSQL** J'ai **créé** une base de **données** PostgreSQL afin de me familiariser avec celle-ci, puis **j'ai importé** le fichier `.csv` **créé** dans le dossier `data` pour **y créer** la table.  
  Données fictives, mais cohérentes, pour tester des analyses classiques (**consommation**, **n° de Bâtiment**, **énergie**...).

- **Rapport Power BI** Un fichier Power BI (.pbix) qui se connecte à la base PostgreSQL et présente :  
  - Des visualisations clés (barres, cartes, segments)  
  - Du code DAX pour permettre de classer les jours (lundi, mardi...) dans le **3ème** graphique.

## Objectifs

- Maîtriser la création d’un modèle relationnel simple  
- Savoir extraire des données dans PostgreSQL
- **Découvrir Power Query** - Réaliser un rapport Power BI clair et interactif  
- Présenter un projet BI complet et opérationnel

## Vidéo de présentation

https://github.com/user-attachments/assets/d3f280f8-3eda-4447-ac2d-84245b7298a0

## Versions :
postgresql :       17.5-3  
**pandas** :           2.3.1  
psycopg2-binary : 2.9.10
