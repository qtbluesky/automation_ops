import dns.resolver

domain = raw_input('Pls input a domain: ')
mx = dns.resolver.query(domain, 'MX')
for i in mx:
    print 'MX preference = ', i.preference, 'mail exchanger = ', i.exchange
