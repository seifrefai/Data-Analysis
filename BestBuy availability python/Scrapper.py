import sys
import time 
from bs4 import BeautifulSoup
import requests
import Data


class bestbuy_checker:

    def __init__(self,urls,headers):
        self.urls=urls
        self.headers=headers

    def website_response(self):
        response_list=[]

        for url in self.urls:
            response= requests.get(url,headers=self.headers)

            if response.status_code != 200:
                raise requests.exceptions(f"Expected status code 200, but got {response.status_code} instead.")

            response_list.append(response)          
            print('\x1b[6;30;42m' + f"Response came back with status code: {response.status_code}" + '\x1b[0m')

        return response_list


    def button_status_list(self):

        response_list=self.website_response()
        button_list=[]

        for response in response_list:

            soup=BeautifulSoup(response.text, "html.parser")
            button2=soup.find('div',attrs={'class':"fulfillment-add-to-cart-button"})
            button_list.append(button2.next_element.next_element.next_element.text)

        return button_list

    def print_results(self,):

        button_status_list=self.button_status_list()
        print('\nBelow is the status of the buttons on the website')
        print('-------------------------------------------------------------------')

        for i,j in zip(button_status_list,self.urls):
            
            print('\x1b[6;30;42m' + 'URL:' + '\x1b[0m' +f" {j}\n\nButton Status: {i}\n")
            


def main():

    bestbuy=bestbuy_checker(Data.urls,Data.headers)
    bestbuy.print_results()



if __name__=='__main__':
    main()

