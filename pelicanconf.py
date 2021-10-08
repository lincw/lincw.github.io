#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'lincw'
SITENAME = '生物資料分析Bioinformatics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('ORCID', 'https://orcid.org/my-orcid?orcid=0000-0002-2509-0562'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Chung-Wen-Lin-2'),)

DEFAULT_PAGINATION = 10
DEFAULT_DATE = (2021, 10, 1, 13, 1, 1)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
