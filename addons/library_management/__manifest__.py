{
    'name': "Library Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ronald León",
    'category': 'Library',
    'summary': ' Manage library members, books and loans',
    'description': "",
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/book_views.xml',
        'views/loan_views.xml',
        'views/member_views.xml',
    ],
    'installable': True,
    'application': True,
}
