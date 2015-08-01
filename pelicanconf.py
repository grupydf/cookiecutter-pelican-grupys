#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

# Configurações Base
SITENAME = u'Grupy-XYZ'
AUTHOR = u'Autor-Padrão'
THEME = "themes/malt"

# Referências à Github
GITHUB_REPO = "http://github.com/grupy-xyz/grupy-xyz.github.io"
GITHUB_BRANCH = "pelican"

# Imagens
ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_LOGO = "images/logo.png"
SITE_LOGO_MOBILE = "images/logo-mobile.png"

# Home settings
WELCOME_TITLE = "Seja bem vindo ao {}".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python em XYZ."
SITE_BACKGROUND_IMAGE = "images/banners/background.png"
FOOTER_ABOUT = "O Grupy-XYZ é uma comunidade de usuários... bla bla bla... "

# Tema do Syntax Hightlight
PYGMENTS_STYLE = "perldoc"

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        "title": "Comunidade",
        "href": "comunidade",
    },
    {
        "title": "Membros",
        "href": "membros",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
]

# Navbar Links do Blog
NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

# Links sociais do rodapé
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

# Membros do Grupy
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

from themes.malt.functions import *
