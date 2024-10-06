import gc
import os 

from flask import Flask
from flask import request
from waitress import serve

from FunctionsSER.GetUserInputs       import GetUserInputs
from FunctionsSER.GetLocation         import GetLocation
from FunctionsSER.GetMapImage         import GetMapImage
from FunctionsSER.EstimateValue       import EstimateValue
from FunctionsSER.EstimateValueByLaw  import EstimateValueByLaw

from FunctionsSER.ReadData            import ReadData
from FunctionsSER.DrawThermometer     import DrawThermometer
from FunctionsSER.PlotAlcobas         import PlotAlcobas
from FunctionsSER.PlotBanos           import PlotBanos
from FunctionsSER.PlotParqueaderos    import PlotParqueaderos
from FunctionsSER.PlotAnoConstruccion import PlotAnoConstruccion
from FunctionsSER.PlotAreaConstruida  import PlotAreaConstruida
from FunctionsSER.PlotPredial         import PlotPredial
from FunctionsSER.PlotTiempo          import PlotTiempo
from FunctionsSER.PlotTiempoIndice    import PlotTiempoIndice
from FunctionsSER.WriteReport         import WriteReport
from FunctionsSER.SendEmail           import SendEmail

from FunctionsSER.GetUserInputsCertificado import GetUserInputsCertificado
from FunctionsSER.SendEmailCertificado     import SendEmailCertificado
from FunctionsSER.WriteReportCertificado   import WriteReportCertificado
from FunctionsSER.WriteReportCertificadoBonito   import WriteReportCertificadoBonito
from FunctionsSER.SendEmailCertificadoBonito import SendEmailCertificadoBonito

from FunctionsSER.GetUserInputsSimilares import GetUserInputsSimilares
from FunctionsSER.SendEmailSimilares     import SendEmailSimilares
from FunctionsSER.WriteReportSimilares   import WriteReportSimilares
from FunctionsSER.FindSimilares          import FindSimilares

import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['POST'])
def ReadPostInfo():

    if request.method == 'POST':
##########################################
        #Avaluos Digitales Gratis
        #Form ID 385
        if request.form['wpforms_id'] == "385":
            #print(dir(request), flush=True)
            #print(request.form['wpforms_id'], flush=True)

            req_body = request.form
    
            DicInputs   = GetUserInputs(req_body)
    
            apikey = 'AIzaSyBBw5MyPbPLFBY6d3kYBQ-swm_XzlFqfyg'
            DicLocation = GetLocation(DicInputs, apikey)
    
            GetMapImage(DicLocation,apikey)
            DicPrecio, scaler, X_scaled_single, RF_median = EstimateValue(DicInputs, DicLocation)
    
            X_data, df_apartamentos_unscaled = ReadData(scaler)
    
            PrecioM2 = DicPrecio['PrecioM2']
            
            df_apartamentos_unscaled_neigh, avg_Precio = DrawThermometer(X_data,X_scaled_single, df_apartamentos_unscaled, PrecioM2)
            AlcobasToPlot = PlotAlcobas(DicInputs, df_apartamentos_unscaled_neigh)
            PlotBanos(DicInputs, df_apartamentos_unscaled_neigh)
            PlotParqueaderos(DicInputs, df_apartamentos_unscaled_neigh)
            PlotAnoConstruccion(DicInputs, df_apartamentos_unscaled_neigh)
            avg_M2Construidos = PlotAreaConstruida(DicInputs, df_apartamentos_unscaled_neigh)
            PlotPredial(DicInputs, df_apartamentos_unscaled_neigh)
            PlotTiempo(DicInputs, DicLocation, scaler, RF_median)
            Precio = DicPrecio['Precio']
            IPVU_Delta_List = PlotTiempoIndice(Precio)
    
    
    
            WriteReport(DicInputs, DicPrecio, avg_Precio, AlcobasToPlot, IPVU_Delta_List, avg_M2Construidos)
            SendEmail(DicInputs)
            
            #Saves inputs and outputs in the file output.csv
            DicInAndOut = {**DicInputs, **DicPrecio}
            df_InAndOut = pd.DataFrame(data=DicInAndOut, index=[0])
            df_InAndOut.to_csv("outputConcepto.csv", mode='a', header=False)
    
            os._exit(0)
#######################################
        #Avaluos certificados. 
        #Form ID 670    
        elif request.form['wpforms_id'] == "670":
            #print(request.form, flush=True)
            req_body = request.form
            
            DicInputs   = GetUserInputsCertificado(req_body)
            DicInputsBasic   = GetUserInputs(req_body)
            #print(DicInputs, flush=True)


            apikey = ''
            DicLocation = GetLocation(DicInputs, apikey)

            GetMapImage(DicLocation,apikey)
            DicPrecio, scaler, X_scaled_single, RF_median = EstimateValue(DicInputs, DicLocation)

            #Avaluo certificado bonito de acuerdo a la ley
            _, df_apartamentos_neigh, PrecioByLaw = EstimateValueByLaw(DicInputs, DicLocation)
            WriteReportCertificadoBonito(DicInputs, df_apartamentos_neigh, PrecioByLaw, DicLocation)
            SendEmailCertificadoBonito(DicInputs)


            #Saves inputs and outputs in the file output.csv
            DicInAndOut = DicInputs # {**DicInputs, **DicPrecio}
            del DicInAndOut['DetallesApartamento']
            del DicInAndOut['DetallesEdificio']
            del DicInAndOut['DetallesSector']
            
            df_InAndOut = pd.DataFrame(data=DicInAndOut, index=[0])
            df_InAndOut.to_csv("outputCertificado.csv", mode='a', header=False)
            

#            print(PrecioByLaw, PrecioM2, flush=True)
#            print(df_apartamentos_neigh, flush=True)
            os._exit(0)


#######################################
        #Inmuebles Similares . 
        #Form ID 713    
        elif request.form['wpforms_id'] == "713":
            #print(request.form, flush=True)
            req_body = request.form

            DicInputs   = GetUserInputsSimilares(req_body)
            #print(DicInputs, flush=True)


            apikey = 'AIzaSyBBw5MyPbPLFBY6d3kYBQ-swm_XzlFqfyg'
            DicLocation = GetLocation(DicInputs, apikey)

            GetMapImage(DicLocation,apikey)
            #DicPrecio, scaler, X_scaled_single, RF_median = EstimateValue(DicInputs, DicLocation)

            #Avaluo certificado bonito de acuerdo a la ley
            _, df_apartamentos_neigh, PrecioByLaw = FindSimilares(DicInputs, DicLocation)
            WriteReportSimilares(DicInputs, df_apartamentos_neigh, PrecioByLaw, DicLocation)
            SendEmailSimilares(DicInputs)


            #Saves inputs and outputs in the file output.csv
            DicInAndOut = DicInputs # {**DicInputs, **DicPrecio}

            df_InAndOut = pd.DataFrame(data=DicInAndOut, index=[0])
            df_InAndOut.to_csv("outputSimilares.csv", mode='a', header=False)


#            print(PrecioByLaw, PrecioM2, flush=True)
#            print(df_apartamentos_neigh, flush=True)
            os._exit(0)



    return '0'



if __name__ == "__main__":
    port = 8080
    host = "10.0.2.4"
#    host = "0.0.0.0"

    print('Server running on host %s and port %s' % (host, port))
    serve(app, host=host, port=port)

#curl -d "foo=bar&bin=baz" http://0.0.0.0:8080
#source ~/.virtualenv/Flask/bin/activate






