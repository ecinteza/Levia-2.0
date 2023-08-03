from gifpy import Gifpy

KEY = "AIzaSyCXIpE5K1P-6eZkI4kX02gTtkZkGukS3JU"  # Your API key goes here
gifpy = Gifpy(KEY, "en_US")
search = gifpy.search("code!", limit=5)
print(search)
print(search[0].url)