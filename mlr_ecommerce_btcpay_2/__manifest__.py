{
    "name": "MLR ecommerce BTCPay 2",
    "summary": "MLR ecommerce BTCPay 2",
    "author": "ERP",
    "website": "https://www.milightningrod.com",
    "category": "Ecommerce",
    "version": "1.0",
    "depends": ["website", "mlr_ecommerce_cryptopayments"],
    "data": [
        "views/btcpay_payment_template.xml",
        "data/btcpay_payment_method_data.xml",  
        "data/btcpay_payment_provider_data.xml",
        "views/btcpay_payment_form.xml",
        "views/btcpay_payment_provider.xml",

    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    "license": "OPL-1",
}
