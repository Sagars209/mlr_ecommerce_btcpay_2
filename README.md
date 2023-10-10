# mlr_ecommerce_btcpay_2
Lightning Rod Ecommerce BTCpay Readme

Overview
This custom module for Odoo 16+ adds BTCpay server as a payment provider to the Ecommerce application. BTCpay server is a potentially self-hosted Bitcoin payment gateway/provider which is queried by API calls from Odoo. BTCpay server account access by API is provided to Odoo and a Bitcoin onchain/lightning option is added to the customer by checkout portal link. If the Bitcoin payment option is selected by a customer, they are forwarded to a BTCpay site with a created invoice and QR code for payment. After the payment is confirmed the customer can be redirected back to the Odoo online store receipt page and the order is registered and queued.

Prerequisites (versions)
<br>Compatible with Odoo 16
<br>Postgres 14+
<br>Nodeless.io account
<br>mlr_ecommerce_cryptopayments custom module

Installation (see this video for tutorial on Odoo module installation)
1. Download repository and place extracted folder in the Odoo addons folder.
2. Login to Odoo database to upgrade and enable developer mode under settings.
3. Under apps Update the App list.
4. Search for the module (MLR) and install.

Setup

1. In Odoo navigate to Website-> Ecommerce -> Payment Providers.
2. Click on BTCpay to open the record.
4. Enter a Name for the Instance. 
5. Login into your BTCpay server and navigate to Account -> API Key. Create a key for use with Odoo.
6. From BTCpay server copy the following information and paste in the Odoo Instance record: the server base URL, API key, and store ID.
7. Click Connect to BTCpay to verify the information is correct. If it is correct a green popup will affirm so, if it is incorrect a red popup will appear.
9. In Configuration -> Payment Form select the icon for lightning, in Configuration -> Payment Followup select the Payment Journal.
10. Select Enable to make BTCpay instance a current method and save (the first time a new Accounting Journal BTCpay will be created and used for recording transactions).
   

Operation
1. A customer will navigate to the Shop section of the website and add items to the cart. After initiating the checkout and filling in customer information the available payment methods will be displayed.
3. The customer can select the Bitcoin option and directions will appear below.
4. After clicking Pay Now  the customer will be taken to a BTCpay server page with the invoice and QR code to be paid.
5. The customer scans the QR code or pastes the invoice text as a send from their wallet.
6. Upon BTCpay server confirmation of the order the customer will have a button to click or be returned automatically to the receipt page of the Odoo site.
8. Odoo will process the order and create a sales order for fulfillment.

