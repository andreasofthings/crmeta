def timeStampFromParsed(parsed: tuple) -> float:
    import time
    import datetime
    from dateutil.parser import parse

    if isinstance(parsed, time.struct_time):
        return datetime.fromtimestamp(time.mktime(parsed))
    elif isinstance(parsed, str):
        return parse(parsed)
    else:
        return parsed
