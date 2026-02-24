import threading 
import requests # Requests library to send HTTP requests
import re # For regex to extract numbers


def download_file(url):
    try:
        print(f"Starting download: {url}")

        response = requests.get(url)
        response.raise_for_status() # Raise error if failed to get url (404 error)

        numbers = re.findall(r'\d+', url)
        if numbers:
            filename = numbers[-1]  # Take the last number
        else:
            filename = "file"

        with open(filename, "wb") as file: # write binary, using binary  mode because PDFs, ZIPs and PNGs are not plain text
            file.write(response.content)

        print(f"Finished download: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

urls = [
    "https://za.pinterest.com/pin/cute-cat-wallpaper--40673202878217745/",
    "https://za.pinterest.com/pin/942589397025580649/"
]

t1 = []

for url in urls:
    thread = threading.Thread(target=download_file, args=(url,)) # Create new thread, pass arguments to function. Without comma, it's not a tuple. Python threading requires args to be a tuple.
    t1.append(thread) # Adds the thread to the list for later control
    thread.start()

for thread in t1:
    thread.join()

print("\nAll downloads completed.")

