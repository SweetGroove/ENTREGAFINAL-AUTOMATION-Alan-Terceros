from page.login_page import LoginPage

def test_login(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login()
    