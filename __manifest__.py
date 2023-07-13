{
    'name': 'Odoo Cars',
    'version': '1.0',
    'description':""" This is the Second module""",
    'category': 'Industry',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'website': 'https://www.odoo.com/',
    'summary': 'This is Odoo Cars ',
    'depends': ['mail'],
    'data':[
                  'secuirity/ir.model.access.csv',
                  'views/car_category.xml',
                  'views/car_fuel_type.xml',
                  'views/car_brand.xml',
                  'views/car_offer.xml',
                  'views/cars_view.xml',
     ],
    'demo':[
        'data/brand.type.csv',
        'data/car.categories.csv',
        'data/car.feature.csv',
    ]
}