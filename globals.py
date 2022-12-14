RESOURCE_TILES = ['brick']*3 + ['grain']*4 + ['lumber']*4 + ['ore']*3 + ['wool']*4 + ['desert']

NUMBER_TOKENS = [2]*1 + [3]*2 + [4]*2 + [5]*2 + [6]*2 + [8]*2 + [9]*2 + [10]*2 + [11]*2 + [12]*1

ROAD_COST = {'brick':1, 'lumber':1}
SETTLEMENT_COST = {'brick':1, 'grain':1, 'lumber':1, 'wool':1}
CITY_COST = {'grain':3, 'ore':2}
DEV_CARD_COST = {'grain':1, 'ore':1, 'wool':1}

HEX_POINTS = { # links hex tiles (left-right, top-down) to their adjecent nodes
    0: [0, 3, 4, 7, 8, 12],
    1: [1, 4, 5, 8, 9, 13],
    2: [2, 5, 6, 9, 10, 14],
    3: [7, 11, 12, 16, 17, 22],
    4: [8, 12, 13, 17, 18, 23],
    5: [9, 13, 14, 18, 19, 24],
    6: [10, 14, 15, 19, 20, 25],
    7: [16, 21, 22, 27, 28, 33],
    8: [17, 22, 23, 28, 29, 34],
    9: [18, 23, 24, 29, 30, 35],
    10: [19, 24, 25, 30, 31, 36],
    11: [20, 25, 26, 31, 32, 37],
    12: [28, 33, 34, 38, 39, 43],
    13: [29, 34, 35, 39, 40, 44],
    14: [30, 35, 36, 40, 41, 45],
    15: [31, 36, 37, 41, 42, 46],
    16: [39, 43, 44, 47, 48, 51],
    17: [40, 44, 45, 48, 49, 52],
    18: [41, 45, 46, 49, 50, 53]
}

NEIGHBOUR_NODES = {
    0: [3, 4],
    1: [4, 5],
    2: [5, 6],
    3: [0, 7],
    4: [0, 1, 8],
    5: [1, 2, 9],
    6: [2, 10],
    7: [3, 11, 12],
    8: [4, 12, 13],
    9: [5, 13, 14],
    10: [6, 14, 15],
    11: [7, 16],
    12: [7, 8, 17],
    13: [8, 9, 18],
    14: [9, 10, 19],
    15: [10, 20],
    16: [11, 21, 22],
    17: [12, 22, 23],
    18: [13, 23, 24],
    19: [14, 24, 25],
    20: [15, 25, 26],
    21: [16, 27],
    22: [16, 17, 28],
    23: [17, 18, 29],
    24: [18, 19, 30],
    25: [19, 20, 31],
    26: [20, 32],
    27: [21, 30],
    28: [22, 33, 34],
    29: [23, 34, 35],
    30: [24, 35, 36],
    31: [25, 36, 37],
    32: [26, 37],
    33: [26, 28, 38],
    34: [28, 29, 39],
    35: [29, 30, 40],
    36: [30, 31, 41],
    37: [31, 32, 42],
    38: [33, 43],
    39: [34, 43, 44],
    40: [35, 44, 45],
    41: [36, 45, 46],
    42: [37, 46],
    43: [38, 39, 47],
    44: [39, 40, 48],
    45: [40, 41, 49],
    46: [41, 42, 50],
    47: [43, 51],
    48: [44, 51, 52],
    49: [45, 52, 53],
    50: [46, 53],
    51: [47, 48],
    52: [48, 49],
    53: [49, 50]
}