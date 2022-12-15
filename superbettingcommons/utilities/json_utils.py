def dump_function(obj):
    try:
        return obj.__dict__
    except Exception:
        return str(obj)
