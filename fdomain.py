#!/usr/bin/env python3

import re,sys, random

class DomainFilter:
    def __init__(self, inputfile):
        self.inputfile = inputfile

    def read_text(self):
        with open(self.inputfile, "r") as file:
            self.text = file.read()

    def find_domains(self):
        self.domains = re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}", self.text)

    def write_filtered_domains(self):
        random_int = random.randint(1, 100000)
        filename = f"{self.inputfile}_Filtered_Domains_{random_int}"
        with open(filename, "w") as file:
            file.write("\n".join(self.domains))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input file provided.")
        print("Usage: fdomain <input_file>")
        print("Usage: python3 fdomain.py <input_file>")
        sys.exit(1)
    inputfile = sys.argv[1]
    domain_filter = DomainFilter(inputfile)
    domain_filter.read_text()
    domain_filter.find_domains()
    domain_filter.write_filtered_domains()
