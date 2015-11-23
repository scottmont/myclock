import urllib, json
url = "https://www.followmee.com/api/tracks.aspx?key=fe26a8c25f3235fb56b041665c80f363&username=scottmont&output=json&function=currentforalldevices"
response = urllib.urlopen(url)
data = json.loads(response.read())
latit = data['Data'][0]['Latitude']
longt = data['Data'][0]['Longitude']
jlatit = data['Data'][1]['Latitude']
jlongt = data['Data'][1]['Longitude']
mlatit = data['Data'][2]['Latitude']
mlongt = data['Data'][2]['Longitude']

# Where is Scott?
if 43.6358 <= float(latit) <= 43.6378 and -79.4185 >= float(longt) >= -79.4248 :
	print ( 'scott at work' , latit , longt )
elif 43.6760 <= float(latit) <= 43.6769 and -79.3425 >= float(longt) >= -79.3439 :
	print ( 'scott at home' , latit , longt )
else:
	print ( 'dunno where scott is' , latit , longt )

# Where is Juliana?
if 43.6909 <= float(jlatit) <= 43.6936 and -79.3315 >= float(jlongt) >= -79.3344 :
        print ( 'juliana at work' , jlatit , jlongt )
elif 43.6760 <= float(jlatit) <= 43.6769 and -79.3425 >= float(jlongt) >= -79.3439 :
	print ( 'juliana at home' , jlatit , jlongt )
else:
        print ( 'dunno where juliana is' , jlatit , jlongt )

# Where is Maxim?
if 43.6909 <= float(mlatit) <= 43.6936 and -79.3315 >= float(mlongt) >= -79.3344 :
        print ( 'maxim at school' , mlatit , mlongt )
elif 43.6760 <= float(mlatit) <= 43.6769 and -79.3425 >= float(mlongt) >= -79.3439 :
        print ( 'maxim at home' , mlatit , mlongt )
else:
        print ( 'dunno where maxim is' , mlatit , mlongt )

