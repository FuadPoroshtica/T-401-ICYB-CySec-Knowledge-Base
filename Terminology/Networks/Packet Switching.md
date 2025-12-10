---
aliases: []
date created: Tuesday, 2. December 2025, 19:12
date modified: Monday, 8. December 2025, 18:12
---

# Packet Switching
The internet uses a method called **packet switching** to send data. Instead of sending data as a continuous stream, it breaks the data into smaller packets. Each packet contains a portion of the data, along with metadata like source and destination addresses, sequence numbers, and error-checking information.
Steps:

1. Data is broken into smaller chunks called “packets”.
2. Packets are sent independently over the network.
3. Packets may take different routes to reach the destination.
4. At the destination, the receiver needs to reassemble the packets into the original data.

Packets may take any path through the network, reassembled by the receiver.

(**Lego analogy**: Each packet is like a Lego brick. You can send the bricks separately, and the receiver can put them together to build the original structure.)

Sometimes we have to consider *where* our packets are being sent. E.g., if you’re in Iceland and you’re sending data to a server in the US, your packets might go through multiple countries. This can have implications for privacy and security.
