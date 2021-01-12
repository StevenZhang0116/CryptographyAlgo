# CryptographyTProjects

This repository includes various small projects about cryptography algorithm implementations (e.g. encryption and attack) introduced in Dan Boneh **Cryptography I** course, Stanford University. 

***many_time_pad.py***: Many-Time Pad Attack. Single stream cipher should never be used to encrypt multiple messages. Given a collection of 11 hex-encoded ciphertexts that are the result of encrypting 11 plaintext messages with the same one-time pad. Based on that, we could decrypt the last ciphertext and obtain the secret message. XOR the ciphertexts together, and consider what happens when a space is XORed with a character in [a-z A-Z].
