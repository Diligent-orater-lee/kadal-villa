import os
import requests
from bs4 import BeautifulSoup

def download_and_update_html(html_file_path, target_string, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all tags with an 'href', 'src', or 'srcset' attribute that contain the target string
    all_tags = soup.find_all(lambda tag: (tag.has_attr('href') and target_string in tag['href']) or
                                           (tag.has_attr('src') and target_string in tag['src']) or
                                           (tag.has_attr('srcset')))
    
    # Download each URL and update tags
    for tag in all_tags:
        if tag.has_attr('href') and target_string in tag['href']:
            update_attribute(tag, 'href', output_folder)
        if tag.has_attr('src') and target_string in tag['src']:
            update_attribute(tag, 'src', output_folder)
        if tag.has_attr('srcset'):
            update_srcset(tag, output_folder)

    # Save the updated HTML content to a new file
    updated_html_file_path = 'updated_' + os.path.basename(html_file_path)
    with open(updated_html_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    print(f"Updated HTML saved to {updated_html_file_path}")

def update_attribute(tag, attr, output_folder):
    url = tag[attr]
    download_path = download_file(url, output_folder)
    if download_path:
        tag[attr] = download_path

def update_srcset(tag, output_folder):
    parts = tag['srcset'].split(',')
    new_srcset = []
    for part in parts:
        url, descriptor = part.strip().split(' ', 1)
        download_path = download_file(url, output_folder)
        if download_path:
            new_srcset.append(f"{download_path} {descriptor}")
    tag['srcset'] = ', '.join(new_srcset)

def download_file(url, output_folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.basename(url)
            download_path = os.path.join(output_folder, filename)
            with open(download_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {url} to {download_path}")
            return download_path
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")
    return None

# Usage
html_file_path = './index.html'  # Update this path
target_string = 'https://www.nicdarkthemes.com/themes/hotel-resort/wp/demo/hotel/wp-content/uploads/sites/2/2022/11'  # The specific string to look for in hrefs
output_directory = './auto_files/uploads'  # Folder where files will be saved

download_and_update_html(html_file_path, target_string, output_directory)
