Tempmail2
=========

Python API Wrapper version 2 for `temp-mail.org <https://temp-mail.org/>`_ service. Temp-mail.org is a service which lets you use anonymous emails for free. You can view full API specification in `api.temp-mail.org <http://api.temp-mail.org/>`_.

Requirements
------------

`requests <https://pypi.org/project/requests/>`_ - required.

You can install it through ::

 $ pip install requests

Installation
------------

Installing with pip::

    $ pip install tempMail2

Usage
-----

Before you can use this, you need to get an API key from https://rapidapi.com/Privatix/api/temp-mail.

So create an account on RapidAPI and get the RapidAPI Key for the Temp Mail API.

Get all emails from given email login and domain::

    from tempmail2 import TempMail

    tm = TempMail(api_key='apikey', login='denis', domain='@cevipsa.com')
    print(tm.get_mailbox())  # list of emails in denis@cevipsa.com

Generate email address and get emails from it::

    from tempmail2 import TempMail

    tm = TempMail(api_key='apikey')
    email = tm.get_email_address()  # v5gwnrnk7f@cevipsa.com
    print(tm.get_mailbox(email))  # list of emails
