import os
import subprocess
from datetime import datetime, timedelta
import shutil

# Define root folders
FOLDERS = ["LeetCode", "GFG", "PatternPrinting"]
TEMPLATE_FILE = "README_template.md"
README_FILE = "README.md"

def count_py_files():
    """Recursively count .py files inside each folder and subfolders."""
    file_counts = {folder: 0 for folder in FOLDERS}
    
    for folder in FOLDERS:
        if os.path.exists(folder):
            for root, _, files in os.walk(folder):
                file_counts[folder] += sum(1 for file in files if file.endswith(".py"))
    
    file_counts["Total"] = sum(file_counts.values())  # Total count
    return file_counts

def get_commit_streak():
    """Fetch commit streak using Git logs and calculate correct streaks."""
    try:
        logs = subprocess.check_output(
            ["git", "log", "--pretty=format:%ad", "--date=short"]
        ).decode().split("\n")

        if not logs:
            return 0, 0  # No commits

        # Convert string dates to datetime.date objects
        commit_dates = sorted(set(datetime.strptime(date, "%Y-%m-%d").date() for date in logs), reverse=True)

        today = datetime.today().date()
        current_streak = 0
        longest_streak = 0
        streak = 0

        for i in range(len(commit_dates)):
            if i == 0 and commit_dates[i] == today:
                current_streak = 1  # Start counting from today if there's a commit

            if i > 0 and (commit_dates[i - 1] - commit_dates[i]).days == 1:
                streak += 1
            else:
                streak = 1  # Reset streak when there is a gap

            longest_streak = max(longest_streak, streak)

            if commit_dates[i] == today - timedelta(days=current_streak):
                current_streak += 1

        return current_streak, longest_streak

    except subprocess.CalledProcessError:
        return 0, 0  # Handle errors gracefully
    

def update_readme():
    """Update README.md with latest problem counts and commit streak."""
    if not os.path.exists(TEMPLATE_FILE):
        print("🚨 Template file not found! Ensure README_template.md exists.")
        return

    # Copy template to README.md before modification
    shutil.copy(TEMPLATE_FILE, README_FILE)

    file_counts = count_py_files()
    current_streak, longest_streak = get_commit_streak()
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(README_FILE, "r") as file:
        content = file.read()

    # Replace placeholders with actual values
    content = content.replace("YY", str(file_counts["LeetCode"]))
    content = content.replace("ZZ", str(file_counts["GFG"]))
    content = content.replace("AA", str(file_counts["PatternPrinting"]))
    content = content.replace("XX", str(file_counts["Total"]))
    content = content.replace("X days", f"{current_streak} days")
    content = content.replace("Y days", f"{longest_streak} days")
    content = content.replace("{{auto-updated-date}}", last_updated)

    with open(README_FILE, "w") as file:
        file.write(content)

    print(f"✅ README updated successfully! Last updated on {last_updated}")

if __name__ == "__main__":
    update_readme()
