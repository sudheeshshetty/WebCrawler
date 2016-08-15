#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import sys

# Author: Sudheesh Shetty


if len(sys.argv)==2:
    #If only the keyword is given, give the list of all the products found for that keyword
    keyword=sys.argv[1]
    
    #get request for the url
    result=requests.get("http://www.shopping.com/products?KW="+keyword)
    
    #gives html code of given url
    data=result.text
    
    #add an xml parser to parse the html
    soup=BeautifulSoup(data,'lxml')
    
    #get the span which has the total count of results for particular keyword
    result=soup.find_all('span',{'class' : 'numTotalResults'})[0].get_text().split()
    
    print "Total number of results found are "+result[-1]
    
elif len(sys.argv)==3:
    #If keyword as well as page number is given print all the results in that page.
    keyword=sys.argv[1]
    pagenumber=sys.argv[2]

    #get request for the url
    result=requests.get("http://www.shopping.com/products~PG-"+pagenumber+"?KW="+keyword)

    #gives html code of given url
    data=result.text

    #add an xml parser to parse the html
    soup=BeautifulSoup(data,'lxml')

    #get the span which has the total count of results for particular keyword
    result=soup.find_all('span',{'class' : 'numTotalResults'})[0].get_text().split()

    #get total count of results in a page
    total_count=int(result[3])-int(result[1])+1
    print "Total number of results found in page are"+str(total_count)
    
    #create an array to append the names of products that we get from that page
    list_items=[]
    
    for i in range(1,total_count):
        #The products are listed with id as nameQA<1-total_count in that page>
        list_items.append(soup.find_all('',{'id' : 'nameQA'+str(i)})[0].get_text())

    for i in range(len(list_items)):
        print list_items[i]
        
else:
    #Print the syntax to enter the input
    print "Correct usage is : \n"\
    "python web_crawler.py <keyword> <page number>\n"\
    "keyword : keyword that is to searched\n"\
    "page number : It is optional. It gives all results on specific page for the keyword"
