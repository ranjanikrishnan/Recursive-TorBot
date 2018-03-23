import requests

from bs4 import BeautifulSoup
from modules.bcolors import Bcolors
from requests.exceptions import ConnectionError, HTTPError
from sys import exit


def connection_msg(site):
    yield "Attempting to connect to {site}".format(site=site)


def read_first_page(site, extension=False):
    headers = {'User-Agent':
               'TorBot - Onion crawler | www.github.com/DedSecInside/TorBot'}
    attempts_left = 3
    err = " "
    while attempts_left:
        try:
            if not extension:
                print(next(connection_msg(site)))
                response = requests.get(site, headers=headers)
                print("Connection successful.")
                page = BeautifulSoup(response.text, 'html.parser')
                return page
            if extension and attempts_left == 3:
                print(next(connection_msg('https://'+site)))
                response = requests.get('https://'+site, headers=headers)
                print("Connection successful.")
                page = BeautifulSoup(response.text, 'html.parser')
                return page
            if extension and attempts_left == 2:
                print(next(connection_msg('http://'+site)))
                response = requests.get('http://'+site, headers=headers)
                print("Connection successful.")
                page = BeautifulSoup(response.text, 'html.parser')
                return page
            if extension and attempts_left == 1:
                msg = ''.join(("There has been an {err} while attempting to ",
                              "connect to {site}.")).format(err=err, site=site)
                exit(msg)

        except (HTTPError, ConnectionError) as e:
            attempts_left -= 1
            err = e

    if err == HTTPError:
        raise("There has been an HTTP error after three attempts.")
    if err == ConnectionError:
        raise("There has been a connection error after three attempts.")


def read_page(site, extension=False):
    headers = {'User-Agent':
               'TorBot - Onion crawler | www.github.com/DedSecInside/TorBot'}
    attempts_left = 3
    err = " "
    while attempts_left:
        try:
            if not extension:
                #print(next(connection_msg(site)))
                response = requests.get(site, headers=headers)
                #print("Connection successful.")
                page = BeautifulSoup(response.text, 'html.parser')
                return page
            if extension and attempts_left == 3:
                #print(next(connection_msg('https://'+site)))
                response = requests.get('https://'+site, headers=headers)
                #print("Connection successful.")
                page = BeautifulSoup(response.text, 'html.parser')
                return page
            if extension and attempts_left == 2:
                #print(next(connection_msg('http://'+site)))
                response = requests.get('http://'+site, headers=headers)
                #print("Connection successful.")
                page = BeautifulSoup(response.text, 'html.parser')
                return page
            if extension and attempts_left == 1:
                msg = ''.join(("There has been an {err} while attempting to ",
                              "connect to {site}.")).format(err=err, site=site)
                exit(msg)

        except (HTTPError, ConnectionError) as e:
            attempts_left -= 1
            err = e

    if err == HTTPError:
        raise("There has been an HTTP error after three attempts.")
    if err == ConnectionError:
        raise("There has been a connection error after three attempts.")


def get_ip():
    """Returns users tor ip address

    https://check.torproject.org/ tells you if you are using tor and it
    displays your IP address which we scape and return
    """

    b_colors = Bcolors()
    page = read_first_page('https://check.torproject.org/')
    pg = page.find('strong')
    ip_addr = pg.renderContents()

    return b_colors.WARNING+b_colors.BOLD+ip_addr.decode("utf-8")+b_colors.ENDC
