




class InventoryPage:

    URL_CURRENT = "/inventory.html"

    def __init__(self, driver):
        self.driver = driver
    
    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url

