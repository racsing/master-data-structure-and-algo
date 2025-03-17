import os
import subprocess
from datetime import datetime, timedelta

# Define root folders
FOLDERS = ["LeetCode", "GFG", "PatternPrinting"]  

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
    """Fetch commit streak using Git logs."""
    try:
        logs = subprocess.check_output(["git", "log", "--pretty=format:%ad", "--date=short"]).decode().split("\n")
        dates = [datetime.strptime(date, "%Y-%m-%d").date() for date in logs]

        current_streak = 0
        longest_streak = 0
        today = datetime.today().date()
        streak = 0

        for i in range(len(dates)):
            if dates[i] == today - timedelta(days=streak):
                streak += 1
                current_streak = max(current_streak, streak)
            else:
                longest_streak = max(longest_streak, current_streak)
                streak = 0

        longest_streak = max(longest_streak, current_streak)
        return current_streak, longest_streak

    except subprocess.CalledProcessError:
        return 0, 0

def update_readme():
    """Update README.md with latest problem counts and commit streak."""
    file_counts = count_py_files()
    current_streak, longest_streak = get_commit_streak()
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("README.md", "r") as file:
        content = file.read()

    # Replace placeholders with actual values
    content = content.replace("YY", str(file_counts["LeetCode"]))
    content = content.replace("ZZ", str(file_counts["GFG"]))
    content = content.replace("AA", str(file_counts["PatternPrinting"]))
    content = content.replace("XX", str(file_counts["Total"]))
    content = content.replace("X days", f"{current_streak} days")
    content = content.replace("Y days", f"{longest_streak} days")
    content = content.replace("{{auto-updated-date}}", last_updated)

    with open("README.md", "w") as file:
        file.write(content)

    print("✅ README.md updated successfully!")

if __name__ == "__main__":
    update_readme()
