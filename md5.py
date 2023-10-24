import subprocess

filename = 'book.tex'  # Replace this with the path and name of the file you want to check

# Construct the command
cmd = ['certutil', '-hashfile', filename, 'MD5']

# Execute the command and capture the output
result = subprocess.run(cmd, capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Extract the MD5 checksum from the output
    md5_checksum = result.stdout.split()[1]
    print(f'MD5 checksum for {filename}: {md5_checksum}')
else:
    print(f'Error executing the command: {result.stderr}')
