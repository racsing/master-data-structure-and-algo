import subprocess
from datetime import datetime, timedelta

def get_commit_streak():
    """Fetch commit streak using Git logs and calculate current and longest streak correctly."""
    try:
        # Fetch commit dates in descending order
        logs = subprocess.check_output(
            ["git", "log", "--pretty=format:%ad", "--date=short"]
        ).decode().split("\n")

        if not logs:
            return 0, 0  # No commits exist

        # Convert to date objects and remove duplicates
        commit_dates = sorted(set(datetime.strptime(date, "%Y-%m-%d").date() for date in logs), reverse=True)
        print("commit_dates", commit_dates)
        today = datetime.today().date()
        current_streak = 0
        longest_streak = 0
        streak = 1  # Start streak at 1 since the first commit itself counts

        # Check if the latest commit is today
        if commit_dates[0] == today:
            current_streak = 1

        # Iterate over commit dates to find the longest streak
        for i in range(1, len(commit_dates)):
            if (commit_dates[i - 1] - commit_dates[i]).days == 1:
                streak += 1  # Increase streak if consecutive
            else:
                longest_streak = max(longest_streak, streak)
                streak = 1  # Reset streak when a gap appears

            longest_streak = max(longest_streak, streak)

        # Calculate current streak starting from today
        for date in commit_dates:
            if date == today - timedelta(days=current_streak):
                current_streak += 1
            else:
                break  # Stop if a gap is found

        return current_streak, longest_streak

    except subprocess.CalledProcessError:
        return 0, 0  # Return zero if git log fails


print(get_commit_streak())
