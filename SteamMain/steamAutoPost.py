from curl_cffi import Session

class SteamPost:
    def __init__(self,configUpload,session):
        self.configUpload = configUpload
        self.session = session
    def PostGroupComment(self):
        try:

            text = self.configUpload['CommentBlock'].get('text')
            data = {
                "comment" : text,
                "count" : "6",
                "sessionid" : self.configUpload['steamCookies']['SI'],
                "feature2" : "-1"
            }
            for groupId in self.configUpload['CommentBlock'].get('groupId'):
                url = f'https://steamcommunity.com/comment/Clan/post/{groupId}/-1/'

                response = self.session.post(url,data=data)

                if (response.status_code==200) and (response.json().get('success') == True):
                    print(f'{groupId} OK!')
                else:
                    print(f'Group Id ERROR', response.json())

            return "Ok"


        except Exception as e:
            print('Post Group',e)
            return



    def ForumTopicPush(self):
        try:

            title = self.configUpload['ForumTopicBlock'].get('title')
            text= self.configUpload['ForumTopicBlock'].get('mainText')
            forumIdCom =self.configUpload['ForumTopicBlock'].get('topicId')
            forumId = self.configUpload['ForumTopicBlock'].get('forumId')
            data = {
                "sessionid" : self.configUpload['steamCookies']['SI'],
                'appid': '730',
                'topic': title,
                'text': text,
                'subforum': f'Trading_{forumIdCom}',
            }
            url = f'https://steamcommunity.com/forum/{forumId}/Trading/createtopic/{forumIdCom}/'
            
            response = self.session.post(url,data=data)
            
            if response.status_code == 200:
                print('Full url Topic: ',response.json().get('topic_url'))
                return 'Ok'
            else:
                print(response.json())
                return 'Err'
        except Exception as e:
            print('ForumTopicPush',e)
            return
    