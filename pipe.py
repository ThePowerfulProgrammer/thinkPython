import os
import subprocess

# Get the current working directory
current_path = os.getcwd()

# Print the current working directory
print("Current path:", current_path)


# Define the command to run (using cmd.exe to invoke the dir command)
cmd = 'cmd /c dir'

# Run the command and capture the output
result = subprocess.run(cmd, capture_output=True, text=True)

# Get the output of the command as a string
output = result.stdout

# Print the output
print(output)