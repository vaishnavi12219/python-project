import instaloader
import json

# Initialize Instaloader
L = instaloader.Instaloader()

def get_profile_data(username):
    try:
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Collect profile information
        profile_data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "external_url": profile.external_url,
            "followers": profile.followers,
            "following": profile.followees,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified,
        }
        
        print("Profile data extracted successfully!")
        
        return profile_data

    except Exception as e:
        print("Error while fetching profile data:", e)
        return None

def get_posts(username, max_posts=5):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts_data = []

        # Fetch posts, limited to max_posts
        for post in profile.get_posts():
            if len(posts_data) >= max_posts:
                break
            post_info = {
                "caption": post.caption,
                "likes": post.likes,
                "comments": post.comments,
                "date": post.date.strftime("%Y-%m-%d"),
                "url": post.url,
            }
            posts_data.append(post_info)

        print(f"Extracted {len(posts_data)} posts from {username}")
        
        return posts_data

    except Exception as e:
        print("Error while fetching posts:", e)
        return []

def save_data(username, profile_data, posts_data):
    data = {
        "profile": profile_data,
        "posts": posts_data
    }
    
    # Save to JSON file
    with open(f"{username}_data.json", "w") as file:
        json.dump(data, file, indent=4)
        
    print(f"Data saved to {username}_data.json")

# Main function to run the extraction process
def main():
    username = input("Enter the Instagram username to scrape: ")
    
    # Get profile data
    profile_data = get_profile_data(username)
    
    # Get post data
    posts_data = get_posts(username, max_posts=5)
    
    # Save data
    save_data(username, profile_data, posts_data)

if __name__ == "__main__":
    main()
