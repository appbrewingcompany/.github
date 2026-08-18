import os
import re

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

for repo in repos:
    readme_path = os.path.join(workspace, repo, "README.md")
    
    badges = (
        f"[![Build Status](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-analyze.yml/badge.svg?branch=main)](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-analyze.yml)\n"
        f"[![Release Status](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-version.yml/badge.svg?branch=main)](https://github.com/appbrewingcompany/{repo}/actions/workflows/melos-version.yml)\n"
    )

    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            content = f.read()
        
        # Avoid duplicating badges
        if "melos-analyze.yml/badge.svg" in content:
            print(f"Badges already exist in {repo}/README.md")
            continue

        # Insert after the first h1 if it exists, otherwise at the top
        match = re.search(r'^#\s+.*$', content, re.MULTILINE)
        if match:
            pos = match.end()
            new_content = content[:pos] + "\n\n" + badges + content[pos:]
        else:
            new_content = badges + "\n" + content
        
        with open(readme_path, 'w') as f:
            f.write(new_content)
        print(f"Added badges to existing README in {repo}")
    else:
        # Create new README.md
        new_content = f"# {repo}\n\n{badges}"
        with open(readme_path, 'w') as f:
            f.write(new_content)
        print(f"Created new README in {repo} with badges")
