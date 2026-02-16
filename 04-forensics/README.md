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
  * has both `volatility2` and `3` versions using python 2 or 3
  * ***Volatility3 did not work for me***
  * neither did manually installing volatility2

## Installing `volatility2`

1. `sudo singularity build $CONTAINERS/volatility2.sif docker://oste/volatility2:amd64`
2. `alias vol2="singularity exec $CONTAINERS/volatility2.sif python2
   /opt/volatility/vol.py"`

## Using Volatility2

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
