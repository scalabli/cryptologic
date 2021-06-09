def get_average(coin: str, currency: str = CURRENCY, exchange: str = 'CCCAGG') -> Optional[Dict]:
    """
    Get the average price

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param exchange: exchange to use (default: 'CCCAGG')
    :returns: dict of coin and currency price pairs
    """
    response = _query_cryptocompare(_URL_AVG.format(
        coin, currency, _format_parameter(exchange)))
    if response:
        return response['RAW']
    return None
