from FunctionsSER.DefineColors import DefineColors

def DefineRcParams():

    #defining colors
    # BlueDark       = "#0c3ae5"
    # BlueDarkDark   = "#05477f"
    # BlueLight      = "#00c3ff"
    # BlueLightLight = "#ccdcff"
    # GrayLight      = "#b3b3b3"
    # GrayDark       = "#66635b"
    # COLOR          = 'black'

    DicColors = DefineColors ()

    DicRcParams = {'text.color'        : DicColors['BlueDarkDark'],
                   'axes.labelcolor'   : DicColors['BlueDarkDark'],
                   'axes.edgecolor'    : DicColors['COLOR'],
                   'xtick.color'       : DicColors['BlueDarkDark'],
                   'ytick.color'       : DicColors['BlueDarkDark'],
                   'font.size'         : 7,
                   'font.family'       : 'sans-serif',
                   'font.sans-serif'   : 'Roboto'}
    return DicRcParams