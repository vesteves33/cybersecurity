from urllib.request import urlopen
import re, json

url = 'https://ipinfo.io/json'

response = urlopen(url)

dados =  json.load(response)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']

print('Detalhes do Ip externo\n')
print('IP: {4}\nRegião: {1} Pais: {2}\nCidade: {3}\nOrg: {0}'.format(org, region, country, city, ip))
