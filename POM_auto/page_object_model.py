class PageObject():


    items_in_basket = ".shopping_cart_badge"
    backpack_text = "//div[contains(text(),'Sauce Labs Backpack')]"
    bike_light_text = "//div[contains(text(),'Sauce Labs Bike Light')]"
    tshirt_text = "//div[contains(text(),'Sauce Labs Bolt T-Shirt')]"

    def open_page(self):
        self.open('https://www.saucedemo.com/')

    def login(self):
        self.open('https://www.saucedemo.com/')
        self.add_text("#user-name", 'standard_user')
        self.add_text("#password", "secret_sauce")
        self.click("#login-button")

    def logout(self):
        self.click("#react-burger-menu-btn")
        self.click("#logout_sidebar_link")

    def adding_items(self):
        self.click("#add-to-cart-sauce-labs-backpack")
        self.click("#add-to-cart-sauce-labs-bike-light")
        self.click("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.assert_text("3", PageObject.items_in_basket)

    def open_basket(self):
        self.click(".shopping_cart_link")


