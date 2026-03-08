## File metadata
Install exiftool  
- `sudo apt install libimage-exiftool-perl`
- `exiftool image_file`

## File characters

`cat -A filename`
- `^I` = tab separated
- `$` = end of line (new line) character

## Extractors
- `xz -d`

## Magic Numbers

- [Wiki - Format Indicators](https://en.wikipedia.org/wiki/Magic_number_(programming)#Format_indicator)
- [NetSpi - Magic Bytes](https://www.netspi.com/blog/technical-blog/web-application-pentesting/magic-bytes-identifying-common-file-formats-at-a-glance/)
- [Huntress - What is Magic Number in Cybersecurity - Explanatory](https://www.huntress.com/cybersecurity-101/topic/what-is-magic-number-in-cybersecurity)

## Barcodes
Barcode scanner app = Cognex

## Bitcoin

[BlockChain - look up transactions](https://www.blockchain.com/)

## DNS
`whois domain_name`

## HTTP Headers
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers

- Request types: `GET`, `PUT`, `POST`, `DELETE`, `CONNECT`
- Browser = `User-Agent` file

## SSL
TODO: import GPG key, return to challenge

## CVEs and Vulnerabilities

**Shellshock**
Shellshock could enable an attacker to cause Bash to execute arbitrary commands and gain unauthorized access[3] to many Internet-facing services, such as web servers, that use Bash to process requests.

Search for `/bin/bash` attempts in HTTP logs

When analyzing access logs (e.g., Apache or Nginx), you should search for the following signatures, often combined with commands like wget or bin/bash: 
- Classic Vulnerability Test: `() { :;}; /bin/bash -c '...'`
- Malware Download: `() { :;}; /usr/bin/wget ...`
- Reverse Shell Attempt: `() { :;}; /bin/bash -i >& /dev/tcp/...`
- Information Leakage: `() { :;}; /bin/cat /etc/passwd `