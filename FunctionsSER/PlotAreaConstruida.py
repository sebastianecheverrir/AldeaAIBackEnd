import matplotlib.pyplot as plt
import bisect
import pandas as pd
from numpy                  import mean


from matplotlib              import rcParams, colors
from mpl_toolkits.axes_grid1 import Divider, Size
from matplotlib.ticker       import PercentFormatter


from FunctionsSER.DefineRcParams         import DefineRcParams
from FunctionsSER.DefineColors           import DefineColors

def PlotAreaConstruida(DicInputs, df_apartamentos_unscaled_neigh):

    DicColors = DefineColors ()
    BlueDark        = DicColors['BlueDark']
    BlueLight       = DicColors['BlueLight']
    GrayLight       = DicColors['GrayLight']


    DicRcParams = DefineRcParams()
    rcParams.update(DicRcParams)


    M2Construidos = DicInputs['M2Construidos']



    fig = plt.figure(figsize=(3.5, 2))


    # The first items are for padding and the second items are for the axes.
    # sizes are in inch.
    h = [Size.Fixed(1.0), Size.Fixed(1.02)]
    v = [Size.Fixed(0.25), Size.Fixed(1.2)]

    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    # The width and height of the rectangle are ignored.

    ax = fig.add_axes(divider.get_position(),
                    axes_locator=divider.new_locator(nx=1, ny=1))

    #M2 Area Construida
    binsArea = [0,80,120,160,200,240,10000]
    labelsArea = [' - 80','80 - 120','120 - 160','160 - 200','200 - 240', '240+' ]
    colorArea = [BlueLight]*len(binsArea)
    colorArea[bisect.bisect_left(binsArea, M2Construidos)-1] = BlueDark

    AreaToPlot = pd.cut(df_apartamentos_unscaled_neigh['M2 Area Construida'], 
                            bins = binsArea,
                            labels = labelsArea)

    ax.barh((AreaToPlot.value_counts(sort=False, normalize=True).index),
                (AreaToPlot.value_counts(sort=False, normalize=True).values),
                color=colorArea,
                height=0.4)
    # ax.set_title('Área Construida $[m^2]$')
    ax.xaxis.set_major_formatter(PercentFormatter(1, decimals = 0))

    #Avrage M2 Area Construida
    avg_M2Construidos = mean(df_apartamentos_unscaled_neigh['M2 Area Construida'])


    #formatting

    ax.xaxis.set_major_formatter(PercentFormatter(xmax=1, decimals = 0))
    ax.set_xlim([0, 1])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_color(GrayLight)
    ax.spines['left'].set_color(GrayLight)

    gridWidth = 0.3
    ax.spines['left'].set_linewidth(gridWidth)
    ax.spines['right'].set_linewidth(gridWidth)

    ax.grid(b=True, axis='x', color=GrayLight, linewidth = gridWidth)

    ax.set_xticks([0, 0.25, 0.5, 0.75,1])
    ax.tick_params(axis='both', which='both',length=0)
    ax.tick_params(axis='x', which='major', pad=6)

    bar = ax.patches[bisect.bisect_left(binsArea, M2Construidos)-1]
    ax.text(bar.get_width()+0.02, bar.get_y()+0.07,  
            str(int(M2Construidos))+' m$^2$', 
            color = BlueDark,
            fontsize = 6) 


    ax.set_axisbelow(True)
    # fig.tight_layout()

    fig.savefig('InfoAreaConstruida.png', 
            transparent = True,
            dpi=250)

    fig.clf()


    return avg_M2Construidos


