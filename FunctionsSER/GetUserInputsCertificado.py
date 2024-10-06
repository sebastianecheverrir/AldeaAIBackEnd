def GetUserInputsCertificado(req_body):
    #Getting all the inputs
    NombrePerito            =    str(    req_body.getlist('entry[fields][71]')[0])
    EmailPerito             =    str(    req_body.getlist('entry[fields][72]')[0])

    Nombre                  =    str(    req_body.getlist('entry[fields][30]')[0])
    Apellidos               =    str(    req_body.getlist('entry[fields][29]')[0])
    Email                   =    str(    req_body.getlist('entry[fields][2]' )[0])
    TipoDeDocumento         =    str(    req_body.getlist('entry[fields][27]')[0])
    NumeroDeDocumento       =    str(    req_body.getlist('entry[fields][44]')[0])
    Celular                 =    str(    req_body.getlist('entry[fields][62]')[0])
    TipoDeInmueble          =    str(    req_body.getlist('entry[fields][41]')[0])
    NombreEdificio          =    str(    req_body.getlist('entry[fields][45]')[0])
    Pais                    =    str(    req_body.getlist('entry[fields][8]' )[0])
    Departamento            =    str(    req_body.getlist('entry[fields][51]')[0])
    Ciudad                  =    str(    req_body.getlist('entry[fields][9]' )[0]) 
    Barrio                  =    str(    req_body.getlist('entry[fields][46]')[0])
    Estrato                 =    int(    req_body.getlist('entry[fields][20]')[0])
    TipoDeSector            =    str(    req_body.getlist('entry[fields][42]')[0])
    TipoDeVia               =    str(    req_body.getlist('entry[fields][3]' )[0])
    Numero1                 =    str(    req_body.getlist('entry[fields][5]' )[0])
    Numero2                 =    str(    req_body.getlist('entry[fields][6]' )[0])
    Numero3                 =    str(    req_body.getlist('entry[fields][7]' )[0])
    NumeroApartamento       =    str(    req_body.getlist('entry[fields][47]')[0])
    Alcobas                 =    int(    req_body.getlist('entry[fields][15]')[0])
    Niveles                 =    int(    req_body.getlist('entry[fields][25]')[0])
    Piso                    =    int(    req_body.getlist('entry[fields][18]')[0])
    Banos                   =    int(    req_body.getlist('entry[fields][26]')[0])
    BanosSociales           =    int(    req_body.getlist('entry[fields][60]')[0])
    BanosPrivados           =    int(    req_body.getlist('entry[fields][61]')[0])
    BanosDeServicio         =    int(    req_body.getlist('entry[fields][67]')[0])
    Salas                   =    int(    req_body.getlist('entry[fields][56]')[0])
    Comedores               =    int(    req_body.getlist('entry[fields][57]')[0])
    Cocinas                 =    int(    req_body.getlist('entry[fields][65]')[0])
    AlcobasDeServicio       =    int(    req_body.getlist('entry[fields][66]')[0])
    Estudios                =    int(    req_body.getlist('entry[fields][58]')[0])
    Estares                 =    int(    req_body.getlist('entry[fields][64]')[0])
    Balcones                =    int(    req_body.getlist('entry[fields][59]')[0])
    Patios                  =    int(    req_body.getlist('entry[fields][68]')[0])
    Terrazas                =    int(    req_body.getlist('entry[fields][69]')[0])
    CuartosUtiles           =    int(    req_body.getlist('entry[fields][70]')[0])
    CantidadParqueaderos    =    int(    req_body.getlist('entry[fields][21]')[0])
    ParqueaderosCubiertos   =    int(    req_body.getlist('entry[fields][52]')[0])
    ParqueaderosDescubiertos=    int(    req_body.getlist('entry[fields][53]')[0])
    ParqueaderosSencillos   =    int(    req_body.getlist('entry[fields][54]')[0])
    ParqueaderosDobles      =    int(    req_body.getlist('entry[fields][55]')[0])
    PisosEdificio           =    int(    req_body.getlist('entry[fields][36]')[0])
    SotanosEdificio         =    int(    req_body.getlist('entry[fields][37]')[0])
    M2Construidos           =    float(  req_body.getlist('entry[fields][19]')[0])
    AreaTerraza             =    float(  req_body.getlist('entry[fields][23]')[0])
    AnoConstruccion         =    int(    req_body.getlist('entry[fields][22]')[0])
    Administracion          =    float(  req_body.getlist('entry[fields][24]')[0])    #Mensual
    Predial                 =    float(  req_body.getlist('entry[fields][17]')[0])    #Anual
    DetallesApartamento     =    str(    req_body.getlist('fields[38][value]')[0])
    DetallesEdificio        =    str(    req_body.getlist('fields[39][value]')[0])
    DetallesSector          =    str(    req_body.getlist('fields[43][value]')[0])
    #DetallesGaraje          =    str(    req_body.getlist('fields[49][value]')[0])
    AnalisisInmueble        =    str(    req_body.getlist('entry[fields][73]' )[0])
    ActividadEdificadora    =    str(    req_body.getlist('entry[fields][80]' )[0])
    OfertaDemanda           =    str(    req_body.getlist('entry[fields][79]' )[0])
    ObservacionesSector     =    str(    req_body.getlist('entry[fields][78]' )[0])
    DescInmuebleAcabados    =    str(    req_body.getlist('entry[fields][77]' )[0])
    ObsConstEstructura      =    str(    req_body.getlist('entry[fields][76]' )[0])
    ObsLiquidación          =    str(    req_body.getlist('entry[fields][74]' )[0])
    ObsGenerales            =    str(    req_body.getlist('entry[fields][75]' )[0])
    PerspValoracion         =    str(    req_body.getlist('entry[fields][81]' )[0])


    #Not from the user
    ReportNumber = 1

    #putting everything in a dictionary
    DicInputs = {
                 'NombrePerito'            : NombrePerito,
                 'EmailPerito'             : EmailPerito,
                 'Nombre'                  : Nombre,
                 'Apellidos'               : Apellidos,
                 'Email'                   : Email,
                 'TipoDeDocumento'         : TipoDeDocumento,
                 'NumeroDeDocumento'       : NumeroDeDocumento,
                 'Celular'                 : Celular,
                 'TipoDeInmueble'          : TipoDeInmueble,
                 'NombreEdificio'          : NombreEdificio,
                 'Pais'                    : Pais,
                 'Departamento'            : Departamento,
                 'Ciudad'                  : Ciudad,
                 'Barrio'                  : Barrio,
                 'Estrato'                 : Estrato,
                 'TipoDeSector'            : TipoDeSector,
                 'TipoDeVia'               : TipoDeVia,
                 'Numero1'                 : Numero1,
                 'Numero2'                 : Numero2,
                 'Numero3'                 : Numero3,
                 'NumeroApartamento'       : NumeroApartamento,
                 'Alcobas'                 : Alcobas,
                 'Niveles'                 : Niveles,
                 'Piso'                    : Piso,
                 'Banos'                   : Banos,
                 'BanosSociales'           : BanosSociales,
                 'BanosPrivados'           : BanosPrivados,
                 'BanosDeServicio'         : BanosDeServicio,
                 'Salas'                   : Salas,
                 'Comedores'               : Comedores,
                 'Cocinas'                 : Cocinas,
                 'AlcobasDeServicio'       : AlcobasDeServicio,
                 'Estudios'                : Estudios,
                 'Estares'                 : Estares,
                 'Balcones'                : Balcones,
                 'Patios'                  : Patios,
                 'Terrazas'                : Terrazas,
                 'CuartosUtiles'           : CuartosUtiles,
                 'CantidadParqueaderos'    : CantidadParqueaderos,
                 'ParqueaderosCubiertos'   : ParqueaderosCubiertos,
                 'ParqueaderosDescubiertos': ParqueaderosDescubiertos,
                 'ParqueaderosSencillos'   : ParqueaderosSencillos,
                 'ParqueaderosDobles'      : ParqueaderosDobles,
                 'PisosEdificio'           : PisosEdificio,
                 'SotanosEdificio'         : SotanosEdificio,
                 'M2Construidos'           : M2Construidos,
                 'AreaTerraza'             : AreaTerraza,
                 'AnoConstruccion'         : AnoConstruccion,
                 'Administracion'          : Administracion,
                 'Predial'                 : Predial,
                 'DetallesApartamento'     : DetallesApartamento.split('\n'),
                 'DetallesEdificio'        : DetallesEdificio.split('\n'),
                 'DetallesSector'          : DetallesSector.split('\n'),
                 'ReportNumber'            : ReportNumber,
                 'PerspValoracion'         : PerspValoracion,
                 'AnalisisInmueble'        : AnalisisInmueble,
                 'ActividadEdificadora'    : ActividadEdificadora,
                 'OfertaDemanda'           : OfertaDemanda,
                 'ObservacionesSector'     : ObservacionesSector,
                 'DescInmuebleAcabados'    : DescInmuebleAcabados,
                 'ObsConstEstructura'      : ObsConstEstructura,
                 'ObsLiquidación'          : ObsLiquidación,
                 'ObsGenerales'            : ObsGenerales,
                }

 


    return DicInputs

