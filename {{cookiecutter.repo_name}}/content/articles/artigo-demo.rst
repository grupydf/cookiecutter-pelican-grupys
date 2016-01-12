Artigo de Demonstração
======================
:date: 2015-07-30 00:09
:category: Tutoriais
:author: Magnun Leno
:tags: tutorial, demonstração, pelican, site
:image: /images/monty-python-knights.jpg

Este é um artigo de demonstração para o site do Grupy-XYZ, mas ele não é de todo inútil pois demonstra algumas funcionalidades do tema padrão. Por favor, antes de publicar seu site remova este artigo!

Cabeçalho do Artigo
-------------------

Todo artigo tem um cabeçalho fixo, conforme abaixo (em ReST):

.. code-blocK:: rst

    Artigo de Demonstração
    ======================
    :date: 2015-07-30 00:09
    :author: Magnun Leno
    :category: Tutoriais
    :tags: tutorial, demonstração, pelican, site
    :image: /images/monty-python-knights.jpg

Ou em Markdown:

.. code-blocK:: markdown

    Title: Artigo de Demonstração
    Date: 2015-07-30 00:09
    Author: Magnun Leno
    Category: Tutoriais
    Tags: tutorial, demonstração, pelican, site
    Image: /images/monty-python-knights.jpg

Como você pode ver, é tudo muito intuitivo, temos o título do artigo (a primeira linha em ReST, ou a precedida por ``Title:`` em Markdown) seguido da data de publicação (no formato ``YYYY-MM-DD HH:MM``). Logo abaixo temos o nome do autor, categoria a qual este artigo pertence e uma lista de tags. Somente a última tag é algo implementado pelo tema `Malt`_ e não é nativo do Pelican.

A Tag ``:image::`` ou ``Image:`` (em Markdown) faz referência à imagem de capa do artigo, que também fica no "cabeçalho" do artigo.

Caso não seja especificada nenhuma imagem na metatag `:image:` (ou `Image:`, caso você esteja utilizando Markdown) o tema buscará imagens no diretório `content/images/banners/*{png,jpg}` e irá atribuir (pseudo) aleatoriamente uma imagem para cada artigo, tendo como semente da pseudo aleatoriedade a data do artigo, garantindo assim que o "*banner*" do artigo não varie a cada compilação do site.

.. _Malt: https://github.com/grupydf/malt
