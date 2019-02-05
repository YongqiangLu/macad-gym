"""Mapping between node IDs and world coordinates for Town01 and Town02.

Defines the static conversion between node IDs (easier to work with) and the
world (X, Y, Z) coordinates defined on the carla Maps. This script should be
extended (in an automatic way) with the conversion/mappings for new towns as
they are made available

"""

# TODO: Refactor & Move the utils in env/carla/POS_COOR to env/carla/core/utils

TOWN01 = {
    "0": [271.0400085449219, 129.489990234375, 39.430625915527344],
    "1": [270.79998779296875, 133.43003845214844, 39.430625915527344],
    "2": [237.6999969482422, 129.75, 39.430625915527344],
    "3": [237.6999969482422, 133.239990234375, 39.430625915527344],
    "4": [216.26998901367188, 129.75, 39.430625915527344],
    "5": [216.26998901367188, 133.239990234375, 39.430625915527344],
    "6": [191.3199920654297, 129.75, 39.430625915527344],
    "7": [191.3199920654297, 133.24002075195312, 39.430625915527344],
    "8": [157.1899871826172, 129.75, 39.430625915527344],
    "9": [157.1899871826172, 133.24002075195312, 39.430625915527344],
    "10": [338.97998046875, 301.2599792480469, 39.430625915527344],
    "11": [128.94998168945312, 129.75, 39.430625915527344],
    "12": [128.94998168945312, 133.24002075195312, 39.430625915527344],
    "13": [119.46998596191406, 129.75, 39.430625915527344],
    "14": [105.43998718261719, 133.24002075195312, 39.430625915527344],
    "15": [92.11000061035156, 39.709999084472656, 39.430625915527344],
    "16": [88.6199951171875, 26.559999465942383, 39.430625915527344],
    "17": [92.11000061035156, 30.820009231567383, 39.430625915527344],
    "18": [88.6199951171875, 15.279999732971191, 39.430625915527344],
    "19": [92.11000061035156, 86.95999908447266, 39.430625915527344],
    "20": [88.6199951171875, 72.6199951171875, 39.430625915527344],
    "21": [335.489990234375, 298.80999755859375, 39.430625915527344],
    "22": [92.1099853515625, 95.44999694824219, 39.430625915527344],
    "23": [88.61998748779297, 95.44999694824219, 39.430625915527344],
    "24": [92.1099853515625, 113.05999755859375, 39.430625915527344],
    "25": [88.61998748779297, 103.37999725341797, 39.430625915527344],
    "26": [92.1099853515625, 159.9499969482422, 39.430625915527344],
    "27": [88.61998748779297, 145.83999633789062, 39.430625915527344],
    "28": [92.1099853515625, 176.88999938964844, 39.430625915527344],
    "29": [88.61998748779297, 169.84999084472656, 39.430625915527344],
    "30": [-2.4200193881988525, 187.97000122070312, 39.430625915527344],
    "31": [1.5599803924560547, 187.9700164794922, 39.430625915527344],
    "32": [338.97998046875, 249.42999267578125, 39.430625915527344],
    "33": [-2.4200096130371094, 149.8300018310547, 39.430625915527344],
    "34": [1.5599901676177979, 149.83001708984375, 39.430625915527344],
    "35": [-2.4200096130371094, 120.0199966430664, 39.430625915527344],
    "36": [1.5599901676177979, 120.02001953125, 39.430625915527344],
    "37": [-2.4200048446655273, 79.31999969482422, 39.430625915527344],
    "38": [1.5599950551986694, 79.32001495361328, 39.430625915527344],
    "39": [-2.4200048446655273, 48.70000076293945, 39.430625915527344],
    "40": [1.5599950551986694, 48.70001983642578, 39.430625915527344],
    "41": [-2.420001268386841, 17.779998779296875, 39.430625915527344],
    "42": [1.55999755859375, 22.440019607543945, 39.430625915527344],
    "43": [335.489990234375, 249.42999267578125, 39.430625915527344],
    "44": [21.770000457763672, -1.9599987268447876, 39.430625915527344],
    "45": [14.139999389648438, 2.0200109481811523, 39.430625915527344],
    "46": [47.939998626708984, -1.9599950313568115, 39.430625915527344],
    "47": [47.939998626708984, 2.020014524459839, 39.430625915527344],
    "48": [72.5999984741211, -1.9599950313568115, 39.430625915527344],
    "49": [62.12999725341797, 2.020014524459839, 39.430625915527344],
    "50": [116.63999938964844, -1.95999014377594, 39.430625915527344],
    "51": [110.02999877929688, 2.02001953125, 39.430625915527344],
    "52": [137.7899932861328, -1.95999014377594, 39.430625915527344],
    "53": [126.38999938964844, 2.02001953125, 39.430625915527344],
    "54": [338.97998046875, 226.75, 39.430625915527344],
    "55": [185.55999755859375, -1.9599803686141968, 39.430625915527344],
    "56": [173.14999389648438, 2.02001953125, 39.430625915527344],
    "57": [209.5800018310547, -1.9599803686141968, 39.430625915527344],
    "58": [209.5800018310547, 2.02001953125, 39.430625915527344],
    "59": [244.09999084472656, -1.9599803686141968, 39.430625915527344],
    "60": [244.09999084472656, 2.02001953125, 39.430625915527344],
    "61": [278.80999755859375, -1.9599803686141968, 39.430625915527344],
    "62": [278.80999755859375, 2.02001953125, 39.430625915527344],
    "63": [316.8500061035156, -1.9599803686141968, 39.430625915527344],
    "64": [306.28997802734375, 2.02001953125, 39.430625915527344],
    "65": [334.8299865722656, 217.0800018310547, 39.430625915527344],
    "66": [363.0, -1.9599609375, 39.430625915527344],
    "67": [356.79998779296875, 2.0200390815734863, 39.430625915527344],
    "68": [378.17999267578125, -1.9599609375, 39.430625915527344],
    "69": [378.17999267578125, 2.0200390815734863, 39.430625915527344],
    "70": [396.4499816894531, 19.9200382232666, 39.430625915527344],
    "71": [392.4700012207031, 19.9200382232666, 39.430625915527344],
    "72": [395.9599914550781, 164.1699981689453, 39.430625915527344],
    "73": [392.4700012207031, 164.1699981689453, 39.430625915527344],
    "74": [395.9599914550781, 105.38999938964844, 39.430625915527344],
    "75": [392.4700012207031, 105.38999938964844, 39.430625915527344],
    "76": [395.9599914550781, 68.86003875732422, 39.430625915527344],
    "77": [392.4700012207031, 68.86003875732422, 39.430625915527344],
    "78": [395.9599914550781, 308.2099914550781, 39.430625915527344],
    "79": [392.4700012207031, 308.2099914550781, 39.430625915527344],
    "80": [395.9599914550781, 249.42999267578125, 39.430625915527344],
    "81": [392.4700012207031, 249.42999267578125, 39.430625915527344],
    "82": [395.9599914550781, 212.89999389648438, 39.430625915527344],
    "83": [392.4700012207031, 212.89999389648438, 39.430625915527344],
    "84": [1.5099804401397705, 308.2099914550781, 39.430625915527344],
    "85": [-1.2800195217132568, 309.4599914550781, 39.430625915527344],
    "86": [1.5099804401397705, 249.42999267578125, 39.430625915527344],
    "87": [-1.980019450187683, 249.42999267578125, 39.430625915527344],
    "88": [121.22996520996094, 195.00999450683594, 39.430625915527344],
    "89": [105.22998809814453, 198.5, 39.430625915527344],
    "90": [118.94999694824219, 55.84000015258789, 39.430625915527344],
    "91": [111.56999969482422, 59.33001708984375, 39.430625915527344],
    "92": [141.12998962402344, 55.84000015258789, 39.430625915527344],
    "93": [125.9699935913086, 59.33001708984375, 39.430625915527344],
    "94": [22.17997932434082, 326.9700012207031, 39.430625915527344],
    "95": [22.17997932434082, 330.4599914550781, 39.430625915527344],
    "96": [92.10997772216797, 308.2099914550781, 39.430625915527344],
    "97": [46.14997863769531, 326.9700012207031, 39.430625915527344],
    "98": [46.14997863769531, 330.4599914550781, 39.430625915527344],
    "99": [65.3499755859375, 326.9700012207031, 39.430625915527344],
    "100": [60.10997772216797, 330.4599914550781, 39.430625915527344],
    "101": [381.3399963378906, 327.04998779296875, 39.430625915527344],
    "102": [381.3399658203125, 330.53997802734375, 39.430625915527344],
    "103": [366.53997802734375, 327.04998779296875, 39.430625915527344],
    "104": [358.39996337890625, 330.53997802734375, 39.430625915527344],
    "105": [320.8699645996094, 327.04998779296875, 39.430625915527344],
    "106": [306.76995849609375, 330.53997802734375, 39.430625915527344],
    "107": [88.61997985839844, 295.32000732421875, 39.430625915527344],
    "108": [301.3399658203125, 327.04998779296875, 39.430625915527344],
    "109": [301.3399658203125, 330.53997802734375, 39.430625915527344],
    "110": [262.5999755859375, 327.04998779296875, 39.430625915527344],
    "111": [262.5999755859375, 330.53997802734375, 39.430625915527344],
    "112": [232.19998168945312, 326.9700012207031, 39.430625915527344],
    "113": [232.19998168945312, 330.4599914550781, 39.430625915527344],
    "114": [199.94998168945312, 326.9700012207031, 39.430625915527344],
    "115": [199.94998168945312, 330.4599914550781, 39.430625915527344],
    "116": [173.11997985839844, 326.9700012207031, 39.430625915527344],
    "117": [173.11997985839844, 330.4599914550781, 39.430625915527344],
    "118": [92.10997772216797, 249.42999267578125, 39.430625915527344],
    "119": [124.73997497558594, 326.9700012207031, 39.430625915527344],
    "120": [114.3499755859375, 330.4599914550781, 39.430625915527344],
    "121": [142.91998291015625, 326.9700012207031, 39.430625915527344],
    "122": [142.91998291015625, 330.4599914550781, 39.430625915527344],
    "123": [142.91998291015625, 195.26998901367188, 39.430625915527344],
    "124": [142.91998291015625, 198.75999450683594, 39.430625915527344],
    "125": [178.7699737548828, 195.26998901367188, 39.430625915527344],
    "126": [178.7699737548828, 198.75999450683594, 39.430625915527344],
    "127": [217.50997924804688, 195.26998901367188, 39.430625915527344],
    "128": [217.50997924804688, 198.75999450683594, 39.430625915527344],
    "129": [88.61997985839844, 249.42999267578125, 39.430625915527344],
    "130": [256.3499755859375, 195.5699920654297, 39.430625915527344],
    "131": [256.3499755859375, 199.05999755859375, 39.430625915527344],
    "132": [299.39996337890625, 195.5699920654297, 39.430625915527344],
    "133": [299.39996337890625, 199.05999755859375, 39.430625915527344],
    "134": [158.0800018310547, 27.18000030517578, 39.430625915527344],
    "135": [153.75999450683594, 18.889999389648438, 39.430625915527344],
    "136": [157.25, 39.709999084472656, 39.430625915527344],
    "137": [153.75999450683594, 28.899999618530273, 39.430625915527344],
    "138": [191.0800018310547, 55.84000015258789, 39.430625915527344],
    "139": [172.2899932861328, 59.33001708984375, 39.430625915527344],
    "140": [92.1099853515625, 227.22000122070312, 39.430625915527344],
    "141": [202.5500030517578, 55.84000015258789, 39.430625915527344],
    "142": [202.5500030517578, 59.33001708984375, 39.430625915527344],
    "143": [234.26998901367188, 55.84001922607422, 39.430625915527344],
    "144": [234.26998901367188, 59.33001708984375, 39.430625915527344],
    "145": [272.2900085449219, 55.84000015258789, 39.430625915527344],
    "146": [272.2900085449219, 59.33003616333008, 39.430625915527344],
    "147": [299.3999938964844, 55.84000015258789, 39.430625915527344],
    "148": [299.3999938964844, 59.33003616333008, 39.430625915527344],
    "149": [299.3999938964844, 129.75, 39.430625915527344],
    "150": [299.3999938964844, 133.2400360107422, 39.430625915527344],
    "151": [88.61998748779297, 212.89999389648438, 39.430625915527344]
}

