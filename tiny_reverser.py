def reverse_tinyurl(url):
	from lxml import etree
	hash = url[url.find(".com/")+5:]
	preview_url = "http://preview.tinyurl.com/"+hash
	parser = etree.HTMLParser()
	tree = etree.parse(preview_url, parser)
	elem = tree.findall('.//a[@id="redirecturl"]')
	if len(elem) == 1:
		return elem[0].get("href")
	return None

def reverse_bitly(url):
	import requests
	redirect = requests.get(url, allow_redirects=False)
	redirect_headers = dict(redirect.headers)
	if('Location' in redirect_headers):
		return str(redirect_headers['Location'])
	else:
		return None
