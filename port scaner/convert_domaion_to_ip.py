# pip install iplookup

from iplookup import iplookup
ip = iplookup.iplookup
domain = input('enter a domain: ')

result = ip(domain)
print(f'ip {domain} = {result}')
