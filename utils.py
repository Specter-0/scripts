#!/usr/local/bin/python3
import os, json, subprocess

# ? This is a module that contains stuff that are used in scripts

def path(string : str):
    return os.path.expanduser(string)

def clear():
    subprocess.run(["clear"])

class Config:
    def __init__(self, filename : str, structure : dict) -> None:
        self.ref = path(f"~/scripts/.{filename}.json")
        
        if not os.path.exists(self.ref):
            self.dump(structure)
    
    def load(self):
        return json.load(open(self.ref))
    
    def dump(self, config : dict):
        json.dump(config, open(self.ref, "w"), indent=4)