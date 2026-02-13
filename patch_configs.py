import os
import json
import re
import subprocess

root_dir = "/home/parzival/3droom"

# Room 06: Add homepage: "."
room06 = os.path.join(root_dir, "ThreeJS-Room06")
pjson = os.path.join(room06, "package.json")
if os.path.exists(pjson):
    with open(pjson, 'r') as f:
        data = json.load(f)
    if "homepage" not in data:
        data["homepage"] = "."
        with open(pjson, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Patched {pjson}")

# Rooms 07-14: Patch webpack.common.js
for i in range(7, 15):
    room = f"ThreeJS-Room{i:02d}"
    path_dir = os.path.join(root_dir, room)
    webpack_config = os.path.join(path_dir, "bundler/webpack.common.js")
    
    if os.path.exists(webpack_config):
        with open(webpack_config, 'r') as f:
            content = f.read()
        
        # Add publicPath: './' to output object if not present
        if "publicPath" not in content:
            # Look for path: ... and append publicPath
            # Regex to find output: { ... path: ... }
            # Simple approach: replace "path: path.resolve(__dirname, '../dist')" with "path: path.resolve(__dirname, '../dist'), publicPath: './'"
            
            new_content = content.replace(
                "path: path.resolve(__dirname, '../dist')",
                "path: path.resolve(__dirname, '../dist'),\n        publicPath: './'"
            )
            
            if new_content != content:
                with open(webpack_config, 'w') as f:
                    f.write(new_content)
                print(f"Patched {webpack_config}")

# Create a master build script to run in parallel?
# We can just print the commands needed and I'll execute them or run them here sequentially (slow)
# Let's run them sequentially but validly.
