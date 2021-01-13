# CryptographyTProjects

This repository includes various small projects about cryptography algorithm implementations (e.g. encryption and attack) introduced in Dan Boneh **Cryptography I** course, Stanford University. 

***many_time_pad.py***: Many-Time Pad Attack. Single stream cipher should never be used to encrypt multiple messages. Given a collection of 11 hex-encoded ciphertexts that are the result of encrypting 11 plaintext messages with the same one-time pad. Based on that, we could decrypt the last ciphertext and obtain the secret message. XOR the ciphertexts together, and consider what happens when space is XORed with a character in [a-z A-Z].

***cbc_ctr.py***: Implement two classical encryption/decryption systems (AES-CBC and AES-CTR) separately. 16-byte encryption IV is chosen at random and is prepended to the ciphertext. For CBC encryption we use the PKCS5 padding scheme. Given an AES key and a ciphertext (hex-encoded), we aim to recover the plaintext. 

***sha256.py***: Build a file authentication system that lets browsers authenticate and play video chunks as they are downloaded without having to wait for the entire file. Instead of computing a hash of the entire file, the website breaks the file into 1KB block (1024 bytes). It computes the hash of the last block and appends the value to the second to last block (recursively doing that). The final hash value h0 – a hash of the first block with its appended hash – is distributed to users via the authenticated channel. When the first block (B0||h1) is received, the browser could check whether it is equal to h0 and if so it begins playing the first video block. If the hash function H is collision-resistant, then the attacker cannot modify any of the video blocks without being detected by the browser. Therefore after the first hash check, the browser is convinced that both B0 and h1 are authentic, and so on for the remaining blocks. 

***padding_oracle_attack.py***: Experiment with a padding oracle attack against a toy web site hosted at *crypto-class.appspot.com*. Padding oracle vulnerabilities affect a wide variety of products, including secure tokens. The website is vulnerable to a CBC padding oracle attack. When a decrypted CBC ciphertext ends in an invalid pad the webserver returns a 403 error code (forbidden request). When the CBC padding is valid, but the message is malformed, the webserver returns a 404 error code (URL not found). To decrypt a single byte, we need to send up to 256 HTTP requests to the site.  The first ciphertext block is the random IV. The decrypted message is ASCII encoded. From this project, we understand that when using encryption we must prevent padding oracle attacks by either using encrypt-then-MAC as in EAX or GCM. Also, if we must use MAC-then-encrypt, then ensure that the site treats padding errors the same way it treats MAC errors.

***discrete_log.py***: Compute discrete log modulo a prime p. Let g be some elements in <img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1">


 and suppose you are given h in 

