import datetime
import config
import re
import time

from robobrowser import RoboBrowser


def prepare_browser():
    br = RoboBrowser(parser='html.parser')
    return br


def check_all_balances(br):
    print(get_datacoup_balance(br,
                               config.DATACOUP_USERNAME,
                               config.DATACOUP_PASSWORD))
    print(get_starbucks_balance(br,
                                config.STARBUCKS_CARD_NUMBER,
                                config.STARBUCKS_CARD_PIN))


def get_datacoup_balance(br, username, password):

    br.open("https://datacoup.com/signin")
    form = br.get_form()
    form['email'] = username
    form['password'] = password
    br.submit_form(form)

    src = str(br.parsed())

    start = '<li class="header-bal">Earned: '
    end = '</li>'

    result = re.search('%s(.*)%s' % (start, end), src).group(1)

    ts = time.time()
    s_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    result = 'DATE: ' + s_date + '\nDATACOUP BALANCE: {0} \n\n'.format(result)
    return result


def get_starbucks_balance(br, username, password):

    br.open("https://www.starbucks.ca/card")
    form = br.get_form(id="CheckBalance")   
    form['Card.Number'] = username
    form['Card.Pin'] = password
    br.submit_form(form)
    
    src = str(br.parsed())
    start = '<h2><span class="fetch_balance_value">'
    end = '</span>'
    result = re.search('%s(.*)%s' % (start, end), src).group(1)

    ts = time.time()
    str_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    result = 'DATE: ' + str_date + '\nSTARBUCKS BALANCE: {0} \n\n'.format(result)
    return result 


br = prepare_browser()

check_all_balances(br)


