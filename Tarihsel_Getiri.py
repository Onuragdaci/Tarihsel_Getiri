from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
import ssl
from urllib import request
import streamlit as st
#python -m streamlit run app.py




#XBANK	#BIST BANKA
#XBLSM	#BIST BİLİŞİM
#XELKT	#BIST ELEKTRİK
#XFINK	#BIST FİNANSAL FAKTÖRİNG
#XGIDA	#BIST GIDA İÇECEK
#XGMYO	#BIST GAYRİMENKUL YATIRIM ORTAKLIĞI
#XHOLD	#BIST HOLDİNGLER
#XILTM	#BIST İLETİŞİM
#XINSA	#BIST İNŞAAT
#XKAGT	#BIST ORMAN KAGIT BASIM
#XKMYA	#BIST KİMYA PETROL PLASTİK
#XKURY	#BIST KURUMSAL YÖNETİM
#XMADN	#BIST MADENCİLİK
#XMANA	#BIST METAL ANA SANAYİİ
#XMESY	#BIST METAL EŞYA MAKİNA
#XTAST	#BIST TAŞ TOPRAK
#XTCRT	#BIST TİCARET
#XTEKS	#BIST TEKSTİL DERİ
#XTRZM	#BIST TURİZM
#XUHIZ	#BIST HİZMETLER
#XULAS	#BIST ULAŞTIRMA
#XUMAL	#BIST MALİ
#XUSIN	#BIST SİNAİ
#XUTEK	#BIST TEKNOLOJİ
#XYORT	#BIST MENKUL KIYMETLER YATIRIM ORTAKLIĞI  

Endeksler=['XU030','XU050','XU100','XUTUM','XBANK','XBLSM','XELKT','XFINK','XGIDA','XGMYO','XHOLD',	
        'XILTM','XINSA','XKAGT','XKMYA','XKURY','XMADN','XMANA',	
        'XMESY','XTAST','XTCRT','XTEKS','XTRZM','XUHIZ','XULAS',	
        'XUMAL','XUSIN','XUTEK','XYORT']

