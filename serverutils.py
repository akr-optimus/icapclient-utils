"""This module is for the ICAP Server methods
"""

from socketserver import TCPServer, StreamRequestHandler


class ICAPError(Exception):
    def __init__(self):
        pass


class ICAPServer(TCPServer):
    def __init__(self):
        pass


class ICAPStreamRequestHandler(StreamRequestHandler):
    def __init__(self):
        pass
