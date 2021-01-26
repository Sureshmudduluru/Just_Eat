from behave import given, when, then
from selenium import webdriver


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="\\Drivers\\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)

@when('Open Just-Eat homepage')
def openHomePage(context):
    context.driver.get("https://www.just-eat.co.uk/")

@then('Verify Just-Eat logo present on page')
def verifyLogoPresent(context):
    logo_title = context.driver.find_element_by_xpath("//a[@class='logo']//img[@class='logo-image']").get_attribute("alt")
    print(logo_title)

@then('Verify search results with an area code "{code}"')
def VerifySearchResults(context, code):
    context.driver.find_element_by_xpath("//input[@name='postcode']").send_keys(code)
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    search_result = context.driver.find_element_by_xpath("//span[@data-search-count='openrestaurants']").text
    print("Available restaurants: ", search_result)

@then('Verify search results with invalid area code "{code}"')
def VerifySearchResults(context, code):
    context.driver.find_element_by_xpath("//input[@name='postcode']").send_keys(code)
    context.driver.find_element_by_xpath("//button[@type='submit']").click()
    error_Message = context.driver.find_element_by_xpath("//div[@id='errorMessage']").text

    print("Error_Message: ", error_Message)

@then('Close browser')
def closeBrowser(context):
    context.driver.close()
