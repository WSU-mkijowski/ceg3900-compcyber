## Regex Patterns

1. The "Flag Finder" (Most Used)

The single most frequent use of regex is searching for the flag itself. 

CTFs usually provide a prefix (e.g., `picoCTF{...}` or `flag{...}`).

* **Basic Search:** `flag\{.*?\}`
* Finds "flag{" followed by any characters until the first "}".

* **Case Insensitive:** `(?i)flag\{.*\}`
* The `(?i)` modifier is crucial because flags are sometimes written as `FLAG{...}` or `FlAg{...}`.

* **Specific Format:** `nactf\{[nac]{10}.{21}[ctf]{14}\}`
* Used in forensics when the challenge description tells you exactly how many of which characters are in the flag.

---

2. Infrastructure & Network Recon

When analyzing PCAP files or server logs, you need to extract specific technical identifiers.

| Target | Regex Pattern | Purpose |
| --- | --- | --- |
| **IPv4 Address** | `\b(?:\d{1,3}\.){3}\d{1,3}\b` | Extracting IP addresses from logs or traffic. |
| **Email Address** | `[\w\.-]+@[\w\.-]+\.\w{2,4}` | Harvesting potential usernames or contact info. |
| **MAC Address** | `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})` | Identifying specific hardware in network captures. |
| **Domain Names** | `[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | Extracting subdomains or external C2 server URLs. |

---

3. Web & Forensics Indicators

These are used to find common "leaks" or indicators of compromise (IoC) in source code or forensic images.

* **Hex/MD5 Hashes:** `\b[a-fA-F0-9]{32}\b`
* Used to find MD5 hashes (often used as passwords or file identifiers). Use `{40}` for SHA-1 or `{64}` for SHA-256.


* **Base64 Strings:** `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
* Crucial for finding encoded data hidden in web responses or config files.


* **HTTP Status Codes:** `HTTP/\d\.\d"\s(\d{3})`
* Finds codes like `403` (Forbidden) or `500` (Internal Error) in server logs to see where an exploit succeeded.


* **URL Parameters:** `(\?\|&)([^=]+)=([^&]+)`
* Used to parse long URLs and extract every parameter (helpful for SQLi or LFI challenges).

---

4. The "Grep" Power-User Commands

In a CTF, you'll rarely type regex into a website; you'll type it into a terminal.

