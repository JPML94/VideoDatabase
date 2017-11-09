from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import os
import time

client = Client(
"http://www.videomarketingdatabase.com/xmlrpc.php",
"hbailey315",
"TradecraftVideo"
)
# set to the path to your file
i = 0
for filename in os.listdir("ytimg"):
    # prepare metadata
    data = {
            'name': filename,
            'type': 'image/jpeg',  # mimetype
    }
    # read the binary file and let the XMLRPC library encode it into base64
    if i %3 == 0:
        time.sleep(3)
    with open("ytimg/" + filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
    response = client.call(media.UploadFile(data))
    i += 1




# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }
