from enum import Enum


class DiceType(Enum):
    BIG = "BIG"              # 大
    SMALL = "SMALL"          # 小
    SINGULAR = "SINGULAR"    # 单
    EVEN = "EVEN"            # 双

    # SUM_THREE = "SUM_THREE"         # 和值3
    SUM_FOUR = "SUM_FOUR"             # 和值4
    SUM_FIVE = "SUM_FIVE"             # 和值5
    SUM_SIX = "SUM_SIX"               # 和值6
    SUM_SEVEN = "SUM_SEVEN"           # 和值7
    SUM_EIGHT = "SUM_EIGHT"           # 和值8
    SUM_NINE = "SUM_NINE"             # 和值9
    SUM_TEN = "SUM_TEN"               # 和值10
    SUM_ELEVEN = "SUM_ELEVEN"         # 和值11
    SUM_TWELVE = "SUM_TWELVE"         # 和值12
    SUM_THIRTEEN = "SUM_THIRTEEN"     # 和值13
    SUM_FOURTEEN = "SUM_FOURTEEN"     # 和值14
    SUM_FIFTEEN = "SUM_FIFTEEN"       # 和值15
    SUM_SIXTEEN = "SUM_SIXTEEN"       # 和值16
    SUM_SEVENTEEN = "SUM_SEVENTEEN"   # 和值17
    # SUM_EIGHTEEN = "SUM_EIGHTEEN"   # 和值18

    # LEOPARD_ONE = 3001    # 豹子1
    # LEOPARD_TWO = 3002    # 豹子2
    # LEOPARD_THREE = 3003  # 豹子3
    # LEOPARD_FOUR = 3004   # 豹子4
    # LEOPARD_FIVE = 3005   # 豹子5
    # LEOPARD_SIX = 3006    # 豹子6


class DiceLabel(Enum):
    BIG = '大'            # 大
    SMALL = '小'          # 小
    SINGULAR = '单'       # 单
    EVEN = '双'           # 双

    SUM_THREE = '和值3'       # 和值3
    SUM_FOUR = '和值4'        # 和值4
    SUM_FIVE = '和值5'        # 和值5
    SUM_SIX = '和值6'         # 和值6
    SUM_SEVEN = '和值7'       # 和值7
    SUM_EIGHT = '和值8'       # 和值8
    SUM_NINE = '和值9'        # 和值9
    SUM_TEN = '和值10'        # 和值10
    SUM_ELEVEN = '和值11'     # 和值11
    SUM_TWELVE = '和值12'     # 和值12
    SUM_THIRTEEN = '和值13'   # 和值13
    SUM_FOURTEEN = '和值14'   # 和值14
    SUM_FIFTEEN = '和值15'    # 和值15
    SUM_SIXTEEN = '和值16'    # 和值16
    SUM_SEVENTEEN = '和值17'  # 和值17
    SUM_EIGHTEEN = '和值18'   # 和值18


class Positions(Enum):
    BIG = 1            # 大
    SMALL = 2          # 小
    SINGULAR = 3       # 单
    EVEN = 4           # 双

    # SUM_THREE = 5       # 和值3
    SUM_FOUR = 5        # 和值4
    SUM_FIVE = 6        # 和值5
    SUM_SIX = 7         # 和值6
    SUM_SEVEN = 8       # 和值7
    SUM_EIGHT = 9       # 和值8
    SUM_NINE = 10        # 和值9
    SUM_TEN = 11        # 和值10
    SUM_ELEVEN = 12     # 和值11
    SUM_TWELVE = 13     # 和值12
    SUM_THIRTEEN = 14   # 和值13
    SUM_FOURTEEN = 15   # 和值14
    SUM_FIFTEEN = 16    # 和值15
    SUM_SIXTEEN = 17    # 和值16
    SUM_SEVENTEEN = 18  # 和值17
    # SUM_EIGHTEEN = 20   # 和值18
