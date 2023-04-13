from flask import Flask, request, jsonify
import json
from datetime import datetime
import subprocess
from app import generate_webpage

def push_to_github():
    # Add the new HTML files to Git
    subprocess.run(["git", "add", "."])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Add generated HTML files"])

    # Push the changes to GitHub
    subprocess.run(["git", "push", "origin", "main"])

name = "Kris Ace"
offer = "Get 2 Weeks Free"
submission_date = datetime.now().date()
generated_file_name = generate_webpage(name, offer, submission_date)

push_to_github()

print("Generated webpage URL:", generated_file_name)
