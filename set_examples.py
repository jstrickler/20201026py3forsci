
bob_countries = ['India', 'Canada', 'Australia', 'Spain', 'Portugal', 'Ireland']
jane_countries = ['France', 'Indonesia', 'Japan', 'India', 'Spain', 'Germany', 'Ireland']

bob = set(bob_countries)
jane = set(jane_countries)

print("Both:", bob & jane)  # intersection  (common)
print("Just one:", bob ^ jane)   # Xor  (not common)
print("All:", bob | jane)   # union (all, but no dupes)
print("Just Bob:", bob - jane)
print("Just Jane:", jane - bob)

