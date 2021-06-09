def get_exchanges() -> Optional[Dict]:
    """
    Get the list of available exchanges.

    :returns: list of available exchanges
    """
    response = _query_cryptocompare(_URL_EXCHANGES)
    if response:
        return response['Data']
    return None
