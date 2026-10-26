import argparse
parser = argparse.ArgumentParser(description="Greeter")
parser.add_argument("name")
parser.add_argument("--times", type=int, default=1)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args(["Ada", "--times", "2", "-v"])     # normally reads sys.argv
for _ in range(args.times):
    print("hello", args.name)
print(args.verbose)
