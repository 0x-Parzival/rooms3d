import subprocess
import os

rooms_to_build = [
    "ThreeJS-Room07", "ThreeJS-Room08", "ThreeJS-Room09", 
    "ThreeJS-Room10", "ThreeJS-Room11", "ThreeJS-Room12", 
    "ThreeJS-Room13", "ThreeJS-Room14"
]

root_dir = "/home/parzival/3droom"
failed_builds = []

env = os.environ.copy()
env["NODE_OPTIONS"] = "--openssl-legacy-provider"

for room in rooms_to_build:
    room_dir = os.path.join(root_dir, room)
    print(f"Building {room}...")
    
    # Check if node_modules exists, if not, install
    if not os.path.exists(os.path.join(room_dir, "node_modules")):
        print(f"Installing dependencies for {room}...")
        subprocess.run(["npm", "install"], cwd=room_dir, capture_output=True)
    
    try:
        result = subprocess.run(
            ["npm", "run", "build"],
            cwd=room_dir,
            env=env,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"Successfully built {room}")
        else:
            print(f"Failed to build {room}")
            print(result.stderr[-500:]) 
            failed_builds.append(room)
            
    except Exception as e:
        print(f"Exception building {room}: {e}")
        failed_builds.append(room)

if failed_builds:
    print(f"The following rooms failed to build: {failed_builds}")
else:
    print("All rooms built successfully.")
