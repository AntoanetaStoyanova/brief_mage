if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter



@data_exporter
def export_data(data, *args, **kwargs):

    from sklearn.feature_extraction import DictVectorizer
    from sklearn.linear_model import LinearRegression

    # Préparation des données
    y = data['duration']
    categorical = ['PULocationID', 'DOLocationID']
    X = data[categorical]
    X_train = X.to_dict(orient='records')

    # Vectorisation
    dv = DictVectorizer()
    X_train = dv.fit_transform(X_train)

    # Entraînement du modèle
    lr = LinearRegression()
    lr.fit(X_train, y)

    # Affichage de l'intercept
    print(f"Intercept du modèle : {lr.intercept_}")