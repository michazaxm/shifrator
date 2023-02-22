from random import seed, shuffle

class BitArray:
	def __init__(self, _bytes: bytes) -> None:
		self.data = self.to_bits(_bytes)
	def to_bits(self, _bytes: bytes) -> list[int]:
		result = []
		for b in _bytes:
		    result.extend(map(int, f'{b:08b}'))
		return result
	def to_bytes(self) -> bytes:
		return bytes(int(''.join(str(bit) for bit in bits), 2) for bits in [self.data[i:i + 8] for i in range(0, len(self.data), 8)])
	def __str__(self) -> str:
		return str([self.data[i:i + 8] for i in range(0, len(self.data), 8)]).replace(', ', '').replace('[', ' ').replace(']', '')[2:]
	def bitEncode(self, password):
		mask = list(range(len(self.data)))
		seed(password)
		shuffle(mask)
		result = [0] * len(self.data)
		for d in range(len(self.data)):
			result[mask[d]] = self.data[d]
		self.data = result
		return self

	def bitDecode(self, password):
		mask = list(range(len(self.data)))
		seed(password)
		shuffle(mask)
		result = []
		for d in mask:
			result.append(self.data[d])
		self.data = result
		return self
