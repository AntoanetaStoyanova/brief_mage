
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd




@transformer
def transform(data, *args, **kwargs):
    """
    Bloc pour transformer les données de taxi jaunes (mars 2023).

    Args:
        data: Les données du fichier parquet chargées depuis le bloc précédent.

    Returns:
        DataFrame : Données transformées avec calcul de durée et conversion des colonnes.
    """
    # Transformation des données
    data.tpep_dropoff_datetime = pd.to_datetime(data.tpep_dropoff_datetime)
    data.tpep_pickup_datetime = pd.to_datetime(data.tpep_pickup_datetime)

    # Calculer la durée en minutes
    data['duration'] = data.tpep_dropoff_datetime - data.tpep_pickup_datetime
    data.duration = data.duration.dt.total_seconds() / 60

    # Filtrer les données (durée entre 1 et 60 minutes)
    data = data[(data.duration >= 1) & (data.duration <= 60)]

    # Conversion des colonnes catégorielles en type string
    categorical = ['PULocationID', 'DOLocationID']
    data[categorical] = data[categorical].astype(str)

    return data