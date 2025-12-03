---
aliases: []
date created: Wednesday, 3. December 2025, 08:12
date modified: Wednesday, 3. December 2025, 09:12
---

In the lab today we’ll be finding vulnerabilities in a web application and how they can be fixed.

# 2025-12-03
Many of these security problems come from the fact that many of the things we use online aren’t being used for what they were originally designed for.
Back in the day the main point was just to share documents and information, no one really considered the security implications of that.

HTTP was invented to transfer documents, not to handle sensitive information like passwords or credit card numbers. It was designed to be stateless and open by default.
But in modern times, we use this same protocol for everything from online banking to social media, which introduces a lot of security risks.
Conflict: We are forcing a protocol designed for *sharing* to perform tasks that require *privacy* and *security*.

# The Attack Surface
The attack surface of a web application is the sum of all the points where an unauthorized user (the attacker) can try to enter data or extract data from the application.
![](../zAttachments/Pasted%20image%2020251203090717.png)
E.g., login forms, search bars, file upload features, APIs, etc. All the computers, networks. Also all the software components, libraries, and frameworks that the application relies on; e.g., the browsers, the programming languages, and *their* web servers and databases.
Bro there are sooo many ways to attack people?
The larger the attack surface, the more opportunities there are for an attacker to find and exploit vulnerabilities
![|500](../zAttachments/Pasted%20image%2020251203091045.png)

Here we mainly we focus on vulnerabilities in the code, rather than the social engineering side of things.

We have to look at it from two main perspectives:
1. The viewpoint of the developer: They need to understand where vulnerabilities might arise in their code and how to mitigate them.
2. The user’s viewpoint: They need to be aware of potential risks when interacting with web applications and how to protect themselves.

## The golden rule of web security
**Never trust the Client.**
(In this context, the client is the user’s web browser or any other application that interacts with the web server.)
- The client is always compromised: The browser is entirely under the control of the user, who may have malicious intent.
- Manipulation: Users can manipulate client-side code (JavaScript, HTML) to exploit vulnerabilities.
- Implication: Client-side validation can be bypassed, so all critical checks must be performed on the server side.
- Rule: All security validations and checks must be done on the server side, regardless of any client-side validations.

## Attack Surface: Server-Side
The ways we can manipulate what is on the server is mainly through the *input* we get.

### Input Vectors
Input vectors are the various ways an attacker can send data to a web application.
- Visible input fields: Forms, search bars, file uploads.
- Hidden inputs: Hidden form fields, cookies, HTTP headers.
- API layer: Endpoints that accept data from clients.
- Supply chain: Third-party libraries and services integrated into the application.

## Attack Surface: Client-Side
Where the attacker targets the user within your application context.
- **The DOM (Document Object Model)**: The structure of the web page that can be manipulated using JavaScript.
	- DOM-based XSS (“XSS” means “Cross-Site Scripting”) attacks exploit vulnerabilities in client-side scripts to inject malicious code into the web page. The attacker can make the user execute some JavaScript by just manipulating the link that the client clicks.
	- (Reminder: The DOM is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. It’s basically a tree of objects that represent the elements on the page.)
	- *Risk*: If an attacker can manipulate the DOM, they can steal sensitive information (like cookies or session tokens), perform actions on behalf of the user, or redirect the user to malicious sites. The server-side essentially has nothing to do with this.
- **Client-side storage**: Local storage, session storage, cookies.
	- Sensitive data stored in client-side storage can be accessed or manipulated by attackers.
	- *Risk*: `localStorage` and `sessionStorage` are accessible by **any** JavaScript code running on the page, making them vulnerable to XSS attacks. So if you’re using them to store any secrets (e.g., tokens) they can be stolen with XSS.
- **Third-party scripts**: Ads, analytics, social media widgets.
	- Analytics, ads, and other third-party scripts can introduce vulnerabilities if they are compromised or malicious.
	- *Risk*: **Magecart** / **Formjacking** attacks, where attackers inject malicious code into third-party scripts to steal payment information.
