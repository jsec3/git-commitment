import os
import shutil
from datetime import datetime

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.extensions = {
            'images': ['.jpg', '.jpeg', '.png', '.gif'],
            'documents': ['.pdf', '.doc', '.docx', '.txt'],
            'code': ['.py', '.js', '.html', '.css'],
            'archives': ['.zip', '.rar', '.7z']
        }

    def organize_files(self):
        """Organize files in the directory based on their extensions."""
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                self._move_file(filename)

    def _move_file(self, filename):
        """Move file to appropriate directory based on its extension."""
        file_extension = os.path.splitext(filename)[1].lower()
        
        for category, extensions in self.extensions.items():
            if file_extension in extensions:
                category_dir = os.path.join(self.directory, category)
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                shutil.move(
                    os.path.join(self.directory, filename),
                    os.path.join(category_dir, filename)
                )
                break

if __name__ == "__main__":
    # Example usage
    organizer = FileOrganizer(".")
    organizer.organize_files() 
# Consider adding more error handling
# Consider adding more error handling
# Consider adding more error handling
# Consider adding more error handling
# TODO: Optimize this function in the future
# Note: This is a work in progress
# Performance improvement needed here
# Last updated: 2025-05-29 14:51:59
# Last updated: 2025-05-29 19:30:21
# Performance improvement needed here
# Note: This is a work in progress
# Note: This is a work in progress
# Last updated: 2025-06-03 09:33:46
# Last updated: 2025-06-03 19:30:21
# Last updated: 2025-06-04 15:29:34
# Performance improvement needed here
# Performance improvement needed here
# Last updated: 2025-06-09 14:53:34
# Last updated: 2025-06-09 19:31:37
# Last updated: 2025-06-10 14:52:51
# Consider adding more error handling
# Last updated: 2025-06-11 09:34:05
# Performance improvement needed here
# Consider adding more error handling
# Last updated: 2025-06-12 09:33:15
# Consider adding more error handling
# Performance improvement needed here
# TODO: Optimize this function in the future
# Performance improvement needed here
# Performance improvement needed here
# TODO: Optimize this function in the future
# Note: This is a work in progress
# TODO: Optimize this function in the future
# Performance improvement needed here
# Performance improvement needed here
# TODO: Optimize this function in the future
# Consider adding more error handling
# Performance improvement needed here
# Performance improvement needed here
# Note: This is a work in progress
# TODO: Optimize this function in the future
# TODO: Optimize this function in the future
# Note: This is a work in progress
# Performance improvement needed here
# Performance improvement needed here
# TODO: Optimize this function in the future
# Last updated: 2025-07-03 19:30:36
# Note: This is a work in progress
# Note: This is a work in progress
# Performance improvement needed here
# Last updated: 2025-07-08 14:53:51
# Note: This is a work in progress
# TODO: Optimize this function in the future
# Performance improvement needed here
# Performance improvement needed here
# Note: This is a work in progress
# Consider adding more error handling
# Consider adding more error handling
# Last updated: 2025-07-14 14:55:08
# Last updated: 2025-07-14 19:33:24