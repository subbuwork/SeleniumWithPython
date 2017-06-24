from PO.Am import Search
from PO.Am import Product
from PO.Am import Cart
from Common import HomePage


def open_home_page(setup,url, product_name):
    HomePage.Homepage(setup).open_home_page(url, product_name)


def search_product(setup, product_name):
    Search.ProductSearch(setup).search_product(product_name)


def select_product(setup):
    Search.ProductSearch(setup).select_product()


def add_to_cart(sertup):
    Product.ProductCart(sertup).add_product_to_cart()


def verify_cart(setup):
    Cart.ProductCart(setup).verify_cart()


def proceed_to_checkout(setup):
    Cart.ProductCart(setup).proceed_to_check_out()
