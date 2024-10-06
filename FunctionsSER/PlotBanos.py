import matplotlib.pyplot as plt
import bisect
import pandas as pd

from matplotlib              import rcParams, colors
from mpl_toolkits.axes_grid1 import Divider, Size
from matplotlib.ticker       import PercentFormatter


from FunctionsSER.DefineRcParams         import DefineRcParams
from FunctionsSER.DefineColors           import DefineColors

def PlotBanos(DicInputs, df_apartamentos_unscaled_neigh):

    DicColors = DefineColors ()
    BlueDark        = DicColors['BlueDark']
    BlueLight       = DicColors['BlueLight']
    GrayLight       = DicColors['GrayLight']


    DicRcParams = DefineRcParams()
    rcParams.update(DicRcParams)


    Banos = DicInputs['Banos']


    fig = plt.figure(figsize=(3.5, 2))


    # The first items are for padding and the second items are for the axes.
    # sizes are in inch.
    h = [Size.Fixed(1.0), Size.Fixed(1.02)]
    v = [Size.Fixed(0.25), Size.Fixed(1.2)]

    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    # The width and height of the rectangle are ignored.

    ax = fig.add_axes(divider.get_position(),
                    axes_locator=divider.new_locator(nx=1, ny=1))


    # # de Baños Completos
    binsBanos = [0.5,1.5,2.5,3.5,4.5, 30]
    labelsBanos = ['1','2','3','4','5+' ]
    colorBanos = [BlueLight]*len(binsBanos)
    colorBanos[bisect.bisect_left(binsBanos, Banos)-1] = BlueDark

    BanosToPlot = pd.cut(df_apartamentos_unscaled_neigh['# de Baños Completos'], 
                            bins = binsBanos,
                            labels = labelsBanos)

    ax.barh((BanosToPlot.value_counts(sort=False, normalize=True).index),
                (BanosToPlot.value_counts(sort=False, normalize=True).values),
                color=colorBanos,
                height=0.4)
    # ax.set_title('Baños')
    ax.xaxis.set_major_formatter(PercentFormatter(1, decimals = 0))


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


    bar = ax.patches[bisect.bisect_left(binsBanos, Banos)-1]
    ax.text(bar.get_width()+0.02, bar.get_y()+0.07,  
            str(Banos)+' baños', 
            color = BlueDark,
            fontsize = 6) 


    ax.set_axisbelow(True)
    # fig.tight_layout()

    fig.savefig('InfoBanos.png', 
            transparent = True,
            dpi=250)
    fig.clf()

    return None

