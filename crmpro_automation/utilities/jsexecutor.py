import traceback

from PyTestFramework.crmpro_automation.pages.base_fixture import BaseFixture

class JsExecutorMethods(BaseFixture):
    
    @staticmethod
    def js_scroll_into_view(locatortype, locator):
        try:
            element=BaseFixture.get_webelement(locatortype,locator)
            BaseFixture.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except:
            BaseFixture.log.error('Page is not scrolled till element with locator [' + locator + '] and locatortype ['+locatortype+']')
            print(traceback.format_exc())

    @staticmethod
    def js_click(locatortype, locator):
        try:
            if locatortype=='name':
                javascript="document.getElementsByName('"+locator+"')[0].click();"
            elif locatortype=='id':
                javascript="document.getElementById('"+locator+"').click();"
            elif locatortype=='xpath':
                element=BaseFixture.driver.find_element_by_xpath(locator)
                BaseFixture.driver.execute_script("arguments[0].click();", element)
            BaseFixture.driver.execute_script(javascript)
        except:
            BaseFixture.log.error('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is not clicked.')
            print(traceback.format_exc())
            
    @staticmethod
    def get_url():
        try:
            return BaseFixture.driver.execute_script('window.location.href')
        except:
            BaseFixture.log.error('URL is not retieved')
            print(traceback.format_exc())
        return None