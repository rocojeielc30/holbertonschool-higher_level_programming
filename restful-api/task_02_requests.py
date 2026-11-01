#!/usr/bin/python3
"""Fetches posts from JSONPlaceholder and prints them or saves them to CSV."""
import csv
import requests


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts, print the status code, then print every post title."""
    response = requests.get(POSTS_URL)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save their id, title and body to posts.csv."""
    response = requests.get(POSTS_URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = []
        for post in posts:
            structured_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        fieldnames = ["id", "title", "body"]

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)