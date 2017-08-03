import lsalib

# To use this, initalize a varible,
lsa = lsalib.termDocMatrix()

# After this, you can add documents to the matrix. This can be done in a number of ways
# With Strings:
lsa.add("HELLO WORLD! THE WIND RISES, WE MUST TRY TO LIVE")

# With Dictionaries (a key:count relationship)
lsa.add({"tree":5, "apple":3, "WORLD":8, "planes":2})

# With lists of strings:
lsa.add(["apples", "oranges", "apples", "WORLD", "HELLO"])

