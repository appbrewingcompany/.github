import subprocess

repos = [
    "actions/checkout",
    "actions/github-script",
    "kuhnroyal/flutter-fvm-config-action",
    "subosito/flutter-action",
    "bluefireteam/melos-action",
    "actions/cache",
    "actions/setup-python",
    "peaceiris/actions-gh-pages",
    "pypa/cibuildwheel",
    "actions/upload-artifact",
    "actions/download-artifact",
    "pypa/gh-action-pypi-publish"
]

for repo in repos:
    print(f"Checking {repo}...")
    try:
        output = subprocess.check_output(["gh", "release", "list", "--repo", repo, "--limit", "3"]).decode('utf-8')
        lines = output.strip().split('\n')
        if lines and lines[0]:
            print(lines[0])
        else:
            print("No releases found.")
    except subprocess.CalledProcessError:
        print("Error fetching releases.")
