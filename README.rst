Template para Grupys-BR
=======================

Este é um "Site Demo" para ser utilizado como base pelos Grupys-BR.

Requerimentos:

- Python >= 2.7;
- Pelican 2.6;
- Tema `Malt`_;

Instalação & Utilização
-----------------------

Para utilizar este demo para o *bootstrap* do seu GrupyBR primeiramente faça um *fork* do projeto e em seguida clone-o em sua máquina local:

.. code::

    $ git clone --recursive git@github.com:magnunleno/grupybr-template.git && cd grupybr-template


Em seguida crie um *Virtual Environment* e instale todos os pré-requisitos do Pelican:

.. code::

    $ mkdir ~/venv
    $ virtualenv --prompt "(grupybr)" ~/venv/grupybr
    $ . ~/venv/grupy-df/bin/activate
    $ pip install -r requirements.txt

Agora basta compilar e servir o site:

.. code::

    $ make html serve

Para um tutorial mais detalhado leia o `artigo do Grupy-DF`_.

Plugins & Tema
--------------

Boa parte das funcionalidades "visuais" dos sites são implementadas no tema, através de *templates* Jinja2 e funções em Python. Para uma lista completa de funcionalidades leia a documentação do tema `Malt`_.

Já a parte funcional do site é controlada por plugins (todos localizados no diretório `.plugins`), neste "Site Demo" estão ativos os seguintes plugins:

- *Better Figures and Images*: Adiciona informações de tamanho de imagens automaticamente;
- *Sitemap*: Gera um sitemap para o site;

Licença
-------

.. code::

    Site Demo para o Grupys-BR
    Copyright (C) 2015  Magnun Leno

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

.. _Malt: https://github.com/grupydf/malt
.. _artigo do Grupy-DF: http://grupydf.github.io/blog/como-publicar-no-blog-do-grupy-df/
