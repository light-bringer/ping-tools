import subprocess

host = ["www.google.com", "192.0.0.25"]
rounds = 32

ping = subprocess.Popen(
        ["ping", "-c", str(rounds), host[1]],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
)


out, error = ping.communicate()

print "Out : %s"%out



import re
matcher = re.compile("rtt min/avg/max/mdev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)")
values =  matcher.search(out).groups()

print "Output : %s"%out

print "Min : %s"%values[0]
print "Average: %s"%values[1]
print "Maximum: %s"%values[2]
print "MDeviation: %s"%values[3]


