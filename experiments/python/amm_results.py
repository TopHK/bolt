#!/usr/bin/env python

from __future__ import print_function

import numpy as np
import pprint

microbench_output = \
"""
ncodebooks = 4
amm multisplit N, D, M, ncodebooks:  10000, 512,  10,  4     (5x5): 0.04 (2504000000/s), 0.035 (2861714285/s), 0.035 (2861714285/s), 0.035 (2861714285/s), 0.035 (2861714285/s),
amm multisplit N, D, M, ncodebooks:  10000, 512, 100,  4     (5x5): 0.228 (4392982456/s), 0.222 (4511711711/s), 0.209 (4792344497/s), 0.216 (4637037037/s), 0.217 (4615668202/s),
amm multisplit N, D, M, ncodebooks:  57593,  24,   3,  4     (5x5): 0.176 (981818181/s), 0.165 (1047272727/s), 0.168 (1028571428/s), 0.162 (1066666666/s), 0.161 (1073291925/s),
amm multisplit N, D, M, ncodebooks: 115193,  24,   3,  4     (5x5): 0.423 (817021276/s), 0.467 (740042826/s), 0.449 (769710467/s), 0.45 (768000000/s), 0.452 (764601769/s),
amm multisplit N, D, M, ncodebooks: 230393,  24,   3,  4     (5x5): 1.031 (670417070/s), 1.005 (687761194/s), 1.004 (688446215/s), 1.006 (687077534/s), 0.976 (708196721/s),
amm multisplit N, D, M, ncodebooks:  49284,  27,   2,  4     (5x5): 0.132 (747151515/s), 0.131 (752854961/s), 0.145 (680165517/s), 0.144 (684888888/s), 0.126 (782730158/s),
ncodebooks = 8
amm multisplit N, D, M, ncodebooks:  10000, 512,  10,  8     (5x5): 0.064 (1565000000/s), 0.065 (1540923076/s), 0.065 (1540923076/s), 0.064 (1565000000/s), 0.064 (1565000000/s),
amm multisplit N, D, M, ncodebooks:  10000, 512, 100,  8     (5x5): 0.302 (3316556291/s), 0.339 (2954572271/s), 0.318 (3149685534/s), 0.312 (3210256410/s), 0.311 (3220578778/s),
amm multisplit N, D, M, ncodebooks:  57593,  24,   3,  8     (5x5): 0.341 (506744868/s), 0.334 (517365269/s), 0.329 (525227963/s), 0.325 (531692307/s), 0.34 (508235294/s),
amm multisplit N, D, M, ncodebooks: 115193,  24,   3,  8     (5x5): 0.956 (361506276/s), 0.974 (354825462/s), 0.941 (367268862/s), 0.939 (368051118/s), 0.937 (368836712/s),
amm multisplit N, D, M, ncodebooks: 230393,  24,   3,  8     (5x5): 1.943 (355738548/s), 1.996 (346292585/s), 1.899 (363981042/s), 1.917 (360563380/s), 1.906 (362644281/s),
amm multisplit N, D, M, ncodebooks:  49284,  27,   2,  8     (5x5): 0.247 (399287449/s), 0.247 (399287449/s), 0.246 (400910569/s), 0.246 (400910569/s), 0.247 (399287449/s),
ncodebooks = 16
amm multisplit N, D, M, ncodebooks:  10000, 512,  10, 16     (5x5): 0.147 (681360544/s), 0.129 (776434108/s), 0.127 (788661417/s), 0.125 (801280000/s), 0.124 (807741935/s),
amm multisplit N, D, M, ncodebooks:  10000, 512, 100, 16     (5x5): 0.556 (1801438848/s), 0.589 (1700509337/s), 0.589 (1700509337/s), 0.562 (1782206405/s), 0.557 (1798204667/s),
amm multisplit N, D, M, ncodebooks:  57593,  24,   3, 16     (5x5): 0.642 (269158878/s), 0.648 (266666666/s), 0.632 (273417721/s), 0.627 (275598086/s), 0.629 (274721780/s),
amm multisplit N, D, M, ncodebooks: 115193,  24,   3, 16     (5x5): 1.753 (197147746/s), 1.732 (199538106/s), 1.65 (209454545/s), 1.648 (209708737/s), 1.652 (209200968/s),
amm multisplit N, D, M, ncodebooks: 230393,  24,   3, 16     (5x5): 3.811 (181369719/s), 3.823 (180800418/s), 3.774 (183147853/s), 3.748 (184418356/s), 3.698 (186911844/s),
amm multisplit N, D, M, ncodebooks:  49284,  27,   2, 16     (5x5): 0.516 (191131782/s), 0.552 (178666666/s), 0.512 (192625000/s), 0.511 (193001956/s), 0.52 (189661538/s),
ncodebooks = 32
amm multisplit N, D, M, ncodebooks:  10000, 512,  10, 32     (5x5): 0.371 (269973045/s), 0.278 (360287769/s), 0.284 (352676056/s), 0.277 (361588447/s), 0.273 (366886446/s),
amm multisplit N, D, M, ncodebooks:  10000, 512, 100, 32     (5x5): 1.091 (918056828/s), 1.063 (942238946/s), 1.115 (898295964/s), 1.099 (911373976/s), 1.121 (893487957/s),
amm multisplit N, D, M, ncodebooks:  57593,  24,   3, 32     (5x5): 1.434 (120502092/s), 1.314 (131506849/s), 1.312 (131707317/s), 1.372 (125947521/s), 1.371 (126039387/s),
amm multisplit N, D, M, ncodebooks: 115193,  24,   3, 32     (5x5): 3.374 (102430349/s), 3.248 (106403940/s), 3.242 (106600863/s), 3.24 (106666666/s), 3.256 (106142506/s),
amm multisplit N, D, M, ncodebooks: 230393,  24,   3, 32     (5x5): 7.929 (87173666/s), 7.415 (93216453/s), 7.442 (92878258/s), 7.622 (90684859/s), 7.405 (93342336/s),
amm multisplit N, D, M, ncodebooks:  49284,  27,   2, 32     (5x5): 1.018 (96880157/s), 1.017 (96975417/s), 1.05 (93927619/s), 1.018 (96880157/s), 1.025 (96218536/s),
ncodebooks = 64
amm multisplit N, D, M, ncodebooks:  10000, 512,  10, 64     (5x5): 0.735 (136272108/s), 0.707 (141669024/s), 0.704 (142272727/s), 0.669 (149715994/s), 0.656 (152682926/s),
amm multisplit N, D, M, ncodebooks:  10000, 512, 100, 64     (5x5): 2.118 (472898961/s), 2.247 (445749888/s), 2.22 (451171171/s), 2.085 (480383693/s), 2.006 (499302093/s),
amm multisplit N, D, M, ncodebooks:  57593,  24,   3, 64     (5x5): 2.646 (65306122/s), 2.788 (61979913/s), 2.6 (66461538/s), 2.599 (66487110/s), 2.595 (66589595/s),
amm multisplit N, D, M, ncodebooks: 115193,  24,   3, 64     (5x5): 6.642 (52032520/s), 6.635 (52087415/s), 6.59 (52443095/s), 6.589 (52451054/s), 6.611 (52276508/s),
amm multisplit N, D, M, ncodebooks: 230393,  24,   3, 64     (5x5): 14.724 (46943765/s), 14.579 (47410659/s), 14.453 (47823981/s), 14.639 (47216339/s), 14.647 (47190550/s),
amm multisplit N, D, M, ncodebooks:  49284,  27,   2, 64     (5x5): 2.048 (48156250/s), 2.036 (48440078/s), 2.036 (48440078/s), 2.115 (46630732/s), 2.145 (45978554/s),
ncodebooks = 4
amm bolt N, D, M, ncodebooks:  10000, 512,  10,  4   (5x5): 7.505 (42638241/s), 7.498 (42678047/s), 7.497 (42683740/s), 7.5 (42666666/s), 7.512 (42598509/s),
amm bolt N, D, M, ncodebooks:  10000, 512, 100,  4   (5x5): 7.508 (170484816/s), 7.5 (170666666/s), 7.488 (170940170/s), 7.508 (170484816/s), 7.686 (166536559/s),
amm bolt N, D, M, ncodebooks:  57593,  24,   3,  4   (5x5): 2.047 (900330239/s), 2.168 (850081180/s), 2.034 (906084562/s), 2.036 (905194499/s), 2.035 (905639312/s),
amm bolt N, D, M, ncodebooks: 115193,  24,   3,  4   (5x5): 4.265 (864285111/s), 4.099 (899286655/s), 4.078 (903917606/s), 4.09 (901265525/s), 4.09 (901265525/s),
amm bolt N, D, M, ncodebooks: 230393,  24,   3,  4   (5x5): 8.285 (889870368/s), 8.131 (906724388/s), 8.151 (904499570/s), 8.402 (877478695/s), 8.172 (902175232/s),
amm bolt N, D, M, ncodebooks:  49284,  27,   2,  4   (5x5): 1.931 (816720870/s), 1.932 (816298136/s), 1.93 (817144041/s), 1.926 (818841121/s), 1.933 (815875840/s),
ncodebooks = 8
amm bolt N, D, M, ncodebooks:  10000, 512,  10,  8   (5x5): 7.239 (44205000/s), 7.231 (44253906/s), 7.236 (44223327/s), 7.298 (43847629/s), 7.268 (44028618/s),
amm bolt N, D, M, ncodebooks:  10000, 512, 100,  8   (5x5): 7.829 (163494699/s), 7.769 (164757369/s), 7.698 (166276955/s), 7.715 (165910563/s), 7.799 (164123605/s),
amm bolt N, D, M, ncodebooks:  57593,  24,   3,  8   (5x5): 2.465 (747657606/s), 2.637 (698891164/s), 2.626 (701818735/s), 2.464 (747961038/s), 2.481 (742835953/s),
amm bolt N, D, M, ncodebooks: 115193,  24,   3,  8   (5x5): 5.411 (681237479/s), 5.132 (718272798/s), 5.13 (718552826/s), 5.135 (717853164/s), 5.133 (718132865/s),
amm bolt N, D, M, ncodebooks: 230393,  24,   3,  8   (5x5): 9.865 (747346781/s), 9.859 (747801602/s), 9.858 (747877459/s), 9.858 (747877459/s), 9.909 (744028257/s),
amm bolt N, D, M, ncodebooks:  49284,  27,   2,  8   (5x5): 2.467 (639273611/s), 2.468 (639014586/s), 2.463 (640311814/s), 2.466 (639532846/s), 2.469 (638755771/s),
ncodebooks = 16
amm bolt N, D, M, ncodebooks:  10000, 512,  10, 16   (5x5): 6.384 (50125313/s), 6.236 (51314945/s), 6.382 (50141021/s), 6.523 (49057182/s), 6.427 (49789948/s),
amm bolt N, D, M, ncodebooks:  10000, 512, 100, 16   (5x5): 7.073 (180969885/s), 6.721 (190447850/s), 6.816 (187793427/s), 6.82 (187683284/s), 6.671 (191875281/s),
amm bolt N, D, M, ncodebooks:  57593,  24,   3, 16   (5x5): 4.38 (420770776/s), 4.377 (421059172/s), 4.377 (421059172/s), 4.378 (420962996/s), 4.378 (420962996/s),
amm bolt N, D, M, ncodebooks: 115193,  24,   3, 16   (5x5): 8.62 (427630626/s), 8.237 (447514386/s), 8.46 (435718203/s), 8.59 (429124097/s), 8.307 (443743348/s),
amm bolt N, D, M, ncodebooks: 230393,  24,   3, 16   (5x5): 16.476 (447473658/s), 16.966 (434550041/s), 16.539 (445769151/s), 16.468 (447691037/s), 16.521 (446254827/s),
amm bolt N, D, M, ncodebooks:  49284,  27,   2, 16   (5x5): 3.525 (447400851/s), 3.651 (431960558/s), 3.539 (445630969/s), 3.531 (446640611/s), 3.527 (447147150/s),
ncodebooks = 32
amm bolt N, D, M, ncodebooks:  10000, 512,  10, 32   (5x5): 6.154 (51998700/s), 6.245 (51240992/s), 6.296 (50825921/s), 6.126 (52236369/s), 6.429 (49774459/s),
amm bolt N, D, M, ncodebooks:  10000, 512, 100, 32   (5x5): 7.11 (180028129/s), 7.135 (179397337/s), 7.14 (179271708/s), 7.131 (179497966/s), 7.135 (179397337/s),
ncodebooks = 64
amm bolt N, D, M, ncodebooks:  10000, 512,  10, 64   (5x5): 7.087 (45153097/s), 7.082 (45184975/s), 6.889 (46450863/s), 6.889 (46450863/s), 7.272 (44004400/s),
amm bolt N, D, M, ncodebooks:  10000, 512, 100, 64   (5x5): 8.876 (144209103/s), 8.905 (143739472/s), 9.097 (140705727/s), 8.761 (146102043/s), 9.615 (133125325/s),
blas matmul N, D, M:  10000,   2,  10    (5x5): 0.032 (3125000000/s), 0.032 (3125000000/s), 0.032 (3125000000/s), 0.032 (3125000000/s), 0.032 (3125000000/s),
our  matmul N, D, M:  10000,   2,  10    (5x5): 0.032 (3125000000/s), 0.032 (3125000000/s), 0.032 (3125000000/s), 0.033 (3030303030/s), 0.033 (3030303030/s),
blas matmul N, D, M:  10000,   4,  10    (5x5): 0.039 (2564102564/s), 0.039 (2564102564/s), 0.039 (2564102564/s), 0.038 (2631578947/s), 0.038 (2631578947/s),
our  matmul N, D, M:  10000,   4,  10    (5x5): 0.039 (2564102564/s), 0.04 (2500000000/s), 0.04 (2500000000/s), 0.04 (2500000000/s), 0.039 (2564102564/s),
blas matmul N, D, M:  10000,   6,  10    (5x5): 0.046 (2173913043/s), 0.046 (2173913043/s), 0.046 (2173913043/s), 0.047 (2127659574/s), 0.046 (2173913043/s),
our  matmul N, D, M:  10000,   6,  10    (5x5): 0.061 (1639344262/s), 0.061 (1639344262/s), 0.059 (1694915254/s), 0.061 (1639344262/s), 0.059 (1694915254/s),
blas matmul N, D, M:  10000,   8,  10    (5x5): 0.051 (1960784313/s), 0.051 (1960784313/s), 0.051 (1960784313/s), 0.051 (1960784313/s), 0.052 (1923076923/s),
our  matmul N, D, M:  10000,   8,  10    (5x5): 0.058 (1724137931/s), 0.058 (1724137931/s), 0.057 (1754385964/s), 0.057 (1754385964/s), 0.057 (1754385964/s),
blas matmul N, D, M:  10000,  12,  10    (5x5): 0.08 (1250000000/s), 0.078 (1282051282/s), 0.078 (1282051282/s), 0.078 (1282051282/s), 0.078 (1282051282/s),
our  matmul N, D, M:  10000,  12,  10    (5x5): 0.076 (1315789473/s), 0.077 (1298701298/s), 0.076 (1315789473/s), 0.076 (1315789473/s), 0.076 (1315789473/s),
blas matmul N, D, M:  10000,  16,  10    (5x5): 0.087 (1149425287/s), 0.086 (1162790697/s), 0.084 (1190476190/s), 0.084 (1190476190/s), 0.085 (1176470588/s),
our  matmul N, D, M:  10000,  16,  10    (5x5): 0.098 (1020408163/s), 0.096 (1041666666/s), 0.096 (1041666666/s), 0.096 (1041666666/s), 0.096 (1041666666/s),
blas matmul N, D, M:  10000,  24,  10    (5x5): 0.121 (826446280/s), 0.121 (826446280/s), 0.117 (854700854/s), 0.116 (862068965/s), 0.116 (862068965/s),
our  matmul N, D, M:  10000,  24,  10    (5x5): 0.135 (740740740/s), 0.141 (709219858/s), 0.139 (719424460/s), 0.139 (719424460/s), 0.138 (724637681/s),
blas matmul N, D, M:  10000,  27,  10    (5x5): 0.155 (645161290/s), 0.151 (662251655/s), 0.152 (657894736/s), 0.153 (653594771/s), 0.161 (621118012/s),
our  matmul N, D, M:  10000,  27,  10    (5x5): 0.165 (606060606/s), 0.163 (613496932/s), 0.163 (613496932/s), 0.159 (628930817/s), 0.159 (628930817/s),
blas matmul N, D, M:  10000,  32,  10    (5x5): 0.172 (581395348/s), 0.183 (546448087/s), 0.165 (606060606/s), 0.163 (613496932/s), 0.162 (617283950/s),
our  matmul N, D, M:  10000,  32,  10    (5x5): 0.181 (552486187/s), 0.179 (558659217/s), 0.179 (558659217/s), 0.179 (558659217/s), 0.179 (558659217/s),
blas matmul N, D, M:  10000,  48,  10    (5x5): 0.26 (384615384/s), 0.248 (403225806/s), 0.245 (408163265/s), 0.242 (413223140/s), 0.24 (416666666/s),
our  matmul N, D, M:  10000,  48,  10    (5x5): 0.27 (370370370/s), 0.264 (378787878/s), 0.263 (380228136/s), 0.263 (380228136/s), 0.262 (381679389/s),
blas matmul N, D, M:  10000,  64,  10    (5x5): 0.342 (292397660/s), 0.329 (303951367/s), 0.324 (308641975/s), 0.321 (311526479/s), 0.321 (311526479/s),
our  matmul N, D, M:  10000,  64,  10    (5x5): 0.371 (269541778/s), 0.387 (258397932/s), 0.374 (267379679/s), 0.364 (274725274/s), 0.365 (273972602/s),
blas matmul N, D, M:  10000, 512,  10    (5x5): 5.784 (17289073/s), 5.738 (17427675/s), 5.755 (17376194/s), 5.809 (17214666/s), 5.961 (16775708/s),
our  matmul N, D, M:  10000, 512,  10    (5x5): 4.218 (23707918/s), 4.175 (23952095/s), 4.04 (24752475/s), 3.968 (25201612/s), 4.083 (24491795/s),
blas matmul N, D, M:  10000,   2, 100    (5x5): 0.318 (3144654088/s), 0.315 (3174603174/s), 0.315 (3174603174/s), 0.313 (3194888178/s), 0.317 (3154574132/s),
our  matmul N, D, M:  10000,   2, 100    (5x5): 0.341 (2932551319/s), 0.34 (2941176470/s), 0.351 (2849002849/s), 0.354 (2824858757/s), 0.36 (2777777777/s),
blas matmul N, D, M:  10000,   4, 100    (5x5): 0.332 (3012048192/s), 0.332 (3012048192/s), 0.326 (3067484662/s), 0.338 (2958579881/s), 0.329 (3039513677/s),
our  matmul N, D, M:  10000,   4, 100    (5x5): 0.439 (2277904328/s), 0.472 (2118644067/s), 0.451 (2217294900/s), 0.434 (2304147465/s), 0.442 (2262443438/s),
blas matmul N, D, M:  10000,   6, 100    (5x5): 0.384 (2604166666/s), 0.388 (2577319587/s), 0.39 (2564102564/s), 0.381 (2624671916/s), 0.394 (2538071065/s),
our  matmul N, D, M:  10000,   6, 100    (5x5): 0.666 (1501501501/s), 0.726 (1377410468/s), 0.663 (1508295625/s), 0.757 (1321003963/s), 0.675 (1481481481/s),
blas matmul N, D, M:  10000,   8, 100    (5x5): 0.411 (2433090024/s), 0.405 (2469135802/s), 0.456 (2192982456/s), 0.403 (2481389578/s), 0.404 (2475247524/s),
our  matmul N, D, M:  10000,   8, 100    (5x5): 0.603 (1658374792/s), 0.587 (1703577512/s), 0.583 (1715265866/s), 0.58 (1724137931/s), 0.58 (1724137931/s),
blas matmul N, D, M:  10000,  12, 100    (5x5): 0.652 (1533742331/s), 0.605 (1652892561/s), 0.631 (1584786053/s), 0.609 (1642036124/s), 0.608 (1644736842/s),
our  matmul N, D, M:  10000,  12, 100    (5x5): 0.754 (1326259946/s), 0.754 (1326259946/s), 0.757 (1321003963/s), 0.753 (1328021248/s), 0.755 (1324503311/s),
blas matmul N, D, M:  10000,  16, 100    (5x5): 0.622 (1607717041/s), 0.621 (1610305958/s), 0.633 (1579778830/s), 0.603 (1658374792/s), 0.612 (1633986928/s),
our  matmul N, D, M:  10000,  16, 100    (5x5): 0.952 (1050420168/s), 0.959 (1042752867/s), 0.953 (1049317943/s), 0.96 (1041666666/s), 0.958 (1043841336/s),
blas matmul N, D, M:  10000,  24, 100    (5x5): 0.802 (1246882793/s), 0.79 (1265822784/s), 0.766 (1305483028/s), 0.797 (1254705144/s), 0.787 (1270648030/s),
our  matmul N, D, M:  10000,  24, 100    (5x5): 1.315 (760456273/s), 1.32 (757575757/s), 1.334 (749625187/s), 1.324 (755287009/s), 1.326 (754147812/s),
blas matmul N, D, M:  10000,  27, 100    (5x5): 1.015 (985221674/s), 0.97 (1030927835/s), 1.006 (994035785/s), 0.975 (1025641025/s), 1.007 (993048659/s),
our  matmul N, D, M:  10000,  27, 100    (5x5): 1.555 (643086816/s), 1.571 (636537237/s), 1.537 (650618087/s), 1.572 (636132315/s), 1.684 (593824228/s),
blas matmul N, D, M:  10000,  32, 100    (5x5): 1.027 (973709834/s), 1.035 (966183574/s), 1.039 (962463907/s), 1.007 (993048659/s), 1.048 (954198473/s),
our  matmul N, D, M:  10000,  32, 100    (5x5): 1.739 (575043128/s), 1.75 (571428571/s), 1.749 (571755288/s), 1.868 (535331905/s), 1.767 (565930956/s),
blas matmul N, D, M:  10000,  48, 100    (5x5): 1.314 (761035007/s), 1.352 (739644970/s), 1.352 (739644970/s), 1.34 (746268656/s), 1.363 (733675715/s),
our  matmul N, D, M:  10000,  48, 100    (5x5): 2.675 (373831775/s), 2.467 (405350628/s), 2.464 (405844155/s), 2.536 (394321766/s), 2.592 (385802469/s),
blas matmul N, D, M:  10000,  64, 100    (5x5): 1.929 (518403317/s), 1.809 (552791597/s), 1.819 (549752611/s), 1.833 (545553737/s), 1.814 (551267916/s),
our  matmul N, D, M:  10000,  64, 100    (5x5): 3.36 (297619047/s), 3.425 (291970802/s), 3.201 (312402374/s), 3.271 (305716906/s), 3.353 (298240381/s),
blas matmul N, D, M:  10000, 512, 100    (5x5): 17.324 (57723389/s), 17.358 (57610323/s), 17.108 (58452186/s), 16.98 (58892815/s), 17.164 (58261477/s),
our  matmul N, D, M:  10000, 512, 100    (5x5): 30.929 (32332115/s), 30.998 (32260145/s), 30.981 (32277847/s), 31.277 (31972375/s), 30.45 (32840722/s),
blas matmul N, D, M:  57593,   2,   3    (5x5): 0.075 (2303720000/s), 0.077 (2243883116/s), 0.077 (2243883116/s), 0.077 (2243883116/s), 0.075 (2303720000/s),
our  matmul N, D, M:  57593,   2,   3    (5x5): 0.062 (2786758064/s), 0.062 (2786758064/s), 0.062 (2786758064/s), 0.062 (2786758064/s), 0.062 (2786758064/s),
blas matmul N, D, M:  57593,   4,   3    (5x5): 0.098 (1763051020/s), 0.102 (1693911764/s), 0.1 (1727790000/s), 0.1 (1727790000/s), 0.1 (1727790000/s),
our  matmul N, D, M:  57593,   4,   3    (5x5): 0.074 (2334851351/s), 0.074 (2334851351/s), 0.074 (2334851351/s), 0.074 (2334851351/s), 0.074 (2334851351/s),
blas matmul N, D, M:  57593,   6,   3    (5x5): 0.127 (1360464566/s), 0.128 (1349835937/s), 0.128 (1349835937/s), 0.126 (1371261904/s), 0.125 (1382232000/s),
our  matmul N, D, M:  57593,   6,   3    (5x5): 0.118 (1464228813/s), 0.118 (1464228813/s), 0.118 (1464228813/s), 0.115 (1502426086/s), 0.115 (1502426086/s),
blas matmul N, D, M:  57593,   8,   3    (5x5): 0.147 (1175367346/s), 0.152 (1136703947/s), 0.153 (1129274509/s), 0.151 (1144231788/s), 0.166 (1040837349/s),
our  matmul N, D, M:  57593,   8,   3    (5x5): 0.123 (1404707317/s), 0.122 (1416221311/s), 0.115 (1502426086/s), 0.114 (1515605263/s), 0.121 (1427925619/s),
blas matmul N, D, M:  57593,  12,   3    (5x5): 0.231 (747961038/s), 0.231 (747961038/s), 0.252 (685630952/s), 0.233 (741540772/s), 0.236 (732114406/s),
our  matmul N, D, M:  57593,  12,   3    (5x5): 0.161 (1073161490/s), 0.151 (1144231788/s), 0.153 (1129274509/s), 0.163 (1059993865/s), 0.161 (1073161490/s),
blas matmul N, D, M:  57593,  16,   3    (5x5): 0.278 (621507194/s), 0.279 (619279569/s), 0.279 (619279569/s), 0.28 (617067857/s), 0.276 (626010869/s),
our  matmul N, D, M:  57593,  16,   3    (5x5): 0.209 (826693779/s), 0.202 (855341584/s), 0.232 (744737068/s), 0.197 (877050761/s), 0.195 (886046153/s),
blas matmul N, D, M:  57593,  24,   3    (5x5): 0.44 (392679545/s), 0.434 (398108294/s), 0.456 (378901315/s), 0.457 (378072210/s), 0.457 (378072210/s),
our  matmul N, D, M:  57593,  24,   3    (5x5): 0.303 (570227722/s), 0.294 (587683673/s), 0.292 (591708904/s), 0.295 (585691525/s), 0.359 (481278551/s),
blas matmul N, D, M:  57593,  27,   3    (5x5): 0.579 (298409326/s), 0.563 (306889875/s), 0.556 (310753597/s), 0.555 (311313513/s), 0.554 (311875451/s),
our  matmul N, D, M:  57593,  27,   3    (5x5): 0.344 (502264534/s), 0.345 (500808695/s), 0.35 (493654285/s), 0.346 (499361271/s), 0.345 (500808695/s),
blas matmul N, D, M:  57593,  32,   3    (5x5): 0.805 (214632298/s), 0.812 (212782019/s), 0.804 (214899253/s), 0.783 (220662835/s), 0.744 (232229838/s),
our  matmul N, D, M:  57593,  32,   3    (5x5): 0.48 (359956250/s), 0.488 (354055327/s), 0.474 (364512658/s), 0.47 (367614893/s), 0.463 (373172786/s),
blas matmul N, D, M:  57593,  48,   3    (5x5): 1.211 (142674649/s), 1.212 (142556930/s), 1.205 (143385062/s), 1.207 (143147473/s), 1.2 (143982500/s),
our  matmul N, D, M:  57593,  48,   3    (5x5): 0.98 (176305102/s), 0.986 (175232251/s), 0.986 (175232251/s), 0.978 (176665644/s), 0.973 (177573484/s),
blas matmul N, D, M:  57593,  64,   3    (5x5): 1.936 (89245351/s), 2.031 (85070901/s), 1.778 (97176040/s), 1.957 (88287685/s), 2.056 (84036478/s),
our  matmul N, D, M:  57593,  64,   3    (5x5): 1.806 (95669435/s), 1.797 (96148580/s), 1.302 (132702764/s), 1.303 (132600920/s), 1.3 (132906923/s),
blas matmul N, D, M: 115193,   2,   3    (5x5): 0.149 (2319322147/s), 0.152 (2273546052/s), 0.152 (2273546052/s), 0.152 (2273546052/s), 0.152 (2273546052/s),
our  matmul N, D, M: 115193,   2,   3    (5x5): 0.13 (2658300000/s), 0.13 (2658300000/s), 0.13 (2658300000/s), 0.13 (2658300000/s), 0.126 (2742690476/s),
blas matmul N, D, M: 115193,   4,   3    (5x5): 0.21 (1645614285/s), 0.209 (1653488038/s), 0.209 (1653488038/s), 0.251 (1376808764/s), 0.217 (1592529953/s),
our  matmul N, D, M: 115193,   4,   3    (5x5): 0.165 (2094418181/s), 0.152 (2273546052/s), 0.152 (2273546052/s), 0.152 (2273546052/s), 0.152 (2273546052/s),
blas matmul N, D, M: 115193,   6,   3    (5x5): 0.318 (1086726415/s), 0.25 (1382316000/s), 0.254 (1360547244/s), 0.252 (1371345238/s), 0.25 (1382316000/s),
our  matmul N, D, M: 115193,   6,   3    (5x5): 0.244 (1416307377/s), 0.244 (1416307377/s), 0.248 (1393463709/s), 0.247 (1399105263/s), 0.264 (1309011363/s),
blas matmul N, D, M: 115193,   8,   3    (5x5): 0.332 (1040900602/s), 0.327 (1056816513/s), 0.321 (1076570093/s), 0.304 (1136773026/s), 0.312 (1107625000/s),
our  matmul N, D, M: 115193,   8,   3    (5x5): 0.26 (1329150000/s), 0.258 (1339453488/s), 0.253 (1365924901/s), 0.273 (1265857142/s), 0.261 (1324057471/s),
blas matmul N, D, M: 115193,  12,   3    (5x5): 0.521 (663299424/s), 0.504 (685672619/s), 0.494 (699552631/s), 0.494 (699552631/s), 0.493 (700971602/s),
our  matmul N, D, M: 115193,  12,   3    (5x5): 0.345 (1001678260/s), 0.344 (1004590116/s), 0.344 (1004590116/s), 0.345 (1001678260/s), 0.344 (1004590116/s),
blas matmul N, D, M: 115193,  16,   3    (5x5): 0.626 (552043130/s), 0.63 (548538095/s), 0.652 (530029141/s), 0.717 (481979079/s), 0.639 (540812206/s),
our  matmul N, D, M: 115193,  16,   3    (5x5): 0.454 (761187224/s), 0.487 (709607802/s), 0.488 (708153688/s), 0.447 (773107382/s), 0.446 (774840807/s),
blas matmul N, D, M: 115193,  24,   3    (5x5): 1.011 (341818991/s), 1.012 (341481225/s), 1.011 (341818991/s), 1.012 (341481225/s), 1.011 (341818991/s),
our  matmul N, D, M: 115193,  24,   3    (5x5): 0.699 (494390557/s), 0.693 (498670995/s), 0.696 (496521551/s), 0.688 (502295058/s), 0.69 (500839130/s),
blas matmul N, D, M: 115193,  27,   3    (5x5): 1.264 (273401107/s), 1.261 (274051546/s), 1.265 (273184980/s), 1.264 (273401107/s), 1.306 (264608728/s),
our  matmul N, D, M: 115193,  27,   3    (5x5): 0.811 (426114673/s), 0.818 (422468215/s), 0.889 (388727784/s), 0.89 (388291011/s), 0.888 (389165540/s),
blas matmul N, D, M: 115193,  32,   3    (5x5): 2.027 (170487913/s), 1.889 (182942826/s), 2.038 (169567713/s), 2.028 (170403846/s), 2.026 (170572063/s),
our  matmul N, D, M: 115193,  32,   3    (5x5): 1.342 (257510432/s), 1.466 (235729195/s), 1.524 (226757874/s), 1.329 (260029345/s), 1.545 (223675728/s),
blas matmul N, D, M: 115193,  48,   3    (5x5): 3.069 (112603128/s), 2.722 (126957751/s), 2.906 (118919132/s), 2.75 (125665090/s), 2.65 (130407169/s),
our  matmul N, D, M: 115193,  48,   3    (5x5): 1.922 (179801768/s), 1.924 (179614864/s), 1.931 (178963749/s), 1.927 (179335236/s), 1.93 (179056476/s),
blas matmul N, D, M: 115193,  64,   3    (5x5): 3.838 (90041427/s), 3.836 (90088373/s), 3.758 (91958222/s), 3.729 (92673370/s), 3.745 (92277436/s),
our  matmul N, D, M: 115193,  64,   3    (5x5): 2.663 (129770559/s), 2.61 (132405747/s), 3.058 (113008175/s), 3.066 (112713307/s), 3.064 (112786879/s),
blas matmul N, D, M: 230393,   2,   3    (5x5): 0.339 (2038876106/s), 0.318 (2173518867/s), 0.334 (2069398203/s), 0.332 (2081864457/s), 0.323 (2139873065/s),
our  matmul N, D, M: 230393,   2,   3    (5x5): 0.312 (2215317307/s), 0.307 (2251397394/s), 0.304 (2273615131/s), 0.305 (2266160655/s), 0.305 (2266160655/s),
blas matmul N, D, M: 230393,   4,   3    (5x5): 0.507 (1363272189/s), 0.488 (1416350409/s), 0.448 (1542810267/s), 0.436 (1585272935/s), 0.474 (1458183544/s),
our  matmul N, D, M: 230393,   4,   3    (5x5): 0.395 (1749820253/s), 0.367 (1883321525/s), 0.367 (1883321525/s), 0.381 (1814118110/s), 0.408 (1694066176/s),
blas matmul N, D, M: 230393,   6,   3    (5x5): 0.698 (990227793/s), 0.602 (1148137873/s), 0.602 (1148137873/s), 0.592 (1167532094/s), 0.667 (1036250374/s),
our  matmul N, D, M: 230393,   6,   3    (5x5): 0.601 (1150048252/s), 0.584 (1183525684/s), 0.611 (1131225859/s), 0.612 (1129377450/s), 0.611 (1131225859/s),
blas matmul N, D, M: 230393,   8,   3    (5x5): 0.733 (942945429/s), 0.731 (945525307/s), 0.729 (948119341/s), 0.796 (868315326/s), 0.763 (905870249/s),
our  matmul N, D, M: 230393,   8,   3    (5x5): 0.624 (1107658653/s), 0.65 (1063352307/s), 0.646 (1069936532/s), 0.644 (1073259316/s), 0.644 (1073259316/s),
blas matmul N, D, M: 230393,  12,   3    (5x5): 1.183 (584259509/s), 1.183 (584259509/s), 1.234 (560112641/s), 1.228 (562849348/s), 1.228 (562849348/s),
our  matmul N, D, M: 230393,  12,   3    (5x5): 0.908 (761210352/s), 0.915 (755386885/s), 0.913 (757041621/s), 0.913 (757041621/s), 0.913 (757041621/s),
blas matmul N, D, M: 230393,  16,   3    (5x5): 1.422 (486061181/s), 1.42 (486745774/s), 1.471 (469870156/s), 1.469 (470509870/s), 1.469 (470509870/s),
our  matmul N, D, M: 230393,  16,   3    (5x5): 1.122 (616024064/s), 1.156 (597905709/s), 1.094 (631790676/s), 1.094 (631790676/s), 1.157 (597388936/s),
blas matmul N, D, M: 230393,  24,   3    (5x5): 2.128 (324802161/s), 2.128 (324802161/s), 2.13 (324497183/s), 2.129 (324649600/s), 2.131 (324344908/s),
our  matmul N, D, M: 230393,  24,   3    (5x5): 1.566 (441365900/s), 1.601 (431717051/s), 1.538 (449401170/s), 1.615 (427974613/s), 1.618 (427181087/s),
blas matmul N, D, M: 230393,  27,   3    (5x5): 2.64 (261810227/s), 2.892 (238996887/s), 2.927 (236139050/s), 2.893 (238914275/s), 2.899 (238419799/s),
our  matmul N, D, M: 230393,  27,   3    (5x5): 2.078 (332617420/s), 1.977 (349610015/s), 1.988 (347675553/s), 1.97 (350852284/s), 1.967 (351387391/s),
blas matmul N, D, M: 230393,  32,   3    (5x5): 3.939 (175470677/s), 3.856 (179247665/s), 3.902 (177134546/s), 3.904 (177043801/s), 3.909 (176817344/s),
our  matmul N, D, M: 230393,  32,   3    (5x5): 2.659 (259939450/s), 2.599 (265940361/s), 2.569 (269045932/s), 2.572 (268732115/s), 2.564 (269570592/s),
blas matmul N, D, M: 230393,  48,   3    (5x5): 6.039 (114452558/s), 5.992 (115350300/s), 5.994 (115311811/s), 6.03 (114623383/s), 6.028 (114661413/s),
our  matmul N, D, M: 230393,  48,   3    (5x5): 3.665 (188589085/s), 3.826 (180653162/s), 3.592 (192421770/s), 3.585 (192797489/s), 3.575 (193336783/s),
blas matmul N, D, M: 230393,  64,   3    (5x5): 8.215 (84136214/s), 7.908 (87402503/s), 8.132 (84994958/s), 8.117 (85152026/s), 7.949 (86951692/s),
our  matmul N, D, M: 230393,  64,   3    (5x5): 4.945 (139773306/s), 5.179 (133458003/s), 5.165 (133819748/s), 5.173 (133612797/s), 4.827 (143190180/s),
blas matmul N, D, M:  49284,   2,   2    (5x5): 0.047 (2097191489/s), 0.047 (2097191489/s), 0.047 (2097191489/s), 0.046 (2142782608/s), 0.047 (2097191489/s),
our  matmul N, D, M:  49284,   2,   2    (5x5): 0.036 (2738000000/s), 0.036 (2738000000/s), 0.036 (2738000000/s), 0.036 (2738000000/s), 0.036 (2738000000/s),
blas matmul N, D, M:  49284,   4,   2    (5x5): 0.063 (1564571428/s), 0.063 (1564571428/s), 0.066 (1493454545/s), 0.101 (975920792/s), 0.069 (1428521739/s),
our  matmul N, D, M:  49284,   4,   2    (5x5): 0.045 (2190400000/s), 0.044 (2240181818/s), 0.044 (2240181818/s), 0.045 (2190400000/s), 0.045 (2190400000/s),
blas matmul N, D, M:  49284,   6,   2    (5x5): 0.081 (1216888888/s), 0.081 (1216888888/s), 0.081 (1216888888/s), 0.081 (1216888888/s), 0.081 (1216888888/s),
our  matmul N, D, M:  49284,   6,   2    (5x5): 0.068 (1449529411/s), 0.068 (1449529411/s), 0.068 (1449529411/s), 0.068 (1449529411/s), 0.067 (1471164179/s),
blas matmul N, D, M:  49284,   8,   2    (5x5): 0.095 (1037557894/s), 0.095 (1037557894/s), 0.095 (1037557894/s), 0.096 (1026750000/s), 0.111 (888000000/s),
our  matmul N, D, M:  49284,   8,   2    (5x5): 0.062 (1589806451/s), 0.061 (1615868852/s), 0.061 (1615868852/s), 0.063 (1564571428/s), 0.063 (1564571428/s),
blas matmul N, D, M:  49284,  12,   2    (5x5): 0.155 (635922580/s), 0.154 (640051948/s), 0.155 (635922580/s), 0.154 (640051948/s), 0.156 (631846153/s),
our  matmul N, D, M:  49284,  12,   2    (5x5): 0.079 (1247696202/s), 0.081 (1216888888/s), 0.081 (1216888888/s), 0.081 (1216888888/s), 0.081 (1216888888/s),
blas matmul N, D, M:  49284,  16,   2    (5x5): 0.2 (492840000/s), 0.195 (505476923/s), 0.192 (513375000/s), 0.193 (510715025/s), 0.212 (464943396/s),
our  matmul N, D, M:  49284,  16,   2    (5x5): 0.125 (788544000/s), 0.123 (801365853/s), 0.117 (842461538/s), 0.117 (842461538/s), 0.115 (857113043/s),
blas matmul N, D, M:  49284,  24,   2    (5x5): 0.279 (353290322/s), 0.281 (350775800/s), 0.318 (309962264/s), 0.297 (331878787/s), 0.279 (353290322/s),
our  matmul N, D, M:  49284,  24,   2    (5x5): 0.149 (661530201/s), 0.149 (661530201/s), 0.149 (661530201/s), 0.15 (657120000/s), 0.148 (666000000/s),
blas matmul N, D, M:  49284,  27,   2    (5x5): 0.363 (271537190/s), 0.366 (269311475/s), 0.366 (269311475/s), 0.366 (269311475/s), 0.371 (265681940/s),
our  matmul N, D, M:  49284,  27,   2    (5x5): 0.193 (510715025/s), 0.192 (513375000/s), 0.19 (518778947/s), 0.188 (524297872/s), 0.188 (524297872/s),
blas matmul N, D, M:  49284,  32,   2    (5x5): 0.702 (140410256/s), 0.704 (140011363/s), 0.71 (138828169/s), 0.72 (136900000/s), 0.512 (192515625/s),
our  matmul N, D, M:  49284,  32,   2    (5x5): 0.297 (331878787/s), 0.289 (341065743/s), 0.276 (357130434/s), 0.295 (334128813/s), 0.282 (349531914/s),
blas matmul N, D, M:  49284,  48,   2    (5x5): 0.853 (115554513/s), 0.834 (118187050/s), 0.829 (118899879/s), 0.822 (119912408/s), 0.827 (119187424/s),
our  matmul N, D, M:  49284,  48,   2    (5x5): 0.501 (196742514/s), 0.498 (197927710/s), 0.498 (197927710/s), 0.497 (198325955/s), 0.503 (195960238/s),
blas matmul N, D, M:  49284,  64,   2    (5x5): 1.4 (70405714/s), 1.229 (80201790/s), 1.426 (69122019/s), 1.485 (66375757/s), 1.484 (66420485/s),
our  matmul N, D, M:  49284,  64,   2    (5x5): 0.822 (119912408/s), 0.82 (120204878/s), 0.824 (119621359/s), 0.818 (120498777/s), 0.82 (120204878/s),
==============================================================================="""  # noqa


