import datetime
import config
import time
from robobrowser import RoboBrowser

def prepare_browser():
    br = RoboBrowser(parser = 'html.parser', history = True)
    return br

def check_all_balances(br):
#------------------- Get Turnpike Balance ---------------------------------------------------------
    print(get_turnpike_balance(br,
                                config.TURNPIKE_USERNAME,
                                config.TURNPIKE_PASSWORD))

def get_turnpike_balance(br, username, password):
    login_url = 'your login here'
    br.open(login_url)
    form = br.get_form(id = "login")
    form['username'] = username
    form['password'] = password
    br.session.headers['Referer'] = login_url
    br.submit_form(form)

    src = str(br.parsed())  # Source code as string
# ------------------------ Sample from source --------------------------------------
#    print(src)
#                Current Balance    $11.76            </td>'
    start = 'Current Balance    '
    end = '            </td>'
    result = str((src.split(start))[1].split(end)[0])
    ts = time.time()
    s_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    result = 'DATE: ' + s_date + '\nCurrent Balance: {0} \n\n'.format(result)
    return result

br = prepare_browser()
check_all_balances(br)
