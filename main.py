import os
from curl_cffi import Session
from backServise.back import Back
import time

if __name__ == "__main__":
    core = os.path.dirname(os.path.abspath(__file__))
    configPath = os.path.join(core,"files",'config.json')
    congifUpload = Back(configPath,{}).uploadJson()
    
    inputUser = str(input('[1] Change Cookies [2] Start Spam'))
    if inputUser == '1':
        SLS = str(input('SLS: '))
        SI = str(input('SI: '))
        congifUpload['steamCookies']['SLS'] = SLS
        congifUpload['steamCookies']['SI'] = SI

        Back(configPath,congifUpload).saveJson()
    else:
        cookies = {
            "steamLoginSecure" : congifUpload['steamCookies']['SLS'],
            "sessionid": congifUpload['steamCookies']['SI']
        }
        session = Session()
        session.cookies.update(cookies)
        text = congifUpload.get('text')
        data = {
            "comment" : text,
            "count" : '6',
            "sessionid" : congifUpload['steamCookies']['SI'],
            "feature2" : '-1'
        }

        group = congifUpload.get('groupId')
        while True:
            for groupId in group:
                url = f'https://steamcommunity.com/comment/Clan/post/{groupId}/-1/'

                response = session.post(url,data=data)
                
                if (response.status_code == 200) and (response.json().get('success') == True):
                    print(f'{groupId} OK!')

            time.sleep(1800)

            