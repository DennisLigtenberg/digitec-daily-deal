
class Product:
    product_name = ""
    product_price = ""
    product_description = ""
    product_url = ""
    product_img = ""

    def __init__(self, name, price, description, url, img):
        self.product_name = name
        self.product_price = price
        self.product_description = description
        self.product_url = url
        self.product_img = img

    def get_product_name(self):
        return self.product_name

    def get_product_price(self):
        return self.product_price

    def get_product_description(self):
        return self.product_description

    def get_product_url(self):
        return self.product_url

    def get_product_img(self):
        return self.product_img
