#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

# Configurações Base
SITENAME = u'{{ cookiecutter.grupy_name }}'
AUTHOR = u'{{ cookiecutter.grupy_name }}'
THEME = "themes/malt"
MALT_BASE_COLOR = "{{ cookiecutter.template_color }}"

# Referências à Github
GITHUB_REPO = "http://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
GITHUB_BRANCH = "pelican"

# Imagens
ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_LOGO = "images/logo.png"
SITE_LOGO_MOBILE = "images/logo-mobile.png"

# Home settings
WELCOME_TITLE = "Seja bem vindo ao {}".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python."
SITE_BACKGROUND_IMAGE = "images/banners/background.png"
FOOTER_ABOUT = "O {{ cookiecutter.grupy_name }} é uma comunidade de usuários..."

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
        "href": "https://github.com/{{ cookiecutter.github_username }}",
        "icon": "fa-github",
        "text": "{{ cookiecutter.grupy_name }}",
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
    ("Nome Membro", {
        "twitter": "@membro",
        "github": "membro",
        "site": {
            "nome": "Site Membro",
            "href": "http://sitemembro.com",
            }
        }),
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "Nos comunicamos através de mailing " +\
                    "lists, grupo no telegram e no slack, mas frequentemente são " +\
                    "promovidos encontros diversos, como almoços, " +\
                    "<em>coding dojos</em> e palestras. ",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade {{ cookiecutter.grupy_name }}, apesar de extensa possui alguns " +\
                        "colaboradores principais, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": " Atualmente possuimos poucos projetos em andamento:" +\
                        "Traduções do Django-docs e Python on Campus.",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "projetos",
                    },
                ],
            },
        ]
    },
    {
        "color": "blue-grey lighten-4",
        "title": "Nosso Projetos",
        "items": [
            {
            "title": "MIG-29",
            "icon": "fa-fighter-jet",
            "text": "MIG-29 é um caça Russo cujo projeto original visava" +\
                    "superar o F-22 Raptor",
            "buttons": [
                    {
                        "text": "Código Fonte",
                        "href": "#",
                    },
                    {
                        "text": "Wiki",
                        "href": "#",
                    },
                ]
            },
            {
            "title": "SNES",
            "icon": "fa-gamepad",
            "text": "O Super Nintendo Entertainment Systems visa superar" +\
                    "o sucesso de seu antecessor, o NES.",
            "buttons": [
                    {
                        "text": "Site",
                        "href": "#",
                    },
                    {
                        "text": "Comprar",
                        "href": "#",
                    },
                ]
            }
        ]
    },
    {
        "color": "blue-grey lighten-5",
        "title": "Entre em Contato",
        "items": [
            {
            "title": "",
            },
            {
            "icon": "fa-envelope",
            "buttons": [
                    {
                        "text": "Envie um e-mail!",
                        "href": "#",
                    },
                ]
            }
        ]
    }
    ]

from themes.malt.functions import *
