# Password cracking

Get the Kali container from someone who knows or here: `wget https://web1.cs.wright.edu/~w114mek/kali.sif`

***Note: requires campus vpn or being on secure wireless!***

#### TL/DR AFTER getting the container above and bash_aliases below

* rockyou dictionary attack (very long): `john --format=<format> --wordlist=/usr/share/wordlists/rockyou.txt <./hashfile>`
* xpspecial windows attack: `ophcrack -t /usr/share/wordlists/xpspecial -f <./windows.hashes>`
* Kore custom rule attack: `john --config=./john-rules.custom --rules=KoreLogicRulesAppend2Num --wordlist=<words>  <./hashfile>`

---

## building your own container

You can build your own by follwoing this but it will take a while and xpspecial is non-trivial to download:

```bash
sudo singularity build --sandbox ./kali/ docker://kalilinux/kali-rolling
sudo singularity shell --writable ./kali/

# inside Singularity>
  sudo apt update && sudo apt install kali-linux-headless ophcrack-cli
  cd /usr/share/wordlists/
  gunzip rockyou.tgz
  mkdir xpspecial
  # put all of the needed xpspecial rainbow tables in the above dir (>6GB!!)
  exit

# you can build the above to a faster read-only container
sudo singularity build kali.sif ./kali/
```

---  

### sample `~/.bash_aliases`

```bash
CONTAINERS=~/containers

alias kali="singularity shell $CONTAINERS/kali.sif"
alias john="singularity exec $CONTAINERS/kali.sif john"
alias ophcrack="singularity exec $CONTAINERS/kali.sif ophcrack"
alias binwalk="singularity exec $CONTAINERS/kali.sif binwalk"
alias whereami="cat /etc/os-release"

#dont forget to source ~/.bashrc after!
```

## custom john rules / shoutout [KoreLogic](https://contest-2010.korelogic.com/rules.html) 

The custom john rules in `john-rules.custom` can be used with:

```bash
john --config=./john-rules.custom --rules=KoreLogicRulesAppend2Num --wordlist=<words> ./hashfile
```

The above example uses the custom rule `KoreLogicRulesAppend2Num` which simply appends 2 numbers
to each word in the wordlist.

More documentation on these rules and features can be found in the `Kore-john-rules.md`

## Password lists

- rockyou - `wget https://github.com/mkijowski/password-attacks/raw/refs/heads/main/dictionaries/rockyou.tgz`
- xp specialist - https://ophcrack.sourceforge.io/tables.php
- OpenWall (from John) - https://www.openwall.com/wordlists/
- Pokemon names - `wget https://gist.githubusercontent.com/ralts00/31415709fb34c1b2ec556c396efc3d80/raw/516ef1179f10f4a0ecb4f50f118e6757fef85243/pokemon_names.txt`
        - `sed -i 's/^./\l&/' pokemon_names.txt` - convert names to lowercase

**Build a wordlist:**
`for i in {0000..9999}; do echo "SKY-HQNT-$i"; done > sky-crack.txt`

## Notes on Hashes

**Common hashes & lengths:**
- MD5SUM ~36 characters
- SHA256SUM ~68 characters
- SHA512SUM ~132 characters

**Shadow file signature lookups:**
| ID | Algorithm | Commonality | Strength |
| -- | ---       | ---         | ---      |
| `$1$` | MD5 | Older systems / Legacy CTFs | Weak (fast to crack) |
| `$2a$` | Blowfish (bcrypt) | OpenBSD / Web Apps | Very Strong |
| `$5$` | SHA-256 | Older RHEL/CentOS | Strong |
| `$6$` | SHA-512 | Standard on modern Linux | Very Strong | 
| `$y$` | yescrypt | Modern Debian/Ubuntu/Fedora | Extremely Strong |

## Notes from NCL Challenges

- `pdf2john` - find hashed password of pdf file
  - **NOTE** Remove pdf name / remove up to `$pdf$...`
- `zip2john` - find hashed password of zip file
- [HashCat](https://hashcat.net/hashcat/)
  - TODO: have not played with.  Current tasks can be done with JtR

[Ophcrack](https://ophcrack.sourceforge.io/) - built into singularity image
`21259DD63B980471AAD3B435B51404EE:1E43E37B818AB5EDB066EB58CCDC1823`
Split into `LM` (left side) and `NT` (right side)
NT side
- `cat passhash | awk -F':' '{print $2}' > ntside`
- `john --format=nt ./ntside` use john built in password list
- `john --format=nt --wordlist=./rockyou.txt ./ntside`
LM side
- `cat passhash | awk -F':' '{print $1}' > lmside`
- `john --format=lm --wordlist=./rockyou.txt ./lmside`
- `john --format=lm ./ntside` use john built in password list
View pot of cracks:
- `cat ~/.john/john.pot`
        - LM appears to break into two segments. May need to "assemble" password