import os
import re

root_dir = "/home/parzival/3droom"
rooms_to_patch = [f"ThreeJS-Room{i:02d}" for i in [1, 2, 3, 5]]

def patch_bundle(room_path):
    # dedicated files to look for
    files_in_root = [f for f in os.listdir(room_path) if os.path.isfile(os.path.join(room_path, f))]
    
    # helper to find bundle
    bundle_file = None
    for f in files_in_root:
        if f.startswith("bundle.") and f.endswith(".js"):
            bundle_file = f
            break
    
    if not bundle_file:
        print(f"No bundle file found in {room_path}")
        return

    bundle_path = os.path.join(room_path, bundle_file)
    with open(bundle_path, 'r', encoding='latin-1') as f: # binary safety?
        content = f.read()

    original_len = len(content)
    
    # 1. Replace references to root files
    # seeking "/filename.ext" patterns
    for f in files_in_root:
        if f == "index.html" or f.endswith(".map") or f == bundle_file:
            continue
            
        # Replace "/file" with "./file"
        # We need to be careful about matching. Usually filenames in code are quoted.
        # Try double quotes
        content = content.replace(f'"/{f}"', f'"./{f}"')
        # Try single quotes
        content = content.replace(f"'/{f}'", f"'./{f}'")
    
    # 2. Heuristic for common resources if not in root
    # e.g. /draco/
    # If draco dir exists in root
    dirs_in_root = [d for d in os.listdir(room_path) if os.path.isdir(os.path.join(room_path, d))]
    for d in dirs_in_root:
        if d == ".git": continue
        content = content.replace(f'"/{d}/', f'"./{d}/')
        content = content.replace(f"'/{d}/", f"'./{d}/")

    if len(content) != original_len or content != open(bundle_path, 'r', encoding='latin-1').read(): # check if changed
        with open(bundle_path, 'w', encoding='latin-1') as f:
            f.write(content)
        print(f"Patched {bundle_file} in {room_path}")
    else:
        print(f"No changes made to {bundle_file} in {room_path}")

for room in rooms_to_patch:
    patch_bundle(os.path.join(root_dir, room))
