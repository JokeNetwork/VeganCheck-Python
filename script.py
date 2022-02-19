import requests
import openfoodfacts
import configparser

# Product EAN
barcode = input("Please enter a barcode: ")

# Define all variables
product_name = None
vegan = None
response = None

if not barcode:
    response = "Barcode can not be empty!"
else:
    # Check if OFF has the product in their db
    # Test: 4251105515388
    if openfoodfacts.products.get_product(barcode)['status'] == 1:
        product = openfoodfacts.products.get_product(barcode)
        if "product_name" in product['product']:
            product_name = product['product']['product_name']
        elif "generic_name" in product:
            product_name = product['product']['generic_name']
        else:
            product_name = "Unknown"
        if "ingredients_analysis_tags" in product['product']:
            array = product['product']['ingredients_analysis_tags']
            if "en:vegan" in array:
                vegan = True
            elif "en:non-vegan" in array:
                vegan = False
            else:
                vegan = "Unknown"
        else:
            vegan = "Unknown"
    # Check if OBF has the product in their db
    # Test: 4305615620473
    elif openfoodfacts.beauty_products.get_product(barcode)['status'] == 1:
        product = openfoodfacts.beauty_products.get_product(barcode)
        if "product_name" in product['product']:
            product_name = product['product']['product_name']
        elif "generic_name" in product:
            product_name = product['product']['generic_name']
        else:
            product_name = "Unknown"

        if "ingredients_analysis_tags" in product:
            array = product['product']['ingredients_analysis_tags']
            if "en:vegan" in array:
                vegan = True
            elif "en:non-vegan" in array:
                vegan = False
            else:
                vegan = "Unknown"
        else:
            vegan = "Unknown"
    # Check if Brocade.io has the product in their db
    # Test: 00011194360535
    elif openfoodfacts.beauty_products.get_product(barcode)['status'] == 0 and openfoodfacts.products.get_product(barcode)['status'] == 0:
        reqUrl = "https://www.brocade.io/api/items/"+barcode
        response = requests.request("GET", reqUrl)
        if "name" in response.json():
            product_name = response.json()['name']
            if "ingredients" in response.json():
                ingredients = response.json()['ingredients']
                reqUrl = "https://api.vegancheck.me/v0/ingredients?ingredients="+ingredients
                response = requests.request("GET", reqUrl)
                vegan = response.json()['data']['vegan']
                if vegan == "true":
                    vegan = True
                else:
                    vegan = False
            else: 
                vegan = "Unknown"
        # Check if Open EAN DB has the product in their db
        # Test: 0079163889067
        else:
            with open('.env', 'r') as f:
                config_string = '[DEFAULT]\n' + f.read()
            config = configparser.ConfigParser()
            config.read_string(config_string)
            queryid = config.get('DEFAULT', 'USER_ID_OEANDB')
            reqUrl = "https://opengtindb.org/?ean="+barcode+"&cmd=query&queryid="+queryid
            get = requests.request("GET", reqUrl)
            string = get.text
            get = '[apicall]\n' + string
            config_string = get.replace("---", "")
            config = configparser.ConfigParser()
            config.read_string(config_string)
            if config.get('apicall', 'error') == "0":
                product_name = config.get('apicall', 'name')
                if config.get('apicall', 'descr'):
                    ingredients = config.get('apicall', 'descr')
                    reqUrl = "https://api.vegancheck.me/v0/ingredients?ingredients="+ingredients
                    response = requests.request("GET", reqUrl)
                    vegan = response.json()['data']['vegan']
                    if vegan == "true":
                        vegan = True
                    else:
                        vegan = False
                else:
                    vegan = "Unknown"
            else:
                response = False


if response == False:
    print("Product not in db! :(")
elif vegan == True:
    print(product_name + " is vegan!")
elif vegan == False:
    print(product_name + " is not vegan :(")
elif vegan == "Unknown":
    print("We dont know if " + product_name + " is vegan :/")
