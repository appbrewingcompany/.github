import os
import glob

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

target_workflows = ["auto-merge.yml", "melos-analyze.yml", "melos-version.yml"]

for repo in repos:
    for target in target_workflows:
        filepath = os.path.join(workspace, repo, ".github", "workflows", target)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Replace agent-marketplace with .github
            new_content = content.replace("appbrewingcompany/agent-marketplace/.github/workflows/", "appbrewingcompany/.github/.github/workflows/")
            
            if content != new_content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {repo}/.github/workflows/{target}")
