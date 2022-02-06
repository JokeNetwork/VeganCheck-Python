<img width="80px" src="https://raw.githubusercontent.com/JokeNetwork/vegancheck.me/main/img/hero_icon.png" align="right" alt="VeganCheck Logo">

# VeganCheck.me Python Port
  
## Overview

VeganCheck.me checks the barcode (EAN or UPC) of a food- or non-food-product and tells you if it is vegan or not. It is an useful tool for vegans and vegetarians - Developed with usability and simplicity in mind, so without distracting irrelevant facts or advertising.
	
This is the simplified Python version of the original [`script.php`](https://github.com/JokeNetwork/vegancheck.me/blob/main/script.php).
	
### Requirements: 
- Python >=3.9.10
- The following components installed:
  ````bash
  $ pip install openfoodfacts
  ````
  ````bash
  $ pip install configparser
  ````
- Optional: Get an API-Key for Open EAN Database by donating to Coast against plastic (Küsten gegen Plastik) - [Learn more here](https://opengtindb-org.translate.goog/userid.php?_x_tr_sl=de&_x_tr_tl=en&_x_tr_hl=de&_x_tr_pto=wapp), insert it in the `.env.example` and rename it to `.env`. 
Also change the path to the .env-file in `script.py:80`. Then you should be good to go!
  ```py
  with open('.env', 'r') as f:
  ````

## Contribute
Please feel free to contribute and add more features from the original [`script.php`](https://github.com/JokeNetwork/vegancheck.me/blob/main/script.php).

## Dependencies & Credits 

This repo uses:
  
* [OpenFoodFacts API](https://openfoodfacts.org/) & [OpenBeautyFacts API](https://openbeautyfacts.org/) [@openfoodfacts](https://github.com/openfoodfacts)
* [Brocade.io API](https://brocade.io) [@ferrisoxide](https://github.com/ferrisoxide)
* [Open EAN Database](https://opengtindb.org)
* [is-vegan](https://github.com/hmontazeri/is-vegan) [@hmontazeri](https://github.com/hmontazeri) as [VeganCheck.me Ingredients API](https://github.com/JokeNetwork/vegan-ingredients-api)

## License

All text and code in this repository is licensed under [MIT](https://github.com/jokenetwork/VeganCheck.me/blob/main/LICENSE), © 2022 Philip Brembeck, © 2022 JokeNetwork.
