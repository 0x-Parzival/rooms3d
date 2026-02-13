import os
import re

root_dir = "/home/parzival/3droom"
index_path = os.path.join(root_dir, "index.html")

with open(index_path, 'r') as f:
    content = f.read()

rooms = [f"ThreeJS-Room{i:02d}" for i in range(1, 18)]
rooms.append("basement")

new_content = content

for room in rooms:
    room_path = os.path.join(root_dir, room)
    
    # Determine the correct link
    link = ""
    if os.path.exists(os.path.join(room_path, "out", "index.html")):
        link = f"./{room}/out/index.html"
    elif os.path.exists(os.path.join(room_path, "dist", "index.html")):
        link = f"./{room}/dist/index.html"
    elif os.path.exists(os.path.join(room_path, "build", "index.html")):
        link = f"./{room}/build/index.html"
    elif os.path.exists(os.path.join(room_path, "index.html")):
        link = f"./{room}/index.html"
    else:
        print(f"Warning: Could not find index.html for {room}")
        continue
    
    print(f"Updating link for {room} to {link}")
    
    # Regex to update the href in index.html
    # Looking for href="./ThreeJS-RoomXX..." or similar
    # We want to replace valid hrefs that point to this room.
    # Pattern: href=["']\./ThreeJS-RoomXX[^"']*["']
    
    # But simpler: find the card for this room and update its link.
    # The current index.html construction uses:
    # <div class="card" onclick="window.location.href='./ThreeJS-RoomXX/index.html'">
    # or similar.
    
    # Let's try to replace the specific string based on directory name
    # e.g. replace './ThreeJS-Room01/...' with the new link
    
    # Regex: (['"])\./{room}/?[^'"]*\1
    pattern = re.compile(rf"(['\"])\./{room}(/[^'\"]*)?\1")
    
    # We check if the match already has the correct suffix?
    # Actually, simpler to just replace the whole href if it matches the room.
    
    def replacer(match):
        return f'"{link}"'
        
    new_content = pattern.sub(replacer, new_content)

with open(index_path, 'w') as f:
    f.write(new_content)

print("Updated index.html links.")
