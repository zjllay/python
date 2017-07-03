import http.client

conn = http.client.HttPConnection("api.wanmen.org")

headers = {
	'cache-control':no-cache,
	'postman-token':"ea58ec1c-ecf0-cc66-1c53-c75112d8b1d1"
}

conn.request("GET","/live/channels/587a7f88df6ce74ffe55d3fe",headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
