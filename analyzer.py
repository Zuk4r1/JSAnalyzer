from __future__ import print_function 
import tornado.ioloop
import tornado.web
import tornado.autoreload
from tornado.escape import json_encode, json_decode

import safeurl
import types
import sys
import re
import mimetypes
import glob
import jsbeautifier
import urllib.parse as urlparse
import pycurl
import calendar
import time
import datetime

from netaddr import *
from collections import defaultdict
from bs4 import BeautifulSoup
from html import escape

BANNER = r"""
      ██╗███████╗  █████╗ ███╗   ██╗ █████╗  ██╗     ██╗ ███████╗███████╗██████╗  
      ██║██╔════╝ ██╔══██╗████╗  ██║██╔══██╗ ██║     ██║ ██╔════╝██╔════╝██╔══██╗
      ██║███████╗ ███████║██╔██╗ ██║███████║ ██║     ██║ ███████╗█████╗  ██████╔╝
 ██   ██║╚════██║ ██╔══██║██║╚██╗██║██╔══██║ ██║     ██║ ╚════██║██╔══╝  ██╔══██╗ 
 ╚█████╔╝███████║ ██║  ██║██║ ╚████║██║  ██║ ███████╗██║ ███████║███████╗██║  ██║ 
  ╚════╝ ╚══════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚══════╝══╝ ╚══════╝╚══════╝╚═╝  ╚═╝ 
         Herramienta de análisis y extracción de JavaScript
              version 1.0 - Creado with <3 by @Zuk4r1
"""

#------------------------------------------------------------
# Base / Status Code Handlers
#------------------------------------------------------------

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return []

    def write_error(self, status_code, **kwargs):
        if status_code in [403, 404, 500, 503]:
            self.render('templates/error.html', status_code=status_code)

class ErrorHandler(tornado.web.ErrorHandler, BaseHandler):
    def get_current_user(self):
        return
    pass

#------------------------------------------------------------
# /parse/ajax
#------------------------------------------------------------

class ViewParseAjaxHandler(BaseHandler):
    def fetchURL(self, url, headers=[]):
        sc = safeurl.SafeURL()
        if headers:
            newHeaders = []
            try:
                for header in json_decode(headers):
                    try:
                        header = header.split(":")
                        key = header.pop(0).strip()
                        val = ":".join(header).strip()
                        newHeaders.append("{0}: {1}".format(key, val))
                    except:
                        continue
            except:
                print("ignorando encabezados personalizados")
            if newHeaders:
                sc._handle.setopt(pycurl.HTTPHEADER, newHeaders)

        try:
            res = sc.execute(url)
            if isinstance(res, bytes):
                res = res.decode('utf-8', errors='ignore')  # Corrección aquí
            return res
        except pycurl.error as e:
            print(f"Error al obtener la URL: {e}")
            return ""

    def parseLinks(self, url, headers=[]):
        html = ""
        file = self.fetchURL(url, headers)
        if file:
            html += "<div>Contenido analizado</div>"
        return html

    def post(self):
        url = self.get_argument("url")
        headers = self.get_argument("headers", [])
        data = self.parseLinks(url, headers)
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode({"url": url, "output": data}))

#------------------------------------------------------------
# Main
#------------------------------------------------------------

settings = {
    'default_handler_class': ErrorHandler,
    'default_handler_args': dict(status_code=404),
}

urls = [
    (r"/", BaseHandler),
    (r"/parse/ajax", ViewParseAjaxHandler),
]

application = tornado.web.Application(urls, debug=True, **settings)

if __name__ == "__main__":
    portNum = input("Please enter the port number to use: ")
    try:
        portNum = int(portNum)
    except ValueError:
        print("Invalid port number. Using default port 8008.")
        portNum = 8008
    print(BANNER)
    application.listen(portNum)
    tornado.ioloop.IOLoop.current().start()
    def fetchURL(self, url, headers=[]):
        sc = safeurl.SafeURL()
        if headers:
            newHeaders = []
            try:
                for header in json_decode(headers):
                    try:
                        header = header.split(":")
                        key = header.pop(0).strip()
                        val = ":".join(header).strip()
                        newHeaders.append("{0}: {1}".format(key, val))
                    except:
                        continue
            except:
                print("ignorando encabezados personalizados")
            if newHeaders:
                sc._handle.setopt(pycurl.HTTPHEADER, newHeaders)

        try:
            res = sc.execute(url)
            if isinstance(res, bytes):
                res = res.decode('utf-8', errors='ignore')
            return res
        except pycurl.error as e:
            print(f"Error al obtener la URL: {e}")
            return ""

    def parseLinks(self, url, headers=[]):
        html = ""
        file = self.fetchURL(url, headers)
        html += self.fileRoutine(url, file)
        return html

    def post(self):
        error = False
        errorMsg = ""
        
        url = self.get_argument("url")
        headers = self.get_argument("headers", [])

        if not error:
            data = self.parseLinks(url, headers)
            self.set_header('Content-Type', 'application/json')
            self.write(json_encode({
                "url": url,
                "output": data,
            }))
        else:
            self.write("error")

#------------------------------------------------------------
# Main
#------------------------------------------------------------

portNum = int(sys.argv[sys.argv.index("-p")+1]) if "-p" in sys.argv else 8008

# Application Settings
settings = {
    'default_handler_class': ErrorHandler,
    'default_handler_args': dict(status_code=404),
}

# Endpoints
urls = [
    (r"/", MainHandler),
    (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": "images/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "js/"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "css/"}),
    (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": "fonts/"}),
    (r"/parse/ajax", ViewParseAjaxHandler),
    (r"/about", ViewAboutHandler),
]

application = tornado.web.Application(
    urls,
    debug=True,
    **settings
)

if __name__ == "__main__":
    portNum = input("Please enter the port number to use: ")
    try:
        portNum = int(portNum)
    except ValueError:
        print("Invalid port number. Using default port 8008.")
        portNum = 8008
    print(BANNER)
    application.listen(portNum)
    tornado.ioloop.IOLoop.current().start()