TOWN02 = {
    "0": [-3.679999828338623, 251.36000061035156, 1.2699999809265137],
    "1": [-3.679999828338623, 142.19000244140625, 1.3700000047683716],
    "2": [132.02999877929688, 211.0, 1.3700000047683716],
    "3": [135.87998962402344, 226.04998779296875, 1.3700000047683716],
    "4": [132.02999877929688, 201.1699981689453, 1.3700000047683716],
    "5": [135.87998962402344, 220.8300018310547, 1.3700000047683716],
    "6": [41.38999938964844, 212.97999572753906, 1.3700000047683716],
    "7": [-7.529999732971191, 158.97999572753906, 1.3700000047683716],
    "8": [45.23999786376953, 225.58999633789062, 1.3700000047683716],
    "9": [41.38999938964844, 203.89999389648438, 1.3700000047683716],
    "10": [45.88999938964844, 216.25999450683594, 1.3700000047683716],
    "11": [41.38999938964844, 275.0299987792969, 1.3700000047683716],
    "12": [45.23999786376953, 291.2900085449219, 1.3700000047683716],
    "13": [41.38999938964844, 257.4599914550781, 1.3700000047683716],
    "14": [45.59000015258789, 271.5099792480469, 1.3700000047683716],
    "15": [150.24002075195312, 191.77003479003906, 1.3700000047683716],
    "16": [165.0900421142578, 187.1199493408203, 1.3700000047683716],
    "17": [9.469999313354492, 191.76998901367188, 1.3700000047683716],
    "18": [-3.679999828338623, 172.42999267578125, 1.3700000047683716],
    "19": [21.9000244140625, 187.9199981689453, 1.3700000047683716],
    "20": [14.200018882751465, 191.76998901367188, 1.3700000047683716],
    "21": [27.72001838684082, 187.9199981689453, 1.3700000047683716],
    "22": [63.34002685546875, 191.76998901367188, 1.3700000047683716],
    "23": [75.4100341796875, 187.9199981689453, 1.3700000047683716],
    "24": [92.34001922607422, 191.76998901367188, 1.3700000047683716],
    "25": [92.34004974365234, 187.9199981689453, 1.3700000047683716],
    "26": [162.02005004882812, 191.77003479003906, 1.3700000047683716],
    "27": [181.800048828125, 187.9199981689453, 1.3700000047683716],
    "28": [104.59001922607422, 191.77003479003906, 1.3700000047683716],
    "29": [-7.529999732971191, 208.9199981689453, 1.3700000047683716],
    "30": [117.93003845214844, 187.91995239257812, 1.3700000047683716],
    "31": [151.30001831054688, 241.280029296875, 1.3700000047683716],
    "32": [162.92002868652344, 237.42996215820312, 1.3700000047683716],
    "33": [59.71002960205078, 241.27999877929688, 1.3700000047683716],
    "34": [71.0400390625, 237.42999267578125, 1.3700000047683716],
    "35": [88.71001434326172, 241.27999877929688, 1.3700000047683716],
    "36": [88.71004486083984, 237.42999267578125, 1.3700000047683716],
    "37": [162.7600555419922, 241.280029296875, 1.3700000047683716],
    "38": [174.33004760742188, 237.42999267578125, 1.3700000047683716],
    "39": [104.30001831054688, 241.280029296875, 1.3700000047683716],
    "40": [-3.679999828338623, 219.4099884033203, 1.3700000047683716],
    "41": [118.77003479003906, 237.42996215820312, 1.3700000047683716],
    "42": [9.530024528503418, 302.57000732421875, 1.3700000047683716],
    "43": [14.010019302368164, 306.41998291015625, 1.3700000047683716],
    "44": [26.940019607543945, 302.57000732421875, 1.3700000047683716],
    "45": [59.60002899169922, 306.41998291015625, 1.3700000047683716],
    "46": [71.53003692626953, 302.57000732421875, 1.3700000047683716],
    "47": [88.83001708984375, 306.41998291015625, 1.3700000047683716],
    "48": [88.83004760742188, 302.57000732421875, 1.3700000047683716],
    "49": [178.29005432128906, 306.4200439453125, 1.3700000047683716],
    "50": [-7.529999732971191, 288.2200012207031, 1.3700000047683716],
    "51": [178.29005432128906, 302.57000732421875, 1.3700000047683716],
    "52": [136.11001586914062, 306.4200439453125, 1.3700000047683716],
    "53": [136.1100311279297, 302.5699462890625, 1.3700000047683716],
    "54": [1.5399999618530273, 109.39999389648438, 1.3700000047683716],
    "55": [1.5400243997573853, 105.54998779296875, 1.3700000047683716],
    "56": [21.420019149780273, 109.39999389648438, 1.3700000047683716],
    "57": [25.530019760131836, 105.54998779296875, 1.3700000047683716],
    "58": [55.41002655029297, 109.39998626708984, 1.3700000047683716],
    "59": [55.410037994384766, 105.54998779296875, 1.3700000047683716],
    "60": [84.41001892089844, 109.29999542236328, 1.1699999570846558],
    "61": [-3.679999828338623, 288.2200012207031, 1.3700000047683716],
    "62": [84.41004943847656, 105.55001068115234, 1.3700000047683716],
    "63": [173.87005615234375, 109.40003967285156, 1.3700000047683716],
    "64": [173.87005615234375, 105.55001068115234, 1.3700000047683716],
    "65": [131.6900177001953, 109.40003967285156, 1.3700000047683716],
    "66": [131.69003295898438, 105.54996490478516, 1.3700000047683716],
    "67": [189.92999267578125, 121.20999908447266, 1.3700000047683716],
    "68": [193.77999877929688, 121.20999908447266, 1.3700000047683716],
    "69": [189.92999267578125, 142.19000244140625, 1.3700000047683716],
    "70": [193.77999877929688, 142.19000244140625, 1.3700000047683716],
    "71": [189.92999267578125, 160.5800018310547, 1.3700000047683716],
    "72": [-7.529999732971191, 251.36000061035156, 1.3700000047683716],
    "73": [193.77999877929688, 171.2899932861328, 1.3700000047683716],
    "74": [189.92999267578125, 208.11000061035156, 1.3700000047683716],
    "75": [193.77999877929688, 218.7899932861328, 1.3700000047683716],
    "76": [189.92999267578125, 293.5400085449219, 1.3700000047683716],
    "77": [193.77999877929688, 293.5400085449219, 1.3700000047683716],
    "78": [189.92999267578125, 252.3300018310547, 1.3700000047683716],
    "79": [193.77999877929688, 266.42999267578125, 1.3700000047683716],
    "80": [-7.529999732971191, 121.20999908447266, 1.3700000047683716],
    "81": [-3.679999828338623, 121.20999908447266, 1.3700000047683716],
    "82": [-7.529999732971191, 142.19000244140625, 1.3700000047683716]
}

