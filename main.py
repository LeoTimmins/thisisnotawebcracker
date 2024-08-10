import requests
import time

# File paths
input_file = 'data/dict.txt'
output_file = 'data/success.txt'

# URL to send the POST request to
url = 'https://codes.thisisnotawebsitedotcom.com/'

# Headers to mimic the request
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryR8RLEBQUI6vWHqZi',
    'origin': 'https://thisisnotawebsitedotcom.com',
    'referer': 'https://thisisnotawebsitedotcom.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
    'content-length': '139'
}

# Open the input dictionary file and the output file
with open(input_file, 'r') as dict_file, open(output_file, 'w') as success_file:
    # Read the file line by line
    for line in dict_file:
        while True:
            #time.sleep(0.1)
            code = line.strip()  # Remove any extra whitespace or newlines

            # Construct the multipart form-data payload
            data = f'------WebKitFormBoundaryR8RLEBQUI6vWHqZi\r\nContent-Disposition: form-data; name="code"\r\n\r\n{code}\r\n------WebKitFormBoundaryR8RLEBQUI6vWHqZi--\r\n'

            # Send the POST request
            response = requests.post(url, headers=headers, data=data)
            print(f"{response.status_code} : {code}")
            # Check the response status
            if response.status_code != 404 and response.status_code != 429:
                success_file.write(code + '\n')
                success_file.flush()
            if response.status_code != 429:
                break
            else:
                print("429 Too many requests")
                time.sleep(1)

print("Script finished running.")
