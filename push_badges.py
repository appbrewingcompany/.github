import os
import subprocess

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

for repo in repos:
    repo_path = os.path.join(workspace, repo)
    print(f"--- Processing {repo} ---")
    
    # Check if there are changes
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path).decode("utf-8")
    if status.strip():
        subprocess.run(["git", "add", "README.md"], cwd=repo_path)
        subprocess.run(["git", "commit", "-m", "docs: add GitHub actions badges"], cwd=repo_path)
        subprocess.run(["git", "push"], cwd=repo_path)
        print(f"Pushed {repo}")
    else:
        print(f"No changes in {repo}")
