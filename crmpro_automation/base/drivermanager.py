from abc import ABC, abstractmethod

class DriverManager(ABC):
    driver=None
    
    @abstractmethod
    def start_service(self):
        pass
    
    @abstractmethod
    def stop_service(self):
        pass
    
    @abstractmethod
    def create_driver(self):
        pass
    
    def quit_driver(self):
        if self.driver!=None:
            self.driver.quit()
            self.driver==None
    
    def close_driver(self):
        if self.driver!=None:
            self.driver.close()
            self.driver==None
            
    def get_driver(self):
        if self.driver==None:
            print('################ First time Starting service')
            self.start_service()
            self.create_driver()
        else:
            print('################ Only creating driver')
            #self.start_service()
            self.create_driver()
        return self.edriver