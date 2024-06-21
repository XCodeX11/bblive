import json
from pathlib import Path

# Function to get the current day number from the JSON file
def get_current_day():
    file_path = Path('current_day.json')
    
    # If the file does not exist, start with day01
    if not file_path.exists():
        return 1
    
    # Read the current day from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['day']

# Function to save the next day number to the JSON file
def save_next_day(current_day):
    next_day = current_day + 1 if current_day < 10 else 1
    with open('current_day.json', 'w') as file:
        json.dump({'day': next_day}, file)

# Main function to update the URLs and save them to a JSON file
def update_urls():
    # Get the current day number
    current_day = get_current_day()
    day_str = str(current_day).zfill(2)

    # Define the base URLs
    base_url1 = 'https://prod-ent-live-gm.jiocinema.com/hls/live/2105483/uhd_akamai_atv_avc_24x7_bbhindi_day'
    base_url2 = 'https://prod-ent-live-gm.jiocinema.com/hls/live/2105483/hd_akamai_androidmob_avc_24x7_bbhindi_day'

    # Update the URLs with the current day number
    updated_url1 = f'{base_url1}{day_str}/master.m3u8'
    updated_url2 = f'{base_url2}{day_str}/master.m3u8'

    # Create a dictionary to hold the updated URLs
    urls = {
        '4k': updated_url1,
        'FHD': updated_url2
    }

    # Save the updated URLs to a JSON file
    with open('updated_urls.json', 'w') as json_file:
        json.dump(urls, json_file, indent=4)

    # Save the next day number
    save_next_day(current_day)

    print(f"URLs updated to day{day_str} and saved to 'updated_urls.json'")

if __name__ == "__main__":
    update_urls()
