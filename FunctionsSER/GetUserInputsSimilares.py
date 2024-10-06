def GetUserInputsSimilares(req_body):
    #Getting all the inputs
    NombrePerito            =    str(    req_body.getlist('entry[fields][71]')[0])
    EmailPerito             =    str(    req_body.getlist('entry[fields][72]')[0])

    TipoDeInmueble          =    str(    req_body.getlist('entry[fields][41]')[0])
    Pais                    =    str(    req_body.getlist('entry[fields][8]' )[0])
    Departamento            =    str(    req_body.getlist('entry[fields][51]')[0])
    Ciudad                  =    str(    req_body.getlist('entry[fields][9]' )[0]) 
    TipoDeVia               =    str(    req_body.getlist('entry[fields][3]' )[0])
    Numero1                 =    str(    req_body.getlist('entry[fields][5]' )[0])
    Numero2                 =    str(    req_body.getlist('entry[fields][6]' )[0])
    Numero3                 =    str(    req_body.getlist('entry[fields][7]' )[0])
    M2Construidos           =    float(  req_body.getlist('entry[fields][19]')[0])


    #Not from the user
    ReportNumber = 1

    #putting everything in a dictionary
    DicInputs = {
                 'NombrePerito'            : NombrePerito,
                 'EmailPerito'             : EmailPerito,
                 'TipoDeInmueble'          : TipoDeInmueble,
                 'Pais'                    : Pais,
                 'Departamento'            : Departamento,
                 'Ciudad'                  : Ciudad,
                 'TipoDeVia'               : TipoDeVia,
                 'Numero1'                 : Numero1,
                 'Numero2'                 : Numero2,
                 'Numero3'                 : Numero3,
                 'M2Construidos'           : M2Construidos,
                }

 


    return DicInputs

