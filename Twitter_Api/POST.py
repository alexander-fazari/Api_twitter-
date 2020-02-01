import urllib2
import base64
import json
import sys

def post():

	url = 'https://gnip-api.twitter.com/search/30day/accounts/shendrickson/wayback.json'
	UN = 'mostafa.fazari@gmail.com'
	PWD = 'mostafa1993'

	rule = "fromDate':'201802010000','toDate':'201802282359'"

	query = {
    'q': '#drones',
    'result_type': 'recent',
    # 'count': 2,
     'maxResults': '100',
    'fromDate':'201802010000', 
    'toDate':'201802282359'  
}


	base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')
	req = urllib2.Request(url=url, data=query)
	req.add_header('Content-type', 'application/json')
	req.add_header("Authorization", "Basic %s" % base64string)
	
	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		print e.read()
	the_page = response.read()
	print the_page

if __name__ == "__main__":
        post()