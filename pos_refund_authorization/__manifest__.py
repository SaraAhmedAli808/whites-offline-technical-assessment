{
    'name': 'POS Refund Authorization',
    'version': '15.0',
    'author': "Sara Ahmed - WhatsApp : +201204453180",
    'depends': ['point_of_sale', 'hr'],
    'data': [
        'views/hr_employee_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_refund_authorization/static/src/js/refund_authorization.js',
        ],
    },
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