Aylar=['Yıllar','Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
Çeyrekler=['Yıllar','Q1','Q2','Q3','Q4']

tv = TvDatafeed()


def Hisse_Temel_Veriler():
    url1="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx#page-1"
    context = ssl._create_unverified_context()
    response = request.urlopen(url1, context=context)
    url1 = response.read()

    df = pd.read_html(url1,decimal=',', thousands='.')                         #Tüm Hisselerin Tablolarını Aktar
    df1=df[2]                                                                  #Tüm Hisselerin Özet Tablosu
    df2=df[6]
    df2['Sektör']=df1[['Sektör']]                                               
    return df2   


def Endeks_Analiz(Endeks):
    Alt_Endeks = tv.get_hist(symbol=Endeks,exchange='BIST',interval=Interval.in_monthly,n_bars=(1000))
    Alt_Endeks.index=pd.to_datetime(Alt_Endeks.index).to_period('M')

    Alt_Endeks = Alt_Endeks.drop(columns=['high', 'low','volume'])
    Alt_Endeks['Yüzde']=((Alt_Endeks['close']-Alt_Endeks['open'])/Alt_Endeks['open'])*100
    Alt_Endeks['Yüzde']=round(Alt_Endeks['Yüzde'],2)
    Yıllar=Alt_Endeks.index.year.drop_duplicates()

    Ocak = list(Alt_Endeks[Alt_Endeks.index.month == 1]['Yüzde'])[::-1]
    Subat = list(Alt_Endeks[Alt_Endeks.index.month == 2]['Yüzde'])[::-1]
    Mart = list(Alt_Endeks[Alt_Endeks.index.month == 3]['Yüzde'])[::-1]
    Nisan = list(Alt_Endeks[Alt_Endeks.index.month == 4]['Yüzde'])[::-1]
    Mayıs = list(Alt_Endeks[Alt_Endeks.index.month == 5]['Yüzde'])[::-1]
    Haziran = list(Alt_Endeks[Alt_Endeks.index.month == 6]['Yüzde'])[::-1]
    Temmuz = list(Alt_Endeks[Alt_Endeks.index.month == 7]['Yüzde'])[::-1]
    Agustos = list(Alt_Endeks[Alt_Endeks.index.month == 8]['Yüzde'])[::-1]
    Eylül = list(Alt_Endeks[Alt_Endeks.index.month == 9]['Yüzde'])[::-1]
    Eylül.insert(0, np.nan)
    Ekim = list(Alt_Endeks[Alt_Endeks.index.month == 10]['Yüzde'])[::-1]
    Ekim.insert(0, np.nan)
    Kasım = list(Alt_Endeks[Alt_Endeks.index.month == 11]['Yüzde'])[::-1]
    Kasım.insert(0, np.nan)
    Aralık = list(Alt_Endeks[Alt_Endeks.index.month == 12]['Yüzde'])[::-1]
    Aralık.insert(0, np.nan)

    Alt_Endeks_Ozet = pd.DataFrame(columns=Aylar)
    Alt_Endeks_Ozet['Yıllar']=Yıllar[::-1]  
    Alt_Endeks_Ozet['Ocak']=pd.Series(Ocak)
    Alt_Endeks_Ozet['Şubat']=pd.Series(Subat)
    Alt_Endeks_Ozet['Mart']=pd.Series(Mart)
    Alt_Endeks_Ozet['Nisan']=pd.Series(Nisan)
    Alt_Endeks_Ozet['Mayıs']=pd.Series(Mayıs)
    Alt_Endeks_Ozet['Haziran']=pd.Series(Haziran)
    Alt_Endeks_Ozet['Temmuz']=pd.Series(Temmuz)
    Alt_Endeks_Ozet['Ağustos']=pd.Series(Agustos)
    Alt_Endeks_Ozet['Eylül']=pd.Series(Eylül)
    Alt_Endeks_Ozet['Ekim']=pd.Series(Ekim)
    Alt_Endeks_Ozet['Kasım']=pd.Series(Kasım)
    Alt_Endeks_Ozet['Aralık']=pd.Series(Aralık)
    
    Alt_Endeks_Ozet.loc['Ortalama Değer'] = Alt_Endeks_Ozet.mean()
    Alt_Endeks_Ozet.loc['Medyan Değer'] = Alt_Endeks_Ozet.median()
    Alt_Endeks_Ozet.loc['Standart Sapma'] = Alt_Endeks_Ozet.std()


    Alt_Endeks_Ozet_2 = pd.DataFrame(columns=Çeyrekler)
    Alt_Endeks_Ozet_2['Yıllar']=Yıllar[::-1]
    Alt_Endeks_Ozet_2['Q1']=100*(100+Alt_Endeks_Ozet['Ocak'])/100
    Alt_Endeks_Ozet_2['Q1']=Alt_Endeks_Ozet_2['Q1']*(100+Alt_Endeks_Ozet['Şubat'])/100
    Alt_Endeks_Ozet_2['Q1']=Alt_Endeks_Ozet_2['Q1']*(100+Alt_Endeks_Ozet['Mart'])/100-100

    Alt_Endeks_Ozet_2['Q2']=100*(100+Alt_Endeks_Ozet['Nisan'])/100
    Alt_Endeks_Ozet_2['Q2']=Alt_Endeks_Ozet_2['Q2']*(100+Alt_Endeks_Ozet['Mayıs'])/100
    Alt_Endeks_Ozet_2['Q2']=Alt_Endeks_Ozet_2['Q2']*(100+Alt_Endeks_Ozet['Haziran'])/100-100

    Alt_Endeks_Ozet_2['Q3']=100*(100+Alt_Endeks_Ozet['Temmuz'])/100
    Alt_Endeks_Ozet_2['Q3']=Alt_Endeks_Ozet_2['Q3']*(100+Alt_Endeks_Ozet['Ağustos'])/100
    Alt_Endeks_Ozet_2['Q3']=Alt_Endeks_Ozet_2['Q3']*(100+Alt_Endeks_Ozet['Eylül'])/100-100

    Alt_Endeks_Ozet_2['Q4']=100*(100+Alt_Endeks_Ozet['Ekim'])/100
    Alt_Endeks_Ozet_2['Q4']=Alt_Endeks_Ozet_2['Q4']*(100+Alt_Endeks_Ozet['Kasım'])/100
    Alt_Endeks_Ozet_2['Q4']=Alt_Endeks_Ozet_2['Q4']*(100+Alt_Endeks_Ozet['Aralık'])/100-100

    Alt_Endeks_Ozet_2.loc['Ortalama Değer'] = Alt_Endeks_Ozet_2.mean()
    Alt_Endeks_Ozet_2.loc['Medyan Değer'] = Alt_Endeks_Ozet_2.median()
    Alt_Endeks_Ozet_2.loc['Standart Sapma'] = Alt_Endeks_Ozet_2.std()
    

    return Alt_Endeks_Ozet, Alt_Endeks_Ozet_2


st.set_page_config(
    page_title="Aylara ve Çeyreklere Göre Getiri",
    layout="wide",
    initial_sidebar_state="expanded")
with st.sidebar:
    Hisse_Ozet=Hisse_Temel_Veriler()
    Hisse_Adı=Hisse_Ozet['Kod'].tolist()
    Secim=Hisse_Adı+Endeksler
    Endeks_Girdi = st.selectbox('Seçim',Secim)

Endeks_Ozet,Endeks_Ozet_Ceyrek=Endeks_Analiz(Endeks_Girdi)

def cooling_highlight(val):
    color = '#ff3300' if val<0 else '#00ff00'
    return f'background-color: {color}'

st.title('Aylık Endeks: '+ Endeks_Girdi)

st.dataframe(Endeks_Ozet[:-3].style.applymap(cooling_highlight, 
                                        subset=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']),
                                        height=1200,
                                        use_container_width=True)


st.header('Aylık Ortalamalar')

Sapmalar=Endeks_Ozet.tail(3).drop(['Yıllar'],axis=1)
Sapmalar=Sapmalar.head(2)
Ortalama=Sapmalar.head(1)
st.dataframe(Sapmalar.style.applymap(cooling_highlight, 
                                        subset=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']),
                                        use_container_width=True)

st.title('Çeyreklik Endeks: '+ Endeks_Girdi)
st.dataframe(Endeks_Ozet_Ceyrek[:-3].style.applymap(cooling_highlight, 
                                        subset=['Q1','Q2','Q3','Q4']),
                                        height=1200,
                                        use_container_width=True)

st.header('Çeyreklik Ortalamalar')

Sapmalar_2=Endeks_Ozet_Ceyrek.tail(3).drop(['Yıllar'],axis=1)
Sapmalar_2=Sapmalar_2.head(2)
Ortalama_2=Sapmalar_2.head(1)
st.dataframe(Sapmalar_2.style.applymap(cooling_highlight, 
                                        subset=['Q1','Q2','Q3','Q4']),
                                        use_container_width=True)
    
 
