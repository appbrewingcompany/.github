import os
import glob
import re

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

for repo in repos:
    # Get all workflow files
    search_paths = [
        os.path.join(workspace, repo, ".github", "workflows", "*.yml"),
        os.path.join(workspace, repo, "workflow-templates", "*.yml"),
    ]
    
    for search_path in search_paths:
        for filepath in glob.glob(search_path):
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Replace list item
            new_content = re.sub(r'(\s+-\s+)master\b', r'\1main', content)
            
            # Replace inline array [master]
            new_content = re.sub(r'\[master\]', '[main]', new_content)
            
            if content != new_content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
