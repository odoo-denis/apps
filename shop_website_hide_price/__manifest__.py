# -*- coding: utf-8 -*-
{
    'name': "E-commerce shop hide public price",

    'summary': 'Hide public price in website shop',

    'description': """Hide public price in website shop
""",

    'author': "Denis Gonzalez",
    'website': "http://innscience.ca",
    'category': 'E-commerce',
    'version': '12.0.0.1',
    'installable': True,
    'license': 'LGPL-3',
	'support':'grmdenis@gmail.com',

    # any module necessary for this one to work correctly
    'depends': ['website'],
    'data': [
        'views/templates.xml',
    ],
}
