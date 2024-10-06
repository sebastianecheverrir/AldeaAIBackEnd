from sklearn.neighbors      import NearestNeighbors
from sklearn.impute         import KNNImputer
from numpy                  import sort, mean, linspace, vstack
from scipy.stats            import zscore

import pandas            as pd
import numpy             as np

def EstimateValueByLaw(DicInputs, DicLocation):

    #reading data from the database
    # Redaing the input datafor the Apartamentos
    df_apartamentos = pd.read_csv('Data/2022-11-12_Clean_Data_apartamentos.csv')
    
    #Separating X and y data
    
    X_data = df_apartamentos[['Latitud','Longitud']].values
    y_data = df_apartamentos['Precio'].values
    
    #Reading data from the current appartment
    Latitud                 =  DicLocation['Latitud']
    Longitud                =  DicLocation['Longitud']
    M2Construidos           =  DicInputs['M2Construidos'] 
    
    X_data_single = np.array([Latitud, Longitud])
    
    #Finding the 20 appartments that are located closer 
    # to the one that we are treating
    
    nbrs = NearestNeighbors(n_neighbors=20, algorithm='ball_tree').fit(X_data)
    distances, indices = nbrs.kneighbors(X_data_single.reshape(-1, 2))
    
    df_apartamentos_neigh = df_apartamentos.iloc[indices[0]]
    df_apartamentos_neigh['PrecioM2'] = df_apartamentos_neigh['Precio']/df_apartamentos_neigh['Area']

    #We now sort by area. The ones that are similar to the reference come first
    #we take 15 out of the 20
    X_data_single = np.array(M2Construidos)
    X_data = df_apartamentos_neigh['Area'].values
    
    nbrs = NearestNeighbors(n_neighbors=12, algorithm='ball_tree').fit(X_data.reshape(-1, 1))
    distances, indices = nbrs.kneighbors(X_data_single.reshape(1, -1))
    
    df_apartamentos_neigh = df_apartamentos_neigh.iloc[indices[0]]
    




    #sorting by z score of the price per m2
    df_apartamentos_neigh['Z_Score_Preciom2'] = np.abs(zscore(df_apartamentos_neigh['PrecioM2']))
    df_apartamentos_neigh.sort_values(by='Z_Score_Preciom2', axis=0, ignore_index=True, inplace=True)


    avg_Precio = mean(df_apartamentos_neigh['PrecioM2'])

    return df_apartamentos, df_apartamentos_neigh, avg_Precio



