import sys
from sec_api import SubsidiaryApi

# Check for required arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <api_key> <ticker>")
    sys.exit(1)

# Get arguments
api_key = sys.argv[1]
ticker = sys.argv[2]

# Initialize the SubsidiaryApi
subsidiary_api = SubsidiaryApi(api_key)

# Define the query
query = {
    "query": f"ticker:{ticker}",
    "from": "0",
    "size": "50",  # Adjust if more results are needed
    "sort": [{"filedAt": {"order": "desc"}}]
}

try:
    # Fetch subsidiary data
    subsidiaries_data = subsidiary_api.get_data(query)

    # Check if data is available
    if not subsidiaries_data or "data" not in subsidiaries_data or not subsidiaries_data["data"]:
        print(f"No subsidiary data found for ticker: {ticker}")
        sys.exit(0)

    # Extract subsidiary names
    subsidiary_names = set()  # Use a set to ensure uniqueness
    for entry in subsidiaries_data["data"]:
        if "subsidiaries" in entry:
            for subsidiary in entry["subsidiaries"]:
                if "name" in subsidiary:
                    subsidiary_names.add(subsidiary["name"])

    # Sort the names and print them
    sorted_names = sorted(subsidiary_names)
    print(f"Subsidiaries for ticker {ticker} (sorted and unique):")
    for name in sorted_names:
        print(name)

except Exception as e:
    print(f"An error occurred: {e}")
