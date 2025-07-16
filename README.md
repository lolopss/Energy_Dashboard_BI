# Mini projet BI - PostgreSQL & Power BI

## Description

Ce projet est une démonstration simple d’un workflow BI : extraction, modélisation et visualisation de données.  
L’objectif était de créer un mini jeu de données réaliste dans PostgreSQL, puis de construire un rapport interactif dans Power BI afin de me familiariser avec ces stacks techniques.

## Contenu du projet

- **Base de données PostgreSQL**  
  Un script SQL crée une base avec plusieurs tables liées (ex : ventes, clients, produits) simulant un cas d’usage commercial.  
  Données fictives, mais cohérentes, pour tester des analyses classiques (chiffre d’affaires, segmentation, évolution).

- **Rapport Power BI**  
  Un fichier Power BI (.pbix) qui se connecte à la base PostgreSQL et présente :  
  - Des visualisations clés (barres, cartes, segments)  
  - Des indicateurs synthétiques (CA, volume, parts de marché)  
  - Des filtres dynamiques pour explorer les données

## Objectifs

- Maîtriser la création d’un modèle relationnel simple  
- Savoir extraire des données via SQL dans PostgreSQL  
- Réaliser un rapport Power BI clair et interactif  
- Présenter un projet BI complet et opérationnel

## Vidéo de présentation

https://github.com/user-attachments/assets/d3f280f8-3eda-4447-ac2d-84245b7298a0

## versions :
postgresql :      17.5-3\
panda :           2.3.1\
psycopg2-binary : 2.9.10
