#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Cesar Sepulveda'
SITENAME = 'csepulveda.io'
SITEURL = 'https://blog.csepulveda.io'

PATH = 'content'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Github', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/csepulvedab/'),
    ('github', 'https://github.com/csepulveda'),
    ('instagram', 'https://instagram.com/csepulvedab/'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Peli-Kiera'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']
SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10


DISQUS_SITENAME = "csepulveda"
GOOGLE_ANALYTICS = "G-YPBW8TZ5KS"