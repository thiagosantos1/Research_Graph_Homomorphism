 #!/usr/bin/env python3
# chmod u+x

import sys
import re


def main():
  if len(sys.argv) < 2:
    print("Usage<path result_LP> to calculate the ratio")
    sys.exit(1)

  file_path = sys.argv[1]

  try:
    with open(file_path,"r") as file:
      total_Integral = 0
      total_Continuos = 0
      for line in file.readlines():
        isIntegral = True
        if line.find("Continuos") >=0:
          isIntegral = False

        splited_line = line.split("Total Cost:")
        if len(splited_line) >1:

          splited_line[1] = splited_line[1].strip() # for spaces
          splited_line[1] = splited_line[1].strip('\n') # for the new line
          cost = float(splited_line[1].split()[0])
          if isIntegral:
            total_Integral += cost
          else:
            total_Continuos += cost
      file.close()

    file_path_splt = file_path.split(".txt")
    file_out = file_path_splt[0] + "_ration.txt"

    with open(file_out,"w") as file:
      file.write(str(total_Continuos/total_Integral))
      file.close()

  except Exception as e:
    print("Error opening file " + file_path)
    raise e

if __name__ == '__main__':
  main()


