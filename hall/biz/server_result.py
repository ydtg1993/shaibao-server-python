from hall.models.hall import Result


def search_result(**params):
    result = Result.search_server(**params)
    result['ls'] = [{
        'hall__name': d['hall__name'],
        'sequence': d['sequence'],
        'bonus': d['bonus'],
        'bet_count': d['bet_count'],
        'result': d['result'],
        'big': d['big'],
        'even': d['even'],
        'sum': d['sum']
    } for d in result['ls']]
    return result
