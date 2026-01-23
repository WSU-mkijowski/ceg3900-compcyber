# Trust

Upload to this folder the following:

- SSH Public Keys with Usernames of each member
- GPG Public Keys of each member
- Signature file named `yourlastname.sigs` which includes *your* signature on each of the other above gpg keys.

## Instructions for GPG

- Create your key `gpg --full-generate-key`
  -  Use your real name and campus email!
  -  Use all the bits (4096)!
  -  Use a password that you will not forget!
  -  We will use this key again so make sure you save it!
- Export your key and upload it to this folder
  - `gpg --export your.email@wright.edu > lastname.gpg`
- Write down your key fingerprint (last ~16 characters)
  - `gpg --fingerprint your.email@wright.edu`

For example:

```bash
mkijowski@mattpc:~$ gpg --fingerprint kijowski

pub   rsa4096 2021-09-08 [SC]
      E477 6341 6159 625F 60AC  E88A 7E5C F54E 1BBA 3984
uid           [ultimate] Matthew Kijowski (Wright State University) <matthew.kijowski@wright.edu>
uid           [ultimate] Matthew Kijowski <matthewkijowski@gmail.com>
sub   rsa4096 2021-09-08 [E]
```

Matt Kijowski's gpg key fingerprint last 16 is `7E5C F54E 1BBA 3984`

---

## Building your keyring

- import gpg public key: `gpg --import <filename>`
- verify user's identity (2 forms of ID! and write down their email & fingerprint)
- sign their key IF you trust they are who they say they are
  - `gpg --edit-key <their.email@wright.edu>
  - `sign` (will require your private key password)
  - `save`
- Bonus professional points, export the signature you just made and email it back to them

---

## GPG advanced commands

- list key(s): `gpg --list-keys <email>`
- list signatures on key(s): `gpg --list-sigs <email>`
- sign a file (several methods): 
  - `gpg --clears-sign <filename>` (adds plain text signature to file)
  - `gpg --detach-sign <filename>` (creates a separate signature file)
- verify signature on file: `gpg --verify <filename>`
- encrypt file (requires a recipient and their public key)
  - `gpg --output <output-encrypted-filename.gpg> --encrypt --recipient <email@wright.edu>`

---

## Setting up Thunderbird

* [Download Thunderbird](https://www.thunderbird.net/en-US/)
* Add your Wright State email account to Thunderbird:
  * Thunderbird *should* now recognize your `@wright.edu` email and take you to the WSU login page.  
    If not needed settings are in a below section.

Once you can send and recieve mail in thunderbird using your `@wright.edu` email set up encryption:

* In Thunderbird settings click on the account you want to set up (`@wright.edu`) > End-To-End Encryption 
  * Add your GPG **secret key**
    * You can retrieve it from `gpg --export-secret-keys <youremail@wright.edu> > your-secret-key.gpg`
  * Open the `OpenPGP Key Manager` and import my **public key** (and anyone else's you want to have secure communications with)

## Advanced Thunderbird settings

 * IMAP settings
    * Server name: `outlook.office365.com`
    * Port: `993`
    * Encryption method: `TLS`
    * Authentication method: `OAuth2`
  * SMTP settings
    * Servername: `smtp.office365.com`
    * Port: `587`
    * Encryption method: `STARTTLS`
    * Authentication method: `OAuth2`
