import pandas as pd
from datetime import datetime, timedelta


def count_ids_per_second(df, date,
                         id_col='id', start_col='date_debut', end_col='date_fin'):
    """
    Compte le nombre d'identifiants actifs pour chaque seconde d'une journée donnée.

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame avec les colonnes d'identifiant, date de début et date de fin
    date : str ou datetime
        Date à analyser (format: 'YYYY-MM-DD' ou datetime)
    id_col : str
        Nom de la colonne contenant les identifiants
    start_col : str
        Nom de la colonne contenant les dates de début
    end_col : str
        Nom de la colonne contenant les dates de fin

    Returns:
    --------
    pandas.DataFrame
        DataFrame avec colonnes 'timestamp' et 'count' pour toute la journée
    """

    # Conversion de la date en datetime si nécessaire
    if isinstance(date, str):
        date = pd.to_datetime(date)

    # Définir le début et la fin de la journée
    start_time = date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = date.replace(hour=23, minute=59, second=59, microsecond=0)

    # Conversion des colonnes en datetime si nécessaire
    df = df.copy()
    df[start_col] = pd.to_datetime(df[start_col])
    df[end_col] = pd.to_datetime(df[end_col])

    # Génération de tous les timestamps par seconde dans l'intervalle
    timestamps = pd.date_range(start=start_time, end=end_time, freq='1S')

    # Liste pour stocker les résultats
    results = []

    # Pour chaque seconde, compter les IDs actifs
    for ts in timestamps:
        # Un ID est actif si ts est entre date_debut (incluse) et date_fin (incluse)
        active_ids = df[
            (df[start_col] <= ts) & (df[end_col] >= ts)
            ]

        count = len(active_ids)

        # Ajouter tous les timestamps, même avec count = 0
        results.append({
            'timestamp': ts,
            'count': count
        })

    # Création du DataFrame résultat
    result_df = pd.DataFrame(results)

    return result_df


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un DataFrame d'exemple
    exemple_data = {
        'id': ['A', 'B', 'C', 'D'],
        'date_debut': [
            '2025-06-04 12:34:48',
            '2025-06-04 12:34:49',
            '2025-06-04 12:34:51',
            '2025-06-04 12:34:50'
        ],
        'date_fin': [
            '2025-06-04 12:34:52',
            '2025-06-04 12:34:51',
            '2025-06-04 12:34:53',
            '2025-06-04 12:34:52'
        ]
    }

    df_exemple = pd.DataFrame(exemple_data)

    # Test de la fonction pour une journée complète
    result = count_ids_per_second(
        df_exemple,
        date='2025-06-04'
    )

    print("DataFrame d'exemple:")
    print(df_exemple)
    print(f"\nRésultat (affichage des 20 premières lignes sur {len(result)} total):")
    print(result.head(20))