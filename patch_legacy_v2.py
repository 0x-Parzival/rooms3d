import os
import re

root_dir = "/home/parzival/3droom"

# Legacy rooms with pre-built bundles
legacy_rooms = ["ThreeJS-Room01", "ThreeJS-Room02", "ThreeJS-Room03", "ThreeJS-Room05"]

def patch_bundle(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    
    # Target common asset extensions in 3D projects
    extensions = ['jpg', 'png', 'glb', 'gltf', 'mp3', 'ico']
    
    for ext in extensions:
        # Replace occurrences of "/filename.ext" with "./filename.ext"
        # We match: quote + / + filename + . + ext + quote
        # But we capture the quote to preserve it.
        
        # Regex: (['"])/([^/]+\.{ext})\1
        # \1 backreferences the quote (single or double)
        # Group 2 is the filename.
        # Replacement: \1./\2\1
        
        pattern = re.compile(rf"(['\"])/([^/\"']+\.{ext})\1")
        content = pattern.sub(r"\1./\2\1", content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {filepath}")
    else:
        print(f"No changes needed for {filepath}")

for room in legacy_rooms:
    room_path = os.path.join(root_dir, room)
    # Bundles might be in root or dist or similar. Room 03 has it in root.
    # Room 01 has script.js? No, it had bundle.js in previous ls.
    # Let's check common names.
    
    for root, dirs, files in os.walk(room_path):
        for file in files:
            if file.endswith(".js"):
                patch_bundle(os.path.join(root, file))
            # Also patch CSS if they reference images with absolute paths
            if file.endswith(".css"):
                patch_bundle(os.path.join(root, file))

print("Legacy bundle patching complete.")
