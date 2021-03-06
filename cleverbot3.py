import pprint
from hashlib import md5
import urllib.request
import urllib.parse
import urllib.request as urlreq
import time

#cleverbot library recoded for use in python 3.3
#recoded by Azuriah McConnell/Riyoken
#original author unknown

class Cleverbot:

    HOST = "www.cleverbot.com"
    PROTOCOL = "http://"
    RESOURCE = "/webservicemin"
    API_URL = PROTOCOL + HOST + RESOURCE
    opener = urlreq.build_opener()
    opener.addheaders = [( 'User-Agent' , 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')]

    def __init__(self):
        self.data = {
            'stimulus' : ''
            , 'start' : 'y'
            , 'sessionid' : ''
            , 'vText8' : ''
            , 'vText7' : ''
            , 'vText6' : ''
            , 'vText5' : ''
            , 'vText4' : ''
            , 'vText3' : ''
            , 'vText2' : ''
            , 'icognoid' : 'wsf'
            , 'icognocheck' : ''
            , 'fno' : 0 
            , 'prevref' : ''
            , 'emotionaloutput' : '' 
            , 'emotionalhistory' : '' 
            , 'asbotname' : '' 
            , 'ttsvoice' : '' 
            , 'typing' : '' 
            , 'lineref' : ''
            , 'sub' : 'Say' 
            , 'islearning' : 1 
            , 'cleanslate' : False 
            }

        self.conversation = []

    def ask(self,q):
        self.data['stimulus'] = q
        resp = self._send()
        self.conversation.append(q)
        parsed = self._parse(resp)
        if self.data['sessionid'] != '':
            self.data['sessionid'] = parsed['conversation_id']
        self.conversation.append(parsed['answer'])
        return parsed['answer']

    def _send(self):
        if self.conversation:
            linecount = 1
            for line in reversed(self.conversation):
                linecount += 1
                self.data['vText'+str(linecount)] = line
                if linecount == 8:
                    break
        enc_data = urllib.parse.urlencode(self.data)
        digest_txt = enc_data[9:35]
        token = md5(digest_txt.encode()).hexdigest()
        self.data['icognocheck'] = token
        enc_data = urllib.parse.urlencode(self.data)
        datas = enc_data.encode()
        conn = self.opener.open(self.API_URL, datas)
        resp = conn.read().decode()
        return resp

    def _parse(self, text):
        parsed = list(map(lambda e: e.split('\r'), text.split('\r\r\r\r\r\r')[:-1]))

        return {
            'answer' : parsed[0][0]
            , 'conversation_id' : parsed[0][1]
            , 'conversation_log_id' : parsed[0][2]
            , 'unknown': parsed[1][-1]
            }

def chat(x):
    """example of use."""
    cb = Cleverbot()
    resp = cb.ask(x)
    return "Bot: " + urllib.parse.unquote(resp)
