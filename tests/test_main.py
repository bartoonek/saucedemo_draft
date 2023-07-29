from seleniumbase import BaseCase
from POM_auto.page_object_model import PageObject
#some text from pc
class Saucedemo(BaseCase):



    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")
        PageObject.open_page(self)
        PageObject.login(self)

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        PageObject.logout(self)
        super().tearDown()


    def test_saucedemo(self):
        PageObject.adding_items(self)

    def test_check_basket(self):
        PageObject.adding_items(self)
        PageObject.open_basket(self)
        self.assert_text("Sauce Labs Backpack", PageObject.backpack_text)
        self.assert_text("Sauce Labs Bike Light", PageObject.bike_light_text)
        self.assert_text("Sauce Labs Bolt T-Shirt", PageObject.tshirt_text)
