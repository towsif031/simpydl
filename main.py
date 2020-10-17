import os
import sys
import wget
import time

links = []
last_index = (len(links) - 1)
download_ok = True

# get save path
if not os.path.exists('downloads'):
    os.makedirs('downloads')
save_path = 'downloads'

print("\n *** SimPyDl ***\n")
print("Enter 'exit' in nothing else to download.\n")

download_url = input("file #1: Enter download url: ")

links.append(download_url)

while download_url != 'exit':
    download_url = input(f"file #{len(links) + 1}: Enter download url: ")
    links.append(download_url)

confirm_start = input("\nStart downloads? Enter 'y' to agree: ")


# download function
def get_downloads(file_download_url):
    try:
        start = time.perf_counter()

        def progress_bar(current, total, width = 80):
            downloadPercentage = int(current / total * 100)
            downloadedSize = round((current / 1048576), 2)
            timePassed = time.perf_counter() - start
            downloadSpeed = round((downloadedSize / timePassed), 2)
            totalSize = round((total / 1048576), 2)
            progress_message = f"    Downloading: {downloadPercentage}% [{downloadedSize} / {totalSize}] MB | Speed: {downloadSpeed} MB/s "
            sys.stdout.write("\r" + progress_message)
            sys.stdout.flush()

        wget.download(file_download_url, save_path, bar = progress_bar)
        print(f"\n    file #{links.index(file_download_url) + 1} download complete.")
    
    except:
        global download_ok
        download_ok = False
        print("\nSomething went wrong!\n")


# start downloads function
def start_download(confirm_start):
    if confirm_start == 'y':
        print("\nStarting download process...")
        for link in links:
            if link != 'exit':
                print(f"file #{links.index(link) + 1}:")
                get_downloads(link)
            else:
                global download_ok
                if download_ok:
                    print("\nEverything downloaded successfully!")
    else:
        print("\nOK! Run the program again if something else to download.\n")


# start process
start_download(confirm_start);
