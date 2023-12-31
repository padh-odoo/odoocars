{
    'name': 'Odoo Cars',
    'version': '1.0',
    'description':""" This is the Second module""",
    'category': 'Odoo Cars/odoocars',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'website': 'https://www.odoo.com/',
    'summary': 'This is Odoo Cars ',
    'depends': ['mail','hr'],
    'data':[
                  'secuirity/secuirity.xml',
                  'wizards/odoocars_wizard.xml',
                  'secuirity/ir.model.access.csv',
                  'views/car_category.xml',
                  'views/car_brand.xml',
                  'views/car_offer.xml',
                  'views/cars_view.xml',
                  'report/odoocars_report.xml',
                  'report/odoocars_template.xml',
     ],
    'demo':[
        'data/brand.type.csv',
        'data/car.categories.csv',
        'data/car.feature.csv',
    ]
}