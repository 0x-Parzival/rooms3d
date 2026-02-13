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
    
    # Clean dist if possible? Webpack clean plugin should do it.
    
    try:
        # Room 12 and others might need legacy provider
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
            print(result.stderr[-500:]) # Print last 500 chars of error
            failed_builds.append(room)
            
    except Exception as e:
        print(f"Exception building {room}: {e}")
        failed_builds.append(room)

if failed_builds:
    print(f"The following rooms failed to build: {failed_builds}")
else:
    print("All rooms built successfully.")
