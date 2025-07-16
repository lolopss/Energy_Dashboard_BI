# Mini projet BI - PostgreSQL & Power BI

## Description

Ce projet est une démonstration simple d’un workflow BI : extraction, modélisation et visualisation de données.  
L’objectif était de créer un mini jeu de données réaliste dans PostgreSQL, puis de construire un rapport interactif dans Power BI afin de me familiariser avec ces stacks techniques.

## Contenu du projet

- **Base de données PostgreSQL**  
  J'ai cree une base de donnee postgresql afin de me familiariser avec, puis ai importer le fichier .csv creer dans le dossier data pour creer la table.
  Données fictives, mais cohérentes, pour tester des analyses classiques (Consomation, n. de Batiment, Energie..).

- **Rapport Power BI**  
  Un fichier Power BI (.pbix) qui se connecte à la base PostgreSQL et présente :  
  - Des visualisations clés (barres, cartes, segments)  
  - Du code DAX pour permettre de classer les jours (lundi, mardi ...) dans le 3 eme graphique

## Objectifs

- Maîtriser la création d’un modèle relationnel simple  
- Savoir extraire des données dans PostgreSQL
- Decouvrir Power Querry  
- Réaliser un rapport Power BI clair et interactif  
- Présenter un projet BI complet et opérationnel

## Vidéo de présentation

https://github.com/user-attachments/assets/d3f280f8-3eda-4447-ac2d-84245b7298a0

## versions :
postgresql :      17.5-3\
panda :           2.3.1\
psycopg2-binary : 2.9.10
