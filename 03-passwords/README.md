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

