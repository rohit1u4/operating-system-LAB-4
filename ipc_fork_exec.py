import os

r, w = os.pipe()
pid = os.fork()

if pid > 0:
    # Parent
    os.close(r)
    os.write(w, b"Hello from parent process via pipe!")
    os.close(w)
    os.wait()
else:
    # Child
    os.close(w)
    data = os.read(r, 1024)
    print("Child received:", data.decode())
    os.close(r)
