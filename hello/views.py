from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import pandas as pd
import numpy as np
import pickle
def home(request):
    hello = request.GET['hello']
    return JsonResponse({'hello':hello})

def KBO(request):    
    try:
        home_pitcher = request.GET['home_pitcher']
        home_batter1 = request.GET['home_hitter1']
        home_batter2 = request.GET['home_hitter2']
        home_batter3 = request.GET['home_hitter3']
        home_batter4 = request.GET['home_hitter4']
        home_batter5 = request.GET['home_hitter5']
        home_batter6 = request.GET['home_hitter6']
        home_batter7 = request.GET['home_hitter7']
        home_batter8 = request.GET['home_hitter8']
        home_batter9 = request.GET['home_hitter9']
        away_pitcher = request.GET['away_pitcher']
        away_batter1 = request.GET['away_hitter1']
        away_batter2 = request.GET['away_hitter2']
        away_batter3 = request.GET['away_hitter3']
        away_batter4 = request.GET['away_hitter4']
        away_batter5 = request.GET['away_hitter5']
        away_batter6 = request.GET['away_hitter6']
        away_batter7 = request.GET['away_hitter7']
        away_batter8 = request.GET['away_hitter8']
        away_batter9 = request.GET['away_hitter9']
        array = np.array([
        away_pitcher,
        away_batter1, 
        away_batter2, 
        away_batter3, 
        away_batter4, 
        away_batter5, 
        away_batter6, 
        away_batter7, 
        away_batter8, 
        away_batter9,
        home_pitcher,
        home_batter1, 
        home_batter2, 
        home_batter3, 
        home_batter4, 
        home_batter5, 
        home_batter6, 
        home_batter7, 
        home_batter8, 
        home_batter9])
        df = pd.DataFrame(array)
        from sklearn.preprocessing import StandardScaler 
        df = StandardScaler().fit_transform(df) 
        with open('KBOpredictor.pickle','rb') as f:
            KBOpredictor= pickle.load(f)
        result = {'result':str(KBOpredictor.predict(df.T))}
        return JsonResponse(result)
    except:
        return JsonResponse({'result':'ERROR'})

def MLB(request):
    try:
        home_OBP = request.GET['home_OBP']
        home_SLG = request.GET['home_SLG']
        home_WHIP = request.GET['home_WHIP']
        home_ERA = request.GET['home_ERA']
        home_WAR_b = request.GET['home_WAR_b']
        home_WAR_p = request.GET['home_WAR_p']
        away_OBP = request.GET['away_OBP']
        away_SLG = request.GET['away_SLG']
        away_WHIP = request.GET['away_WHIP']
        away_ERA = request.GET['away_ERA']
        away_WAR_b = request.GET['away_WAR_b']
        away_WAR_p = request.GET['away_WAR_p']
        array = np.array([
            home_OBP,	
            home_SLG,	
            home_WAR_b,	
            away_OBP,	
            away_SLG,	
            away_WAR_b,	
            home_WHIP,	
            home_ERA,	
            home_WAR_p,	
            away_WHIP,	
            away_ERA,	
            away_WAR_p])
        df=pd.DataFrame(array)
        from sklearn.preprocessing import StandardScaler 
        df = StandardScaler().fit_transform(df) 
        with open('MLBpredictor.pickle','rb') as f:
            MLBpredictor= pickle.load(f)
        result = {'result':str(MLBpredictor.predict(df.T))}
        return JsonResponse(result)
    except:
        return JsonResponse({'result':'ERROR'})

def NBA(request):
    try:
        home_BPM = request.GET['home_BPM']
        away_BPM = request.GET['away_BPM']
        home_VORP = request.GET['home_VORP']
        away_VORP = request.GET['away_VORP']
        home_WS = request.GET['home_WS']
        away_WS = request.GET['away_WS']
    
        array = np.array([
            home_BPM,
            away_BPM,
            home_VORP,
            away_VORP,
            home_WS,
            away_WS])
        df=pd.DataFrame(array)
        
        from sklearn.preprocessing import StandardScaler 
        df = StandardScaler().fit_transform(df) 
    
        with open('NBApredictor.pickle','rb') as f:
            NBApredictor= pickle.load(f)
        prediction = str(NBApredictor.predict(df.T))
        
        result = {'result':prediction}
        
        return JsonResponse(result)
    except:
        return JsonResponse({'result':'ERROR'})

def house(request):
    return(JsonResponse({'Hello':'Hello django'}))

