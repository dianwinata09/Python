import phonenumbers

import folium

from number import number

from phonenumbers import geocoder

key ='eb520b80ca6847aeaa17af202bc9fdd5'

sanNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sanNumber, 'en')
print(yourLocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

Query = str(yourLocation)

results = geocoder.geocode(Query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,  lng)

myMap = folium.Map(location=[lat, lng], zoom_start_= 9)

folium.Marker([lat, lng], popup= yourLocation).add_to((myMap))

myMap.save('myLocation.html')
