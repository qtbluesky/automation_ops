import dns.resolver
import os
import httplib2

iplist=[]
appdomain="www.google.com.hk"

def get_iplist(domain=""):
	try:
		A = dns.resolver.query(domain, 'A')
	except Exception,e:
		print "dns resolver error:" + str(e)
		return
	for answers in A.response.answer:
		for answer in answers.items:
			iplist.append(answer.address)
	return True

def checkip(ip):
	checkurl = ip + ":80"
	getcontent = ""
	httplib2.socket.setdefaulttimeout(5)
#	conn=httplib2.HTTPConnection(checkurl)
	conn = httplib2.Http(".cache")

	try:
#		conn.request("GET", "/", headers = {"host": appdomain})
		resp, content = conn.request(checkurl, "GET")

		print "resp: " + resp
		print "content: " + content
		r=conn.getresponse()
		getcontent = r.read(15)
	finally:
		if getcontent == "<!doctype html>":
			print ip + " [OK]"
		else:
			print ip + " [Error]"


if __name__=="__main__":
	if get_iplist(appdomain) and len(iplist) > 0:
		print "produce chckip func"
		for ip in iplist:
			checkip(ip)
	else:
		print "dns resolver error."
