#!/usr/bin/env python2

import urllib2
import json

url = "http://sisbase.in-planet.net/api/datos/?id=%s"

def ip_address(id_sisbase):

    datos = { 'ip': None }

    try:
        datos = json.load(urllib2.urlopen(url % id_sisbase))

    except urllib2.HTTPError:
        pass

    return datos
