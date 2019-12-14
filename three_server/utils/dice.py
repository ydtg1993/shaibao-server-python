import random
from three_server.enums.dice_type import DiceType

sum_types = {
    3: None,
    4: DiceType.SUM_FOUR.value,
    5: DiceType.SUM_FIVE.value,
    6: DiceType.SUM_SIX.value,
    7: DiceType.SUM_SEVEN.value,
    8: DiceType.SUM_EIGHT.value,
    9: DiceType.SUM_NINE.value,
    10: DiceType.SUM_TEN.value,
    11: DiceType.SUM_ELEVEN.value,
    12: DiceType.SUM_TWELVE.value,
    13: DiceType.SUM_THIRTEEN.value,
    14: DiceType.SUM_FOURTEEN.value,
    15: DiceType.SUM_FIFTEEN.value,
    16: DiceType.SUM_SIXTEEN.value,
    17: DiceType.SUM_SEVENTEEN.value,
    18: None,
}


def create_result():
    result = [random.randint(1, 6) for _ in range(3)]
    # result = [6, 6, 6]
    sum_value = sum(result)
    wins = [
        DiceType.BIG.value if 11 <= sum_value <= 18 else DiceType.SMALL.value,
        DiceType.EVEN.value if sum_value % 2 == 0 else DiceType.SINGULAR.value
    ]
    result.sort()
    if sum_types[sum_value] is not None:
        wins.append(sum_types[sum_value])
    return {
        'result': result,
        'wins': wins
    }
