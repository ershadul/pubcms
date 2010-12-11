# -*- coding: utf-8 -*-
import urllib

from django import template
from pubcms import utils

register = template.Library()

@register.filter
def bengalinumber(value):
    return utils.convert_e2b(value)

@register.filter
def tinyurl(url):
    url = 'http://www.alqualam.com' + url
    try:
        apiurl = "http://tinyurl.com/api-create.php?url="        
        tiny_url =  urllib.urlopen(apiurl + url).read()
    except:
        return url
    return tiny_url
