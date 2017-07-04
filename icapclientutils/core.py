#!/usr/bin/env python

import os
import sys
import socket

__default_port__ = 1344


class ErrorHandler(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Unknown error occurred"
        super(ErrorHandler, self).__init__(message)


class ICAPClientHandler:
    def __init__(self, host=None, port=None):
        if not host:
            raise ErrorHandler("Host is a mandatory parameter")

        self._host = host
        if not port:
            port = __default_port__
        self._port = port
        self.socket = None
        self.icap_method = None
        self.icap_service = None

    def set_icap_options(self, method='REQMOD', service='/'):
        self.icap_method = method
        self.icap_service = service

    def create_icap_headers(self, **kwargs):
        pass

    def set_http_req_options(self):
        pass

    def set_http_resp_options(self):
        pass

    def send_icap_request(self):
        self.socket = socket.socket()
        self.socket.connect(self._host, self._port)

    def get_icap_response(self):
        pass

