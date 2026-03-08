# Bases, encoding, and encryption

## simple encoding (from number bases gym)

![number bases](./img/num-base.svg)

* you can view hexadecimal data using command line tools like `xxd`
* you can even edit and save this data using vim!
  * open the file you want to edit `vim encoding-example`
  * start an xxd buffer in vim `:%!xxd` then edit the hex values
  * close the buffer and view the results! `:%!xxd -r`
  * save the new data if you so choose `:wq`


Topics to cover for the week:

* Password cracking / hash cracking
  * focus on `john` the ripper
  * find top 500 passwords list
  * find `rockyou.txt` but DO NOT include it in your repository (too big)
  * solve the pokemon gym challenge for week 2 using `john`
    * again, take notes useful for others to crack passwords / make wordlists / permutations
* Windows and PDF password cracking
  * focus on both `john` AND `ophcrack`
  * solve PDF and Windows gyms for week 2 and take notes
  * find some example windows hashes (online)
  * document where hashed passwords are on Windows XP, 7, 10, and 11 (how to retrieve them)
* Data and encoding
  * `base64` encode and decode (can you do it similar to above for `xxd` inside vim?)
  * `strings` gym for week 2
    * find out how to view the challenge flag via given the above `vim` tips to view the image as hex
  * side challenge on a linux only system:
    * cleanly format a USB drive
    * mount it and make a text file with some unique known contents
    * delete the text file using `rm`
    * unmount the drive (but still leave it attached so it is in `/dev`)
    * run `strings` on the USB drive hardware device directly: ie. `sudo strings /dev/sdb`
  * Other challenge working with encryption person:
    * take the encrypted `tux.png` (from your encryption person) and find out how to use 
      `dd` or `vim` with `xxd` (above) and overwrite JUST the bytes of the image
      that correspond to the `.png` header and meta data, take this data from the original `tux.png`.  Then rename the encrypted file 
      as a .png and view it in an image viewer.
    * document this header / file carving process 
* Cypher / crypto
  * cyberchef local install?
  * cyberchef notes
  * quipquip notes
  * solve shift, french, strings, bash, fencing gyms.
    * notes on how to use above tools to solve gyms
    * notes on any command line tools that do the same
* Encryption (RSA / GPG)
  * `openssl`, document using openssl to encrypt / decrypt files using 128-bit CBC, 128-bit ECB, and 128-bit OFB symmetric encryption
    * encrypt `tux.png` with all three methods above and give to the `Data and encoding` person
  * Watch / do the RSA gym in week 2
  * will also use cyberchef
  * may use command line
  * send me an encrypted email (via thunderbird)
* Have and extra person?  Install Kali linux (VM via virtualbox) or on a spare laptop in room!
  * This person can tackle the USB drive `data and encoding` challenge
  * work with the linux password person to find the wordlists needed in kali linux.

  ## Encoding / Cryptography
hex to text
- `echo 0x73636f7270696f6e | xxd -r -p`
- https://linuxhandbook.com/convert-hex-ascii/

base64 to text
- `echo "c2NyaWJibGU=" | base64 -d`
- https://www.hostzealot.com/blog/how-to/linux-command-line-basics-base64-encoding-and-decoding-strings

binary -> hex -> ascii
```bash
for arg in "$@"; do
        echo "obase=16; ibase=2; $arg" | bc | xxd -r -p

done
```

binary -> hex -> base64 -> ascii
- `bash bin-hex-ascii.sh 01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101 | base64 -d`

- [CyberChef](https://gchq.github.io/CyberChef/)
- [Rumkin - Ciphers & Codes](https://rumkin.com/tools/cipher/)
- [quipquip - Simple Substitution Cipher Solver](https://quipqiup.com/)

Rot13 = rotate alphabet by 13 -> a to i
- https://rumkin.com/tools/cipher/rot13/ 
- Encoding to Rot13: `echo "Hello World" | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- Decoding from Rot13: `echo "iveghny ynxr" | tr 'A-Za-z' 'N-ZA-Mn-za-m'`

atbash cipher = all the letters are reversed that is A to Z and Z to A
- https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()
- Decoding and encoding: `echo "hzuvob lyerlfh xzev" | tr 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'`

Morse (no audio file) - select delimiter for letter and word
- https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Forward%20slash')
- Install python3, `pip install morsecodepy`
    - `morsecodepy encode "text" english`
    - `morsecodepy decode "string" english`
- TODO: add this to Kali singularity image

Key based ciphers:
- Caesar Cipher: Shifts letters by a fixed number determined by the key.
- Vigenère Cipher: Uses a keyword to apply multiple, varying Caesar shifts.
- Keyword Cipher: Reorders the alphabet based on a keyword to create a substitution alphabet.
- Playfair Cipher: Encrypts pairs of letters (digraphs) using a 
 grid generated from a keyword.
- Rail Fence Cipher: A transposition cipher that rearranges text in a zigzag pattern, with the number of rails determined by the key.
- Beaufort/Variant Beaufort: Similar to Vigenère, but uses a different mechanism to encipher, using a key. 

Fencing:
- Use [CyberChef](https://gchq.github.io/CyberChef/#recipe=Rail_Fence_Cipher_Decode(2,0))
- use [`rail-fence.py`](../scripts/rail-fence.py)

Vigenere:
- Use [CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode(''))
- use [`vigenere.py`](../scripts/vigenere.py)
---

**RSA** (Kayleigh did not like this)
1. Generate two prime numbers `p` and `q`
2. Calculate `n`, which is the value of `p*q`
3. Calculate values `d` and `e` such that `d∗e≡1mod(p−1)(q−1)`
4. The public key consists of `n` and `e` and the private key consists of `d` `p` and `q`

Challenge:  

`n=1079`.  [Factor Calculator](https://www.calculator.net/factor-calculator.html?cvar=1079&x=Calculate) shows 83 * 13 = 1079. `p` and `q` are `13` or `87`

`e=43` -> [RSA Calculator](https://www.tausquared.net/pages/ctf/rsa.html); `d=103`

See [rsa.py](../scripts/rsa.py)

