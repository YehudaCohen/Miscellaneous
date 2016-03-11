class HashMap:

    def __init__(self,n_buckets, hash_function_generator):
        self.n_buckets = n_buckets
        self.array = n_buckets * [None]
        self.hash = hash_function_generator(n_buckets)


    def set(self, key, value):
        self.array.insert(self.hash(key), value)

    def get(self, key):
        return self.array[self.hash(key)]


def hash_function_generator(n_buckets):
    return lambda input: sum((ord(char) for char in str(input))) % n_buckets

a = HashMap(100, hash_function_generator)
a.set("hello", True)

assert a.get("hello")
assert a.get("goodbye") == None