def _load_matmul_times_for_n_d_m(startswith):
    lines = microbench_output.split('\n')
    matmul_lines = [line for line in lines if line.startswith(startswith)]
    matmul_shape_to_times = {}
    matmul_shape_to_thruputs = {}
    for line in matmul_lines:
        start_idx = line.find(':') + 1
        end_idx = line.find('(')
        nmd_str = line[start_idx:end_idx]
        N, D, M = [int(substr) for substr in nmd_str.split(',')[:3]]
        speeds_str = line[line.find('):') + 2:]
        speed_pairs = speeds_str.split(',')[:5]
        times = []
        thruputs = []
        for pair in speed_pairs:
            pair = pair.strip()
            time_str, thruput_str = pair.split()
            times.append(float(time_str))
            thruput_str = thruput_str.strip('()s/')
            thruputs.append(float(thruput_str))

        key = (N, D, M)
        matmul_shape_to_times[key] = times
        matmul_shape_to_thruputs[key] = thruputs

    # pprint.pprint(matmul_shape_to_times)
    # pprint.pprint(matmul_shape_to_thruputs)

    return matmul_shape_to_times, matmul_shape_to_thruputs


def load_matmul_times_for_n_d_m():
    shape2lat0, shape2thruput0 = _load_matmul_times_for_n_d_m('blas matmul')
    shape2lat1, shape2thruput1 = _load_matmul_times_for_n_d_m('our matmul')

    # take minimum of time from eigen blas and our sgemm
    shape2lat = {}
    for k in shape2lat0:
        vals0 = shape2lat0.get(k, [1e20])
        vals1 = shape2lat1.get(k, [1e20])
        mean0, mean1 = np.mean(vals0), np.mean(vals1)
        if mean0 < mean1:
            shape2lat[k] = shape2lat0[k]
        else:
            shape2lat[k] = shape2lat1[k]
    shape2thruput = {}
    for k in shape2thruput0:
        vals0 = shape2thruput0.get(k, [-1e20])
        vals1 = shape2thruput1.get(k, [-1e20])
        mean0, mean1 = np.mean(vals0), np.mean(vals1)
        if mean0 > mean1:
            shape2thruput[k] = shape2lat0[k]
        else:
            shape2thruput[k] = shape2lat1[k]

    return shape2lat, shape2thruput


