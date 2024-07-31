
{
    'name': 'Remove Powered By Odoo',
    'version': '16.0.3',
    'author': 'Muhammad Mubeen',
    'license': 'LGPL-3',
    'category': 'Email',
    'website': 'https://www.dsmpk.com',
    'images': ['static/description/banner.png'],
    'summary': 'Remove Powered By Odoo',
    'description': """Remove power by odoo on footer of emails and the website""",
    'depends': ['base', 'mail', 'web','account'],
    'data': [
        'views/mail_template_remove_odoo_views.xml',
        'views/website_footer_brand_promotion.xml'
    ],
    'installable': True,
    'support': 'm.mubeen1020@gmail.com',
    'application': True,
}
