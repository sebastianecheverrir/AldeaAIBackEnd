import os

def WriteReport(DicInputs, DicPrecio, avg_Precio, 
                AlcobasToPlot, IPVU_Delta_List, avg_M2Construidos):
    #writing the report

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
    ReportNumber            =   DicInputs['ReportNumber']
    TipoDeVia               =   DicInputs['TipoDeVia']
    Numero1                 =   DicInputs['Numero1']
    Numero2                 =   DicInputs['Numero2']
    Numero3                 =   DicInputs['Numero3']
    Ciudad                  =   DicInputs['Ciudad']
    Pais                    =   DicInputs['Pais']
    
    Precio                  =   DicPrecio['Precio']
    PrecioM2                =   DicPrecio['PrecioM2']
    PrecioArriendo          =   DicPrecio['PrecioArriendo']
    # Latitud                 =   DicLocation['Latitud']
    # Longitud                =   DicLocation['Longitud']


    filename = "Report.tex"

    f = open(filename, 'w')

    #headers
    f.write(r'''

    %https://tex.stackexchange.com/questions/167719/how-to-use-background-image-in-latex


    \documentclass{article}

    %Tipo de letra parecido a tahoma
    %sudo apt install texlive-fonts-extra
    \usepackage[default]{roboto} 

    %package needed for the background
    \usepackage{eso-pic,graphicx}

    %defining the margins and the page size
    \usepackage[top=0cm, bottom=0cm, outer=0cm, inner=0cm, 
                letterpaper]{geometry}

    %package for formating numbers
    \usepackage{siunitx}

    %defining colors
    \definecolor{BlueDark}{RGB}{12,58,229}
    \definecolor{BlueDarkDark}{RGB}{5,71,127}
    \definecolor{BlueLight}{RGB}{0,195,255}
    \definecolor{GrayLight}{RGB}{179,179,179}
    \definecolor{GrayDark}{RGB}{102,99,91}

    %Command to insert text in the desired positions
    %https://tex.stackexchange.com/questions/168141/can-latex-place-text-by-mm-coordinates
    \usepackage{tikz}
    \newcommand\PlaceText[3]{%
    \begin{tikzpicture}[remember picture,overlay]
        \node[outer sep=0pt,inner sep=0pt,anchor=south west] 
            at ([xshift=#1,yshift=-#2]current page.north west) { #3};
    \end{tikzpicture}%
    }

    %Command to insert image in the desired positions

    \newcommand\PlaceFigure[3]{%
    \begin{tikzpicture}[overlay, remember picture]
    \node[anchor=north west, %anchor is upper left corner of the graphic
        xshift=#1, %shifting around
        yshift=-#2] 
        at (current page.north west) %left upper corner of the page
        {\includegraphics[]{#3}}; 
    \end{tikzpicture}%
    }
    ''')

    #begin document
    f.write(r'''
    \begin{document}
    ''')

    ########################################3

    #first page
    f.write(r'''
    %insert Background page 1
    %https://tex.stackexchange.com/questions/167719/how-to-use-background-image-in-latex
    \AddToShipoutPictureBG*{\includegraphics[width=\paperwidth, height=\paperheight, page=1]{ALDEAAIAVALUOV3plantillaSebas.pdf}}
    ''')

    f.write(r'''
    %%%%%%%%%%%%%%%%%%%%%%%%%%5
    %Inserting text

    %Numero de reporte
    ''')

    f.write(r'\PlaceText{0.92\paperwidth}{0.113\paperheight}{{\textbf{\color{GrayDark} {'+
            str(ReportNumber)+ r'}}}}')

    f.write(r'''
    %Dirección
    ''')

    f.write(r'\PlaceText{0.6\paperwidth}{0.2315\paperheight}{\color{BlueDarkDark} {' + 
            TipoDeVia    + ' '    +
            str(Numero1) + r' \# ' +
            str(Numero2) + r' - ' +
            str(Numero3) + ' '    +
            Ciudad       + ', '   +
            Pais         + r'.}}')


    f.write(r'''
    %Estrato
    ''')
    f.write(r'\PlaceText{0.567\paperwidth}{0.243\paperheight}{\color{BlueDarkDark} {' + 
            str(Estrato) + r'}}')

    f.write(r'''
    %Valor Estimado
    ''')
    f.write(r'\PlaceText{0.7\paperwidth}{0.28\paperheight}{\large{{\color{BlueLight} {' +
            r'\$ ' +            
            r'\SI[]{' +  str(int(round(Precio[0]-0.05*Precio[0], -6))) + r'}{} - ' +
            r'\$ ' +            
            r'\SI[]{' +  str(int(round(Precio[0]+0.05*Precio[0], -6))) + r'}{}' +
            '}}}}') 


    f.write(r'''
    %Valor por m2
    ''')
    f.write(r'\PlaceText{0.7\paperwidth}{0.3175\paperheight}{\large{{\color{BlueLight} {' +
            r'\$ ' + 
            r'\SI[]{' +  str(int(round(PrecioM2[0]-0.05*PrecioM2[0], -5))) + r'}{} - ' +
            r'\$ ' +
            r'\SI[]{' +  str(int(round(PrecioM2[0]+0.05*PrecioM2[0], -5))) + r'}{}' +            
            '}}}}') 

    f.write(r'''
    %Valor Estimado Arriendo
    ''')
    f.write(r'\PlaceText{0.76\paperwidth}{0.355\paperheight}{\large{{\color{BlueLight} {' +
            r'\$ ' + 
            r'\SI[]{' +  str(int(round(PrecioArriendo-0.05*PrecioArriendo, -5))) + r'}{} - ' +
            r'\$ ' +
            r'\SI[]{' +  str(int(round(PrecioArriendo+0.05*PrecioArriendo, -5))) + r'}{}' +
            '}}}}') 

    f.write(r'''
    %Valor por m2 en la zona
    ''')
    if (PrecioM2[0] < avg_Precio):
        f.write(r'\PlaceText{0.677\paperwidth}{0.8795\paperheight}{\scriptsize{\textbf{\color{BlueDarkDark} {por debajo}}}}')
    else:
        f.write(r'\PlaceText{0.674\paperwidth}{0.8795\paperheight}{\scriptsize{\textbf{\color{BlueDarkDark} {por encima}}}}')


    f.write(r'''


    %%%%%%%%%%%%%%%%%%%%%%%%%%5
    %Inserting mages

    %Mapa
    \begin{tikzpicture}[overlay, remember picture]
    \node[anchor=north west, %anchor is upper left corner of the graphic
        xshift=0.0\paperwidth, %shifting around
        yshift=-0.174\paperheight] 
        at (current page.north west) %left upper corner of the page
        {\includegraphics[scale=0.5, trim=0 40 0 0, clip]{Mapa.png}}; 
    \end{tikzpicture}%


    %Alcobas
    \PlaceFigure{-0.047\paperwidth}{0.484\paperheight}{InfoAlcobas.png}

    %Banos 
    \PlaceFigure{0.206\paperwidth}{0.484\paperheight}{InfoBanos.png}

    %Parqueaderos
    \PlaceFigure{0.449\paperwidth}{0.484\paperheight}{InfoParqueaderos.png}

    %Predial
    \PlaceFigure{0.6866\paperwidth}{0.484\paperheight}{InfoPredial.png}

    %Anos de contruido
    \PlaceFigure{-0.047\paperwidth}{0.701\paperheight}{InfoAnoConstruccion.png}

    %Area Construida
    \PlaceFigure{0.206\paperwidth}{0.701\paperheight}{InfoAreaConstruida.png}

    %Valor por m2
    \PlaceFigure{0.525\paperwidth}{0.745\paperheight}{PricePerM2.png}

    \newpage
    ''')

    ########################################3
    ########################################3
    ########################################3

    #second page

    f.write(r'''

    %%%%%%%%%%%%%%%%%%%%%%%%%%5
    %%%%%%%%%%%%%%%%%%%%%%%%%%5

    %insert Background page 2
    %https://tex.stackexchange.com/questions/167719/how-to-use-background-image-in-latex
    \AddToShipoutPictureBG*{\includegraphics[width=\paperwidth, height=\paperheight, page=2]{ALDEAAIAVALUOV3plantillaSebas.pdf}}

    %%%%%%%%%%%%%%%%%%%%%%%%%%5
    %Inserting text
    ''')

    #print(AlcobasToPlot.value_counts(sort=False, normalize=True).values[Alcobas-1])


    f.write(r'''
    %Alcobas
    ''')
    f.write(r'\PlaceText{0.1025\paperwidth}{0.1659\paperheight}{\scriptsize{\textbf{\color{BlueDarkDark} {' + 
            str(int(AlcobasToPlot.value_counts(sort=False, normalize=True).values[Alcobas-1]*100)) + 
            '\%}}}}')
    f.write(r'\PlaceText{0.175\paperwidth}{0.1754\paperheight}{\scriptsize{\color{BlueDarkDark} {' + 
            str(Alcobas) + 
            '}}}')

    f.write(r'''
    %Area construida
    ''')
    f.write(r'\PlaceText{0.515\paperwidth}{0.1754\paperheight}{\scriptsize{\color{BlueDarkDark} {' + 
            str(int(avg_M2Construidos)) + 
            'm$^{2}$}}}')

    f.write(r'''
    %Valor Promedio
    ''')
    f.write(r'\PlaceText{0.819\paperwidth}{0.1759\paperheight}{\scriptsize{\color{BlueDarkDark} {\$' +
            r'\SI[]{' +  str(int(round(avg_Precio, -5))) + r'}{}' +
            '}}}')

    f.write(r'''
    %Valorización
    ''')
    if IPVU_Delta_List[-1] < 0:
        f.write(r'\PlaceText{0.515\paperwidth}{0.5877\paperheight}{\large{\textbf{\color{BlueDarkDark} {valorizado}}}}')
    else :
        f.write(r'\PlaceText{0.515\paperwidth}{0.5877\paperheight}{\large{\textbf{\color{BlueDarkDark} {desvalorizado}}}}')
    f.write(r'\PlaceText{0.355\paperwidth}{0.604\paperheight}{\large{\textbf{\color{BlueDarkDark} {' + 
            str(int(IPVU_Delta_List[-1])) + 
            '\%}}}}')

    f.write(r'''
    %Anexos
    ''')

    f.write(r'\PlaceText{0.07\paperwidth}{0.744\paperheight}{\color{GrayDark} {No. de alcobas}}')
    f.write(r'\PlaceText{0.24\paperwidth}{0.744\paperheight}{\color{GrayLight} {' + 
            str(Alcobas) + '}}')

    f.write(r'\PlaceText{0.07\paperwidth}{0.765\paperheight}{\color{GrayDark} {No. de ba\~{n}os}}')
    f.write(r'\PlaceText{0.24\paperwidth}{0.765\paperheight}{\color{GrayLight} {' + 
            str(Banos) + '}}')

    f.write(r'\PlaceText{0.07\paperwidth}{0.786\paperheight}{\color{GrayDark} {No. de niveles}}')
    f.write(r'\PlaceText{0.24\paperwidth}{0.786\paperheight}{\color{GrayLight} {' + 
            str(Niveles) + '}}')

    f.write(r'\PlaceText{0.07\paperwidth}{0.807\paperheight}{\color{GrayDark} {Valor administraci\'{o}n}}')
    f.write(r'\PlaceText{0.24\paperwidth}{0.807\paperheight}{\color{GrayLight} {\$ \SI{' + 
            str(int(Administracion)) + '}{} }}')

    f.write(r'\PlaceText{0.38\paperwidth}{0.744\paperheight}{\color{GrayDark} {\'{A}rea terraza}}')
    f.write(r'\PlaceText{0.55\paperwidth}{0.744\paperheight}{\color{GrayLight} {\SI{' + 
            str(int(AreaTerraza)) + '}{\square\meter}}}')

                                                                    
    f.write(r'\PlaceText{0.38\paperwidth}{0.765\paperheight}{\color{GrayDark} {A\~{n}o de construcci\'{o}n}}')
    f.write(r'\PlaceText{0.55\paperwidth}{0.765\paperheight}{\color{GrayLight} {' +
            str(AnoConstruccion) + '}}')

    f.write(r'\PlaceText{0.38\paperwidth}{0.786\paperheight}{\color{GrayDark} {No. parqueaderos}}')
    f.write(r'\PlaceText{0.55\paperwidth}{0.786\paperheight}{\color{GrayLight} {' + 
            str(CantidadParqueaderos) + '}}')

    f.write(r'\PlaceText{0.38\paperwidth}{0.807\paperheight}{\color{GrayDark} {Estrato}}')
    f.write(r'\PlaceText{0.55\paperwidth}{0.807\paperheight}{\color{GrayLight} {' + 
            str(Estrato) + '}}')


    f.write(r'\PlaceText{0.705\paperwidth}{0.744\paperheight}{\color{GrayDark} {\'{A}rea Construida}}')
    f.write(r'\PlaceText{0.875\paperwidth}{0.744\paperheight}{\color{GrayLight} {\SI{' + 
            str(int(M2Construidos)) + '}{\square\meter}}}')


                                                                    
    f.write(r'\PlaceText{0.705\paperwidth}{0.765\paperheight}{\color{GrayDark} {Piso}}')
    f.write(r'\PlaceText{0.875\paperwidth}{0.765\paperheight}{\color{GrayLight} {' + 
            str(Piso) + '}}')

    f.write(r'\PlaceText{0.705\paperwidth}{0.786\paperheight}{\color{GrayDark} {Valor predial}}')
    f.write(r'\PlaceText{0.875\paperwidth}{0.786\paperheight}{\color{GrayLight} {\$ \SI{' + 
            str(int(Predial)) + '}{} }}')

    f.write(r'''

    %%%%%%%%%%%%%%%%%%%%%%%%%%5
    %Inserting images

    %Evolucion de precio en el tiempo
    \PlaceFigure{0.052\paperwidth}{0.31\paperheight}{InfoTiempoIndice.png}

    ''')


    #end document

    f.write(r'''

    \end{document}
    ''')





    f.close()

    os.system('xelatex --interaction=batchmode ' + filename)
    os.system('xelatex --interaction=batchmode ' + filename)

    # os.system('xelatex ' + filename)
#     os.system('rm *png')
    #0 means that the output is fine
    return None

