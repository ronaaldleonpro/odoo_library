{
    'name': "Library Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ronald León",
    'category': 'Library',
    'summary': 'Manage library members, books and loans',
    'description': "",
    'data': [
        'security/ir.model.access.csv',
        'views/member_views.xml',
        'views/book_views.xml',
        'views/loan_views.xml',
        'views/menu_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
