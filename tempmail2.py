import string
import random
from hashlib import md5

import requests


class TempMail:
    """
    API Wrapper for service which provides temporary email address.

    :param api_key: RapidAPI key for authentication.
    :param login: (optional) login for email address.
    :param domain: (optional) domain (from current available)
    for email address.
    :param api_domain: (optional) domain for temp-mail api.
    Default value is ``privatix-temp-mail-v1.p.rapidapi.com``.
    """

    def __init__(self, api_key, login=None, domain=None, api_domain='privatix-temp-mail-v1.p.rapidapi.com'):
        self.login = login
        self.domain = domain
        self.api_domain = api_domain
        self.api_key = api_key

    def __repr__(self):
        return f'<TempMail [{self.get_email_address()}]>'

    @property
    def available_domains(self):
        """
        Return list of available domains for use in email address.
        """
        if not hasattr(self, '_available_domains'):
            url = f'https://{self.api_domain}/request/domains/'
            try:
                req = requests.get(url, headers={
                    'x-rapidapi-host': self.api_domain,
                    'x-rapidapi-key': self.api_key
                })
                req.raise_for_status()  # Raise exception for 4XX/5XX responses
                domains = req.json()
                setattr(self, '_available_domains', domains)
            except requests.exceptions.RequestException as e:
                raise ConnectionError(f"Error fetching available domains: {str(e)}")
            except ValueError:
                raise ValueError("Invalid JSON response when fetching domains")
        return self._available_domains

    def generate_login(self, min_length=6, max_length=10, digits=True):
        """
        Generate string for email address login with defined length and
        alphabet.

        :param min_length: (optional) min login length.
        Default value is ``6``.
        :param max_length: (optional) max login length.
        Default value is ``10``.
        :param digits: (optional) use digits in login generation.
        Default value is ``True``.
        """
        chars = string.ascii_lowercase
        if digits:
            chars += string.digits
        length = random.randint(min_length, max_length)
        return ''.join(random.choice(chars) for x in range(length))

    def get_email_address(self):
        """
        Return full email address from login and domain from params in class
        initialization or generate new.
        """
        if self.login is None:
            self.login = self.generate_login()

        available_domains = self.available_domains
        if self.domain is None:
            self.domain = random.choice(available_domains)
        elif self.domain not in available_domains:
            raise ValueError('Domain not found in available domains!')
        return f'{self.login}{self.domain}'

    def get_hash(self, email):
        """
        Return md5 hash for given email address.

        :param email: email address for generate md5 hash.
        """
        return md5(email.encode('utf-8')).hexdigest()

    def get_mailbox(self, email=None, email_hash=None):
        """
        Return list of emails in given email address
        or dict with `error` key if mail box is empty.

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = f'https://{self.api_domain}/request/mail/id/{email_hash}/'
        try:
            req = requests.get(url, headers={
                'x-rapidapi-host': self.api_domain,
                'x-rapidapi-key': self.api_key
            })
            req.raise_for_status()
            return req.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error fetching mailbox: {str(e)}")
        except ValueError:
            raise ValueError("Invalid JSON response when fetching mailbox")

    def delete_email(self, email=None, email_hash=None):
        """
        Delete a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = f'https://{self.api_domain}/request/delete/id/{email_hash}/'

        try:
            req = requests.get(url, headers={
                'x-rapidapi-host': self.api_domain,
                'x-rapidapi-key': self.api_key
            })
            req.raise_for_status()
            return req.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error deleting email: {str(e)}")
        except ValueError:
            raise ValueError("Invalid JSON response when deleting email")

    def get_attachments(self, email=None, email_hash=None):
        """
        Get attachments of a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()        
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = f'https://{self.api_domain}/request/atchmnts/id/{email_hash}/'

        try:
            req = requests.get(url, headers={
                'x-rapidapi-host': self.api_domain,
                'x-rapidapi-key': self.api_key
            })
            req.raise_for_status()
            return req.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error fetching attachments: {str(e)}")
        except ValueError:
            raise ValueError("Invalid JSON response when fetching attachments")

    def get_message(self, email=None, email_hash=None):
        """
        Get a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = f'https://{self.api_domain}/request/one_mail/id/{email_hash}/'

        try:
            req = requests.get(url, headers={
                'x-rapidapi-host': self.api_domain,
                'x-rapidapi-key': self.api_key
            })
            req.raise_for_status()
            return req.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error fetching message: {str(e)}")
        except ValueError:
            raise ValueError("Invalid JSON response when fetching message")


    def source_message(self, email=None, email_hash=None):
        """
        Source a given email in a given email address

        :param email: (optional) email address.
        :param email_hash: (optional) md5 hash from email address.
        """
        if email is None:
            email = self.get_email_address()
        if email_hash is None:
            email_hash = self.get_hash(email)

        url = f'https://{self.api_domain}/request/source/id/{email_hash}/'

        try:
            req = requests.get(url, headers={
                'x-rapidapi-host': self.api_domain,
                'x-rapidapi-key': self.api_key
            })
            req.raise_for_status()
            return req.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error fetching message source: {str(e)}")
        except ValueError:
            raise ValueError("Invalid JSON response when fetching message source")
