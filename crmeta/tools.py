import time
from datetime import datetime
from dateutil.parser import parse


def timeStampFromParsed(parsed: tuple) -> float:
    """
    """
    if isinstance(parsed, time.struct_time):
        result = datetime.fromtimestamp(time.mktime(parsed))
    elif isinstance(parsed, str):
        result = parse(parsed)
    else:
        result = parsed
    return result
