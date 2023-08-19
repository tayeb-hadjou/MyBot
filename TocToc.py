import requests
import json
from bs4 import BeautifulSoup

def main():
    params_file= open('params.json')
    params= json.load(params_file)
    url= params['url2']
    assert url is not None
    r= requests.get(url)
    assert r.status_code == 200
    content_type = r.headers.get("content-type")
    if "text/html" in content_type:
        html_content = r.content.decode("utf-8")  # Decode bytes to UTF-8 string
        search_for_wath_you_want(html_content)
        print(html_content)
    elif "application/json" in content_type:
        json_data = r.json()  # Parse JSON content if applicable
        pass
    else:
        print("Unsupported content type:", content_type)
        pass

def search_for_wath_you_want(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())




if __name__=='__main__':
    main()