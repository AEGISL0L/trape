#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
#########
# trape #
#########
#
# GeoIP lookup using MaxMind GeoLite2 local database
# For full copyright information this visit: https://github.com/jofpin/trape
#
#**
import os

try:
    import geoip2.database
except ImportError:
    geoip2 = None

_reader = None

def _get_reader():
    global _reader
    if _reader is not None:
        return _reader
    db_path = os.environ.get('GEOIP_DB_PATH', 'GeoLite2-City.mmdb')
    if os.path.exists(db_path) and geoip2 is not None:
        try:
            _reader = geoip2.database.Reader(db_path)
        except Exception:
            _reader = None
    return _reader

def lookup(ip):
    result = {
        'ip': ip,
        'city': 'Unknown',
        'country_code2': 'XX',
        'country_code3': 'XXX',
        'country_name': 'Unknown',
        'latitude': 0,
        'longitude': 0,
        'isp': 'Unknown',
        'state_prov': 'Unknown',
        'zipcode': '',
        'organization': 'Unknown'
    }
    reader = _get_reader()
    if reader is None:
        return result
    try:
        resp = reader.city(ip)
        result['city'] = resp.city.name or 'Unknown'
        result['country_code2'] = resp.country.iso_code or 'XX'
        result['country_name'] = resp.country.name or 'Unknown'
        result['latitude'] = resp.location.latitude or 0
        result['longitude'] = resp.location.longitude or 0
        if resp.subdivisions and len(resp.subdivisions) > 0:
            result['state_prov'] = resp.subdivisions.most_specific.name or 'Unknown'
        if resp.postal and resp.postal.code:
            result['zipcode'] = resp.postal.code
        # GeoLite2-City doesn't include ISP/ASN; keep defaults
    except Exception:
        pass
    return result