* **`grep -oE 'flag\{.*\}' file.txt`**
* `-o`: Only shows the match (not the whole line).
* `-E`: Enables Extended Regex (so you don't have to escape `( )` or `{ }`).

* **`grep -rwi "password" .`**
* `-r`: Recursive (searches every folder).
* `-w`: Whole word only (ignores "passwords").
* `-i`: Case-insensitive.

---

Pro-Tip: Greedy vs. Lazy

In CTFs, you usually want **Lazy matching**.

* **Greedy:** `flag\{.*\}` will match from the first `flag{` to the very last `}` in the entire file. If there are two flags on one line, it will merge them into one giant mess.
* **Lazy:** `flag\{.*?\}` matches from `flag{` to the *nearest* `}`. Always use the `?` after a quantifier in CTFs to avoid "over-matching."

## Log Analysis

**SSH Log Files**

`last` = history of logged in users
`who` = see who is currently logged in
`lastlog` = overview of who is logged in and when last logged in

Location: 
- Ubuntu - `/var/log/auth.log`
- RHEL / CentOS - `/var/log/secure`
- Windows Event Log (Applications and Services Logs -> OpenSSH) - TODO: confirm

Service Logs:
- `journalctl -u ssh || sshd`
- Follow with `-f`
- Time window with `--since "1 hour ago"` 

**SQL**

Firefox browsing history
- Windows: `C:\Users\<YourUsername>\AppData\Roaming\Mozilla\Firefox\Profiles\<ProfileName>`
- macOS: `~/Library/Application Support/Firefox/Profiles/<ProfileName>`
- Linux: `~/.mozilla/firefox/<ProfileName>`
1. places.sqlite: Stores bookmarks, browsing history, and metadata.
2. cookies.sqlite: Contains all browser cookies.
3. formhistory.sqlite: Saves autocomplete form data.
4. webappsstore.sqlite: Stores site-specific data.

- `sqlite3 dbfile` = opens db in sqlite
        - DBeaver supports SQLite
        - [SQLite Viewer is web app - gets search fields without SQL](https://sqliteviewer.app/)
- `.schema` = print all tables in DB
- `.quit` = gracefully exit shell

Show only rows from column with search term
```sql
SELECT url, title, visit_count, last_visit_date
FROM moz_places
WHERE title LIKE '%gmail%'
ORDER BY last_visit_date DESC;
```

In case of date time stored in epochs:
```sql 
    datetime(last_visit_date/1000000, 'unixepoch', 'localtime') AS last_visited
```

**Challenges - notes for the complicated ones**
SSH gym can be solved by looking for `Failed` vs `Accepted`. Use `head` since log file is already time sorted

`awk -F'\t' '{print $3}' login.log | sort | uniq -c | sort`
- file is tab delimited, sort column 3 (login names), add number of occurrences to unique, sort to find max

`awk -F'\t' '{print $1}' login.log | awk '{print $1}'` 
- pipe out first column (date time stamp) to awk to get only date (awk is space delimited by default)

`awk -F'\t' '{print $3 " " $2}' login.log | sort | uniq | awk '{print $1}' | uniq -c | sort`
- username that had logins from the most unique IP addresses. Get list of logins with IPs, sort and find only uniq entries (non duplicate logins with given IP). Parse again for only logins, get uniq count and sort to find max

`cat vsftpd.log | grep -P "UPLOAD" | grep -P -o "/[a-zA-Z0-9._/-]+\.\w{1,}" | grep -P -o "\.\w{1,}" | sort | uniq -c | sort`
- only lines with UPLOAD have file; only want file paths and extensions, not upload size; parse to just file extensions, sort and count
- **TODO: this DID NOT factor in that there was another user in the logs**

`cat vsftpd.log | grep -v "ftpuser" | grep -P ".*\[pid\s\d{1,}\]\s\[\w{1,}"`
- knockout lines containing `ftpuser`, then seek lines that have a user specifier after the `pid`

`cat vsftpd.log | grep -v "ftpuser" | grep -P ".*\[pid\s\d{1,}\]\s\[\w{1,}" | grep -P -o "\d{1,}\sbytes" | grep -P -o "\d{1,}" | awk '{ sum += $1 } END { print sum }'`
- For jimmy, parse out just the ### bytes, then ship to awk for final count

`cat vsftpd.log | grep -P "UPLOAD" | grep -P "ftpuser" | grep -P -o "\d{1,}\sbytes" | grep -P -o "\d{1,}" | awk '{ sum += $1 } END { print sum }'`
- this one does say you gotta be `ftpuser` to count num bytes uploaded

`cat vsftpd.log | grep -v "ftpuser" | grep -v "jimmy"`
- assuming `ftpuser` and `jimmy` are in the logs, checking for who isn't in the logs. From the challenge you also know client IPs for `ftpuser` and `jimmy`

`cat access.log | grep -P -o "(GET|POST|PUT|DELETE).*200" | wc`
- requests can be `GET`, `PUT`, `POST`, `DELETE`. Seeking status code of `200` explicit

`cat access.log | grep -P "(GET|POST|PUT|DELETE|CONNECT).*4\d\d" | wc`
- OMG, `CONNECT` is also a status; answer needs to be any `4XX` error

`cat access.log | grep -P -i "(doorbell|bell)"`
- apparently checking for bell or doorbell is a thing - made it case insensitive 

`cat access.log | grep -P -i -o "Firefox\/[0-9.]{1,}"`
- versions of Firefox

Date does not do milliseconds
- `date -d @1443892381725656` will not properly convert
- `date -d @1443892381` will get Oct 3 13:13:01 2015
- `date -d '1970-01-01 + 18934 days'` where `18934` came from `shadow` file (is last change of password calculated since Linux beginning of time)

`grep -A 6 OrderTotal.*998.6.*OrderTotal payments.log`
- show number of lines *after* a match

`grep -o StateOrProvince.[A-Z][A-Z]......StateOrProvince payments.log | grep -o [A-Z][A-Z] | sort | uniq -c | sort -n`
- awk-less solution