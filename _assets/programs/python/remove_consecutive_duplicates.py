def traverse_string(IN):
	i = 0
	OUT = []
	while i < len(IN):
		OUT.append(IN[i])
		i = i + 1
	return OUT

def mark_all_consecutive_duplicates_1(IN):
	i = 0
	OUT = IN
	while i < len(IN):
		if IN[i] == IN[i+1]:
			OUT[i] = '0'
		i = i + 1
	return OUT

def mark_all_consecutive_duplicates_2(IN):
	i = 0
	OUT = IN[:]
	while i + 1 < len(IN):
		if IN[i] == IN[i+1]:
			OUT[i] = '0'
		i = i + 1
	return OUT

def mark_all_consecutive_duplicates_and_original_1(IN):
	i = 0
	OUT = IN[:]
	while i + 1 < len(IN):
		if IN[i] == IN[i+1]:
			OUT[i] = '0'
		elif IN[i] == IN[i-1]:
			OUT[i] = '0'
		i = i + 1
	return OUT

def mark_all_consecutive_duplicates_and_original_2(IN):
	i = 0
	OUT = IN[:]
	while i + 1 < len(IN):
		if IN[i] == IN[i+1]:
			OUT[i] = '0'
		elif IN[i] == IN[i-1] and i != 0:
			OUT[i] = '0'
		i = i + 1
	if IN[i] == IN[i-1]:
		OUT[i] = '0'
	return OUT

class Stack():
	def __init__(self, val=None):
		if val == None:
			val = []
		self.val = val[:]
	def pop(self):
		return self.val.pop()
	def peek(self):
		if not self.is_empty():
			return self.val[-1]
		return None
	def push(self, item):
		self.val.append(item)
	def is_empty(self):
		return len(self.val) == 0
	def reversed_list(self):
		return reversed(self.val)



if __name__ == "__main__":
	IN = list("aaabbcbdd")
	print("".join(traverse_string(IN)))
	# print("".join(mark_all_consecutive_duplicates_1(IN)))
	print("".join(mark_all_consecutive_duplicates_2(IN)))
	print("".join(mark_all_consecutive_duplicates_and_original_1(IN)))
	print("".join(mark_all_consecutive_duplicates_and_original_2(IN)))
	