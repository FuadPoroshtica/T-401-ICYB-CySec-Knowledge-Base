Our main goal is to break the hash and open the .dd file.
We need to bruteforce the disk, main tool used is John the ripper, first thing to do is use 
bitlocker2john -i bitlocker-1.dd > bitlocker_hash.txt ot to get all the hashes

You get something like this 
User Password hash:  
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d

Now we need to brute force it to get the password of the user
hashcat -m 22100 -a 0 bitlocker_hash.txt top2k.txt -w 3

We use hashmap to bruteforce the it, you need to check the numbers like 22100 for each system you are breaking. 

sudo dislocker bitlocker-1.dd -ujacqueline dislocker, we now use dislocker to dislock the disk and make it accessible,

sudo mount -o loop dislocker/dislocker-file mounted

use mount to load the disk so we can read of it