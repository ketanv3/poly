class PolyException(Exception):
    def __init__(self, reason, *args, **kwargs):
        self.reason = reason
        super(*args, **kwargs)
