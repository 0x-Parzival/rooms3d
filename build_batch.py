import os
import subprocess
import time

root_dir = "/home/parzival/3droom"
rooms_to_build = [
    f"ThreeJS-Room{i:02d}" for i in [6, 7, 8, 9, 10, 11, 13, 14]
]
# Room 12 will be added after I fix it.

# Sequential build to save resources (or semi-parallel?)
# Sequential is safer to avoid crashing the system.

for room in rooms_to_build:
    room_path = os.path.join(root_dir, room)
    print(f"Building {room}...")
    try:
        # Check if node_modules exists to skip install if possible? No, best to install.
        subprocess.run("npm install", shell=True, cwd=room_path, check=True)
        subprocess.run("npm run build", shell=True, cwd=room_path, check=True)
        print(f"Finished {room}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build {room}: {e}")

print("All builds completed.")
