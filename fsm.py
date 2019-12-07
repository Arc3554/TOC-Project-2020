from transitions.extensions import GraphMachine
from utils import send_text_message
from utils import send_img_url

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
            if self.a==1:
                if self.b1==1:
                    send_img_url(reply_token,"https://imgur.com/imibKOa.jpg")
                elif self.b1==2:
                    send_img_url(reply_token,"https://imgur.com/JVlRELt.jpg")
                elif self.b1 == 3:
                    send_img_url(reply_token,"https://imgur.com/uMeHvxC.jpg")
                elif self.b1 == 4:
                    send_img_url(reply_token,"https://imgur.com/qraRmAl.jpg") 
                elif self.b1 == 5:
                    send_img_url(reply_token,"https://imgur.com/TnkcGw0.jpg") 
                elif self.b1 == 6:
                    send_img_url(reply_token,"https://imgur.com/7vpgmMg.jpg")                     
                elif self.b1 == 7:
                    send_img_url(reply_token,"https://imgur.com/p6iFMvS.jpg")                         
                elif self.b1 == 8:
                    send_img_url(reply_token,"https://imgur.com/OtC2BuP.jpg")                     
                elif self.b1 == 9:
                    send_img_url(reply_token,"https://imgur.com/jQmsDBF.jpg") 
                elif self.b1 == 10:
                    send_img_url(reply_token,"https://imgur.com/qCpeJIY.jpg")                     
                elif self.b1 == 0:
                    send_img_url(reply_token,"https://imgur.com/5KOsANK.jpg")       
                                        
            elif self.a==2:
                if self.b2==1:
                    send_img_url(reply_token,"https://imgur.com/5JsObtq.jpg")
                elif self.b2==2:
                    send_img_url(reply_token,"https://imgur.com/3MLOpgg.jpg")
                elif self.b2 == 3:
                    send_img_url(reply_token,"https://imgur.com/dtrj2V6.jpg")
                elif self.b2 == 4:
                    send_img_url(reply_token,"https://imgur.com/yRDEUg2.jpg") 
                elif self.b2 == 5:
                    send_img_url(reply_token,"https://imgur.com/aUYhxbS.jpg") 
                elif self.b2 == 6:
                    send_img_url(reply_token,"https://imgur.com/LbOoTEf.jpg")                     
                elif self.b2 == 7:
                    send_img_url(reply_token,"https://imgur.com/qlgpXwm.jpg")                         
                elif self.b2 == 8:
                    send_img_url(reply_token,"https://imgur.com/HXyJSOK.jpg")                     
                elif self.b2 == 9:
                    send_img_url(reply_token,"https://imgur.com/oFAmeLn.jpg") 
                elif self.b2 == 10:
                    send_img_url(reply_token,"https://imgur.com/QN1Qpn1.jpg")                     
                elif self.b2 == 0:
                    send_img_url(reply_token,"https://imgur.com/yBzFges.jpg")       
                    
            elif self.a==3:
                if self.b3==1:
                    send_img_url(reply_token,"https://imgur.com/PVKRgEJ.jpg")
                elif self.b3==2:
                    send_img_url(reply_token,"https://imgur.com/krAYv8p.jpg")
                elif self.b3 == 3:
                    send_img_url(reply_token,"https://imgur.com/iOl4T3j.jpg")
                elif self.b3 == 4:
                    send_img_url(reply_token,"https://imgur.com/pvzFa58.jpg") 
                elif self.b3 == 5:
                    send_img_url(reply_token,"https://imgur.com/bhSabWc.jpg") 
                elif self.b3 == 6:
                    send_img_url(reply_token,"https://imgur.com/p59JTgE.jpg")                     
                elif self.b3 == 7:
                    send_img_url(reply_token,"https://imgur.com/3P71DAg.jpg")                         
                elif self.b3 == 8:
                    send_img_url(reply_token,"https://imgur.com/89CVsYC.jpg")                     
                elif self.b3 == 9:
                    send_img_url(reply_token,"https://imgur.com/mob1EBm.jpg") 
                elif self.b3 == 10:
                    send_img_url(reply_token,"https://imgur.com/G2keoPW.jpg")        
                elif self.b3 == 11:
                    send_img_url(reply_token,"https://imgur.com/C45Kvi5.jpg")    
                elif self.b3 == 0:
                    send_img_url(reply_token,"https://imgur.com/Z7QQ3o9.jpg")        
                    
            elif self.a==4:
                if self.b4==1:
                    send_img_url(reply_token,"https://imgur.com/UIlKNNR.jpg")
                elif self.b4==2:
                    send_img_url(reply_token,"https://imgur.com/z2rjrEr.jpg")
                elif self.b4 == 3:
                    send_img_url(reply_token,"https://imgur.com/ixcj7ia.jpg")
                elif self.b4 == 4:
                    send_img_url(reply_token,"https://imgur.com/snTqoiI.jpg") 
                elif self.b4 == 5:
                    send_img_url(reply_token,"https://imgur.com/1pi44iU.jpg") 
                elif self.b4 == 6:
                    send_img_url(reply_token,"https://imgur.com/h5edeXy.jpg")                     
                elif self.b4 == 7:
                    send_img_url(reply_token,"https://imgur.com/5P1zR4C.jpg")                         
                elif self.b4 == 8:
                    send_img_url(reply_token,"https://imgur.com/UFvjz33.jpg")                     
                elif self.b4 == 9:
                    send_img_url(reply_token,"https://imgur.com/d1G1v0d.jpg") 
                elif self.b4 == 10:
                    send_img_url(reply_token,"https://imgur.com/JrJdKBF.jpg")           
                elif self.b4 == 11:
                    send_img_url(reply_token,"https://imgur.com/ouDPmEH.jpg")         
                elif self.b4 == 0:
                    send_img_url(reply_token,"https://imgur.com/cvSCuc4.jpg")     
                            
            elif self.a==5:
                if self.b5==1:
                    send_img_url(reply_token,"https://imgur.com/TJfqJDs.jpg")
                elif self.b5==2:
                    send_img_url(reply_token,"https://imgur.com/pXEf246.jpg")
                elif self.b5 == 3:
                    send_img_url(reply_token,"https://imgur.com/dPBP3Sv.jpg")
                elif self.b5 == 4:
                    send_img_url(reply_token,"https://imgur.com/HwnnScy.jpg") 
                elif self.b5 == 5:
                    send_img_url(reply_token,"https://imgur.com/mvpobTy.jpg") 
                elif self.b5 == 6:
                    send_img_url(reply_token,"https://imgur.com/XHd2Lkm.jpg")                     
                elif self.b5 == 7:
                    send_img_url(reply_token,"https://imgur.com/mTasJkT.jpg")                         
                elif self.b5 == 8:
                    send_img_url(reply_token,"https://imgur.com/v4b6Kz1.jpg")                         
                elif self.b5 == 0:
                    send_img_url(reply_token,"https://imgur.com/k18KujL.jpg")      
                    
            elif self.a==6:
                if self.b6==1:
                    send_img_url(reply_token,"https://imgur.com/b37okRi.jpg")
                elif self.b6==2:
                    send_img_url(reply_token,"https://imgur.com/JVNi0R4.jpg")
                elif self.b6 == 3:
                    send_img_url(reply_token,"https://imgur.com/7f8uOaQ.jpg")
                elif self.b6 == 4:
                    send_img_url(reply_token,"https://imgur.com/nrpHsFH.jpg") 
                elif self.b6 == 5:
                    send_img_url(reply_token,"https://imgur.com/tVzVKfc.jpg") 
                elif self.b6 == 6:
                    send_img_url(reply_token,"https://imgur.com/RU2VKwN.jpg")                     
                elif self.b6 == 7:
                    send_img_url(reply_token,"https://imgur.com/bbWkqKs.jpg")                         
                elif self.b6 == 8:
                    send_img_url(reply_token,"https://imgur.com/4hvJHq4.jpg")           
                elif self.b6 == 9:
                    send_img_url(reply_token,"https://imgur.com/9wOc2aY.jpg")                      
                elif self.b6 == 0:
                    send_img_url(reply_token,"https://imgur.com/hwkcJIl.jpg")              
                    
            elif self.a==7:
                if self.b7==1:
                    send_img_url(reply_token,"https://imgur.com/mDZboGQ.jpg")
                elif self.b7==2:
                    send_img_url(reply_token,"https://imgur.com/NKqrmIj.jpg")
                elif self.b7 == 3:
                    send_img_url(reply_token,"https://imgur.com/NZSd1Jn.jpg")
                elif self.b7 == 4:
                    send_img_url(reply_token,"https://imgur.com/gJVsX7z.jpg") 
                elif self.b7 == 5:
                    send_img_url(reply_token,"https://imgur.com/AWwNYvz.jpg") 
                elif self.b7 == 6:
                    send_img_url(reply_token,"https://imgur.com/hu1mnkC.jpg")                     
                elif self.b7 == 7:
                    send_img_url(reply_token,"https://imgur.com/wXQDOKk.jpg")                         
                elif self.b7 == 8:
                    send_img_url(reply_token,"https://imgur.com/BhZmf7v.jpg")                       
                elif self.b7 == 0:
                    send_img_url(reply_token,"https://imgur.com/c8CUtWW.jpg")     
                    
            elif self.a==8:
                if self.b8==1:
                    send_img_url(reply_token,"https://imgur.com/lhMPDIv.jpg")
                elif self.b8==2:
                    send_img_url(reply_token,"https://imgur.com/ILFkHP7.jpg")
                elif self.b8 == 3:
                    send_img_url(reply_token,"https://imgur.com/NME3pWd.jpg")
                elif self.b8 == 4:
                    send_img_url(reply_token,"https://imgur.com/KqZHKzb.jpg") 
                elif self.b8 == 5:
                    send_img_url(reply_token,"https://imgur.com/XErzvIV.jpg") 
                elif self.b8 == 6:
                    send_img_url(reply_token,"https://imgur.com/NhqNPbo.jpg")                                            
                elif self.b8 == 0:
                    send_img_url(reply_token,"https://imgur.com/GsKP5om.jpg")
                
        self.a=0
        self.go_back()
        
        