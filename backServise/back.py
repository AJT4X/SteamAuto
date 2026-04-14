import json

class Back:
    def __init__(self,file=None,info=None):
        self.file = file
        self.info = info



    def uploadJson(self):
        with open(self.file,'r',encoding='utf-8') as f:
            data = json.load(f)
            return data
        


    def saveJson(self):
        with open(self.file,"w",encoding='utf-8') as f:
            json.dump(self.info,f,indent=4,ensure_ascii=False)
        return