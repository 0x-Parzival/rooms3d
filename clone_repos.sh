#!/bin/bash
mkdir -p /home/parzival/3droom
cd /home/parzival/3droom

repos=(
"https://github.com/ricardoolivaalonso/basement"
"https://github.com/ricardoolivaalonso/ThreeJS-Room17"
"https://github.com/ricardoolivaalonso/ThreeJS-Room16"
"https://github.com/ricardoolivaalonso/ThreeJS-Room13"
"https://github.com/ricardoolivaalonso/ThreeJS-Room15"
"https://github.com/ricardoolivaalonso/ThreeJS-Room14"
"https://github.com/ricardoolivaalonso/ThreeJS-Room12"
"https://github.com/ricardoolivaalonso/ThreeJS-Room11"
"https://github.com/ricardoolivaalonso/ThreeJS-Room10"
"https://github.com/ricardoolivaalonso/ThreeJS-Room09"
"https://github.com/ricardoolivaalonso/ThreeJS-Room08"
"https://github.com/ricardoolivaalonso/ThreeJS-Room07"
"https://github.com/ricardoolivaalonso/ThreeJS-Room06"
"https://github.com/ricardoolivaalonso/ThreeJS-Room05"
"https://github.com/ricardoolivaalonso/ThreeJS-Room03"
"https://github.com/ricardoolivaalonso/ThreeJS-Room02"
"https://github.com/ricardoolivaalonso/ThreeJS-Room01"
)

# Note: ThreeJS-Room05 was listed twice in the prompt, so I only included it once.
# Room 04 was missing in the prompt list.

for repo in "${repos[@]}"; do
    echo "Cloning $repo..."
    git clone "$repo"
done

echo "All repositories cloned."