def _load_vq_times_for_n_d_m(startswith):
    lines = microbench_output.split('\n')
    lines = [line for line in lines if line.startswith(startswith)]
    shape_ncodebooks_to_times = {}
    shape_ncodebooks_to_thruputs = {}
    for line in lines:
        start_idx = line.find(':') + 1
        end_idx = line.find('(')
        nmd_str = line[start_idx:end_idx]
        N, D, M, C = [int(substr) for substr in nmd_str.split(',')[:4]]
        speeds_str = line[line.find('):') + 2:]
        speed_pairs = speeds_str.split(',')[:5]
        times = []
        thruputs = []
        for pair in speed_pairs:
            pair = pair.strip()
            time_str, thruput_str = pair.split()
            times.append(float(time_str))
            thruput_str = thruput_str.strip('()s/')
            thruputs.append(float(thruput_str))

        key = (N, D, M, C)
        shape_ncodebooks_to_times[key] = times
        shape_ncodebooks_to_thruputs[key] = thruputs

    # print("startswith: ", startswith)
    # if 'bolt' in startswith:
    #     print("bolt speed dicts:")
    #     pprint.pprint(shape_ncodebooks_to_times)
    #     pprint.pprint(shape_ncodebooks_to_thruputs)

    return shape_ncodebooks_to_times, shape_ncodebooks_to_thruputs


def load_multisplit_times_for_n_d_m():
    return _load_vq_times_for_n_d_m('amm multisplit')


def load_bolt_times_for_n_d_m():
    return _load_vq_times_for_n_d_m('amm bolt')


def main():
    load_matmul_times_for_n_d_m()
    load_multisplit_times_for_n_d_m()
    load_bolt_times_for_n_d_m()


if __name__ == '__main__':
    main()
