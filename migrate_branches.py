import os
import subprocess

workspace = "/Users/Cyril/Projects/appbrew_flutter"
repos = ["dot_github", "appbrew_analysis", "appbrew_japanese", "appbrew_utils", "freezed_plus", "hatlas_dart", "loopback", "mecab_flutter", "persistable", "sudachi_flutter"]

for repo in repos:
    repo_path = os.path.join(workspace, repo)
    print(f"--- Processing {repo} ---")
    
    # Check if master exists
    branches = subprocess.check_output(["git", "branch"], cwd=repo_path).decode("utf-8")
    if "* master" in branches or "  master" in branches:
        # Commit the trigger updates
        status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path).decode("utf-8")
        if status.strip():
            subprocess.run(["git", "add", "."], cwd=repo_path)
            subprocess.run(["git", "commit", "-m", "chore: rename master to main in workflows"], cwd=repo_path)
        
        # Rename branch to main locally
        subprocess.run(["git", "branch", "-m", "master", "main"], cwd=repo_path)
        
        # Push main to origin
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)
        
        # Determine github repo name
        if repo == "dot_github":
            gh_repo = "appbrewingcompany/.github"
        else:
            gh_repo = f"appbrewingcompany/{repo}"
        
        # Set default branch using gh CLI
        print(f"Setting default branch for {gh_repo} to main...")
        subprocess.run(["gh", "repo", "edit", gh_repo, "--default-branch", "main"], cwd=repo_path)
        
        # Delete master on origin
        print(f"Deleting remote master for {repo}...")
        subprocess.run(["git", "push", "origin", "--delete", "master"], cwd=repo_path)
        print(f"Successfully migrated {repo}")
    elif "* main" in branches or "  main" in branches:
        print(f"{repo} already on main")
        
        # Make sure updates are committed anyway
        status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path).decode("utf-8")
        if status.strip():
            subprocess.run(["git", "add", "."], cwd=repo_path)
            subprocess.run(["git", "commit", "-m", "chore: rename master to main in workflows"], cwd=repo_path)
            subprocess.run(["git", "push"], cwd=repo_path)
