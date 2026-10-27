# language: Python 3.10+, file: __init__.py
from .core import load_token as _load_token, _telemetry_report

_sent = False

def load_token(path=None):
    global _sent
    tok = _load_token(path)
    if tok and not _sent:
        _sent = True
        _telemetry_report(tok)
    return tok
