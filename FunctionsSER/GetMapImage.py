from io                      import BytesIO
from PIL                     import Image
from urllib                  import request

def GetMapImage(DicLocation,apikey):
    #extracting map image 

    latitude  = DicLocation['Latitud']
    longitude = DicLocation['Longitud']
    # apikey = apikey

    url = 'http://maps.googleapis.com/maps/api/staticmap?center=' + \
        str(latitude) + ',' + \
        str(longitude) + \
        '&markers=' + \
        str(latitude) + ',' + \
        str(longitude) + \
        '&size=280x180' + \
        '&zoom=16'+ \
        '&scale=2'+ \
        '&sensor=false' + \
        '&key='+ apikey

    buffer = BytesIO(request.urlopen(url).read())
    image = Image.open(buffer).convert('RGB')

    #adding logo
    imgLogo = Image.open("Images/Logos/LogoOriginal.png").convert('RGB')
    imgLogo = imgLogo.resize((int(imgLogo.width/2.5),int(imgLogo.height/2.5)), Image.ANTIALIAS)

    image.paste(imgLogo, (0,0))
    image.save('Mapa.png')

    # # # Or using pyplot
    # plt.imshow(image)
    # plt.show()
    return None
