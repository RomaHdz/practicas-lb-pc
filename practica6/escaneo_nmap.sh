#!/bin/bash

# Escaneo a mi segmento de red privada
read -p "Introduce la ip de tu segmento: " sec_ip

echo -e "\n1) Resultado de nmap a mi segmento de red: \n$sec_ip\n" >> resultinfo6.txt
nmap $sec_ip | tee -a resultinfo6.txt


# Escaneo de una IP de mi segmento de red:

read -p "Una IP de mi segmento: " ip_sec

echo -e "\n2) Resultado de nmap a una ip del segmento: \n$ip_sec\n" >> resultinfo6.txt
nmap $ip_sec | tee -a resultinfo6.txt


# Escaneo de nmap a un sitio web:

sit_web='wikipedia.org'

echo -e "\n3) Resultado de nmap a un sitio web: \n$sit_web\n" >> resultinfo6.txt
nmap $sit_web | tee -a resultinfo6.txt

