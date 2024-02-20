#!/usr/local/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mkf = open("makefile", "w")
        match sys.argv[1]:
            case "rust":
                mkf.write(
"""
all:
    cargo run

test:
    @cargo test

check:
    @cargo check

doc:
    @cargo doc --open                
"""
                )
            case "python":
                mkf.write(
"""
all:
    python3 main.py
"""
                )
            case other:  
                print(f"could not find a makefile for: '{sys.argv[1]}'")
    
        mkf.close()
    else:
        print(
			""" Usage: pass the language as an argument to create a makefile for that language. """
		)