TOWN04 = {
    "0": [-515.2499389648438, 240.95675659179688, 1.1999999284744263],
    "1": [-511.74993896484375, 240.9485626220703, 1.1999999284744263],
    "2": [-508.24993896484375, 240.94039916992188, 1.1999999284744263],
    "3": [-504.75, 240.93223571777344, 1.1999999284744263],
    "4": [-493.2300720214844, 177.6527557373047, 1.1999999284744263],
    "5": [-489.7301330566406, 177.67459106445312, 1.1999999284744263],
    "6": [-486.230224609375, 177.69642639160156, 1.1999999284744263],
    "7": [-482.7302551269531, 177.71827697753906, 1.1999999284744263],
    "8": [334.0113525390625, -117.60023498535156, 1.2195922136306763],
    "9": [348.0001525878906, -142.8535614013672, 1.2043334245681763],
    "10": [351.4998474121094, -142.80618286132812, 1.2043334245681763],
    "11": [334.0682067871094, -121.09976196289062, 1.2195922136306763],
    "12": [248.58294677734375, -385.22991943359375, 1.1999999284744263],
    "13": [248.5648956298828, -388.7298278808594, 1.1999999284744263],
    "14": [248.54684448242188, -392.2298278808594, 1.1999999284744263],
    "15": [248.52882385253906, -395.7297668457031, 1.1999999284744263],
    "16": [-514.2296752929688, 177.52096557617188, 1.1999999284744263],
    "17": [-510.7297058105469, 177.54283142089844, 1.1999999284744263],
    "18": [-507.22979736328125, 177.56466674804688, 1.1999999284744263],
    "19": [-503.7298583984375, 177.5865020751953, 1.1999999284744263],
    "20": [160.49594116210938, -385.6398010253906, 1.1999999284744263],
    "21": [160.5265655517578, -389.1396789550781, 1.1999999284744263],
    "22": [160.55718994140625, -392.6395568847656, 1.1999999284744263],
    "23": [160.58782958984375, -396.139404296875, 1.1999999284744263],
    "24": [248.691162109375, -364.2301940917969, 1.1999999284744263],
    "25": [248.6731414794922, -367.7301025390625, 1.1999999284744263],
    "26": [248.65509033203125, -371.2301025390625, 1.1999999284744263],
    "27": [248.6370391845703, -374.73004150390625, 1.1999999284744263],
    "28": [-494.25, 240.90774536132812, 1.1999999284744263],
    "29": [-490.7500305175781, 240.8995819091797, 1.1999999284744263],
    "30": [-487.2500305175781, 240.89141845703125, 1.1999999284744263],
    "31": [-483.7500305175781, 240.88323974609375, 1.1999999284744263],
    "32": [160.31092834472656, -364.640625, 1.1999999284744263],
    "33": [160.34152221679688, -368.1404724121094, 1.1999999284744263],
    "34": [160.37213134765625, -371.6403503417969, 1.1999999284744263],
    "35": [160.40272521972656, -375.1402282714844, 1.1999999284744263],
    "36": [6.560737133026123, 312.0257873535156, 1.1999999284744263],
    "37": [9.043990135192871, 314.4922790527344, 1.1999999284744263],
    "38": [-45.63199234008789, 340.2911376953125, 1.1999999284744263],
    "39": [-48.38798904418945, 338.1336975097656, 1.1999999284744263],
    "40": [-51.14398956298828, 335.976318359375, 1.1999999284744263],
    "41": [-53.89998245239258, 333.81884765625, 1.1999999284744263],
    "42": [-1.4151203632354736, 306.8454895019531, 1.1999999284744263],
    "43": [-4.622522354125977, 305.4445495605469, 1.1999999284744263],
    "44": [-7.8299241065979, 304.04364013671875, 1.1999999284744263],
    "45": [-11.037324905395508, 302.6427307128906, 1.1999999284744263],
    "46": [194.699951171875, -311.1709899902344, 1.2336608171463013],
    "47": [211.311767578125, -307.8799743652344, 1.2043486833572388],
    "48": [205.48858642578125, -317.73675537109375, 1.2195922136306763],
    "49": [201.5546417236328, -298.8638610839844, 1.2195922136306763],
    "50": [348.28558349609375, -164.05177307128906, 1.2043334245681763],
    "51": [341.3101806640625, -172.21388244628906, 1.3958922624588013],
    "52": [356.21246337890625, -168.62899780273438, 1.3958922624588013],
    "53": [351.9571533203125, -176.76959228515625, 1.2043334245681763],
    "54": [200.88221740722656, -385.3092346191406, 1.1999999284744263],
    "55": [200.90847778320312, -388.8091735839844, 1.1999999284744263],
    "56": [200.9347381591797, -392.3090515136719, 1.1999999284744263],
    "57": [200.96099853515625, -395.8089294433594, 1.1999999284744263],
    "58": [208.99591064453125, -367.7478942871094, 1.1999999284744263],
    "59": [209.02215576171875, -371.247802734375, 1.1999999284744263],
    "60": [209.04843139648438, -374.7476806640625, 1.1999999284744263],
    "61": [202.94073486328125, -359.2735595703125, 1.2195922136306763],
    "62": [208.96926879882812, -364.24798583984375, 1.1999999284744263],
    "63": [250.85569763183594, -310.97308349609375, 1.2043486833572388],
    "64": [263.3051452636719, -307.3447570800781, 1.2043486833572388],
    "65": [255.3369903564453, -302.60601806640625, 1.219584584236145],
    "66": [315.26519775390625, -256.2635498046875, 1.2043486833572388],
    "67": [311.6084899902344, -238.71185302734375, 1.2043486833572388],
    "68": [304.38616943359375, -250.0477294921875, 1.2043334245681763],
    "69": [322.6086120605469, -246.67312622070312, 1.2043334245681763],
    "70": [315.0611877441406, -233.3867645263672, 1.2043486833572388],
    "71": [311.4590148925781, -221.94686889648438, 1.2043486833572388],
    "72": [314.5877380371094, -180.29779052734375, 1.2043486833572388],
    "73": [310.9175109863281, -161.22764587402344, 1.2043486833572388],
    "74": [303.2471618652344, -172.43052673339844, 1.3958922624588013],
    "75": [321.7052917480469, -168.82542419433594, 1.3958922624588013],
    "76": [314.1199645996094, -127.8437271118164, 1.2043486833572388],
    "77": [310.4871826171875, -112.97294616699219, 1.2043486833572388],
    "78": [304.1087951660156, -121.58297729492188, 1.2195922136306763],
    "79": [410.94744873046875, -14.670990943908691, 1.1999999284744263],
    "80": [321.527099609375, -117.80158996582031, 1.2195922136306763],
    "81": [4.61154317855835, -83.30665588378906, 1.1999999284744263],
    "82": [8.111515998840332, -83.32039642333984, 1.1999999284744263],
    "83": [11.611489295959473, -83.3341293334961, 1.1999999284744263],
    "84": [15.111461639404297, -83.34786987304688, 1.1999999284744263],
    "85": [-16.254446029663086, -49.11910629272461, 1.1999999284744263],
    "86": [-12.754473686218262, -49.13283920288086, 1.1999999284744263],
    "87": [-9.254500389099121, -49.14657974243164, 1.1999999284744263],
    "88": [-5.754527568817139, -49.160316467285156, 1.1999999284744263],
    "89": [24.689603805541992, -80.39801788330078, 1.1999999284744263],
    "90": [258.4601745605469, -180.45677185058594, 1.219584584236145],
    "91": [254.899169921875, -160.67750549316406, 1.219584584236145],
    "92": [246.87356567382812, -172.7514190673828, 1.3958922624588013],
    "93": [266.2822265625, -169.140869140625, 1.3958922624588013],
    "94": [403.0406494140625, -174.05661010742188, 1.1999999284744263],
    "95": [406.54046630859375, -174.02005004882812, 1.1999999284744263],
    "96": [410.0402526855469, -173.98348999023438, 1.1999999284744263],
    "97": [413.54010009765625, -173.94692993164062, 1.1999999284744263],
    "98": [385.45733642578125, -166.17127990722656, 1.1999999284744263],
    "99": [388.9571533203125, -166.1347198486328, 1.1999999284744263],
    "100": [392.4569396972656, -166.09817504882812, 1.1999999284744263],
    "101": [381.9574890136719, -166.20762634277344, 1.1999999284744263],
    "102": [376.7408142089844, -172.01220703125, 1.3958922624588013],
    "103": [329.1581115722656, -172.28305053710938, 1.3958922624588013],
    "104": [335.2097473144531, -168.74855041503906, 1.3958922624588013],
    "105": [330.9915466308594, -175.8546600341797, 1.2043448686599731],
    "106": [5.25870943069458, 68.0704116821289, 1.1999999284744263],
    "107": [8.758665084838867, 68.05274963378906, 1.1999999284744263],
    "108": [12.258620262145996, 68.03508758544922, 1.1999999284744263],
    "109": [15.758575439453125, 68.01742553710938, 1.1999999284744263],
    "110": [-15.447463035583496, 126.34944915771484, 1.1999999284744263],
    "111": [-11.94750690460205, 126.331787109375, 1.1999999284744263],
    "112": [-8.447552680969238, 126.31411743164062, 1.1999999284744263],
    "113": [-4.947597026824951, 126.29646301269531, 1.1999999284744263],
    "114": [-24.995059967041016, 123.359619140625, 1.1999999284744263],
    "115": [68.31673431396484, 16.860254287719727, 12.184279441833496],
    "116": [68.33094787597656, 13.360282897949219, 12.184279441833496],
    "117": [68.34515380859375, 9.860311508178711, 12.184279441833496],
    "118": [68.35936737060547, 6.360339641571045, 12.184279441833496],
    "119": [110.96759796142578, 38.20707321166992, 11.66282844543457],
    "120": [111.0273208618164, 34.70758056640625, 11.66282844543457],
    "121": [111.08706665039062, 31.20808982849121, 11.66282844543457],
    "122": [111.14680480957031, 27.708600997924805, 11.66282844543457],
    "123": [107.80445861816406, 47.71295928955078, 11.720589637756348],
    "124": [131.18211364746094, -180.5467529296875, 1.2386962175369263],
    "125": [133.1906280517578, -169.8984375, 1.3958922624588013],
    "126": [125.03673553466797, -173.44491577148438, 1.3958922624588013],
    "127": [380.93096923828125, -62.89579391479492, 1.1999999284744263],
    "128": [375.6085205078125, -68.68538665771484, 1.2043486833572388],
    "129": [401.9940185546875, -71.04511260986328, 1.1999999284744263],
    "130": [405.4939270019531, -71.01829528808594, 1.1999999284744263],
    "131": [408.9937744140625, -70.99147033691406, 1.1999999284744263],
    "132": [412.49371337890625, -70.96464538574219, 1.1999999284744263],
    "133": [384.43084716796875, -62.869163513183594, 1.1999999284744263],
    "134": [387.93072509765625, -62.842342376708984, 1.1999999284744263],
    "135": [391.43060302734375, -62.81551742553711, 1.1999999284744263],
    "136": [-25.112159729003906, -245.74539184570312, 1.1999999284744263],
    "137": [-28.01565933227539, -247.6997528076172, 1.1999999284744263],
    "138": [20.18295669555664, -288.97021484375, 1.1999999284744263],
    "139": [23.319177627563477, -287.4164733886719, 1.1999999284744263],
    "140": [26.455394744873047, -285.86273193359375, 1.1999999284744263],
    "141": [29.591617584228516, -284.3089904785156, 1.1999999284744263],
    "142": [-15.538305282592773, -242.2172393798828, 1.1999999284744263],
    "143": [-12.065874099731445, -241.77880859375, 1.1999999284744263],
    "144": [-8.593442916870117, -241.34036254882812, 1.1999999284744263],
    "145": [-5.121011734008789, -240.90194702148438, 1.1999999284744263],
    "146": [-105.51869201660156, 16.305519104003906, 10.39791202545166],
    "147": [-105.51399993896484, 12.805521965026855, 10.39791202545166],
    "148": [-105.50930786132812, 9.305526733398438, 10.39791202545166],
    "149": [-105.5046157836914, 5.805529594421387, 10.39791202545166],
    "150": [-69.65084075927734, 37.35363006591797, 11.007528305053711],
    "151": [-69.64614868164062, 33.853633880615234, 11.007528305053711],
    "152": [-69.6414566040039, 30.3536376953125, 11.007528305053711],
    "153": [-69.63676452636719, 26.853641510009766, 11.007528305053711],
    "154": [-99.5702896118164, -3.6702024936676025, 10.541708946228027],
    "155": [204.06927490234375, -255.87893676757812, 1.2195922136306763],
    "156": [211.27268981933594, -245.90652465820312, 1.2043334245681763],
    "157": [200.1762237548828, -238.7903289794922, 1.2195922136306763],
    "158": [194.09445190429688, -248.6903533935547, 1.2386962175369263],
    "159": [62.13904571533203, -180.00250244140625, 1.2336608171463013],
    "160": [54.10126876831055, -173.84866333007812, 1.3958922624588013],
    "161": [66.74894714355469, -170.276611328125, 1.3958922624588013],
    "162": [-390.3832702636719, 5.730833053588867, 1.1999999284744263],
    "163": [-390.31549072265625, 16.230613708496094, 1.1999999284744263],
    "164": [-390.3380432128906, 12.73068618774414, 1.1999999284744263],
    "165": [-390.36053466796875, 9.230758666992188, 1.1999999284744263],
    "166": [-365.04302978515625, 37.06854248046875, 1.1999999284744263],
    "167": [-365.0655822753906, 33.5686149597168, 1.1999999284744263],
    "168": [-365.08807373046875, 30.06868553161621, 1.1999999284744263],
    "169": [-365.1105651855469, 26.56875991821289, 1.1999999284744263],
    "170": [-6.2216644287109375, -168.18861389160156, 1.1999999284744263],
    "171": [-9.721637725830078, -168.1748809814453, 1.1999999284744263],
    "172": [-13.221610069274902, -168.1611328125, 1.1999999284744263],
    "173": [-16.72158432006836, -168.14739990234375, 1.1999999284744263],
    "174": [11.246291160583496, -176.38783264160156, 1.1999999284744263],
    "175": [7.746318817138672, -176.37408447265625, 1.1999999284744263],
    "176": [4.246345520019531, -176.3603515625, 1.1999999284744263],
    "177": [14.746261596679688, -176.40213012695312, 1.1999999284744263],
    "178": [20.040634155273438, -170.54249572753906, 1.3958922624588013],
    "179": [262.7838134765625, -118.74906158447266, 1.2195922136306763],
    "180": [258.3017883300781, -129.0966796875, 1.219584584236145],
    "181": [249.52442932128906, -122.46336364746094, 1.2195922136306763],
    "182": [407.50823974609375, -15.320548057556152, 1.1999999284744263],
    "183": [400.62994384765625, -16.620092391967773, 1.1999999284744263],
    "184": [404.0691223144531, -15.970556259155273, 1.1999999284744263],
    "185": [369.87420654296875, -0.9899870157241821, 1.1999999284744263],
    "186": [372.38775634765625, 1.4456130266189575, 1.1999999284744263],
    "187": [374.9012756347656, 3.8812131881713867, 1.1999999284744263],
    "188": [377.4148254394531, 6.316812992095947, 1.1999999284744263]
}
