import pandas as pd
import matplotlib.pyplot as plt

from matplotlib              import rcParams, colors

from FunctionsSER.DefineRcParams         import DefineRcParams
from FunctionsSER.DefineColors           import DefineColors



def PlotTiempo(DicInputs, DicLocation, scaler, RF_median):

    DicColors = DefineColors ()
    BlueLight       = DicColors['BlueLight']
    GrayLight       = DicColors['GrayLight']

    DicRcParams = DefineRcParams()
    rcParams.update(DicRcParams)

    Alcobas                 =   DicInputs['Alcobas']
    Banos                   =   DicInputs['Banos']
    Niveles                 =   DicInputs['Niveles']
    Administracion          =   DicInputs['Administracion']
    AreaTerraza             =   DicInputs['AreaTerraza']
    AnoConstruccion         =   DicInputs['AnoConstruccion']
    CantidadParqueaderos    =   DicInputs['CantidadParqueaderos']
    Estrato                 =   DicInputs['Estrato']
    M2Construidos           =   DicInputs['M2Construidos']
    Piso                    =   DicInputs['Piso']
    Predial                 =   DicInputs['Predial']
    
    Latitud                 =   DicLocation['Latitud']
    Longitud                =   DicLocation['Longitud']


    FechaHoy = pd.to_datetime('today') - pd.offsets.MonthBegin(1) - pd.DateOffset(months = 1)
    VectorFechas = [FechaHoy] 

    for i in range(1,7):
        VectorFechas.append(FechaHoy - pd.DateOffset(months = i))

    PrecioVector = []
    # ErrorRangeVector = []
        

    for Fecha in VectorFechas:
    # MesDeExtraccion        = date.today().month

        X_data_single = [[Alcobas, Banos, Niveles, Administracion, 
                        AreaTerraza, AnoConstruccion, CantidadParqueaderos,
                        Estrato, Latitud, Longitud, M2Construidos, Piso, 
                        Predial, Fecha.year, Fecha.month]]
        X_scaled_single = scaler.transform(X_data_single)
        PrecioTmp = RF_median.predict(X_scaled_single)
    #     ErrorRange = abs(RF_upper.predict(X_scaled_single) - RF_lower.predict(X_scaled_single))

        #Valor por M2
    #     PrecioM2 = Precio/M2Construidos

        PrecioVector.append(PrecioTmp[0]/1e6)
    #     ErrorRangeVector.append(ErrorRange[0]/2/1e6)
    #     MesVector.append(Fecha.month)
        
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
                        'Hace\n$\mathbf{1}$ mes',
                        'Hace\n$\mathbf{2}$ meses',
                        'Hace\n$\mathbf{3}$ meses',
                        'Hace\n$\mathbf{4}$ meses',
                        'Hace\n$\mathbf{5}$ meses',
                        'Hace\n$\mathbf{6}$ meses'])

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

    fig.savefig('InfoTiempo.png', 
            transparent = True,
            dpi=250)
    fig.clf()

    return None
