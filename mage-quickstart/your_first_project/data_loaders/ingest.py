if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@data_loader
def load_data(*args, **kwargs):
    """
    Bloc pour charger les données de taxi jaunes de mars 2023.
    
    Returns:
        DataFrame : Les données du fichier parquet
    """
    # Spécifiez le chemin du fichier Parquet
    file_path = 'your_first_project/yellow_tripdata_2023-03.parquet'
    
    # Charger le fichier Parquet
    df = pd.read_parquet(file_path)
    
    # Retourner les données sous forme de DataFrame
    return df

@test
def test_output(output, *args) -> None:
    """
    Test de la sortie du bloc pour vérifier le chargement des données.
    """
    assert output is not None, "Le chargement des données a échoué"
    assert isinstance(output, pd.DataFrame), "La sortie n'est pas un DataFrame"
    assert not output.empty, "Le DataFrame est vide"
