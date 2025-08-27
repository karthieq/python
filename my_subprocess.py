import subprocess

p = subprocess.run('dir *.py', shell=True, capture_output=True, text=True)

print(p.args)
print(p.returncode)
print(p.stdout)
print(p.stderr)
