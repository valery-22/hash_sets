def simple_hash(input_string):
    summation = sum(ord(ch) for ch in input_string)
    return summation % 10


print(simple_hash("Hello"))
print(simple_hash("World"))