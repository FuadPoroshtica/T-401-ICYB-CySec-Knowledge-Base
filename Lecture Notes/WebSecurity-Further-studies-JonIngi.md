***Further studies web security***

***Cross-site request forgery (CSRF)***
CSRF is an attack where a victims browser is tricked into performing unwanted actions where users are authenticated. Usually they are performed by a link to a malicious website and after getting the token they can use it to change email address of the account, transfer money or make purchases if the victim is a normal user. If an admin is attacked it can be used to compromise the whole website.

***Cross-site scripting (XSS)***
XSS is an attack where the attacker injects malicious javascript into a trusted website. It can be used to steal data, steal session tokens, manipulate the web page and perform actions on users behalf. XSS does not require anyone to be logged in but if they are their session can be stolen.

***Difference between CSRF and XSS***
The difference between CSRF and XSS is that CSRF does not inject any malicious content to the website. Instead it is taking advantage of a users cookie. If the victim is authenticated and the website unsafe the attacker can trick the victims browser to perform unwanted actions. It is best used when the web application has “ease of use” features like one-click actions but only works when the user is logged in.

***Preventing CSRF***
To prevent CSRF attacks, it’s not enough to check whether a request has a valid session cookie. The application also needs to have a unique, unpredictable token with every request. This token is placed in hidden form fields and URLs and is freshly generated for each page and action. If the attacker cannot see or guess this random token, all forged requests they create won’t work.

***CSRF status in OWASP top 10***
Back in 2017 CSRF attacks were ranked number 8 in the OWASP top 10. In the most recent top 10 list in 2021 CSRF attacks were merged into “Broken Access Control” which is ranked number 1 on the OWASP top 10 but most frameworks nowadays include defense for CSRF attacks so there have been fewer attacks recently.



***Server-side request forgery (SSRF)***
SSRF is an attack where the attackers make requests to internal and unauthorized locations on a vulnerable server. They do this by controlling the URL of the server. The attacker can access internal services, read sensitive data or interact with the system that were not meant to be publicly reachable. This allows them to bypass restrictions and potentially give them more access into the infrastructure.

***Potential risks of SSRF***
The risks of SSRF are access of networks, theft of meta data, remote execution (RCE), unauthorized actions, data exfiltration, firewall/network bypass and more access to the infrastructure.  

If the attacker gets access to the networks they can get a lot of sensitive data E.G. The database, admin panels and internal APIs. 

If they steal the metadata the attacker can get access of all access keys, tokens and cookies giving them full control of their cloud. 

RCE can be used to execute commands and upload files which giving the attacker the opportunity to do almost anything to the infrastructure. 

Unauthorized actions can allow the attacker to make post requests to internal endpoints, they can reset passwords and enableing/disabling services. This of course depends on how much access they get.

Data exfiltration can give the attacker a lot of information allowing them to read configuration files, internal api responses and system statuses. 

Firewall bypass allows the attacker to use the server as a proxy allowing them access to networks that should be isolated.

With more access to the infrastructure the attacker can escalate privileges, search for more vulnerabilities and scan internal ports.

***Prevention of SSRF***
To prevent SSRF you should enforce a strict allowlist, block internal IP ranges, validate all URLs, restrict network permissions and prevent access to to cloud metadata and internal services

***SSRF status in OWASP TOP 10***
In the most recent OWASP top 10 SSRF attacks were ranked number 10 and its the first time it has had its own category. It was added due to it being frequently severe when attackers are able to use it and when they manage to it often leads to a full system compromise.

***Insecure deserialization***
Insecure deserialization attacks occur when an application takes in untrusted user controlled data and turns it into and object without verifying the safety of the data. When these objects are deserialized the system can automatically run contractors, methods or internal logic. If the attacker modifies the serialized data before it’s deserialized they can manipulate the rebuild of the object. This works because some programming languages allow code to execute during deserialization so a maliciously crafted payload can force the server to perform the actions. This can alter internal application state, escalate privileges and execute arbitrary code to the server. Insecure deserialization works by letting the attacker control the structure and contents of the objects to application that blindly trust and rebuild allowing them to influence the program execution.
