from __future__ import print_function
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser("===Super Cool Application===")
  parser.add_argument("name", help="name of a person")

args = parser.parse_args()
if args.name == None:
  print("hello world!")
else:
  print("hello {}".format(args.name))

print("Bye!")
