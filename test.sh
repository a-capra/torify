#!/bin/bash

if [[ -f /etc/tor/torrc ]]; then
    echo "TOR conf exists"
fi

new_circuit(){
    #echo -e 'AUTHENTICATE ""\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
    echo -e 'AUTHENTICATE "tor4me.p"\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051

    myIP=`torify curl ${1} 2> /dev/null`
    echo "$myIP with new tor circuit"
}

url="https://ifconfig.me"
url="http://httpbin.org/ip"


myIP=`curl ${url} 2> /dev/null`
echo "$myIP without tor"

echo "sleep one sec"
sleep 1

myIP=`torify curl ${url} 2> /dev/null`
echo "$myIP with tor"


#echo "sleep one sec"
#sleep 1
#new_circuit $url
