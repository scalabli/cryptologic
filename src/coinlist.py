def coin_list(format: bool = False) -> Union[Dict, List, None]:
    """
    Get the coin list (all available coins).

    :param format: format as python list (default: False)
    :returns: dict or list of available coins
    """
    response = _query_cryptocompare(_URL_COIN_LIST, False)
    if response:
        response = typing.cast(Dict, response['Data'])
        return list(response.keys()) if format else response
    return None

# TODO: add option to filter json response according to a list of fields


