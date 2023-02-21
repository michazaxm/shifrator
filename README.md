# About
This library turns bytes into bits and allows them to be encrypted with a password
# Installing:
```bash
pip install shifrator
```
# Using:
```python
from shifrator import BitArray
data = BitArray('Hello'.encode('UTF-8'))
print(data) # Printing bits
data.bitEncode('password') # Encoding with password, password must be str
print(data.to_bytes()) # printing bytes
data.bitDecode('password') # Decoding with password, password must be str
print(data.to_bytes()) # Printing of original value
```
