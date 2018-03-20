import subprocess

host = "www.google.com"

ping = subprocess.Popen(
        ["ping", "-c", "8", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
)


out, error = ping.communicate()

print "Out : %s"%out



import re
matcher = re.compile("rtt min/avg/max/mdev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)")
values =  matcher.search(out).groups()

print values[0]
print values[2]

