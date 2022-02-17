# Vigenère cipher

We're all familiar with Ceaser's cipher i.e. the words are enrypted by shifting the alplhabets by a constant position. One key issue with with this algorithm is that it's highly vulnerable to frequency analysis. This signified the need for a strong cipher algorithmn in order to move ahead than cryptoanalysts. This led to procurement of a cipher algorighmn known as Vigenère cipher. 

This algrithmn implements the Ceaser's cipher to each letters based on a agreeed upon cipher key. Using this algorithm, a same letter can appear in many form - making it strong against frequency analysis. Let's go with an example...

Say, the cipher key we're using be `CODER` - it's just an example you're free to choose yours but make sure it's mutual between you and your recipient.

We have a plaintext of `Hello Github, add a README file to a project.`
Now, we assign the Key to our plaintext.

|C|O|D|E|R|C|O|D|E|R|C|O|

|H | e | l | l | o | | G | i | t | h | u | b |  







See [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) for more additional information.
