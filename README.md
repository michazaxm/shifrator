# About
This library turns bytes into bits and allows them to be encrypted with a password
# Installing:
```bash
pip install bit-shifrator
```
# Using:
### BitEncode
```python
from shifrator import BitArray
data = BitArray('Hello'.encode('UTF-8'))
print(data) # Printing bits
data.bitEncode('password') # Encoding with password, password must be str
print(data.to_bytes()) # printing bytes
data.bitDecode('password') # Decoding with password, password must be str
print(data.to_bytes()) # Printing of original value
```
### XOR
```python
from shifrator import BitArray
data = BitArray('Hello'.encode('UTF-8'))
print(data) # Printing bits
key = data.xorEncode() # Return key
print(data.to_bytes()) # printing bytes
data.xorDecode(key) # Decoding with key, key must be bytes
print(data.to_bytes()) # Printing of original value
```
