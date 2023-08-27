from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
import streamlit as st





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

Hisseler=['A1CAP','ACSEL','ADEL','ADESE','AEFES','AFYON','AGESA','AGHOL','AGYO','AHGAZ','AKBNK','AKCNS','AKENR','AKFGY','AKFYE','AKGRT','AKMGY',
        'AKSA','AKSEN','AKSGY','AKSUE','AKYHO','ALARK','ALBRK','ALCAR','ALCTL','ALFAS','ALGYO','ALKA','ALKIM','ALMAD','ANELE','ANGEN','ANHYT','ANSGR',
        'ARASE','ARCLK','ARDYZ','ARENA','ARSAN','ARZUM','ASELS','ASGYO','ASTOR','ASUZU','ATAGY','ATAKP','ATATP','ATEKS','ATLAS','ATSYH','AVGYO','AVHOL',
        'AVOD','AVTUR','AYCES','AYDEM','AYEN','AYES','AYGAZ','AZTEK','BAGFS','BAKAB','BALAT','BANVT','BARMA','BASCM','BASGZ','BAYRK','BERA','BEYAZ','BFREN',
        'BIENY','BIGCH','BIMAS','BIOEN','BIZIM','BJKAS','BLCYT','BMSCH','BMSTL','BNTAS','BOBET','BOSSA','BRISA','BRKO','BRKSN','BRKVY','BRLSM','BRMEN','BRSAN',
        'BRYAT','BSOKE','BTCIM','BUCIM','BURCE','BURVA','BVSAN','BYDNR','CANTE','CASA','CCOLA','CELHA','CEMAS','CEMTS','CEOEM','CIMSA','CLEBI','CMBTN','CMENT','CONSE',
        'COSMO','CRDFA','CRFSA','CUSAN','CVKMD','CWENE','DAGHL','DAGI','DAPGM','DARDL','DENGE','DERHL','DERIM','DESA','DESPC','DEVA','DGATE','DGGYO','DGNMO','DIRIT','DITAS',
        'DMSAS','DNISI','DOAS','DOBUR','DOCO','DOGUB','DOHOL','DOKTA','DURDO','DYOBY','DZGYO','ECILC','ECZYT','EDATA','EDIP','EGEEN','EGEPO','EGGUB','EGPRO','EGSER','EKGYO',
        'EKIZ','EKSUN','ELITE','EMKEL','EMNIS','ENERY','ENJSA','ENKAI','ENSRI','EPLAS','ERBOS','ERCB','EREGL','ERSU','ESCAR','ESCOM','ESEN','ETILR','ETYAT','EUHOL','EUKYO',
        'EUPWR','EUREN','EUYO','EYGYO','FADE','FENER','FLAP','FMIZP','FONET','FORMT','FORTE','FRIGO','FROTO','FZLGY','GARAN','GARFA','GEDIK','GEDZA','GENIL','GENTS','GEREL',
        'GESAN','GLBMD','GLCVY','GLRYH','GLYHO','GMTAS','GOKNR','GOLTS','GOODY','GOZDE','GRNYO','GRSEL','GRTRK','GSDDE','GSDHO','GSRAY','GUBRF','GWIND','GZNMI','HALKB','HATEK',
        'HDFGS','HEDEF','HEKTS','HKTM','HLGYO','HTTBT','HUBVC','HUNER','HURGZ','ICBCT','ICUGS','IDEAS','IDGYO','IEYHO','IHAAS','IHEVA','IHGZT','IHLAS','IHLGM','IHYAY','IMASM',
        'INDES','INFO','INGRM','INTEM','INVEO','INVES','IPEKE','ISATR','ISBIR','ISBTR','ISCTR','ISDMR','ISFIN','ISGSY','ISGYO','ISKPL','ISKUR','ISMEN','ISSEN','ISYAT','ITTFH',
        'IZENR','IZFAS','IZINV','IZMDC','JANTS','KAPLM','KAREL','KARSN','KARTN','KARYE','KATMR','KAYSE','KCAER','KCHOL','KENT','KERVN','KERVT','KFEIN','KGYO','KIMMR','KLGYO',
        'KLKIM','KLMSN','KLNMA','KLRHO','KLSER','KLSYN','KMPUR','KNFRT','KONKA','KONTR','KONYA','KOPOL','KORDS','KOZAA','KOZAL','KRDMA','KRDMB','KRDMD','KRGYO','KRONT','KRPLS',
        'KRSTL','KRTEK','KRVGD','KSTUR','KTLEV','KTSKR','KUTPO','KUVVA','KUYAS','KZBGY','KZGYO','LIDER','LIDFA','LINK','LKMNH','LOGO','LUKSK','MAALT','MACKO','MAGEN','MAKIM',
        'MAKTK','MANAS','MARKA','MARTI','MAVI','MEDTR','MEGAP','MEPET','MERCN','MERIT','MERKO','METRO','METUR','MGROS','MIATK','MIPAZ','MMCAS','MNDRS','MNDTR','MOBTL','MPARK',
        'MRGYO','MRSHL','MSGYO','MTRKS','MTRYO','MZHLD','NATEN','NETAS','NIBAS','NTGAZ','NTHOL','NUGYO','NUHCM','OBASE','ODAS','OFSYM','ONCSM','ORCAY','ORGE','ORMA','OSMEN',
        'OSTIM','OTKAR','OTTO','OYAKC','OYAYO','OYLUM','OYYAT','OZGYO','OZKGY','OZRDN','OZSUB','PAGYO','PAMEL','PAPIL','PARSN','PASEU','PCILT','PEGYO','PEKGY','PENGD','PENTA',
        'PETKM','PETUN','PGSUS','PINSU','PKART','PKENT','PLTUR','PNLSN','PNSUT','POLHO','POLTK','PRDGS','PRKAB','PRKME','PRZMA','PSDTC','PSGYO','QNBFB','QNBFL','QUAGR','RALYH',
        'RAYSG','RNPOL','RODRG','ROYAL','RTALB','RUBNS','RYGYO','RYSAS','SAFKR','SAHOL','SAMAT','SANEL','SANFM','SANKO','SARKY','SASA','SAYAS','SDTTR','SEGYO','SEKFK',
        'SEKUR','SELEC','SELGD','SELVA','SEYKM','SILVR','SISE','SKBNK','SKTAS','SMART','SMRTG','SNGYO','SNICA','SNKRN','SNPAM','SODSN','SOKE','SOKM','SONME','SRVGY','SUMAS',
        'SUNTK','SUWEN','TATEN','TATGD','TAVHL','TBORG','TCELL','TDGYO','TEKTU','TERA','TETMT','TEZOL','TGSAS','THYAO','TKFEN','TKNSA','TLMAN','TMPOL','TMSN','TNZTP','TOASO',
        'TRCAS','TRGYO','TRILC','TSGYO','TSKB','TSPOR','TTKOM','TTRAK','TUCLK','TUKAS','TUPRS','TUREX','TURGG','TURSG','UFUK','ULAS','ULKER','ULUFA','ULUSE','ULUUN','UMPAS',
        'UNLU','USAK','UZERB','VAKBN','VAKFN','VAKKO','VANGD','VBTYZ','VERTU','VERUS','VESBE','VESTL','VKFYO','VKGYO','VKING','YAPRK','YATAS','YAYLA','YBTAS','YEOTK','YESIL',
        'YGGYO','YGYO','YKBNK','YKSLN','YONGA','YUNSA','YYAPI','YYLGD','ZEDUR','ZOREN','ZRGYO',]
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
    
 
