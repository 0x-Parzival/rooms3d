import os
import re

root_dir = "/home/parzival/3droom"
rooms = [f"ThreeJS-Room{i:02d}" for i in range(6, 18)]
# Room 06 might need it too? It has src/App.js usually or similar.
# Rooms 07-14 use src/script.js.
# Rooms 15-17 use src/main.js or similar? checked 17: src/main.js

def fix_file(filepath):
    if not os.path.exists(filepath):
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace .load('/ with .load('./
    # Replace .load("/ with .load("./
    
    # Regex for .load( quote /
    # Captures the load method call locally
    
    # Pattern 1: .load('/...') -> .load('./...')
    new_content = re.sub(r"\.load\s*\(\s*['\"]/([^'\"]+)['\"]", r".load('./\1')", content)
    
    # Also handle map: ... '/...' if they exist implies direct texture loading sometimes?
    # But usually it's textureLoader.load
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed paths in {filepath}")

for room in rooms:
    room_path = os.path.join(root_dir, room)
    
    # Common locations
    files_to_check = [
        "src/script.js",
        "src/main.js", 
        "src/index.js",
        "src/App.jsx",
        "src/App.js",
        "src/Experience/World/Environment.js" # deeply nested?
    ]
    
    # Walk src dir
    src_dir = os.path.join(room_path, "src")
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if file.endswith(".js") or file.endswith(".jsx") or file.endswith(".ts") or file.endswith(".tsx"):
                    fix_file(os.path.join(root, file))

print("Source code patching complete.")
