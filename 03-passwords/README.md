# Password cracking

Get the Kali container from someone who knows...

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
alias kali="singularity shell $CONTAINERS/kali/"
alias john="singularity exec $CONTAINERS/kali/ john"
alias binwalk="singularity exec $CONTAINERS/kali/ binwalk"
alias whereami="cat /opt/os-release"

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

