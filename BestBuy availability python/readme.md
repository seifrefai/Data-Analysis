##BestBuyButtonTracker

For this project, The objective was to be able to check the status of the 'Add To Cart' button for a product on the BestBuy Website.
I used the requests library in order to make a get request to the website and BeautifulSoup library in order to obtain the button and find out its current status. 
I created a Data.py file, which includes the User agents and the urls we wanted to scrape. You can simply add more urls to check for more products.

## LocalSetup
1) Install All Dependencies   
    * `pip3 install -r requirements.txt`

2) Modify the Data.py file, by changing the urls in the Data dictionary to the urls you want to track from the BestBuy website

3) Run the Scrapper.py file:
`python3 Scrapper.py`
    * You will then see the status of the request for each url, with should be 200
    * Then you will see the URL and the button status for each url that was in the Data.py file.

## ToDo
* Add automation to regulary check for button status
* Add feature to send an email when button status is 'Add To Cart'
* Standardize the program to be able to use other websites urls such as Target, Gamestop, etc.

