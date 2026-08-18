import os
import glob
import re

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

replacements = {
    r"actions/checkout@v[0-9]+": "actions/checkout@v7",
    r"actions/github-script@v[0-9]+": "actions/github-script@v9",
    r"actions/cache@v[0-9]+": "actions/cache@v5",
    r"actions/setup-python@v[0-9]+": "actions/setup-python@v7",
    r"pypa/cibuildwheel@v[0-9.]*": "pypa/cibuildwheel@v4.2.0",
    r"actions/upload-artifact@v[0-9]+": "actions/upload-artifact@v7",
    r"actions/download-artifact@v[0-9]+": "actions/download-artifact@v8",
}

for repo in repos:
    search_paths = []
    
    # Python/Rust actions are typically deeply nested in sudachi_flutter
    # So let's glob recursively for .github/workflows/*.yml
    repo_dir = os.path.join(workspace, repo)
    for root, dirs, files in os.walk(repo_dir):
        if '.github/workflows' in root or 'workflow-templates' in root:
            for file in files:
                if file.endswith('.yml') or file.endswith('.yaml'):
                    search_paths.append(os.path.join(root, file))

    for filepath in search_paths:
        with open(filepath, 'r') as f:
            content = f.read()
        
        new_content = content
        for pattern, replacement in replacements.items():
            new_content = re.sub(pattern, replacement, new_content)
        
        if content != new_content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
