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

---

## git history
`git log --format='%ae' | sort -u` where
- `%ae`: Author email.
- `%ce`: Committer email (useful if someone else merged the code).
- `sort -u`: Removes duplicates so you only see unique addresses.

`git rev-list --all --objects | awk '{print $1}' | xargs -I {} git cat-file -p {}`

It is a three-part pipeline designed to force Git to reveal the contents of every single object it has ever stored, regardless of whether that object is in your current branch, an old deleted branch, or a hidden configuration.

Here is the breakdown of the "anatomy" of this command:

1. `git rev-list --all --objects`
Standard git log only shows you commits. This command goes much deeper.

- `--all`: Tells Git to look at every single "ref" (all branches, all tags, and the stash).

- `--objects`: Tells Git to list not just the commits, but also the Trees (folder structures) and Blobs (the actual file contents) associated with those commits.

The Output: A long list of SHA-1 hashes followed by their file paths.

2. `awk '{print $1}'`
The previous command outputs two columns: [`hash`] `[path`].

This awk command simply strips away the filenames and paths, leaving you with a clean list of hashes. This is necessary because the next command only understands hashes, not names.

3. `xargs -I {} git cat-file -p {}`
This is where the heavy lifting happens.
- `xargs -I {}`: This takes each hash from the list and prepares it to be used as an argument.
- `git cat-file -p`: This is the "caterpillar" (print) command for Git objects. The `-p` flag stands for pretty-print. It tells Git: "Take this compressed, binary blob and turn it back into readable text/content."

TODO: investigate [TruffleHog](https://github.com/trufflesecurity/trufflehog)

---

## PDFs
`pdfinfo` - show creating program
- Creator: The software used to write the original content (e.g., Microsoft® Word 2021)
- Producer: The "engine" that generated the PDF (e.g., macOS Version 14.2 (Build 23C71) Quartz PDFContext).

`strings api.pdf | grep "SKY"`

TODO: this aws easy with `strings` because they used a simple program.  Need to try more advanced redaction removal techniques