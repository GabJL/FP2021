def posACGT(seq, nuc):
  pos = []
  for i in range(len(seq)):
    if seq[i] == nuc:
      pos.append(i+1)
  return pos

# Programa principal
seq = 'ATCCATTCGACTCCACACAGCTAGCGTGGCACTTTCACGACATCTAAACGAAAGGTCTCG'
print(posACGT(seq, "A"))
