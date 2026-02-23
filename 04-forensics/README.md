# Forensics

Many of the tools you need can be found in the Kali container (checkout
`03-Passwords` for instructions on setting this up).

## Tools needed

* `xxd` - good quick hex viewer
* `vim` then `:%!xxd` - rough but serviceable hex editor.
  * inside `vim` to save hex data back to file use `:%!xxd -r`
* `binwalk` - tool used to extract data from a file
  * WARNING!!!! some file types have extracted data inside of them
    which can look like another file but its not...
* `volatility` - volatile memory dump parser and more.
  * has both `volatility2` and `3` versions using python 2 or 3, neither of
    which install properly...
  * Volatility2 container *mostly* worked
  * Volatility3 eventually worked fine...

---

## Installing `volatility3`


1. `singularity build $CONTAINERS/volatility3.sif docker://sk4la/volatility3`
2. `alias vol3="singularity exec $CONTAINERS/volatility3.sif volatility3"`

## Using `vol3`

Check available plugins: `vol3 -h`

1. Start by checkign the information in your memory dump file:
  *  `vol3 -f <./memdump_file> windows.imageinfo`
2. View process info:
  *  `vol3 -f <./memdump_file> windows.psscan`
  *  `vol3 -f <./memdump_file> windows.pstree`
3. View open files:
  *  `vol3 -f <./memdump_file> windows.filescan`
4. Extract file from memory location:
  *  `vol3 -f <./memdump_file> -o ./<tempdir>/ windows.dumpfiles --virtaddr <VirtualAddress-from-filescan>`
  * check in `./tempdir/` after completion
5. Extract password hashes:
  *  `vol3 -f <./memdump_file> windows.hashdump`

---

### Don't bother installing `volatility2` (this is just for documentation)

1. `sudo singularity build $CONTAINERS/volatility2.sif docker://oste/volatility2:amd64`
2. `alias vol2="singularity exec $CONTAINERS/volatility2.sif python2
   /opt/volatility/vol.py"`

### Don't bother using Volatility2

1. Start by checkign the information in your memory dump file:
  *  `vol2 -f <./memdump_file> imageinfo`
  * pay close attention to the `Profile` info for what profile you should be
    using for future commands!
2. Check process info:
  * `vol2 -f <./memdump_file> -profile=<from-above> pslist`
  * `vol2 -f <./memdump_file> -profile=<from-above> pstree`
3. Check environment variables for system / user info:
  * `vol2 -f <./memdump_file> -profile=<from-above> envars`
4. Check for password hashes:
  * `vol2 -f <./memdump_file> -profile=<from-above> hashdump`
5. ??
