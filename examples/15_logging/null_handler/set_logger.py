In [1]: import logging

In [2]: from base_ssh_class import BaseSSH

In [3]: logging.basicConfig(level=logging.DEBUG)

In [4]: logger = logging.getLogger("base_ssh_class")

In [5]: r1 = BaseSSH('192.168.100.1', 'cisco', 'cisco')
DEBUG:paramiko.transport:starting thread (client mode): 0xb4dd4c0c
DEBUG:paramiko.transport:Local version/idstring: SSH-2.0-paramiko_2.6.0
DEBUG:paramiko.transport:Remote version/idstring: SSH-2.0-Cisco-1.25
INFO:paramiko.transport:Connected (version 2.0, client Cisco-1.25)
DEBUG:paramiko.transport:kex algos:['diffie-hellman-group-exchange-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1'] server key:['ssh-rsa'] client encrypt:['aes128-cbc', '3des-cbc', 'aes192-cbc', 'aes256-cbc'] server encrypt:['aes128-cbc', '3des-cbc', 'aes192-cbc', 'aes256-cbc'] client mac:['hmac-sha1', 'hmac-sha1-96', 'hmac-md5', 'hmac-md5-96'] server mac:['hmac-sha1', 'hmac-sha1-96', 'hmac-md5', 'hmac-md5-96'] client compress:['none'] server compress:['none'] client lang:[''] server lang:[''] kex follows?False
DEBUG:paramiko.transport:Kex agreed: diffie-hellman-group-exchange-sha1
DEBUG:paramiko.transport:HostKey agreed: ssh-rsa
DEBUG:paramiko.transport:Cipher agreed: aes128-cbc
DEBUG:paramiko.transport:MAC agreed: hmac-sha1
DEBUG:paramiko.transport:Compression agreed: none
DEBUG:paramiko.transport:Got server p (2048 bits)
DEBUG:paramiko.transport:kex engine KexGex specified hash_algo <built-in function openssl_sha1>
DEBUG:paramiko.transport:Switch to new keys ...
DEBUG:paramiko.transport:Adding ssh-rsa host key for 192.168.100.1: b'c4bdee47f420a0e2498c8b69fb26171f'
DEBUG:paramiko.transport:userauth is OK
INFO:paramiko.transport:Authentication (password) successful!
DEBUG:paramiko.transport:[chan 0] Max packet in: 32768 bytes
DEBUG:paramiko.transport:[chan 0] Max packet out: 4096 bytes
DEBUG:paramiko.transport:Secsh channel 0 opened.
DEBUG:paramiko.transport:[chan 0] Sesch channel 0 request ok
DEBUG:paramiko.transport:[chan 0] Sesch channel 0 request ok
DEBUG:base_ssh_class:Подключение к 192.168.100.1

In [6]: logging.getLogger('paramiko').setLevel(logging.WARNING)

In [7]: r1 = BaseSSH('192.168.100.1', 'cisco', 'cisco')
DEBUG:base_ssh_class:Подключение к 192.168.100.1

In [8]: r1.send_show_command('sh clock')
DEBUG:base_ssh_class:Отправка команды sh clock на 192.168.100.1
Out[8]: 'sh clock\r\n*20:14:09.593 UTC Sat Nov 16 2019\r\nR1>'


