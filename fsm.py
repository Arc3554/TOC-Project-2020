from transitions.extensions import GraphMachine
from utils import send_text_message
from utils import send_img_url
import sqlite3
import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.a=0
        self.b1=0
        self.b2=0
        self.b3=0
        self.b4=0
        self.b5=0
        self.b6=0
        self.b7=0
        self.b8=0

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "日常"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "戰鬥"
    
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "劇情"
        
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "戀愛"
    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "穿越"
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "科幻"
    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "音樂"    
    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "熱血"    
    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "預覽"    
    
    
    def on_enter_state1(self, event):
        reply_token = event.reply_token
        if self.b1 == 0:
            send_text_message(reply_token, "白箱\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 1:
            send_text_message(reply_token, "紫羅蘭永恆花園\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 2:
            send_text_message(reply_token, "搖曳露營\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 3:
            send_text_message(reply_token, "冰菓\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 4:
            send_text_message(reply_token, "櫻花莊的寵物女孩\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 5:
            send_text_message(reply_token, "青春豬頭少年 系列\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 6:
            send_text_message(reply_token, "SPYxFAMILY\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 7:
            send_text_message(reply_token, "New Game\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 8:
            send_text_message(reply_token, "工作細胞\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 9:
            send_text_message(reply_token, "可塑性記憶\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b1 == 10:
            send_text_message(reply_token, "男子高校生的日常\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b1=(self.b1+1)%11
        self.a=1

    def on_enter_state2(self, event):
        reply_token = event.reply_token
        if self.b2 == 0:
            send_text_message(reply_token, "一拳超人\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 1:
            send_text_message(reply_token, "鬼滅之刃\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 2:
            send_text_message(reply_token, "我的英雄學院\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 3:
            send_text_message(reply_token, "Kill la kill\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 4:
            send_text_message(reply_token, "JoJo系列\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 5:
            send_text_message(reply_token, "CANDY & CIGARETTES\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 6:
            send_text_message(reply_token, "黑色子彈\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 7:
            send_text_message(reply_token, "路人超能100\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 8:
            send_text_message(reply_token, "文豪野犬\n推薦載體: 動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 9:
            send_text_message(reply_token, "便·當\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b2 == 10:
            send_text_message(reply_token, "企業傭兵\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b2=(self.b2+1)%11
        self.a=2
        
    def on_enter_state3(self, event):
        reply_token = event.reply_token
        if self.b3 == 0:
            send_text_message(reply_token, "比宇宙更遠的地方\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 1:
            send_text_message(reply_token, "鋼之煉金術師\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 2:
            send_text_message(reply_token, "命運石之門 系列\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 3:
            send_text_message(reply_token, "彌留之國的愛麗絲\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 4:
            send_text_message(reply_token, "只有我不存在的城市\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 5:
            send_text_message(reply_token, "銀之匙\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 6:
            send_text_message(reply_token, "奇諾之旅\n推薦載體:小說\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 7:
            send_text_message(reply_token, "樂園追放\n推薦載體:電影\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 8:
            send_text_message(reply_token, "地球防衛少年\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 9:
            send_text_message(reply_token, "賭博默示錄\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b3 == 10:
            send_text_message(reply_token, "叛逆的魯魯修\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")            
        elif self.b3 == 11:
            send_text_message(reply_token, "Aldnoah zero\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b3=(self.b3+1)%12
        self.a=3
        
    def on_enter_state4(self, event):
        reply_token = event.reply_token
        if self.b4 == 0:
            send_text_message(reply_token, "輝夜姬想讓人告白\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 1:
            send_text_message(reply_token, "來自風平浪靜的明日\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 2:
            send_text_message(reply_token, "寄宿學校的茱麗葉\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 3:
            send_text_message(reply_token, "愚蠢天使與惡魔共舞\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 4:
            send_text_message(reply_token, "虎與龍\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 5:
            send_text_message(reply_token, "白聖女與黑牧師\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 6:
            send_text_message(reply_token, "來自繽紛世界的明日\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 7:
            send_text_message(reply_token, "多田君不戀愛\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b4 == 8:
            send_text_message(reply_token, "擅長捉弄人的高木同學\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片") 
        elif self.b4 == 9:
            send_text_message(reply_token, "真實之淚 true tears\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片") 
        elif self.b4 == 10:
            send_text_message(reply_token, "五等分的花嫁\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片") 
        elif self.b4 == 11:
            send_text_message(reply_token, "言葉之庭\n推薦載體:電影\n\n輸入'預覽'以獲得預覽圖片") 
        self.go_back()
        self.b4=(self.b4+1)%12
        self.a=4
        
    def on_enter_state5(self, event):
        reply_token = event.reply_token
        if self.b5 == 0:
            send_text_message(reply_token, "遊戲人生\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 1:
            send_text_message(reply_token, "灰與幻想的格林姆迦爾\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 2:
            send_text_message(reply_token, "為美好的世界獻上祝福\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 3:
            send_text_message(reply_token, "無職轉生\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 4:
            send_text_message(reply_token, "Gate奇幻自衛隊\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")            
        elif self.b5 == 5:
            send_text_message(reply_token, "Overlord\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 6:
            send_text_message(reply_token, "關於我轉生變成史萊姆這檔事\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 7:
            send_text_message(reply_token, "萌萌侵略者\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b5 == 8:
            send_text_message(reply_token, "幼女戰記\n推薦載體:小說\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b5=(self.b5+1)%9
        self.a=5
        
    def on_enter_state6(self, event):
        reply_token = event.reply_token
        if self.b6 == 0:    
            send_text_message(reply_token, "寄生獸\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 1:    
            send_text_message(reply_token, "進擊的巨人\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 2:    
            send_text_message(reply_token, "Fate/Zero\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 3:    
            send_text_message(reply_token, "魔法少女小圓\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 4:    
            send_text_message(reply_token, "來自新世界\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 5:    
            send_text_message(reply_token, "心靈判官\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 6:    
            send_text_message(reply_token, "空之境界 系列\n推薦載體:電影\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 7:    
            send_text_message(reply_token, "死亡遊行\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 8:    
            send_text_message(reply_token, "暗殺教室\n推薦載體:漫畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b6 == 9:    
            send_text_message(reply_token, "科學超電磁砲\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b6=(self.b6+1)%10
        self.a=6       
        
    def on_enter_state7(self, event):
        reply_token = event.reply_token
        if self.b7==0:
            send_text_message(reply_token, "吹響吧！上低音號\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==1:
            send_text_message(reply_token, "四月是你的謊言\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==2:
            send_text_message(reply_token, "Tari Tari\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==3:
            send_text_message(reply_token, "佐賀偶像是傳奇\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==4:
            send_text_message(reply_token, "少女☆歌劇Revue Starlight\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==5:
            send_text_message(reply_token, "蟲師\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==6:
            send_text_message(reply_token, "偶像大師(本家)\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b7==7:
            send_text_message(reply_token, "坂道上的阿波羅\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")     
        elif self.b7==8:
            send_text_message(reply_token, "K-on\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b7=(self.b7+1)%9
        self.a=7
        
    def on_enter_state8(self, event):
        reply_token = event.reply_token
        if self.b8 == 0:
            send_text_message(reply_token, "天元突破 紅蓮螺巖\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b8 == 1:
            send_text_message(reply_token, "排球少年\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b8 == 2:
            send_text_message(reply_token, "乒乓\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b8 == 3:
            send_text_message(reply_token, "強風吹拂\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b8 == 4:
            send_text_message(reply_token, "頭文字D\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b8 == 5:
            send_text_message(reply_token, "Megalo Box\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        elif self.b8 == 6:
            send_text_message(reply_token, "花牌情緣\n推薦載體:動畫\n\n輸入'預覽'以獲得預覽圖片")
        self.go_back()
        self.b8=(self.b8+1)%7
        self.a=8
        
    def on_enter_state9(self, event):
        reply_token = event.reply_token
        if self.a == 0:
            send_text_message(reply_token, "請先輸入想要的類型")
        else:
            mydb=sqlite3.connect("test.db")
            cursor=mydb.cursor()
            if self.a==1:
                if self.b1==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 82")
                elif self.b1==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 83")
                elif self.b1 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 84")
                elif self.b1 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 85")
                elif self.b1 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 86")
                elif self.b1 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 87")                  
                elif self.b1 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 88")                        
                elif self.b1 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 89")                   
                elif self.b1 == 9:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 90")
                elif self.b1 == 10:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 91")                    
                elif self.b1 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 92")
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])
                                        
            elif self.a==2:
                if self.b2==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 93")
                elif self.b2==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 94")
                elif self.b2 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 95")
                elif self.b2 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 96")
                elif self.b2 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 97")
                elif self.b2 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 98")              
                elif self.b2 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 99")                
                elif self.b2 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 100")                
                elif self.b2 == 9:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 101")   
                elif self.b2 == 10:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 102")                      
                elif self.b2 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 103")      
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                    
            elif self.a==3:
                if self.b3==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 104")   
                elif self.b3==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 105")   
                elif self.b3 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 106")   
                elif self.b3 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 107")   
                elif self.b3 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 108")   
                elif self.b3 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 109")                     
                elif self.b3 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 110")                 
                elif self.b3 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 111")                     
                elif self.b3 == 9:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 112")   
                elif self.b3 == 10:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 113")   
                elif self.b3 == 11:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 114")   
                elif self.b3 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 115")   
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                       
            elif self.a==4:
                if self.b4==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 116")   
                elif self.b4==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 117")   
                elif self.b4 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 118")   
                elif self.b4 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 119")   
                elif self.b4 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 120")   
                elif self.b4 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 121")         
                elif self.b4 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 122")           
                elif self.b4 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 123")                   
                elif self.b4 == 9:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 124")   
                elif self.b4 == 10:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 125")       
                elif self.b4 == 11:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 126")   
                elif self.b4 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 127")   
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                                  
            elif self.a==5:
                if self.b5==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 128")   
                elif self.b5==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 129")   
                elif self.b5 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 130")   
                elif self.b5 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 131")   
                elif self.b5 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 132")   
                elif self.b5 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 133")             
                elif self.b5 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 134")                          
                elif self.b5 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 135")                          
                elif self.b5 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 136")     
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                          
            elif self.a==6:
                if self.b6==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 137")   
                elif self.b6==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 138")   
                elif self.b6 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 139")   
                elif self.b6 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 140")   
                elif self.b6 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 141")   
                elif self.b6 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 142")                    
                elif self.b6 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 143")                           
                elif self.b6 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 144")   
                elif self.b6 == 9:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 145")                
                elif self.b6 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 146")   
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                          
            elif self.a==7:
                if self.b7==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 147")   
                elif self.b7==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 148")   
                elif self.b7 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 149")   
                elif self.b7 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 150")   
                elif self.b7 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 151")   
                elif self.b7 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 152")         
                elif self.b7 == 7:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 153")              
                elif self.b7 == 8:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 154")                   
                elif self.b7 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 155")    
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                          
            elif self.a==8:
                if self.b8==1:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 156")   
                elif self.b8==2:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 157")   
                elif self.b8 == 3:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 158")   
                elif self.b8 == 4:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 159")   
                elif self.b8 == 5:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 160")   
                elif self.b8 == 6:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 161")                                       
                elif self.b8 == 0:
                    cursor.execute("SELECT username FROM users WHERE role_id = 9 and id = 162")   
                Tables=cursor.fetchall()
                send_img_url(reply_token,random.choice(Tables)[0])                      
        self.a=0
        self.go_back()
        
        