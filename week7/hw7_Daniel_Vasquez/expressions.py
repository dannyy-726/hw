import re

# 4.1 Parse a string and return a list of all 3-digit numbers
def extract_three_digit_numbers(text: str) -> list:
    match = re.findall(r'\d{3}',text)
    return match

# 4.2 Find and extract the full URL, but only if it starts with http: or https://
def extract_secure_urls(text: str) -> str:
    match = re.findall(r'https?://[^\s]+[^\.,\s]',text)
    return match

# 4.3 Strip all simple HTML tags from string
def strip_html_tags(text: str) -> str:
    match = re.sub(r'</?[a-z]+>','',text)
    return match

# 4.4 Dind dates in the format MM-DD-YYYY and reformat them to YYYY/MM/DD
def reformat_date(text: str) -> str:
    match = re.findall(r'(\d{2})-(\d{2})-(\d{4})',text)

    for month, day, year in match:
        text = re.sub(f"{month}-{day}-{year}",f"{year}/{month}/{day}", text)
    return text    
