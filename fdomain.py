#!/usr/bin/env python3

import re, sys, random

class DomainFilter:
    def __init__(self, inputfile=None):
        self.inputfile = inputfile

    def read_text(self):
        if self.inputfile:
            with open(self.inputfile, "r") as file:
                self.text = file.read()
        else:
            if not sys.stdin.isatty():
                self.text = sys.stdin.read()
            else:
                print("---> Error: No input file or pipe provided.")
                print("---> Usage: 'cat urls.txt|fdomain' or 'python3 fdomain.py <input_file>'")
                sys.exit(1)

    def find_domains(self):
        self.domains = re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}", self.text)

    def write_filtered_domains(self):
        random_int = random.randint(1, 100000)
        filename = f"{self.inputfile or 'Pipe_'}Filtered_Domains_{random_int}"
        with open(filename, "w") as file:
            file.write("\n".join(self.domains))
            print(f"---> Result Saved as {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        domain_filter = DomainFilter()
    else:
        inputfile = sys.argv[1]
        domain_filter = DomainFilter(inputfile)
    domain_filter.read_text()
    domain_filter.find_domains()
    domain_filter.write_filtered_domains()
