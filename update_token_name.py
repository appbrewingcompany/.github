import os
import glob

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

for repo in repos:
    search_paths = [
        os.path.join(workspace, repo, ".github", "workflows", "*.yml"),
        os.path.join(workspace, repo, "workflow-templates", "*.yml"),
    ]
    
    for search_path in search_paths:
        for filepath in glob.glob(search_path):
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content.replace("PRIVATE_REPO_TOKEN", "PAT_TOKEN")
            
            if content != new_content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
