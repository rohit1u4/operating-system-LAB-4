import subprocess

scripts = ['script1.py', 'script2.py', 'script3.py']

print("----- Batch Processing Started -----")

for script in scripts:
    print(f"\nExecuting {script} ...")
    subprocess.call(['python3', script])

print("\n----- Batch Processing Completed -----")
