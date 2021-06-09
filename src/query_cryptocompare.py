import quo

def _query_cryptocompare(url: str, errorCheck: bool = True, api_key: str = None) -> Optional[Dict]:
    """
    Query the url and return the result or None on failure.

    :param url: the url
    :param errorCheck: run extra error checks (default: True)
    :returns: respones, or nothing if errorCheck=True
    :api_key: optional, if you want to add an API Key
    """
    api_key_parameter = _set_api_key_parameter(api_key)
    try:
        response = requests.get(url + api_key_parameter).json()
    except Exception as e:
        quo.echo('Error getting coin information. %s' % str(e))
        return None
    if errorCheck and (response.get('Response') == 'Error'):
        quo.echo('[ERROR] %s' % response.get('Message'))
        return None
    return response
