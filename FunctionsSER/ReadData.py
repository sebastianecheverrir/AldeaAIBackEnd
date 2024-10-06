import pandas as pd
from sklearn.impute          import KNNImputer
# from joblib                  import load

def ReadData(scaler):

    # scaler = load('Models/scaler_2020-12-19.joblib')

    #reading data
    # Redaing the input datafor the Apartamentos
    df_apartamentos = pd.read_csv('Data/2020-12-19_Clean_Data_apartamentos.csv')

    #Separating X and y data
    X_data = df_apartamentos.drop(columns=['Precio'])
    y_data = df_apartamentos['Precio']

    #Normalizing data
    # scaler = StandardScaler()
    # scaler.fit(X_data)
    X_data = scaler.transform(X_data)

    #Filling in missing values using the KNNImputer
    imputer = KNNImputer(n_neighbors    = 5)
    X_data = imputer.fit_transform(X_data)

    #going back to the dataframe
    df_apartamentos_scaled = pd.DataFrame(data = X_data,
                                        columns = df_apartamentos.drop(columns=['Precio']).columns)
    df_apartamentos_scaled['Precio'] = y_data

    #unscaling the data
    df_apartamentos_unscaled = pd.DataFrame(data = scaler.inverse_transform(X_data),
                                        columns = df_apartamentos.drop(columns=['Precio']).columns)
    df_apartamentos_unscaled['Precio'] = y_data
    df_apartamentos_unscaled['PrecioM2'] = df_apartamentos_unscaled['Precio']/df_apartamentos_unscaled['M2 Area Construida']

    return X_data, df_apartamentos_unscaled
