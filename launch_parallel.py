import subprocess
import os
import sys

rooms = ["ThreeJS-Room06", "ThreeJS-Room07", "ThreeJS-Room08", "ThreeJS-Room09", "ThreeJS-Room10", "ThreeJS-Room11", "ThreeJS-Room13", "ThreeJS-Room14"]
root = "/home/parzival/3droom"
env = os.environ.copy()
env["NODE_OPTIONS"] = "--openssl-legacy-provider"

for room in rooms:
    print(f"Launching {room}...")
    subprocess.Popen(
        ["npm", "run", "build"],
        cwd=os.path.join(root, room),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
print("Launched all builds in background.")
