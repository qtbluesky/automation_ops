import httplib2

httplib2.debuglevel = 1

h = httplib2.Http(".cache")
resp, content = h.request("http://www.baidu.com/", "GET")
print "resp: " + str(resp.status)
print "resp: " + str(resp.fromcache)
#print "content: " + content

#print("\nresponse.status is : ", resp.status)
#print("content len is : ", len(content))
#print("is from cache : ", resp.fromcache)
