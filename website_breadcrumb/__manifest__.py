# -*- coding: utf-8 -*-

{
    "name": "Website Breadcrumbs",
    "summary": "Breadcrumbs in website pages",
    "version": "10.0.1.0.0",
    "category": "Website",
    "author": "Andrey Semko (andriisem)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website",
    ],
    "data": [
        'views/snippet_breadcrumb.xml',
    ],
    "qweb": [
        'static/src/xml/breadcrumbs.xml',    
    ],
}
