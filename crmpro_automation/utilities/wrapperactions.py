import traceback
from selenium.webdriver.support.ui import Select
from PyTestFramework.crmpro_automation.utilities.explicitwaits import ExplicitWaits
from PyTestFramework.crmpro_automation.utilities.jsexecutor import JsExecutorMethods
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class ClickActions(ExplicitWaits):
    
    def click_element(self,locatortype, locator):
        flag=True
        try:
            ExplicitWaits.presence_of_element(locatortype, locator)
            #ExplicitWaits.visibility_of_element_located_by(locatortype, locator)
            #element is of type tuple so 0th index value is taken
            #JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            element=self.get_webelement(locatortype,locator)
            element.click()
            self.log.info('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is clicked.')
        except:
            flag=False
            self.log.error('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is not clicked.')
            print(traceback.format_exc())
        return flag
    
    def click_element_by_scrolling(self, locatortype, locator):
        flag=True
        try:
            ExplicitWaits.presence_of_element(locatortype, locator)
            #ExplicitWaits.visibility_of_element_located_by(locatortype, locator)
            #element is of type tuple so 0th index value is taken
            JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            element=self.get_webelement(locatortype,locator)
            element.click()
            self.log.info('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is clicked.')
        except:
            flag=False
            self.log.error('Element with locator ['+locator+'] and locatortype ['+locatortype+'] is not clicked.')
            print(traceback.format_exc())
        return flag

class InputActions(ExplicitWaits):
        
    def enter_text(self,locatortype, locator, value):
        flag=True
        try:
            # WebDriverWebMethods.presence_of_element(driver,locatortype, locator)
            #WebDriverWebMethods.visibility_of_element_located_by(driver, locatortype, locator)
            # element is of type tuple so 0th index value is taken
            element = self.get_webelement(locatortype, locator)
            #JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            self.clear_element_field(element)
            element.send_keys(value)
            self.log.info('Text is entered in element with locator ['+locator+'] and locatortype ['+locatortype+'].')
        except:
            flag=False
            self.log.error('Text is not entered in element with locator ['+locator+'] and locatortype ['+locatortype+'].')
            print(traceback.format_exc())
        return flag
    
    def enter_text_by_scrolling(self,locatortype, locator, value):
        flag=True
        try:
            # WebDriverWebMethods.presence_of_element(driver,locatortype, locator)
            #WebDriverWebMethods.visibility_of_element_located_by(driver, locatortype, locator)
            # element is of type tuple so 0th index value is taken
            element = self.get_webelement(locatortype, locator)
            JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            self.clear_element_field(element)
            element.send_keys(value)
            self.log.info('Text is entered in element with locator ['+locator+'] and locatortype ['+locatortype+'].')
        except:
            flag=False
            self.log.error('Text is not entered in element with locator ['+locator+'] and locatortype ['+locatortype+'].')
            print(traceback.format_exc())
        return flag

