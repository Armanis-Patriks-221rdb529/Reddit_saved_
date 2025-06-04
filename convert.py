import requests
import os 
from urllib.parse import urlparse




#print('current directory: ', os.getcwd())
folder_path = os.getcwd() + '\saved_images'

try:
    os.mkdir(folder_path)
    print(f"Izveidots folderis norādītajā ceļā: '{folder_path}'")
except FileExistsError:
    print(f"Folderis '{folder_path}' jau izveidots")
except PermissionError:
    print(f"Nevarēja izveidot folderi ceļā: '{folder_path}' nav atļaujas")
except Exception as e:
    print(f"An error occurred: {e}")


'''
with open('processed.txt', 'r') as f:
    processed = [line.strip() for line in f if line.strip()]
'''


def download(url, folder_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or '.' not in filename:
            content_type = response.headers.get('Content-Type', '')
            ext = {
                'image/jpeg': '.jpg',
                'image/png': '.png',
                'image/gif': '.gif',
                'image/bmp': '.bmp',
                'image/webp': '.webp',
            }.get(content_type, '')
            filename = f'image_{ext}'
        
        file_path = os.path.join(folder_path, filename)

        # Save
        with open(file_path, 'wb') as out_file:
            for chunk in response.iter_content(1024):
                out_file.write(chunk)

        print(f"Instalēts: {filename}")

    except Exception as e:
        print(f"Nevarēja instalēt {url}: {e}")
        