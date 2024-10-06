import pandas as pd
from joblib                  import load


def EstimateValue(DicInputs, DicLocation):

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
    
    #Estimating value 
    RF_median = load('Models/GBR_regr_Median2020-12-20.joblib')
    # RF_lower = load('../../../4_Training/4_2_IncludingDate/Appartments/GBR_regr_Lower2020-12-20.joblib')
    # RF_upper = load('../../../4_Training/4_2_IncludingDate/Appartments/GBR_regr_Upper2020-12-20.joblib')
    scaler = load('Models/scaler_2020-12-19.joblib')

    #note tht we take the data from last month. The reason is 
    # that most likely we don't have data for this month
    FechaHoy = pd.to_datetime('today') - pd.offsets.MonthBegin(1) - pd.DateOffset(months = 1)
    # FechaHoy = pd.to_datetime('2020-12-19')
    AnoDeExtraccion        = FechaHoy.year
    MesDeExtraccion        = FechaHoy.month


    X_data_single = [[Alcobas, Banos, Niveles, Administracion, 
                    AreaTerraza, AnoConstruccion, CantidadParqueaderos,
                    Estrato, Latitud, Longitud, M2Construidos, Piso, 
                    Predial, AnoDeExtraccion, MesDeExtraccion]]
    X_scaled_single = scaler.transform(X_data_single)
    Precio = RF_median.predict(X_scaled_single)

    #we need to correct the price, because my predictions are for end 2020
    #This method is based in the index (IPVU) that can be found here:
    #   https://www.banrep.gov.co/es/estadisticas/indice-precios-vivienda-usada-ipvu

    #vector containin the index. The index changes every three months.
    #2020-II    131.75
    #2022-II	135.38
    Precio = Precio*135.38/131.75


    # ErrorRange = abs(RF_upper.predict(X_scaled_single) - RF_lower.predict(X_scaled_single))

    # Precio_UpperLimit = Precio + ErrorRange/2
    # Precio_LowerLimit = Precio - ErrorRange/2

    # print('Valor Estimado ' + str(round(Precio[0], -6)))
    # print('Valor Estimado Min ' + str(round(Precio_LowerLimit[0], -6)))
    # print('Valor Estimado Max ' + str(round(Precio_UpperLimit[0], -6)))

    #Valor por M2
    PrecioM2 = Precio/M2Construidos
    # print('Valor Estimado por Metro Cuadrado  ' + str(round(PrecioM2[0], -3)))

    #Calculating rental prices
    if ((Estrato == 1) | (Estrato == 2)):
        PrecioArriendo = Precio[0]*0.40/100
    if ((Estrato == 3) | (Estrato == 4)):
        PrecioArriendo = Precio[0]*0.51/100
    if ((Estrato == 5) | (Estrato == 6)):
        PrecioArriendo = Precio[0]*0.65/100
        
    DicPrecio = {   'Precio'   : Precio, 
                    'PrecioM2' : PrecioM2, 
                    'PrecioArriendo'    : PrecioArriendo}

    return DicPrecio, scaler, X_scaled_single, RF_median
    #valor arriendo estimado

