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

