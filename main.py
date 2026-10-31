import argparse
import sys


def main(argv=None):
    p = argparse.ArgumentParser(prog="tool", description="small cli helper")
    p.add_argument("values", nargs="*", help="values to process")
    p.add_argument("--version", action="version", version="tool 0.1.0")
    a = p.parse_args(argv)
    if not a.values:
        print("nothing to do — pass at least one value", file=sys.stderr)
        return 2
    for v in a.values:
        print("%s -> %s" % (v, v.strip().lower()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
