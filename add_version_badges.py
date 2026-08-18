import os
import yaml
import urllib.parse
import re

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

dashboard_content = """# App Brewing Company - CI/CD Health Dashboard

Here is a live view of the GitHub Actions build and release statuses across all your repositories:

| Repository | Build Status (`melos-analyze`) | Release Status (`melos-version`) |
|---|---|---|
"""

for repo in repos:
    repo_path = os.path.join(workspace, repo)
    
    # 1. Dashboard core badges
    dashboard_content += f"| **[{repo}](https://github.com/appbrewingcompany/{repo})** | "
    dashboard_content += f"[![Build Status](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-analyze.yml/badge.svg?branch=main)](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-analyze.yml) | "
    dashboard_content += f"[![Release Status](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-version.yml/badge.svg?branch=main)](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-version.yml) |\n"

dashboard_content += "\n## Package Versions\n\nLive versions for all Dart packages across the organization:\n\n"
dashboard_content += "| Repository | Packages |\n|---|---|\n"

# Process package versions for each repo
for repo in repos:
    repo_path = os.path.join(workspace, repo)
    
    packages = []
    
    for root, dirs, files in os.walk(repo_path):
        if '.git' in root or '.dart_tool' in root or 'build' in root:
            continue
        if 'pubspec.yaml' in files:
            pubspec_path = os.path.join(root, 'pubspec.yaml')
            rel_path = os.path.relpath(pubspec_path, repo_path)
            
            with open(pubspec_path, 'r') as f:
                try:
                    data = yaml.safe_load(f)
                except:
                    continue
            
            if data and isinstance(data, dict) and 'name' in data and 'version' in data:
                pkg_name = data['name']
                raw_url = f"https://raw.githubusercontent.com/appbrewingcompany/{repo}/main/{rel_path}"
                encoded_url = urllib.parse.quote(raw_url, safe='')
                encoded_query = urllib.parse.quote("$.version", safe='')
                encoded_label = urllib.parse.quote(pkg_name, safe='')
                
                badge_md = f"[![{pkg_name}](https://img.shields.io/badge/dynamic/yaml?url={encoded_url}&query={encoded_query}&label={encoded_label}&color=blue)](https://github.com/appbrewingcompany/{repo}/tree/main/{os.path.dirname(rel_path)})"
                packages.append((pkg_name, badge_md))
    
    # Sort packages alphabetically
    packages.sort(key=lambda x: x[0])
    
    if packages:
        # Add to dashboard
        badges_str = " ".join([p[1] for p in packages])
        dashboard_content += f"| **{repo}** | {badges_str} |\n"
        
        # Add to repository README.md
        readme_path = os.path.join(repo_path, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                readme = f.read()
            
            # Find the section to insert package versions
            # We'll insert it right after the Release Status badge
            release_badge_str = f"actions/workflows/melos-version.yml/badge.svg?branch=main)](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-version.yml)"
            
            if "Package Versions" not in readme and release_badge_str in readme:
                # Insert after the release badge line
                parts = readme.split(release_badge_str)
                if len(parts) == 2:
                    new_readme = parts[0] + release_badge_str + "\n\n### Package Versions\n\n" + badges_str + parts[1]
                    with open(readme_path, 'w') as f:
                        f.write(new_readme)
                    print(f"Updated README in {repo}")

# Update Dashboard Artifact
dashboard_path = "/Users/Cyril/.gemini/antigravity/brain/7665e451-20b9-4a66-8aad-99a6f5acad51/repo_health_dashboard.md"
with open(dashboard_path, 'w') as f:
    f.write(dashboard_content)
print("Updated dashboard artifact")
