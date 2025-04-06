#ProcessData.py
#Name: Ryan Meegan
#Date: Apr 6 2025
#Assignment: Lab 8

import random

def main():

  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  outFile.write("Last Name,First Name,UserID,Major-Year\n")

  inFile.readline()

  for line in inFile:
    data = line.strip().split()

    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)

    major = major.upper()
    major = major[0:3]

    if year == "Freshman":
      yearCode = "FR"
    elif year == "Sophomore":
      yearCode = "SO"
    elif year == "Junior":
      yearCode = "JR"
    elif year == "Senior":
      yearCode = "SR"
    else:
      yearCode = "??"

    majorYear = major + "-" + yearCode

    output = last + "," + first + "," + student_id + "," + majorYear + "\n"
    outFile.write(output)

  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  #print(id)
  return id

if __name__ == '__main__':
  main()