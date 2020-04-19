import requests
from bs4 import BeautifulSoup


while(1):
        pincode = input('Please enter your pincode')

        payload = {
                "q":pincode
        }

        latlngr = requests.get('https://www.geonames.org/postalcode-search.html',payload)
        if latlngr.status_code == 200 :
                soup = BeautifulSoup(latlngr.content, "html.parser")
                div = soup.find('table', {'class': 'restable'})
                #print(div)
                location = div.find_all("a")
                #print(location)
                location = location[0].text.split('/')
                #print(location)
                lat = location[0]
                lng = location[1]
                print(lat, lng)
                r = requests.get('https://local.fedex.com/search-results/{lat},{lng}/'.format(lat = lat, lng = lng))
                if r.status_code == 200:
                        soup = BeautifulSoup(r.content, "html.parser")
                        details = soup.find_all('div', {'class' : 'loc-item-contain'})
                        for detail in details:
                                try:
                                        itemcount = detail.find('div', {'class' : 'loc-item-count'}).text
                                        itemtitle = detail.find('strong', {'class' : 'loc-item-title'}).text
                                        itemaddress = detail.find('span', {'class' : 'loc-item-address'}).text
                                        itemdistance = detail.find('span', {'class' : 'loc-item-distance'}).text
                                        print(itemcount)
                                        print(itemtitle)
                                        print(itemaddress)
                                        print(itemdistance)
                                        print('\n')
                                except:
                                        print("Error in pincode")
                                        break
                                
                        
                

        print()
        print()
