#1 CCC 2023 Junior Q4

colums = int(input(""))
row1 = list(input(""))
row2 = list(input(""))
idx1 = []
idx2 = []
for nums in row1:
  idx = row1.index(nums)
  if nums == "1":
    idx1.append(row1.index(nums))
  row1[idx] = "0"
for nums in row2:
  idx = row2.index(nums)
  if nums == "1":
    idx = row2.index(nums)
    idx2.append(row2.index(nums))
  row2[idx] = "0"
totalTriangles = len(idx1) + len(idx2)
tapeNeded = totalTriangles * 3
for i in idx1:
  if i + 2 in idx1:
    tapeNeded -= 1
  try:
    if i - 2 in idx1:
      tapeNeded -= 1
  except:
    pass
  if i%2 == 0 and i in idx2:
    tapeNeded -= 1

for i in idx2:
  if i + 1 in idx2:
    tapeNeded -= 2
  try:
    if i - 2 in idx2:
      tapeNeded -= 1
  except:
    pass
  if i%2 == 0 and i in idx1:
    tapeNeded -= 1
print(tapeNeded)
print(idx1, idx2)
