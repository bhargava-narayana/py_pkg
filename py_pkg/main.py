#!/usr/bin/env python3
from py_pkg.imp_eg import myYaml

def main() -> None:
    print("inside py_pkg.main.main()")
    print(f"import example: {myYaml()}")

if __name__ == "__main__":
    main()
