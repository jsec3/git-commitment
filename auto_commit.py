import os
import random
import subprocess
from datetime import datetime, timedelta

# List of commit messages that look natural
COMMIT_MESSAGES = [
    "refactor: improve code organization",
    "docs: update README with new features",
    "fix: resolve file organization edge case",
    "feat: add new utility function",
    "style: improve code formatting",
    "test: add test cases for file organizer",
    "chore: update dependencies",
    "perf: optimize file processing",
    "ci: update GitHub Actions workflow",
    "build: update build configuration"
]

def make_random_change():
    """Make a random change to one of the utility files."""
    files = [
        "utils/file_organizer.py",
        "utils/code_quality.py"
    ]
    
    file_to_modify = random.choice(files)
    
    if not os.path.exists(file_to_modify):
        return False
        
    with open(file_to_modify, 'r') as file:
        content = file.read()
    
    # Make a random change (add a comment or modify a string)
    changes = [
        f"\n# Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\n# TODO: Optimize this function in the future",
        f"\n# Note: This is a work in progress",
        f"\n# Performance improvement needed here",
        f"\n# Consider adding more error handling"
    ]
    
    with open(file_to_modify, 'a') as file:
        file.write(random.choice(changes))
    
    return True

def make_commit():
    """Make a commit with a random message."""
    if not make_random_change():
        return False
        
    # Add all changes
    subprocess.run(['git', 'add', '.'])
    
    # Create commit with random message
    commit_message = random.choice(COMMIT_MESSAGES)
    subprocess.run(['git', 'commit', '-m', commit_message])
    
    return True

def main():
    """Main function to make commits."""
    # Configure git if not already configured
    if not os.path.exists('.git/config'):
        subprocess.run(['git', 'config', '--global', 'user.email', 'your-email@example.com'])
        subprocess.run(['git', 'config', '--global', 'user.name', 'Your Name'])
    
    # Make a commit
    if make_commit():
        print("Successfully made a commit!")
    else:
        print("Failed to make a commit.")

if __name__ == "__main__":
    main() 