def has_odd_product_pair(sequence):
    """
    mathematically we only get an odd number ifwe multiply 2 distinct odd numbers so we will be just searching for odd numbers and if it's more than 2 numbers then we are fine to go
    """
    distinct_odds = set(x for x in sequence if x%2!=0)
    return len(distinct_odds)>=2

# example usage:
seq1 = [2, 4, 3, 8, 5]
seq2 = [2, 4, 3, 8, 3] # only one distinct odd number (3)
seq3 = [2, 4, 6, 8]

print(f"Sequence {seq1} has distinct odd product pair?", has_odd_product_pair(seq1))
print(f"Sequence {seq2} has distinct odd product pair?", has_odd_product_pair(seq2))
print(f"Sequence {seq3} has distinct odd product pair?", has_odd_product_pair(seq3))
