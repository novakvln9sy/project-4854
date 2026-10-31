import sys


def run(args):
    if not args:
        return 1
    total = 0
    for a in args:
        try:
            total += int(a)
        except ValueError:
            print("skipping non-numeric: %s" % a, file=sys.stderr)
    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
