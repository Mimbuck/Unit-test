import unittest
from basket import Basket
import numbers

class BasketTests(unittest.TestCase):

    #setup method to create test object
    def setUp(self):
        print("setting up!")
        self.keijon_ostoskori = Basket("Keijo",["kissa","pasi"],20, 0.24)

    #teardown method to delete the test object
    def tearDown(self):
        print("tearing down!")
        del self.keijon_ostoskori
    
    #Lets test if variable customer is a string
    def test_customer_is_string(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.customer, str),"variable customer name should be string")

    #let's test if the variable contents is a list
    def test_contents_is_list(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.contents, list),"variable contents should be a list")

    #let's test if variable price is a number
    def test_price_is_number(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.price, numbers.Number), "variable price should be numbers")

    #let's test if add_product method works
    def test_list_add(self):
        self.keijon_ostoskori.add_product("kala",5)
        self.assertIn("kala",self.keijon_ostoskori.contents,"add_product did not add product to the list")

    #let's test if delete_product method works
    def test_list_delete(self):
        self.keijon_ostoskori.delete_product("kala",5)
        self.assertNotIn("kala",self.keijon_ostoskori.contents,"delete_product did not delete product from the list")

    #test average price
    def test_average_price(self):
        self.assertEqual(self.keijon_ostoskori.calculate_average_price(),10,"calculate_average_price does not calculate correct value")

    #test vat
    def test_vat(self):
        self.assertEqual(self.keijon_ostoskori.calculate_vat(),15.2,"calculate_vat does not calculate")

    #test vat is number
    def test_vat_is_number(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.vat, numbers.Number), "variable vat should be numbers")
    
if __name__=='__main__':
    unittest.main()
