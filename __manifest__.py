{
    'name'          : 'Monstar Sales',
    'author'        : 'MLES',
    'version'       : '1.0.0',
    'category'      : 'accounting',
    'depends'       : ['account',
                        'sale_management',

    ],
    'data'          : [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml'
    ],
    'installable'   : True,
    'auto_install'  : False
}