class SelectActions(ExplicitWaits):
     
    def select_by_visible_text(self, locatortype, locator, text):
        flag=True
        try:
            element=self.get_webelement(locatortype, locator)
            JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            select=Select(element)
            select.select_by_visible_text(text)
            self.log.info(str(text)+' is selected in element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag=False
            self.log.error(str(text)+' is not selected in element with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag

    def select_by_value(self,locatortype, locator, value):
        flag = True
        try:
            element = self.get_webelement(locatortype, locator)
            JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            select = Select(element)
            select.select_by_value(value)
            self.log.info(
                'Value is selected in element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag = False
            self.log.error(
                'Value is not selected in element with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag

    def select_by_index(self, locatortype, locator, index):
        flag = True
        try:
            element = self.get_webelement(locatortype, locator)
            JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            select=Select(element)
            select.select_by_index(index)
            self.log.info(
                'Value is selected in element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag = False
            self.log.error(
                'Value is not selected in element with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag

class ActionClass(ExplicitWaits):
    
    def move_to_element(self, locatortype, locator):
        flag=True
        try:
            actions = ActionChains(self.driver)
            element = self.get_webelement(locatortype, locator)
            actions.move_to_element(element).perform()
            self.log.info(
                'Mouse cursor is moved to element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag=False
            self.log.error(
                'Mouse cursor is not moved to element with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag
    
    def move_and_click_same_element(self, locatortype, locator):
        flag=True
        try:
            actions = ActionChains(self.driver)
            element = self.get_webelement(locatortype, locator)
            #JsExecutorMethods().js_scroll_into_view(locatortype, locator)
            actions.move_to_element(element).click(element).perform()
            self.log.info(
                'Mouse cursor is moved and clicked to element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag=False
            self.log.error
            ('Mouse cursor is not moved and clicked to element with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag
    
    def click_and_hold(self, locatortype, locator):
        flag=True
        try:
            actions=ActionChains(self.driver)
            element = self.get_webelement(locatortype, locator)
            actions.click_and_hold(element).perform()
            self.log.info('Element is clicked and held with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag=False
            self.log.info('Element is not clicked and held with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag
    
    def right_click(self, locatortype, locator):
        flag=True
        try:
            actions=ActionChains(self.driver)
            element = self.get_webelement(locatortype, locator)
            actions.context_click(element).perform()
            self.log.info('Right click is performed on element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag=False
            self.log.info('Right click is not performed on element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        return flag
    
    def double_click(self, locatortype, locator):
        flag=True
        try:
            actions=ActionChains(self.driver)
            element = self.get_webelement(locatortype, locator)
            actions.double_click(element).perform()
            self.log.info('Double click is performed on element with locator [' + locator + '] and locatortype [' + locatortype + '].')
        except:
            flag=False
            self.log.info('Double click is not performed on element with locator [' + locator + '] and locatortype [' + locatortype + '].')
            print(traceback.format_exc())
        return flag
    
    def drag_and_drop(self, source_locatortype, source_locator, dest_locatortype, dest_locator):
        flag=True
        try:
            actions=ActionChains(self.driver)
            source_element = self.get_webelement(source_locatortype, source_locator)
            dest_element = self.get_webelement(dest_locatortype, dest_locator)
            actions.drag_and_drop(source_element, dest_element).perform()
            self.log.info('Element is dragged and dropped.')
        except:
            flag=False
            self.log.info('Element is not dragged and dropped.')
            print(traceback.format_exc())
        return flag
    
    def drag_and_drop_by_offset(self, locatortype, locator, xoffset, yoffset):
        flag=True
        try:
            actions=ActionChains(self.driver)
            element = self.get_webelement(locatortype, locator)
            actions.drag_and_drop_by_offset(element, xoffset, yoffset).perform()
            self.log.info('Element is dragged and dropped by given offset.')
        except:
            flag=False
            self.log.info('Element is not dragged and dropped by given offset.')
            print(traceback.format_exc())
        return flag
    
    def key_down(self, key_type):
        '''Sends a key press only, without releasing it. Should only be used with modifier keys 
            (Control, Alt and Shift).'''
        flag=True
        key=None
        try:
            if key_type.upper()=='CONTROL': key=Keys.CONTROL 
            elif key_type.upper()=='SHIFT': key=Keys.SHIFT 
            elif key_type.upper()=='ALT': key=Keys.ALT
            actions=ActionChains(self.driver)
            actions.key_down(key).perform()
            self.log.info(key_type+' is clicked down.')
        except:
            flag=False
            self.log.info(key_type+' is not clicked down.')
            print(traceback.format_exc())
        return flag
    
    def key_up(self, key_type):
        '''Sends a key press only, without releasing it. Should only be used with modifier keys 
            (Control, Alt and Shift).'''
        flag=True
        key=None
        try:
            if key_type.upper()=='CONTROL': key=Keys.CONTROL 
            elif key_type.upper()=='SHIFT': key=Keys.SHIFT 
            elif key_type.upper()=='ALT': key=Keys.ALT
            actions=ActionChains(self.driver)
            actions.key_up(key).perform()
            self.log.info(key_type+' is clicked up.')
        except:
            flag=False
            self.log.info(key_type+' is not clicked up.')
            print(traceback.format_exc())
        return flag
    
    def copy(self):
        flag=True
        try:
            actions=ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
            self.log.info('Text is copied')
        except:
            flag=False
            self.log.info('Text is not copied')
            print(traceback.format_exc())
        return flag
    
    def cut(self):
        flag=True
        try:
            actions=ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
            self.log.info('Text is cut')
        except:
            flag=False
            self.log.info('Text is not cut')
            print(traceback.format_exc())
        return flag
    
    def pause_actions(self, seconds):
        flag=True
        try:
            actions=ActionChains(self.driver)
            actions.pause(seconds).perform()
            self.log.info('Actions are paused')
        except:
            flag=False
            self.log.info('Actions are not paused')
            print(traceback.format_exc())
        return flag
    
class AlertClass(ExplicitWaits):
    
    def accept(self):
        alert = Alert(self.driver)
        alert.accept()
        
    def dismiss(self):
        alert = Alert(self.driver)
        alert.dismiss()
    
    def alert_send_keys(self, text):
        alert = Alert(self.driver)
        alert.send_keys(text)
        
    def get_alert_text(self):
        return Alert(self.driver).text
    
class HandleIFrame(ExplicitWaits):
    
    def switch_to_frame_element(self, locatortype, locator):
        flag = True
        try:
            element=self.get_web_element(locatortype, locator)
            self.driver.switch_to.frame(element)
            self.log.info('Switched to iframe with locatortype: ['+locatortype+'] and locator: ['+locator+'].')
        except:
            flag=False
            self.log.info('Not switched to iframe with locatortype: ['+locatortype+'] and locator: ['+locator+'].')
            print(traceback.format_exc())
        return flag
            
    def switch_to_frame_index(self, index):
        flag = True
        try:
            self.driver.switch_to.frame(index)
            self.log.info('Switched to iframe with index: ['+index+'].')
        except:
            flag=False
            self.log.info('Not witched to iframe with index: ['+index+'].')
            print(traceback.format_exc())
        return flag
    
    def switch_to_frame_id(self, id):
        flag = True
        try:
            self.driver.switch_to.frame(id)
            self.log.info('Switched to iframe with id: ['+id+'].')
        except:
            flag=False
            self.log.info('Not witched to iframe with id: ['+id+'].')
            print(traceback.format_exc())
        return flag
        
    def switch_to_frame_name(self, name):
        flag = True
        try:
            self.driver.switch_to.frame(name)
            self.log.info('Switched to iframe with name: ['+name+'].')
        except:
            flag=False
            self.log.info('Not witched to iframe with name: ['+name+'].')
            print(traceback.format_exc())
        return flag
    
    def switch_to_first_frame(self):
        #Switches to first frame or main page
        self.driver.switch_to.default_content()
        self.log.info('Switched to first frame or main page')
    
    def switch_to_parent_frame(self):
        #Switches to first frame or main page
        self.driver.switch_to.parent_frame()
        self.log.info('Switched to parent frame of the current frame')