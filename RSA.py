import math

'''
Exponentiation of large integers is the basis of common algorithms for public-key en
cryption. Read the Wikipedia page on the RSA algorithm (http://en.wikipedia.org/wiki/
RSA) and write functions to encode and decode messages


Key Generation:

Select two distinct prime numbers, p and q.
Compute the modulus, n, by multiplying p and q: n = p * q.
Calculate the totient, φ(n), which is the number of positive integers less than n that are coprime with n. For two primes, φ(n) = (p - 1) * (q - 1).
Choose a public exponent, e, such that 1 < e < φ(n) and e is coprime with φ(n). The most common choice is e = 65537 (2^16 + 1), which is a known prime number.
Compute the private exponent, d, which is the modular multiplicative inverse of e modulo φ(n). In other words, d satisfies the equation: (d * e) % φ(n) = 1.
The public key is (e, n), and the private key is (d, n).
'''

# Grab two prime numbers from a range
def sieve_of_eratosthenes(max_limit):
    primes = []
    is_prime = [True] * (max_limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(math.sqrt(max_limit)) + 1):
        if is_prime[num]:
            for multiple in range(num * num, max_limit + 1, num):
                is_prime[multiple] = False

    for num in range(2, max_limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes[:2]  # Return the first two primes

# Usage:
max_limit = 100  # Adjust this value as per your requirements
distinct_primes = sieve_of_eratosthenes(max_limit)

if len(distinct_primes) == 2:
    p, q = distinct_primes
    print("Distinct prime numbers:", p, q)
else:
    print("Unable to find two distinct prime numbers within the specified limit.")

# Compute the modulus, n, by multiplying p and q: n = p * q.
modulus_n = p * q

# Calculate the totient, φ(n), which is the number of positive integers less than n that are coprime with n. For two primes, φ(n) = (p - 1) * (q - 1).
totient = (p-1)*(q-1)


# Choose a public exponent, e, such that 1 < e < φ(n) and e is coprime with φ(n). The most common choice is e = 65537 (2^16 + 1), which is a known prime number.
publicExponent = 65537 #65537*(2**16+1)

# Compute the private exponent, d, which is the modular multiplicative inverse of e modulo φ(n). In other words, d satisfies the equation: (d * e) % φ(n) = 1.
privateExponent = publicExponent%totient

# The public key is (e, n), and the private key is (d, n).
publicKey = (publicExponent,modulus_n)
privateKey = (privateExponent,modulus_n)

# the public key (e, n) can be shared with others for encryption, while the private key (d, n) should be kept secret and used for decryption


# ------------------------------------------------------------------------------------------------------------------------------------------
# Encryption:

# Convert the plaintext message into a numerical representation. This can be done using various encoding schemes, such as ASCII or Unicode.
def plainText_To_Numeric(plaintext):
    ascii_values = [ord(character) for character in plaintext]
    return ascii_values
    

text = input("Enter a string: ")
numericText = plainText_To_Numeric(text)
print(numericText)
# Break the message into smaller blocks if necessary.

# For each block, calculate the ciphertext by raising it to the power of the public exponent, e, modulo n: ciphertext = (block^e) % n.
def cipherText(numText,e,n):
    secretText = [((num**e) % n) for num in numText]
    with open("cipherText.txt", "w") as file:
        for num in secretText:
            file.write(str(num) + " ")
    return secretText;

print(cipherText(numericText, publicExponent, modulus_n))
# The resulting ciphertext is the encrypted message


# Decrypt
def decrypt(cipherFile,d,n):
    regularText = []
    with open(cipherFile, "r") as file:
        ciphertext = file.read().strip().split()  # Read the ciphertext from the file and split it into blocks

    for block in ciphertext:
        num = int(block)  # Convert the block to an integer
        decrypted_num = pow(num, d, n)
        print(f"value --> {decrypted_num} <--")
        regularText.append(decrypted_num)
    return regularText

print(decrypt("cipherText.txt",privateExponent,modulus_n))