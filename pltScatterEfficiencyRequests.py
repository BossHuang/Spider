__author__ = 'leihuang'
import matplotlib.pyplot as plt

requestCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000]
requestTime = [19.351085901260376, 28.448940992355347, 36.99282693862915, 45.52345585823059, 53.10605502128601, 60.19332194328308, 70.77816891670227, 78.54293489456177, 87.8220419883728, 97.62302684783936, 106.58274102210999, 114.04364705085754, 123.41260194778442, 132.18039107322693, 141.90454602241516, 149.27416896820068, 160.4277069568634, 169.59082984924316, 178.52350401878357, 188.42664694786072, 199.04585194587708, 212.35099506378174, 223.70968985557556, 232.99183988571167, 242.57015585899353, 252.05087804794312, 263.8313648700714, 273.4286148548126, 282.17728900909424, 289.69563698768616, 297.9435420036316, 307.04749298095703, 314.1798748970032, 321.80815505981445, 328.9918808937073, 336.4113938808441, 343.51220297813416, 352.18027687072754, 359.73884201049805, 368.174733877182, 374.6600480079651, 381.23181796073914, 388.9974009990692, 395.9845700263977, 403.11713886260986, 410.8182649612427, 418.00855803489685, 425.67727184295654, 432.8383150100708, 439.8818168640137, 447.5719618797302, 454.51169896125793, 465.57067489624023, 473.5506088733673, 481.74204897880554, 489.07500195503235, 496.21854400634766, 504.1419429779053, 512.9257769584656, 520.4343090057373, 527.6944448947906, 535.490061044693, 542.9827170372009, 550.8639738559723, 558.9913489818573, 567.0572319030762, 574.7224969863892, 583.2393469810486, 592.3473958969116, 601.4390249252319, 610.7755389213562, 619.236181974411, 629.2778308391571, 637.6190528869629, 645.8640739917755, 655.0839328765869, 663.723876953125, 672.7889800071716, 681.5123898983002, 689.2198350429535, 698.2810099124908, 708.5913360118866, 717.5440759658813, 726.368775844574, 735.516037940979, 745.2123119831085, 754.1927318572998, 782.3863668441772, 793.9016599655151, 803.3969969749451, 812.639683008194, 820.5426158905029, 828.2207419872284, 837.0820920467377, 845.4548740386963, 853.9831490516663, 863.007884979248, 869.7909619808197, 877.391674041748, 884.8565728664398]
avgRequestTime = [0.19351085901260376, 0.14224470496177674, 0.12330942312876383, 0.11380863964557647, 0.10621211004257203, 0.10032220323880514, 0.10111166988100324, 0.09817866861820221, 0.09758004665374756, 0.09762302684783936, 0.0968934009291909, 0.09503637254238129, 0.09493277072906495, 0.09441456505230494, 0.0946030306816101, 0.09329635560512543, 0.09436923938639023, 0.09421712769402397, 0.09395973895725451, 0.09421332347393035, 0.09478373902184623, 0.09652317957444624, 0.09726508254590242, 0.0970799332857132, 0.09702806234359741, 0.09694264540305504, 0.09771532032224867, 0.09765307673386166, 0.0973025134514118, 0.09656521232922873, 0.09611082000117148, 0.09595234155654907, 0.09520602269606157, 0.09464945737053367, 0.09399768025534494, 0.09344760941134558, 0.09284113594003626, 0.09267902022913882, 0.09224072872064053, 0.0920436834692955, 0.09138049951413782, 0.09076948046684265, 0.09046451186024865, 0.08999649318781766, 0.0895815864139133, 0.08930831846983536, 0.08893799107125465, 0.08868276496728261, 0.08833435000205526, 0.08797636337280273, 0.0877592082117118, 0.08740609595408806, 0.08784352356532835, 0.08769455719877173, 0.08758946345069192, 0.08733482177768435, 0.08705588491339433, 0.08692102465136298, 0.08693657236584162, 0.08673905150095622, 0.08650728604832633, 0.0863693646846279, 0.08618773286304776, 0.08607249591499568, 0.0859986690741319, 0.085917762409557, 0.08577947716214764, 0.08577049220309538, 0.08584744868071183, 0.08591986070360456, 0.08602472379174031, 0.08600502527422375, 0.08620244258070646, 0.0861647368766166, 0.08611520986557007, 0.0861952543258667, 0.08619790609780845, 0.08625499743681687, 0.08626739112636711, 0.08615247938036918, 0.08620753208796184, 0.0864135775624252, 0.08645109348986522, 0.08647247331483024, 0.08653129858129165, 0.08665259441664053, 0.08668881975371262, 0.08890754168683833, 0.08920243370399046, 0.08926633299721612, 0.0893010640668345, 0.08918941477070684, 0.08905599376206758, 0.08905128638795082, 0.08899524989881014, 0.08895657802621523, 0.08896988504940702, 0.08875417979396119, 0.08862542162037859, 0.08848565728664398]

plt.title("request Count with total time")
plt.xlabel("count")
plt.ylabel("total time")
plt.scatter(requestCount,requestTime)
plt.show()

plt.title("request Count with average time")
plt.xlabel("count")
plt.ylabel("average time")
plt.scatter(requestCount,avgRequestTime)
plt.show()

size = [4936,91068,153856]
time = [9.25033903122,10.4056820869,38.8785321712]
plt.title("the size of page and request time")
plt.xlabel("size")
plt.ylabel("time")
plt.scatter(size,time)
plt.show()