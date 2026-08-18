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

dashboard_content += "\n## Environment & Package Versions\n\nVersions for all packages across the organization. *(Note: Because these are private repositories, dynamic badges from Shields.io are blocked. These are static snapshots.)*\n\n"
dashboard_content += "| Repository | Environment | Packages |\n|---|---|---|\n"

# Process package versions for each repo
for repo in repos:
    repo_path = os.path.join(workspace, repo)
    
    packages = []
    dart_sdk = "unknown"
    flutter_sdk = "stable"
    
    # Read .fvmrc if it exists
    fvmrc_path = os.path.join(repo_path, ".fvmrc")
    if os.path.exists(fvmrc_path):
        import json
        with open(fvmrc_path, 'r') as f:
            try:
                fvm_data = json.load(f)
                if "flutter" in fvm_data:
                    flutter_sdk = fvm_data["flutter"]
            except:
                pass

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
            
            if data and isinstance(data, dict):
                # Check root pubspec for Dart sdk constraint
                if rel_path == 'pubspec.yaml' and 'environment' in data and 'sdk' in data['environment']:
                    dart_sdk = data['environment']['sdk'].replace(' ', '')
                
                if 'name' in data and 'version' in data:
                    pkg_name = data['name']
                    version = str(data['version']).replace('-', '--') # shields.io requires -- for literal dashes
                    
                    encoded_label = urllib.parse.quote(pkg_name, safe='')
                    encoded_version = urllib.parse.quote(version, safe='')
                    
                    badge_md = f"![{pkg_name}](https://img.shields.io/badge/{encoded_label}-{encoded_version}-blue)"
                    packages.append((pkg_name, badge_md))
    
    # Generate Environment badges
    env_badges = []
    encoded_dart = urllib.parse.quote(dart_sdk, safe='')
    env_badges.append(f"![Dart](https://img.shields.io/badge/Dart-{encoded_dart}-0175C2?logo=dart)")
    
    encoded_flutter = urllib.parse.quote(flutter_sdk, safe='')
    env_badges.append(f"![Flutter](https://img.shields.io/badge/Flutter-{encoded_flutter}-02569B?logo=flutter)")
    
    env_badges_str = " ".join(env_badges)
    
    # Sort packages alphabetically
    packages.sort(key=lambda x: x[0])
    
    if packages:
        # Add to dashboard
        badges_str = " ".join([p[1] for p in packages])
        dashboard_content += f"| **{repo}** | {env_badges_str} | {badges_str} |\n"
        
        # Add to repository README.md
        readme_path = os.path.join(repo_path, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, 'r') as f:
                readme = f.read()
            
            # Find the section to replace package versions
            start_marker = "### Package Versions"
            
            if start_marker in readme:
                # Replace everything after the marker
                parts = readme.split(start_marker)
                new_readme = parts[0] + "### Environment & Package Versions\n\n" + env_badges_str + "\n\n" + badges_str + "\n"
                with open(readme_path, 'w') as f:
                    f.write(new_readme)
                print(f"Updated README in {repo}")

# Update Dashboard Artifact
dashboard_path = "/Users/Cyril/.gemini/antigravity/brain/7665e451-20b9-4a66-8aad-99a6f5acad51/repo_health_dashboard.md"
with open(dashboard_path, 'w') as f:
    f.write(dashboard_content)
print("Updated dashboard artifact")
