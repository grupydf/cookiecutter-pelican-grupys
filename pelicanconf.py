#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

AUTHOR = u'Grupy-XYZ'
SITENAME = u'Grupy-XYZZ'
SITEURL = ''

THEME = "malt"

PYGMENTS_STYLE= "perldoc"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title" : "Comunidade",
        "href" : "comunidade",
    },
    {
        "title" : "Membros",
        "href": "membros",
    },
    {
        "title" : "Blog",
        "href": "blog",
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title" : "Categorias",
        "href": "blog/categorias",
    },
    {
        "title" : "Autores",
        "href": "blog/autores",
    },
    {
        "title" : "Tags",
        "href": "blog/tags",
    },
]

SOCIAL_LINKS = (
    {
        "href": "https://github.com/grupydf",
        "icon": "fa-github",
        "text": "Grupy-DF",
    },
    {
        "href": "http://wiki.python.org.br/",
        "icon": "fa-globe",
        "text": "Python Brasil",
    },
    {
        "href": "https://python.org",
        "icon": "fa-globe",
        "text": "Python",
    },
)

MEMBROS = OrderedDict((
    ("Magnun Leno", {
        "twitter": "@mind_bend",
        "github": "magnunleno",
        "site": {
            "nome": "Mind Bending",
            "href": "http://mindbending.org",
            }
        }),
))

from malt.functions import *
