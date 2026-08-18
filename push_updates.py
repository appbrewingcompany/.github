import os
import subprocess

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

for repo in repos:
    repo_path = os.path.join(workspace, repo)
    print(f"Committing and pushing {repo}...")
    
    # Check if there are changes
    status_cmd = ["git", "status", "--porcelain"]
    status_output = subprocess.check_output(status_cmd, cwd=repo_path).decode("utf-8")
    
    if status_output.strip():
        subprocess.run(["git", "add", ".github/workflows/auto-merge.yml", ".github/workflows/melos-analyze.yml", ".github/workflows/melos-version.yml"], cwd=repo_path)
        subprocess.run(["git", "commit", "-m", "chore: migrate reusable workflows to .github repo"], cwd=repo_path)
        subprocess.run(["git", "push"], cwd=repo_path)
        print(f"Pushed {repo}")
    else:
        print(f"No changes in {repo}")
