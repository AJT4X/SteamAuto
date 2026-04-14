import os
from curl_cffi import Session
import time
from backServise.back import Back
from SteamMain.steamAutoPost import SteamPost



if __name__=='__main__':
    core = os.path.dirname(os.path.abspath(__file__))
    configFile = os.path.join(core,'files','config.json')
    configUpload = Back(configFile,{}).uploadJson()
   

    picuserInput = str(input('[1] Change cookies [2] Start Script'))

    lastCommentSendTime = 0
    lastPushTopicForum = 0

    if picuserInput == "1":
        SLS = str(input('SLS: '))
        SI = str(input("SI: "))
        configUpload['steamCookies']['SLS'] = SLS
        configUpload['steamCookies']['SI'] = SI
        Back(configFile,configUpload).saveJson()
    else:
        cookies = {

            "steamLoginSecure" :configUpload['steamCookies']['SLS'],
            "sessionid" : configUpload['steamCookies']['SI']
        }
        session = Session()
        session.cookies.update(cookies)

        while True:
            current_time = time.time()
            if configUpload['status'].get('GroupCommet') and current_time - lastCommentSendTime > 1800:
                groupCommentSend = SteamPost(configUpload,session).PostGroupComment()
                if groupCommentSend == "Ok":
                    print("Group OK!")
                    lastCommentSendTime=current_time

            if configUpload['status'].get('ForumTopicTrade') and current_time - lastPushTopicForum > 3600:
                forumPush = SteamPost(configUpload,session).ForumTopicPush()
                if forumPush =='Ok':
                    print('forumPush ok!')
                    lastPushTopicForum = current_time

            time.sleep(1800)
