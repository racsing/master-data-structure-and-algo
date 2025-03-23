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
        # Fetch commit dates in descending order
        logs = subprocess.check_output(
            ["git", "log", "--pretty=format:%ad", "--date=short"]
        ).decode().split("\n")

        if not logs:
            return 0, 0  # No commits exist

        # Convert to date objects and remove duplicates
        commit_dates = sorted(set(datetime.strptime(date, "%Y-%m-%d").date() for date in logs), reverse=True)

        today = datetime.today().date()
        current_streak = 0
        longest_streak = 0
        streak = 1  # Start with 1 since the first commit counts

        # Check if latest commit is today
        if commit_dates[0] == today:
            current_streak = 1

        # Iterate over commit dates to calculate streaks
        for i in range(1, len(commit_dates)):
            if (commit_dates[i - 1] - commit_dates[i]).days == 1:
                streak += 1  # Increase streak if consecutive
            else:
                longest_streak = max(longest_streak, streak)
                streak = 1  # Reset streak if gap exists

            longest_streak = max(longest_streak, streak)

        # Calculate current streak based on today
        for date in commit_dates:
            if date == today - timedelta(days=current_streak):
                current_streak += 1
            else:
                break  # Stop if a gap is found

        return current_streak, longest_streak

    except subprocess.CalledProcessError:
        return 0, 0  # Return zero if git log fails
    

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
