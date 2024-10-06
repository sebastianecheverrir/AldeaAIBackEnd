from geopy                   import geocoders

def GetLocation(DicInputs, apikey):

    #getting location from google maps

    # apikey = apikey # (your API key here)

    g = geocoders.GoogleV3(api_key=apikey)
    # g = geocoders.Nominatim()

    #create an input address string
    #you can also build this by reading from an input database and building a string

    TipoDeVia   = DicInputs['TipoDeVia']
    Numero1     = DicInputs['Numero1']
    Numero2     = DicInputs['Numero2']
    Numero3     = DicInputs['Numero3']
    Ciudad      = DicInputs['Ciudad']
    Pais        = DicInputs['Pais']

    inputAddress = TipoDeVia + ' '  + \
                    str(Numero1) + ' # ' + \
                    str(Numero2) + ' - ' + \
                    str(Numero3) + ' , ' + \
                    Ciudad  + ' , ' + \
                    Pais

    #do the geocode
    location = g.geocode(inputAddress, timeout=10)

    Latitud                = location.latitude   #
    Longitud               = location.longitude  #

    #some things you can get from the result
    # print(location.latitude, location.longitude)

    DicLocation = { 'Latitud' : Latitud,
                    'Longitud' : Longitud}
    
    return DicLocation