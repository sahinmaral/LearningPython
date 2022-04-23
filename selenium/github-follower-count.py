from selenium import webdriver
import time
import pwinput

# Sign-in kismina gir
# Username veya email gir
# Sifre gir
# (Kontrol) Eger sifre yanlis hatasi gorursek burda programi durdur
# Profil resmine tikla , cikan menuden your profile secenegine tikla
# Following kisminin solunda cikan yaziyi al

# username_email = input('Enter username or email : ')
# password = input('Enter password : ')

username_email = input('Email veya kullanici adi giriniz : ')
password=pwinput.pwinput('Sifre giriniz : ')

driver = webdriver.Edge()

driver.get('http://github.com')
driver.maximize_window()

time.sleep(2)

login_link = driver.find_element_by_link_text('Sign in')
login_link.click()

time.sleep(2)

driver.find_element_by_name('login').send_keys(username_email) # username-email-input

driver.find_element_by_name('password').send_keys(password) # password-input

driver.find_element_by_name('commit').click()

time.sleep(2)

if len(driver.find_elements_by_css_selector('.flash .flash-full .flash-error')) > 0:
    print('Yanlis kullanici adi veya sifresi girdiniz')
    exit()



driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[1]').click()
time.sleep(2)

following_count = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[2]/span')
print(following_count.text + ' tane takipciniz var')

driver.close()


