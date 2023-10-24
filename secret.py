import urllib.request

try:
    with urllib.request.urlopen('') as conn:
        for line in conn:
            print(line.decode().strip())
except:
    print('Error handled :)')