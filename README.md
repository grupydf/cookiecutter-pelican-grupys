# Cookiecutter Pelican Grupys

Este é um cookiecutter de pelican para os grupos locais de python poderem criar facilmente uma página usando pelican.

Requerimentos:

- Python >= 2.7;
- [Cookiecutter](https://github.com/audreyr/cookiecutter);
- Pelican 2.6;
- Tema [Malt](https://github.com/grupydf/malt);

## Instalação & Utilização

Rode o cookiecutter para realizar o bootstrap do projeto:

```
$ pip install cookiecutter
$ cookiecutter gh:grupydf/cookiecutter-pelican-grupys
grupy_name [Grupy-XYZ]: 
template_color [blue-grey]: 
github_username [grupy-xyz]: 
repo_name [grupyxyz.github.io]:
```

Acesse a página gerada, crie uma virtualenv e instale os requerimentos:

```
$ cd grupyxyz.github.io
$ pip install virtualenvwrapper
$ mkvirtualenv grupyxyz
$ pip install -r requirements.txt
```

Em seguida clone o tema usado na pasta de templates

```
$ git clone git@github.com:grupydf/malt.git themes/malt 
```

Agora basta compilar e servir o site:


```
$ make html serve
```

Para um tutorial mais detalhado leia o [artigo do Grupy-DF](http://grupydf.github.io/blog/como-publicar-no-blog-do-grupy-df/).

## Plugins & Tema

Boa parte das funcionalidades "visuais" dos sites são implementadas no tema, através de *templates* Jinja2 e funções em Python. Para uma lista completa de funcionalidades leia a documentação do tema [Malt](https://github.com/grupydf/malt).

Já a parte funcional do site é controlada por plugins (todos localizados no diretório `.plugins`), neste "Site Demo" estão ativos os seguintes plugins:

- *Better Figures and Images*: Adiciona informações de tamanho de imagens automaticamente;
- *Sitemap*: Gera um sitemap para o site;

## Licença

```
Cookiecutter Pelican Grupys
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
```
