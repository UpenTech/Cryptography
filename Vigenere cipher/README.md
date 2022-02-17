# Vigenère cipher

We're all familiar with Ceaser's cipher i.e. the words are enrypted by shifting the alplhabets by a constant position. One key issue with with this algorithm is that it's highly vulnerable to frequency analysis. This signified the need for a strong cipher algorithm in order to move ahead than cryptoanalysts. This led to procurement of a cipher algorithm known as Vigenère cipher. 

This algrithmn implements the Ceaser's cipher to each letters based on a agreeed upon cipher key. Using this algorithm, a same letter can appear in many form - making it strong against frequency analysis. Let's go with an example...

Say, the cipher key we're using be `CODER` - it's just an example you're free to choose yours but make sure it's mutual between you and your recipient.

We have a plaintext of `Hello Github, add a README file to a project.`
Now, we assign the Key to our plaintext.

| C | O | D | E | R | C | O | D | E | R | C | O |
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|H | e | l | l | o | | G | i | t | h | u | b |  


Now, we create a Ceaser's cipher table where alphabets are shifted in such a way that the each row starts with letters from our `CIPHER KEY`.

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |
| O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N |
| D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |
| E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |

Well, now follow the same pattern -just skip the letters other than the ones in English Alphabet. I'm a bit lazy to type all those out but you get the idea, for now that's more important.

Hold ypur horses, we're almost done ..
Now, compare the plaintext letters with our ceaser's list and arrage it accordingly; that'll be our encrypted text.

Here, 1st letter of our plaintext `H` is aligned with letter `J` in 1st Row of our Ceaser's list.
2nd letter of our plaintext `e` is aligned with letter `S` in 2nd Row of our Ceaser's list.
3rd letter of our plaintext `l` is aligned with letter `O` in 3rd Row of our Ceaser's list.
4th letter of our plaintext `l` is aligned with letter `P` in 4th Row of our Ceaser's list.
5th letter of our plaintext `o` is aligned with letter `Q` in 5th Row of our Ceaser's list.

So, our ciphertext will be `JSOPQ` for our plaintext word `Hello`. Just implement the same procedure for words henceafter - you can
cipher the characters other than the ones in the English Alphabet as your wish.


See [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) for more additional information.
