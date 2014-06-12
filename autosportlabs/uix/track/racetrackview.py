import kivy
kivy.require('1.8.0')
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.app import Builder
from kivy.metrics import dp
from kivy.graphics import Color, Line
from autosportlabs.racecapture.geo.geopoint import GeoPoint
from utils import *

Builder.load_file('autosportlabs/uix/track/racetrackview.kv')
        
class RaceTrackView(BoxLayout):
    trackmap = None
    def __init__(self, **kwargs):
        super(RaceTrackView, self).__init__(**kwargs)

    def loadTracks(self):
        self.initMap()
                
    def initMap(self):
        trackPoints = [
            [47.254699, -123.190424]
            ,[47.254690, -123.188863]
            ,[47.254675, -123.186508]
            ,[47.254673, -123.186264]
            ,[47.254674, -123.186095]
            ,[47.254676, -123.186037]
            ,[47.254681, -123.185989]
            ,[47.254691, -123.185938]
            ,[47.254714, -123.185835]
            ,[47.254755, -123.185705]
            ,[47.254816, -123.185569]
            ,[47.254909, -123.185376]
            ,[47.255047, -123.185120]
            ,[47.255270, -123.184767]
            ,[47.255344, -123.184673]
            ,[47.255422, -123.184604]
            ,[47.255457, -123.184573]
            ,[47.255495, -123.184547]
            ,[47.255529, -123.184533]
            ,[47.255564, -123.184527]
            ,[47.255601, -123.184529]
            ,[47.255635, -123.184534]
            ,[47.255669, -123.184543]
            ,[47.255708, -123.184558]
            ,[47.255770, -123.184594]
            ,[47.255836, -123.184645]
            ,[47.255929, -123.184723]
            ,[47.256008, -123.184789]
            ,[47.256066, -123.184832]
            ,[47.256100, -123.184853]
            ,[47.256140, -123.184871]
            ,[47.256180, -123.184881]
            ,[47.256231, -123.184887]
            ,[47.256279, -123.184879]
            ,[47.256326, -123.184867]
            ,[47.256368, -123.184853]
            ,[47.256418, -123.184834]
            ,[47.256477, -123.184801]
            ,[47.256700, -123.184671]
            ,[47.256883, -123.184568]
            ,[47.256965, -123.184525]
            ,[47.257016, -123.184499]
            ,[47.257052, -123.184486]
            ,[47.257093, -123.184476]
            ,[47.257130, -123.184478]
            ,[47.257169, -123.184488]
            ,[47.257203, -123.184502]
            ,[47.257241, -123.184522]
            ,[47.257273, -123.184543]
            ,[47.257448, -123.184680]
            ,[47.257659, -123.184881]
            ,[47.257801, -123.185045]
            ,[47.257848, -123.185108]
            ,[47.257880, -123.185164]
            ,[47.257908, -123.185214]
            ,[47.257931, -123.185265]
            ,[47.257950, -123.185319]
            ,[47.257965, -123.185382]
            ,[47.257984, -123.185467]
            ,[47.258000, -123.185579]
            ,[47.258009, -123.185707]
            ,[47.258017, -123.185931]
            ,[47.258019, -123.186058]
            ,[47.258015, -123.186236]
            ,[47.258001, -123.186414]
            ,[47.257985, -123.186587]
            ,[47.257971, -123.186792]
            ,[47.257958, -123.186987]
            ,[47.257954, -123.187101]
            ,[47.257954, -123.187242]
            ,[47.257958, -123.187396]
            ,[47.257975, -123.187631]
            ,[47.258006, -123.187879]
            ,[47.258046, -123.188179]
            ,[47.258068, -123.188362]
            ,[47.258080, -123.188485]
            ,[47.258088, -123.188619]
            ,[47.258091, -123.188729]
            ,[47.258091, -123.188923]
            ,[47.258085, -123.189417]
            ,[47.258076, -123.189860]
            ,[47.258067, -123.190011]
            ,[47.258046, -123.190212]
            ,[47.258032, -123.190334]
            ,[47.258004, -123.190489]
            ,[47.257980, -123.190586]
            ,[47.257956, -123.190671]
            ,[47.257923, -123.190757]
            ,[47.257893, -123.190820]
            ,[47.257861, -123.190868]
            ,[47.257818, -123.190920]
            ,[47.257773, -123.190963]
            ,[47.257722, -123.191008]
            ,[47.257670, -123.191044]
            ,[47.257613, -123.191071]
            ,[47.257565, -123.191092]
            ,[47.257497, -123.191119]
            ,[47.257449, -123.191131]
            ,[47.257390, -123.191135]
            ,[47.257307, -123.191127]
            ,[47.257240, -123.191107]
            ,[47.257171, -123.191075]
            ,[47.257099, -123.191029]
            ,[47.257038, -123.190978]
            ,[47.256964, -123.190902]
            ,[47.256888, -123.190800]
            ,[47.256841, -123.190718]
            ,[47.256792, -123.190600]
            ,[47.256748, -123.190452]
            ,[47.256730, -123.190361]
            ,[47.256720, -123.190263]
            ,[47.256716, -123.190169]
            ,[47.256719, -123.190074]
            ,[47.256728, -123.189972]
            ,[47.256743, -123.189878]
            ,[47.256762, -123.189758]
            ,[47.256786, -123.189629]
            ,[47.256811, -123.189492]
            ,[47.256853, -123.189330]
            ,[47.256900, -123.189170]
            ,[47.256957, -123.188997]
            ,[47.257022, -123.188824]
            ,[47.257077, -123.188673]
            ,[47.257119, -123.188514]
            ,[47.257149, -123.188392]
            ,[47.257183, -123.188248]
            ,[47.257208, -123.188116]
            ,[47.257226, -123.187998]
            ,[47.257239, -123.187893]
            ,[47.257248, -123.187766]
            ,[47.257252, -123.187672]
            ,[47.257249, -123.187572]
            ,[47.257241, -123.187470]
            ,[47.257228, -123.187365]
            ,[47.257207, -123.187187]
            ,[47.257174, -123.186980]
            ,[47.257148, -123.186798]
            ,[47.257121, -123.186630]
            ,[47.257106, -123.186547]
            ,[47.257092, -123.186489]
            ,[47.257072, -123.186434]
            ,[47.257051, -123.186386]
            ,[47.257032, -123.186358]
            ,[47.257013, -123.186331]
            ,[47.256987, -123.186302]
            ,[47.256961, -123.186275]
            ,[47.256930, -123.186247]
            ,[47.256901, -123.186233]
            ,[47.256862, -123.186217]
            ,[47.256818, -123.186201]
            ,[47.256772, -123.186198]
            ,[47.256708, -123.186202]
            ,[47.256657, -123.186209]
            ,[47.256605, -123.186224]
            ,[47.256549, -123.186247]
            ,[47.256480, -123.186272]
            ,[47.256426, -123.186295]
            ,[47.256368, -123.186327]
            ,[47.256313, -123.186371]
            ,[47.256278, -123.186408]
            ,[47.256244, -123.186457]
            ,[47.256216, -123.186503]
            ,[47.256193, -123.186552]
            ,[47.256170, -123.186607]
            ,[47.256147, -123.186696]
            ,[47.256118, -123.186809]
            ,[47.256084, -123.186956]
            ,[47.255989, -123.187362]
            ,[47.255861, -123.187928]
            ,[47.255790, -123.188248]
            ,[47.255766, -123.188367]
            ,[47.255751, -123.188471]
            ,[47.255738, -123.188560]
            ,[47.255729, -123.188650]
            ,[47.255728, -123.188732]
            ,[47.255731, -123.188811]
            ,[47.255736, -123.188887]
            ,[47.255751, -123.188968]
            ,[47.255774, -123.189059]
            ,[47.255823, -123.189212]
            ,[47.255959, -123.189605]
            ,[47.256167, -123.190207]
            ,[47.256371, -123.190802]
            ,[47.256462, -123.191065]
            ,[47.256553, -123.191288]
            ,[47.256630, -123.191457]
            ,[47.256702, -123.191599]
            ,[47.256764, -123.191704]
            ,[47.256837, -123.191796]
            ,[47.256911, -123.191867]
            ,[47.257066, -123.191992]
            ,[47.257255, -123.192129]
            ,[47.257366, -123.192225]
            ,[47.257441, -123.192302]
            ,[47.257528, -123.192413]
            ,[47.257596, -123.192512]
            ,[47.257654, -123.192605]
            ,[47.257700, -123.192681]
            ,[47.257741, -123.192768]
            ,[47.257772, -123.192841]
            ,[47.257797, -123.192920]
            ,[47.257818, -123.192999]
            ,[47.257839, -123.193078]
            ,[47.257854, -123.193159]
            ,[47.257863, -123.193240]
            ,[47.257866, -123.193321]
            ,[47.257863, -123.193392]
            ,[47.257853, -123.193470]
            ,[47.257833, -123.193533]
            ,[47.257812, -123.193576]
            ,[47.257789, -123.193609]
            ,[47.257764, -123.193632]
            ,[47.257734, -123.193651]
            ,[47.257701, -123.193659]
            ,[47.257668, -123.193663]
            ,[47.257630, -123.193660]
            ,[47.257589, -123.193647]
            ,[47.257508, -123.193600]
            ,[47.257345, -123.193497]
            ,[47.257072, -123.193313]
            ,[47.256812, -123.193143]
            ,[47.256556, -123.192978]
            ,[47.256418, -123.192889]
            ,[47.256374, -123.192858]
            ,[47.256324, -123.192829]
            ,[47.256290, -123.192809]
            ,[47.256261, -123.192797]
            ,[47.256231, -123.192791]
            ,[47.256201, -123.192790]
            ,[47.256160, -123.192795]
            ,[47.256123, -123.192806]
            ,[47.256086, -123.192826]
            ,[47.256053, -123.192860]
            ,[47.256024, -123.192904]
            ,[47.255993, -123.192966]
            ,[47.255962, -123.193042]
            ,[47.255927, -123.193149]
            ,[47.255904, -123.193262]
            ,[47.255886, -123.193360]
            ,[47.255872, -123.193491]
            ,[47.255865, -123.193631]
            ,[47.255864, -123.193839]
            ,[47.255865, -123.194182]
            ,[47.255866, -123.194771]
            ,[47.255866, -123.195400]
            ,[47.255867, -123.195916]
            ,[47.255870, -123.196523]
            ,[47.255870, -123.197081]
            ,[47.255875, -123.197642]
            ,[47.255876, -123.197806]
            ,[47.255877, -123.197912]
            ,[47.255877, -123.197972]
            ,[47.255876, -123.198022]
            ,[47.255873, -123.198051]
            ,[47.255866, -123.198089]
            ,[47.255856, -123.198123]
            ,[47.255844, -123.198156]
            ,[47.255828, -123.198178]
            ,[47.255805, -123.198201]
            ,[47.255791, -123.198213]
            ,[47.255774, -123.198221]
            ,[47.255754, -123.198221]
            ,[47.255732, -123.198221]
            ,[47.255711, -123.198216]
            ,[47.255689, -123.198201]
            ,[47.255615, -123.198148]
            ,[47.255531, -123.198071]
            ,[47.255498, -123.198040]
            ,[47.255478, -123.198019]
            ,[47.255452, -123.197999]
            ,[47.255421, -123.197976]
            ,[47.255396, -123.197964]
            ,[47.255369, -123.197957]
            ,[47.255340, -123.197957]
            ,[47.255307, -123.197961]
            ,[47.255271, -123.197973]
            ,[47.255241, -123.197992]
            ,[47.255214, -123.198015]
            ,[47.255185, -123.198047]
            ,[47.255161, -123.198083]
            ,[47.255139, -123.198122]
            ,[47.255119, -123.198166]
            ,[47.255101, -123.198225]
            ,[47.255088, -123.198290]
            ,[47.255080, -123.198358]
            ,[47.255074, -123.198451]
            ,[47.255070, -123.198573]
            ,[47.255066, -123.198628]
            ,[47.255058, -123.198679]
            ,[47.255047, -123.198730]
            ,[47.255033, -123.198775]
            ,[47.255014, -123.198815]
            ,[47.254995, -123.198848]
            ,[47.254972, -123.198885]
            ,[47.254946, -123.198916]
            ,[47.254918, -123.198939]
            ,[47.254886, -123.198958]
            ,[47.254838, -123.198971]
            ,[47.254788, -123.198983]
            ,[47.254735, -123.198984]
            ,[47.254683, -123.198979]
            ,[47.254636, -123.198967]
            ,[47.254593, -123.198941]
            ,[47.254546, -123.198900]
            ,[47.254511, -123.198850]
            ,[47.254481, -123.198795]
            ,[47.254455, -123.198727]
            ,[47.254437, -123.198652]
            ,[47.254424, -123.198551]
            ,[47.254419, -123.198455]
            ,[47.254425, -123.198374]
            ,[47.254438, -123.198290]
            ,[47.254458, -123.198215]
            ,[47.254486, -123.198137]
            ,[47.254523, -123.198058]
            ,[47.254559, -123.197991]
            ,[47.254590, -123.197940]
            ,[47.254625, -123.197879]
            ,[47.254652, -123.197831]
            ,[47.254673, -123.197787]
            ,[47.254690, -123.197739]
            ,[47.254705, -123.197684]
            ,[47.254718, -123.197629]
            ,[47.254725, -123.197567]
            ,[47.254731, -123.197512]
            ,[47.254735, -123.197452]
            ,[47.254739, -123.197387]
            ,[47.254740, -123.197320]
            ,[47.254740, -123.197244]
            ,[47.254740, -123.196778]
            ,[47.254740, -123.196383]
            ,[47.254736, -123.195814]
            ,[47.254732, -123.195437]
            ,[47.254730, -123.194873]
            ,[47.254722, -123.193770]
            ,[47.254714, -123.192479]
            ,[47.254713, -123.192473]
            ,[47.254699, -123.190424]
            ]
        points = []
        for trackPoint in trackPoints:
            gp = GeoPoint()
            gp.latitude = trackPoint[0]
            gp.longitude = trackPoint[1]
            points.append(gp)
        
        trackmap = kvFind(self, 'rcid', 'trackmap1')  

        trackmap.setTrackPoints(points)    
