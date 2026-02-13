import os
import json

root_dir = "/home/parzival/3droom"
repos = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

results = []

for repo in repos:
    repo_path = os.path.join(root_dir, repo)
    package_json_path = os.path.join(repo_path, "package.json")
    
    if os.path.exists(package_json_path):
        try:
            with open(package_json_path, 'r') as f:
                data = json.load(f)
                scripts = data.get("scripts", {})
                dev_deps = data.get("devDependencies", {})
                deps = data.get("dependencies", {})
                
                tool = "Unknown"
                if "vite" in dev_deps or "vite" in deps:
                    tool = "Vite"
                elif "webpack" in dev_deps or "webpack" in deps:
                    tool = "Webpack"
                elif "parcel" in dev_deps or "parcel" in deps:
                    tool = "Parcel"
                elif "next" in deps:
                    tool = "Next.js"
                
                results.append({
                    "repo": repo,
                    "tool": tool,
                    "build_script": scripts.get("build", "")
                })
        except Exception as e:
            results.append({
                "repo": repo,
                "error": str(e)
            })
    else:
        results.append({
            "repo": repo,
            "tool": "No package.json"
        })

for r in sorted(results, key=lambda x: x['repo']):
    print(f"{r['repo']}: {r.get('tool', 'Error')} - Build: {r.get('build_script', 'N/A')}")
