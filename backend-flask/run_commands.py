#!/usr/bin/env python

import subprocess

# Replace these commands with the ones specified in your Dockerfile CMD line
commands = ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

# Execute the commands
for command in commands:
    subprocess.run(command, shell=True)