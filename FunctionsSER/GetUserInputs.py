def GetUserInputs(req_body):
    #Getting all the inputs

    Nombre                  =    str(    req_body.getlist('entry[fields][30]')[0])
    Apellidos               =    str(    req_body.getlist('entry[fields][29]')[0])
    Email                   =    str(    req_body.getlist('entry[fields][2]' )[0])                  #
    TipoDeInmueble          =    str(    req_body.getlist('entry[fields][27]')[0])

    Pais                    =    str(    req_body.getlist('entry[fields][8]' )[0])
    Ciudad                  =    str(    req_body.getlist('entry[fields][9]' )[0]) 
    TipoDeVia               =    str(    req_body.getlist('entry[fields][3]' )[0]) 
    Numero1                 =    str(    req_body.getlist('entry[fields][5]' )[0])
    Numero2                 =    str(    req_body.getlist('entry[fields][6]' )[0])
    Numero3                 =    str(    req_body.getlist('entry[fields][7]' )[0])
    Alcobas                 =    int(    req_body.getlist('entry[fields][15]')[0])                  #
    Banos                   =    int(    req_body.getlist('entry[fields][26]')[0])                  #
    Niveles                 =    int(    req_body.getlist('entry[fields][25]')[0])
    Piso                    =    int(    req_body.getlist('entry[fields][18]')[0])
    CantidadParqueaderos    =    int(    req_body.getlist('entry[fields][21]')[0])                  #
    Estrato                 =    int(    req_body.getlist('entry[fields][20]')[0])                   #
    M2Construidos           =    float(  req_body.getlist('entry[fields][19]')[0])                #
    AreaTerraza             =    float(  req_body.getlist('entry[fields][23]')[0])
    AnoConstruccion         =    int(    req_body.getlist('entry[fields][22]')[0])               #
    Administracion          =    float(  req_body.getlist('entry[fields][24]')[0])            #Mensual
    Predial                 =    float(  req_body.getlist('entry[fields][17]')[0])            #Anual






#    Email                   =    str(    req_body.get('Email'))                  #
#
#
#    Alcobas                 =    int(    req_body.get('Alcobas'))                  #
#    Banos                   =    int(    req_body.get('Banos'))                  #
#    Niveles                 =    int(    req_body.get('Niveles'))
#    Administracion          =    float(  req_body.get('Administracion'))            #Mensual
#    AreaTerraza             =    float(  req_body.get('AreaTerraza'))
#    AnoConstruccion         =    int(    req_body.get('AnoConstruccion'))               #
#    CantidadParqueaderos    =    int(    req_body.get('CantidadParqueaderos'))                  #
#    Estrato                 =    int(    req_body.get('Estrato'))                   #
#    M2Construidos           =    float(  req_body.get('M2Construidos'))                #
#    Piso                    =    int(    req_body.get('Piso'))  
#    Predial                 =    float(  req_body.get('Predial'))            #Anual
#
#    TipoDeVia               =    str(    req_body.get('TipoDeVia')) # 'Calle', 'Avenida', 'Diagonal', 'Transversal'
#    Numero1                 =    str(    req_body.get('Numero1'))
#    Numero2                 =    str(    req_body.get('Numero2'))
#    Numero3                 =    str(    req_body.get('Numero3'))
#    Ciudad                  =    str(    req_body.get('Ciudad')) #'Caldas', 'Estrella', 'Itagui',  'Medellin', 'Bello', 'Copacabana', 'Barbosa', 'Rionegro', 'El Retiro', 'Bucaramanga', 'Floridablanca'
#    Pais                    =    str(    req_body.get('Pais'))
#
    #Not from the user
    ReportNumber = 1

    #putting everything in a dictionary
    DicInputs = {'Nombre'                : Nombre,
                 'Apellidos'             : Apellidos,
                 'Email'                 : Email,
                 'Alcobas'               : Alcobas,
                 'Banos'                 : Banos,
                 'Niveles'               : Niveles,
                 'Administracion'        : Administracion,
                 'AreaTerraza'           : AreaTerraza,
                 'AnoConstruccion'       : AnoConstruccion,
                 'CantidadParqueaderos'  : CantidadParqueaderos,
                 'Estrato'               : Estrato,
                 'M2Construidos'         : M2Construidos,
                 'Piso'                  : Piso,
                 'Predial'               : Predial,
                 'TipoDeVia'             : TipoDeVia,
                 'Numero1'               : Numero1,
                 'Numero2'               : Numero2,
                 'Numero3'               : Numero3,
                 'Ciudad'                : Ciudad,
                 'Pais'                  : Pais,
                 'ReportNumber'          : ReportNumber }



    return DicInputs

