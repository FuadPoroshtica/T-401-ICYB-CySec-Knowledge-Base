---
aliases: [File Transfer Protocol]
date created: Tuesday, 2. December 2025, 19:12
date modified: Thursday, 11. December 2025, 09:12
---

# FTP
**FTP** stands for **File Transfer Protocol**. It is a standard network protocol used for transferring files between a client and a server over a computer network, such as the internet. FTP operates on the [Application Layer](../OSI%20Model/7-Application%20Layer.md) of the [OSI Model](../OSI%20Model/OSI%20Model.md).
FTP allows users to upload, download, and manage files on a remote server. It supports various commands for file operations, such as listing directories, changing directories, and deleting files.
FTP can operate in two modes: active and passive.
- In active mode, the client opens a random port and waits for the server to connect to it,
- While in passive mode, the server opens a random port and waits for the client to connect to it.

FTP typically uses two separate channels for communication:

- A control channel for sending commands and responses (default port: 21)
- And a data channel for transferring files (default port: 20).

FTP does not provide built-in encryption, which means that data, including usernames and passwords, is transmitted in plain text. To enhance security, secure variants of FTP, such as FTPS (FTP over SSL/[TLS](../TLS.md)) and SFTP (SSH File Transfer Protocol), are commonly used.

FTP is widely used for website management, file sharing, and data backup. It is supported by various FTP clients and servers, making it a versatile and widely adopted protocol for file transfer.
