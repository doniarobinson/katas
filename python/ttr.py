def ttr(str):
  calc_score = 0

  points = [1,2,4,7,10,15]
  pindex = 0

  for num in str.split(","):
    calc_score += int(num)*points[pindex]
    pindex += 1

  print "Score: ", calc_score

print "Enter train quantities in this format: 1,0,2,5,3,1"
str = raw_input("Enter your input: ");
ttr(str)