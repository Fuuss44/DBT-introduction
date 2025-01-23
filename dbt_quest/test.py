import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Paramètres de connexion
username = "root"  # Utilisateur MySQL
password = "25091999#!"  # Mot de passe MySQL
host = "localhost"  # Utiliser 127.0.0.1 ou localhost selon votre configuration
port = 3306
database = "my_dbt_db"

# On crée la connexion vers la base de données
DATABASE_URI = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(DATABASE_URI)

# On crée la base de données si elle n'existe pas
if not database_exists(engine.url):
    create_database(engine.url)

# Liste des tables à importer
liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

for table in liste_tables:
    try:
        # URL du fichier CSV correspondant
        csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"

        # Chargement du CSV dans un DataFrame
        df = pd.read_csv(csv_url)

        # Ajout des données dans la base de données MySQL
        df.to_sql(f"raw_{table}", engine, if_exists="replace", index=False)
        print(f"Table {table} importée avec succès.")

    except Exception as e:
        print(f"Erreur lors de l'importation de la table {table}: {e}")
