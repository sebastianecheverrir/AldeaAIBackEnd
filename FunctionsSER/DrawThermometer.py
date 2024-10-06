from sklearn.neighbors      import NearestNeighbors
from numpy                  import sort, mean, linspace, vstack
from matplotlib             import rcParams, colors

import matplotlib.pyplot as plt 

from FunctionsSER.DefineRcParams         import DefineRcParams
from FunctionsSER.DefineColors           import DefineColors


def DrawThermometer(X_data,X_scaled_single, df_apartamentos_unscaled, PrecioM2):


    DicColors = DefineColors ()
    BlueLightLight  = DicColors['BlueLightLight']
    BlueDark        = DicColors['BlueDark']
    BlueLight       = DicColors['BlueLight']
    BlueDarkDark    = DicColors['BlueDarkDark']


    DicRcParams = DefineRcParams()
    rcParams.update(DicRcParams)

    #Plotting a color line with the price per m2 of 
    # the 20 closest appartments


    #Finding the 20 appartments that are located closer 
    # to the one that we are treating

    nbrs = NearestNeighbors(n_neighbors=30, algorithm='ball_tree').fit(X_data[:, [8,9]])
    distances, indices = nbrs.kneighbors(X_scaled_single[0][8:10].reshape(-1, 2))

    df_apartamentos_unscaled_neigh = df_apartamentos_unscaled.iloc[indices[0]]

    min_Precio = sort(df_apartamentos_unscaled_neigh['PrecioM2'])[0]
    max_Precio = sort(df_apartamentos_unscaled_neigh['PrecioM2'])[-1]
    avg_Precio = mean(df_apartamentos_unscaled_neigh['PrecioM2'])


    #we need to correct the price, because my predictions are for end 2020
    #This method is based in the index (IPVU) that can be found here:
    #   https://www.banrep.gov.co/es/estadisticas/indice-precios-vivienda-usada-ipvu

    #vector containin the index. The index changes every three months.
    #2020-II    131.75
    #2022-II    135.38
    min_Precio = min_Precio*135.38/131.75
    max_Precio = max_Precio*135.38/131.75
    avg_Precio = avg_Precio*135.38/131.75


    cmap = colors.LinearSegmentedColormap.from_list("", 
                                    [BlueLightLight,BlueDark, BlueLight]) 

    #plotting
    x = linspace(min_Precio, max_Precio, 1000)
    y = linspace(0, 1, 2)
    z = linspace(min_Precio, max_Precio, 1000)
    z = vstack((z,z))

    fig, ax = plt.subplots(1,1, figsize=(3.3, 1.35))

    fig.subplots_adjust(top=0.7, bottom=0.4, left=0.0, right=1.0)
    ax.axis('off')
    ax.pcolormesh(x,y,z,  cmap=plt.get_cmap(cmap), shading='gouraud')
    # ax.set_title('Valor por Metro Cuadrado')

    ax.vlines(PrecioM2,-0.1,1.1 ,color=BlueDarkDark)
    ax.text(PrecioM2,1.5, '$' + str((round(PrecioM2[0]/10e5,1))), 
            horizontalalignment = 'center',
        verticalalignment = 'top',
        weight = 'bold',
        color=BlueDarkDark)

    # ax.vlines(min_Precio,-0.1,1)
    ax.text(min_Precio,-0.3, '$' + str((round(min_Precio/10e5,1))) + '\nMínimo',
            horizontalalignment = 'center',
        verticalalignment = 'top',
        color=BlueLightLight)

    # ax.vlines(max_Precio,-0.1,1)
    ax.text(max_Precio,-0.3, '$' + str((round(max_Precio/10e5,1))) + '\nMáximo', 
            horizontalalignment = 'center',
        verticalalignment = 'top',
        color=BlueLight)

    # ax.vlines(avg_Precio,-0.1,1)
    ax.text(avg_Precio,-0.3, '$' + str((round(avg_Precio/10e5,1))) + '\nPromedio', 
            horizontalalignment = 'center',
        verticalalignment = 'top',
        color=BlueDark)



    fig.savefig('PricePerM2.png', 
            transparent = True,
            bbox_inches = "tight",
            dpi=1000)

    fig.clf()

    # print(min_Precio, max_Precio, avg_Precio)

    return df_apartamentos_unscaled_neigh, avg_Precio
