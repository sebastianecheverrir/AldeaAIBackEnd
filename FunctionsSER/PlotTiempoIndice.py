import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib              import rcParams, colors

from FunctionsSER.DefineRcParams         import DefineRcParams
from FunctionsSER.DefineColors           import DefineColors


def PlotTiempoIndice(Precio):

    DicColors = DefineColors ()
    BlueLight       = DicColors['BlueLight']
    GrayLight       = DicColors['GrayLight']

    DicRcParams = DefineRcParams()
    rcParams.update(DicRcParams)

    #unfotunately we need an alternative way to do the calculation. 
    #  If we dont have fresh data, the previous method does not work.
    #This method is based in the index (IPVU) that can be found here:
    #   https://www.banrep.gov.co/es/estadisticas/indice-precios-vivienda-usada-ipvu

    #vector containin the index. The index changes every three months.
    #2021-IV	136.98
    #2022-I	137.13
    #2022-II	135.62
    #2022-III	133.96
    #2022-IV	129.51



    #   Recent first 
#    IPVU_List = np.array([139.45, 138.70, 142.49, 140.60, 142.63])
#    IPVU_List = np.array([140.24, 141.53, 140.26, 138.94, 135.55])
#    IPVU_List = np.array([135.38,139.65,139.90,139.38,138.79])
    IPVU_List = np.array([129.51,133.96,135.62,137.13,136.98])

    baseline = IPVU_List[0]

    IPVU_Delta_List = IPVU_List - baseline

    #calculating the price with the index
    PrecioVector = (Precio*IPVU_Delta_List/100 + Precio)/1e6


    #Vector with dates
    FechaHoy = pd.to_datetime('today') - pd.offsets.MonthBegin(1) - pd.DateOffset(months = 1)
    VectorFechas = [FechaHoy] 

    for i in range(1,5):
        VectorFechas.append(FechaHoy - pd.DateOffset(months = i*3))


        
    fig, ax = plt.subplots(1,1, figsize=(7.3, 2.5))
    plt.rcParams.update({'font.size': 10})
    # date_form = DateFormatter("%m-%Y")
    # ax.xaxis.set_major_formatter(date_form)
    # ax.tick_params(axis='x', rotation=70)
    ax.plot(VectorFechas, PrecioVector,'o-', color=BlueLight)
    # ax.set_title('Precio [MCOP]')

    # from matplotlib.ticker import StrMethodFormatter
    # from matplotlib.ticker import FormatStrFormatter
    # matplotlib.rc('text', usetex = False)


    ax.set_xticks(VectorFechas)
    ax.set_xticklabels(['Hoy',
                        'Hace\n$\mathbf{3}$ meses',
                        'Hace\n$\mathbf{6}$ meses',
                        'Hace\n$\mathbf{9}$ meses',
                        'Hace\n$\mathbf{12}$ meses'])

    # ax.xaxis.set_major_formatter(StrMethodFormatter('{x}'))
    # ax.xaxis.set_major_formatter(FormatStrFormatter(''))


    gridWidth = 0.3
    ax.spines['left'].set_linewidth(gridWidth)
    ax.spines['right'].set_linewidth(gridWidth)

    ax.grid(b=True, axis='both', color=GrayLight, linewidth = gridWidth)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_color(GrayLight)
    ax.spines['left'].set_color(GrayLight)
    ax.tick_params(axis='both', which='both',length=0)
    ax.tick_params(axis='both', which='major', pad=6)


    ax.set_axisbelow(True)
    fig.tight_layout()

    fig.savefig('InfoTiempoIndice.png', 
            transparent = True,
            dpi=250)
    fig.clf()

    return IPVU_Delta_List
