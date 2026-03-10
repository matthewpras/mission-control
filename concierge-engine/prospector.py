import requests
import json
import os
import time

# Config
APOLLO_API_KEY = os.environ.get("APOLLO_API_KEY", "YOUR_API_KEY_HERE")
TARGET_LOCATION = "Philadelphia"
TARGET_ROLES = ["Founder", "CEO", "Owner", "Marketing Director"]
TARGET_INDUSTRIES = ["Software", "Marketing and Advertising", "Internet"]

def search_apollo(roles, industries, location):
    """
    Search for prospects using Apollo.io API.
    Docs: https://apolloio.github.io/apollo-api-docs/
    """
    if APOLLO_API_KEY == "YOUR_API_KEY_HERE":
        print("SIMULATION MODE: No Apollo API key found. Generating sample data.")
        return generate_sample_data()

    url = "https://api.apollo.io/v1/mixed_people/search"
    
    payload = {
        "api_key": APOLLO_API_KEY,
        "person_titles": roles,
        "q_organization_keyword_tags": industries,
        "person_locations": [location],
        "page": 1,
        "display_mode": "regular"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "X-Api-Key": APOLLO_API_KEY
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return generate_sample_data()
    except Exception as e:
        print(f"Exception: {str(e)}")
        return generate_sample_data()

def generate_sample_data():
    """Generates sample B2B leads for Philadelphia for UI testing."""
    return {
        "people": [
            {
                "name": "Sarah Jenkins",
                "title": "Founder @ PhillySaaS",
                "email": "sarah@phillysaas.io",
                "linkedin_url": "https://linkedin.com/in/sjenkins",
                "organization": {"name": "PhillySaaS", "website_url": "https://phillysaas.io"}
            },
            {
                "name": "Marcus Thorne",
                "title": "CEO @ BlueRocket Marketing",
                "email": "m.thorne@bluerocket.agency",
                "linkedin_url": "https://linkedin.com/in/mthorne",
                "organization": {"name": "BlueRocket Marketing", "website_url": "https://bluerocket.agency"}
            },
            {
                "name": "Elena Rossi",
                "title": "Owner @ Luxe-Home Shopify",
                "email": "elena@luxehomes.com",
                "linkedin_url": "https://linkedin.com/in/erossi",
                "organization": {"name": "Luxe-Home", "website_url": "https://luxehomes.com"}
            }
        ]
    }

def save_leads(data):
    with open("concierge-engine/leads.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"OK - Saved {len(data.get('people', []))} leads to concierge-engine/leads.json")

if __name__ == "__main__":
    print(f"Starting Prospecting for {TARGET_LOCATION}...")
    prospects = search_apollo(TARGET_ROLES, TARGET_INDUSTRIES, TARGET_LOCATION)
    save_leads(prospects)
