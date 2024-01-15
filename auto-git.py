import os
from datetime import datetime
import time

def git_auto_commit_push(repo_path, commit_message):

    print(f"\nsystem INFO:\t start git process.\n")

    try:

        os.chdir(repo_path)
        os.system('git add .')
        os.system(f'git commit -m "{commit_message}"')
        os.system('git push origin main')
        print("\nsystem OK:\t git commit and push successful!")

    except Exception as e:

        print(f"system DETAIL:\t {e}")

git_repo_path = "D:\Code\GitHub\Web_commercial_website_for_creator"

current_time = datetime.now()
commit_message = formatted_time = current_time.strftime("%Y/%m/%d %H:%M")

while (True):

    time.sleep(60)
    git_auto_commit_push(git_repo_path, commit_message)