def get_pairs(exchange: str = None) -> Optional[Dict]:
    """
    Get the list of available pairs for a particular exchange or for 
    all exchanges (if exchange is None)

    :param exchange: exchange to use (default: None)
    :returns: list of available exchanges
    """
    if exchange is None:
        response = _query_cryptocompare(_URL_PAIRS.split('?')[0])

    else:
        response = _query_cryptocompare(_URL_PAIRS.format(exchange))
    if response:
        return response['Data']
    return None
