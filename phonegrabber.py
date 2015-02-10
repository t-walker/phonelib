import sys
from libphone import isPhoneNumber

def grab(text):
  for i in range(len(text)):
    chunk = text[i:i+12]
    if isPhoneNumber(chunk):
      print("Phone number found: " + chunk)
  print("Done.")


def main():
  file_arg = sys.argv[1]

  in_file = open(file_arg, "r")
  
  file_data = in_file.read()
  
  grab(file_data)

  return 0

if __name__ == "__main__":
  main()
