from selenium import webdriver
import time

link=("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
browser=webdriver.Chrome()
browser.get(link)

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")