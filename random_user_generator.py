# The project uses the requests library to:

# Fetch random user data from the Random User API.
# Display user details like name, gender, email, and location.

import requests

def fetch_random_user():
    """
    Fetches random user data from the Random User API and returns it as a dictionary.
    """
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()
        user = data["results"][0]  # Get the first user from the results
        return {
            "name": f"{user['name']['title']} {user['name']['first']} {user['name']['last']}",
            "gender": user["gender"],
            "email": user["email"],
            "location": f"{user['location']['city']}, {user['location']['country']}",
        }
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_user_info(user):
    """
    Displays user information in a readable format.
    """
    if user:
        print("Random User Information:")
        print(f"Name     : {user['name']}")
        print(f"Gender   : {user['gender']}")
        print(f"Email    : {user['email']}")
        print(f"Location : {user['location']}")
    else:
        print("No user information available.")

if __name__ == "__main__":
    print("Fetching a random user...")
    user = fetch_random_user()
    display_user_info(user)
