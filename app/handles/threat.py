class ThreatStackError(Exception):
    '''Base Threat Stack error.'''
    status_code = 500

class ThreatStackRequestError(ThreatStackError):
    '''Threat Stack request error.'''

class ThreatStackAPIError(ThreatStackError):
    '''Threat API Stack error.'''


