---
aliases: []
date created: Tuesday, 2. December 2025, 13:12
date modified: Tuesday, 2. December 2025, 17:12
---

# Lab 7 (Gísli)

Services and versions on the ports:
```bash
gislih24@icybjump:~$ nmap -sV 130.208.246.241
Starting Nmap 7.93 ( https://nmap.org ) at 2025-12-02 10:35 EST
Nmap scan report for 130.208.246.241
Host is up (0.00015s latency).
Not shown: 978 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
7/tcp    open  echo
9/tcp    open  discard?
13/tcp   open  daytime
19/tcp   open  chargen
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
25/tcp   open  smtp        Postfix smtpd
79/tcp   open  finger      Debian fingerd
80/tcp   open  http        nginx 1.22.1
110/tcp  open  pop3        Dovecot pop3d
111/tcp  open  rpcbind     2-4 (RPC #100000)
139/tcp  open  netbios-ssn Samba smbd 4.6.2
143/tcp  open  imap        Dovecot imapd
445/tcp  open  netbios-ssn Samba smbd 4.6.2
993/tcp  open  ssl/imap    Dovecot imapd
995/tcp  open  ssl/pop3    Dovecot pop3d
2049/tcp open  nfs_acl     3 (RPC #100227)
5000/tcp open  http        Docker Registry (API: 2.0)
6666/tcp open  irc         Hybrid ircd
6667/tcp open  irc         Hybrid ircd
6668/tcp open  irc         Hybrid ircd
6669/tcp open  irc         Hybrid ircd
Service Info: Host:  icybtarget; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 157.50 seconds
gislih24@icybjump:~$
```


After doing the port-forwarding thing, I could do this stuff:
```bash
┌──(kali㉿kali)-[~]
└─$ curl http://localhost:8080           
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

┌──(kali㉿kali)-[~]
└─$
```
The HTTP server is up and running, but this likely isn’t anything juicy, so I’m moving on.

Next, I used `smbclient`:
```bash
┌──(kali㉿kali)-[~]
└─$ smbclient -L //localhost/ -p 1445 -N
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
        labshare        Disk      
        IPC$            IPC       IPC Service (Samba 4.17.12-Debian)
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to localhost failed (Error NT_STATUS_CONNECTION_REFUSED)
Unable to connect with SMB1 -- no workgroup available

┌──(kali㉿kali)-[~]
└─$ smbclient //localhost/labshare -p 1445 -N
Anonymous login successful
tree connect failed: NT_STATUS_ACCESS_DENIED

┌──(kali㉿kali)-[~]
└─$
```
Here I’ve discovered that I can see the shares in the file server, but I can’t actually view them directly. However, this does tell me that:
Anonymous users can enumerate (list) the shares on the Samba server.
Though, when I tried to log in, it won’t let me, so I probably need to find the correct login information elsewhere:
```bash
┌──(kali㉿kali)-[~]
└─$ smbclient //localhost/labshare -p 1445 -U gislih24        
Password for [WORKGROUP\gislih24]:
session setup failed: NT_STATUS_LOGON_FAILURE
```


Using `ftp`:
```bash
┌──(kali㉿kali)-[~]
└─$ ftp localhost 2121
Trying [::1]:2121 ...
Connected to localhost.
220 (vsFTPd 3.0.3)
Name (localhost:kali): gislih24
530 This FTP server is anonymous only.
ftp: Login failed
ftp> ls
530 Please login with USER and PASS.
530 Please login with USER and PASS.
ftp: Can't bind for data connection: Address already in use
ftp> exit
221 Goodbye.
```
I’ve learned that anonymous FTP login is allowed on the internal server (which is bad, I think?).




Internal IRC server on ports 6666–6669 requires identd and disconnects clients without it.

Checking the Docker repo:
```bash
┌──(kali㉿kali)-[~]
└─$ curl http://localhost:5000/v2/_catalog
{"repositories":[]}

┌──(kali㉿kali)-[~]
└─$ curl http://localhost:5000/v2/        
{}
┌──(kali㉿kali)-[~]
└─$ curl http://localhost:5000/   

┌──(kali㉿kali)-[~]
└─$
```
Here we can see that there’s an unauthenticated Docker repository exposed, though it doesn’t seem to have any images in it right now.



Now, using the password we got, we can do this:
```bash
┌──(kali㉿kali)-[~]
└─$ smbclient -L //localhost/ -p 1445 -N       
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
        labshare        Disk      
        IPC$            IPC       IPC Service (Samba 4.17.12-Debian)
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to localhost failed (Error NT_STATUS_CONNECTION_REFUSED)
Unable to connect with SMB1 -- no workgroup available

┌──(kali㉿kali)-[~]
└─$ smbclient //localhost/labshare -p 1445 -U smtpuser
Password for [WORKGROUP\smtpuser]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Dec  2 10:57:24 2025
  ..                                  D        0  Tue Dec  2 10:57:24 2025
  flag.txt                            N       38  Tue Dec  2 11:26:21 2025

                64753252 blocks of size 1024. 58292724 blocks available
smb: \> get flag.txt 
getting file \flag.txt of size 38 as flag.txt (0.6 KiloBytes/sec) (average 0.6 KiloBytes/sec)
smb: \> exit

┌──(kali㉿kali)-[~]
└─$ ls
autologin.exp  Documents  flag.txt  nmap_output.txt  Public     Videos
Desktop        Downloads  Music     Pictures         Templates

┌──(kali㉿kali)-[~]
└─$ cat flag.txt   
icyb{super_secret_lab7_flag_congrats}

┌──(kali㉿kali)-[~]
└─$ 
```
