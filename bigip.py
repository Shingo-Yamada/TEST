from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from bs4 import BeautifulSoup


login_name = 'admin'
login_pass = 'admin'
login_url  = 'https://10.15.2.80/'
tcp_url    = 'https://10.15.2.80/tmui/Control/jspmap/tmui/locallb/profile/tcp/list.jsp'

print("Start...\n")
des_cap = dict(DesiredCapabilities.PHANTOMJS)
des_cap['phantomjs.page.settings.userAgent'] = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/28.0.1500.52 Safari/537.36'
)

driver = webdriver.PhantomJS(desired_capabilities=des_cap, service_args=['--web-security=no', '--ignore-ssl-errors=yes'])
driver.set_window_size(800,700)
driver.get(login_url)  # Set login URL
driver.save_screenshot('01.png')

# Set login Username and Password
loginid = driver.find_element_by_id('username')
password = driver.find_element_by_id('passwd')
loginid.send_keys(login_name)
password.send_keys(login_pass)
driver.save_screenshot('02.png')
# Click Login Button
driver.find_element_by_xpath("//button[@type='submit' and @tabindex='3']").click()
driver.save_screenshot('03.png')
# Get HTML Soruce
wait = WebDriverWait(driver, 3)
wait.until(ec.presence_of_all_elements_located)
soup = BeautifulSoup(driver.page_source, "html.parser")
# HTML Parser
links = soup.find_all('a')
for link in links:
    if 'href' in link.attrs:
        print(link.text, ':', link.attrs['href'])


driver.save_screenshot('04.png')
print("\nFinished\n")
driver.quit()
