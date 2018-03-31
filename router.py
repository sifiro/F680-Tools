import requests
class API:
    def __init__(self):
        self.SESSION_TOKEN=''
        self.session=requests.session()

    def login(self):
        LoadedPage = self.session.get("http://192.168.1.1")
        Logintoken=LoadedPage.text[LoadedPage.text.find("getObj(\"Frm_Logintoken\").value = \"")+34:]
        Logintoken=Logintoken[0:Logintoken.find("\"")]
        LoginForm={'frashnum':"",
              'action':'login',
              'Frm_Logintoken':Logintoken,
              'Username':"1234",
              'Password':"1234"
              }
        self.session.post("http://192.168.1.1" , data=LoginForm)
        LoadedPage = self.session.get('http://192.168.1.1/template.gch')
        SESSION_TOKEN=LoadedPage.text[LoadedPage.text.find("var session_token = \"")+21:]
        self.SESSION_TOKEN=SESSION_TOKEN[0:SESSION_TOKEN.find("\"")]
        return

    def resetRouter(self):
        ResetBody={
            '_SESSION_TOKEN':self.SESSION_TOKEN,
            'flag':'1',
            'IF_ACTION':'devrestart',
            'IF_ERRORPARAM':'SUCC',
            'IF_ERRORSTR':'SUCC',
            'IF_ERRORTYPE':'-1'
        }
        self.session.post('http://192.168.1.1/getpage.gch?pid=1002&nextpage=manager_dev_conf_t.gch',data=ResetBody)
        return
