import bs4
from bs4 import BeautifulSoup

def find_tags_with_url(file_path, url_start):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        tags = soup.find_all(True)  # Find all tags
        matching_tags = set()

        for tag in tags:
            for attr in ['href', 'src', 'srcset', ]:  # Add more attributes if necessary
                if tag.has_attr(attr) and url_start in tag[attr]:
                    matching_tags.add((tag.name, attr, tag[attr]))

        return matching_tags
    except Exception as e:
        return f"Error processing {file_path}: {str(e)}"

# URL to search for
url_start = 'https://www.nicdarkthemes.com/themes/hotel-resort/wp/demo/hotel/wp-includes/js'

# Files to search in
file1 = './about.html'
file2 = './index.html'

# Finding tags
tags_in_file1 = find_tags_with_url(file1, url_start)
tags_in_file2 = find_tags_with_url(file2, url_start)

# Find common tags
common_tags = tags_in_file1.intersection(tags_in_file2)

# Display results
print("Common Tags in Both Files:")
for tag in common_tags:
    print(tag)