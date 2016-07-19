## Classical
### Algebraic attack:
You express the plaintext-to-ciphertext relationship as a system of equations. Given a set of (plaintext, ciphertext) pairs, you try to solve the equations for the encryption key.

As you will , encryption algorithms involve nonlinearities. In algebraic attacks, one attempts to **introduce additional variables into the system of equations and make nonlinear equations look linear**.

### Time-memory tradeoff in attacking ciphers: 
The brute-force and the codebook attacks represent two opposite cases in terms of time versus memory needs of the algorithms. Pure brute-force attacks have very little memory needs, but can require inordinately long times to scan through all possible keys. On the other hand, codebook attacks can in principle yield results instantaneously, but their memory needs can be humongously large. Just imagine a codebook for a 64-bit block cipher; it may need as many as 264 rows in it. In some cases, by trading off memory for time, it is possible to devise more effective attacks that are sometimes referred to as time-memory tradeoff attacks.


“All internet communications are character based” data file available to the TCP/IP engine in your computer could corrupt your data if it is not based on just printable characters.(Base64, this 64-element set consists of the characters A-Z, a-z, 0-9, ‘+’, and ‘/’.])


## Block Cipher
### Diffusion and confusion are the two cornerstones of block cipher design.
Note that the goal of the substitution step implemented by the S-box is to introduce diffusion in the generation of the output from the input. Diffusion means that each plaintext bit must affect as many ciphertext bits as possible.

The strategy used for creating the different round keys from the main key is meant to introduce confusion into the encryption process. Confusion in this context means that the relation-ship between the encryption key and the ciphertext must be as complex as possible. Another way of describing confusion would be that each bit of the key must affect as many bits as possible of the output ciphertext block.
> Also see substitution and permutation