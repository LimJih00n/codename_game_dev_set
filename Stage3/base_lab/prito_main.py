from js import document, window, Image, console
import js
import world
import img_dic_set as ids
from pyodide import create_proxy
import datetime as dt
import asyncio
import pywebcanvas as pwc
import random


lastTime = 6
canvas = document.getElementById('Canvas')
canvas.width = 500
canvas.height = 500
ctx = canvas.getContext('2d')
console.log("Hey there, from 'console.log' inside PyScript!")

################################JS context########################################
class SpeechBubble: # 말풍선그리기!
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.width = len(text)*9  # 말풍선 너비 조절
        self.height = 25  # 말풍선 높이 조절
    
    def draw(self):
        # 말풍선 본체의 시작 지점 조정
        bubbleStartX = self.x - self.width / 2

        # 말풍선 본체 그리기
        ctx.fillStyle = 'white'  # 말풍선 배경색
        ctx.beginPath()
        ctx.moveTo(bubbleStartX + 10, self.y)
        ctx.lineTo(bubbleStartX + self.width - 10, self.y)
        ctx.quadraticCurveTo(bubbleStartX + self.width, self.y, bubbleStartX + self.width, self.y + 10)
        ctx.lineTo(bubbleStartX + self.width, self.y + self.height - 10)
        ctx.quadraticCurveTo(bubbleStartX + self.width, self.y + self.height, bubbleStartX + self.width - 10, self.y + self.height)
        ctx.lineTo(bubbleStartX + 10, self.y + self.height)
        ctx.quadraticCurveTo(bubbleStartX, self.y + self.height, bubbleStartX, self.y + self.height - 10)
        ctx.lineTo(bubbleStartX, self.y + 10)
        ctx.quadraticCurveTo(bubbleStartX, self.y, bubbleStartX + 10, self.y)
        ctx.closePath()
        ctx.fill()

        # 살짝 뾰족한 부분 그리기 - 캐릭터의 바로 아래에 위치하도록 조정
        ctx.beginPath()
        ctx.moveTo(self.x - 5, self.y + self.height)
        ctx.lineTo(self.x + 5, self.y + self.height)
        ctx.lineTo(self.x, self.y + self.height + 10)
        ctx.fillStyle = 'white'
        ctx.fill()

        # 텍스트 쓰기
        ctx.fillStyle = 'black'  # 텍스트 색상
        ctx.fillText(self.text, bubbleStartX + 5, self.y + 15)  # 텍스트 출력 위치


# 'say' 함수 구현
def say(text):
    global warrior, ctx
    speech_bubble = SpeechBubble(text, warrior.get_x()+30, warrior.get_y() - 30)  # 말풍선 객체 생성
    speech_bubble.draw()  # 말풍선 그리기
    
class DrawImage: 
    def __init__(self,obj) -> None:
        self.image = Image.new()  # 이 부분은 실제 이미지 로딩 로직에 맞게 수정 필요
        self.image.src = "!"
        self.state = "default"
        self.frame_idx = 0
        self.frame_length = 0
        self.update_image_properties(obj)
    
    
    def update_image_properties(self, obj):
        """이미지 속성 업데이트"""
        img_info = obj.get_img_dic()[obj.get_state()]
        self.frame_length = img_info["frame"]
        self.draw_width = img_info.get("draw_width", obj.get_width())  # 그리기 너비
        self.draw_height = img_info.get("draw_height", obj.get_height())  # 그리기 높이
        
    def draw(self, obj):
        """이미지 그리기"""
        self.update_image_properties(obj)
        frame_width_move = obj.get_img_dic()[obj.get_state()]["f-width-full"] // self.frame_length
        frame_width = obj.get_img_dic()[obj.get_state()]["f-width"]
        frame_height = obj.get_img_dic()[obj.get_state()]["f-height"]
        
        if self.image.src != "!" or self.state != obj.get_state():
            self.image.src = obj.get_img_dic()[obj.get_state()]["img-url"]
        self.state = obj.get_state()
                
        if self.frame_length == 1:
            ctx.drawImage(self.image, obj.get_x(), obj.get_y(), self.draw_width, self.draw_height)
        else:
            ctx.drawImage(
                self.image, 
                self.frame_idx * frame_width_move, 0,  # 스프라이트 시트에서의 x, y 위치
                frame_width, frame_height,  # 추출할 프레임의 너비와 높이
                obj.get_x(), obj.get_y(),  # 캔버스 상의 x, y 위치
                self.draw_width, self.draw_height  # 캔버스 상의 프레임의 너비와 높이
            )
            self.frame_idx = (self.frame_idx + 1) % self.frame_length

    
def check_out(obj):
    if obj.get_x() < -10:
        return True
    if obj.get_x() + obj.get_width() > canvas.width+10:
        return True
    if obj.get_y() < -10:
        return True
    if obj.get_y() + obj.get_height() > canvas.height+10 :
        return True
    return False

# 게임 완료 상태를 서버에 알리기
def notify_server_game_completed():
    window.sendCompletionMessage()

################################JS context########################################

################################# user #########################
def UserInitCode():
    state = 0
#$user_init_start
    # Enter your code here
#$user_init_out
def UserLoopCode():
    state=0
#$user_loop_start
    
#$user_loop_out
################################# user #########################

################################othet function################
def game_com_codition():
    global Item_count


def update_draw(obj_world,obj_js):
    obj_js.draw(obj_world)
    obj_world.update_state()
    obj_world.update_position()


def tree_checker(wall):
    global warrior
    global World_Items
    global World_objects_draw
    global World_Walls
    
    if wall.get_type() == "tree":
                
        if "attack" in warrior.get_state():
            if warrior.get_gold()<=0: 
                say("나무를 베려면 돈이 있어야해...")
            else:
                
                if not warrior.is_attack_hit(wall):
                    say("주변에 나무가 없어..")
                else:
                    say("나무를 베고있어!")
                    
                if wall.get_hp() <= 0:
                    #spawn wood
                    warrior.gold_change(-1)
                    spawn_w = world.Item(wall.get_x()+20,wall.get_y()+50,ids.wood_img_dic,"wood",0)
                    spawn_w_draw = DrawImage(spawn_w)
                    World_Items.append(spawn_w)
                    World_objects_draw.append((spawn_w,spawn_w_draw))
                    
                    #delete tree
                    World_Walls.remove(wall)
                    World_objects_draw = [pair for pair in World_objects_draw if pair[0].get_id() != wall.get_id()]


def Build(X,Y):
    global warrior
    global World_objects_draw
    global World_Walls
    
    if warrior.get_wood() > 0:
        console.log("Hey there, building!!")
        warrior.wood_change(-1)
        building = world.Wall(X,Y,ids.House_img_dic,"wall",100)
        building_draw = DrawImage(building)
        World_Walls.append(building)
        World_objects_draw.append((building,building_draw))
    else:
        say("나무가 부족해!!")
################################



###################  map make #####################
# append한 순서대로 그려집니다. 배경을 제일 먼저 append하기 append로 그릴시!!
# (obj,obj_draw)

World_Walls  = []
World_Items  = []
World_objects_draw = []

warrior = world.Hero(0,0,ids.knight_img_dic,"hero",100)

warrior.Build = Build

gold1 = world.Item(400,100,ids.gold_img_dic,"gold",0)
gold2 = world.Item(200,200,ids.gold_img_dic,"gold",0)
gold3 = world.Item(400,400,ids.gold_img_dic,"gold",0)

wood = world.Item(300,300,ids.wood_img_dic,"wood",0)

sheep = world.Wall(0,225,ids.sheep_img_dic,"sheep",1000)
goblin = world.Wall(350,350,ids.goblin_img_dic,"goblin",1000)

tree1 = world.Wall(75,330,ids.tree_img_dic,"tree",1000)
tree2 = world.Wall(175,330,ids.tree_img_dic,"tree",1000)
tree3 = world.Wall(375,230,ids.tree_img_dic,"tree",1000)

castle = world.Wall(100,100,ids.Castle_img_dic,"wall",1000000)
house = world.Wall(250,70,ids.House_img_dic,"wall",100000)
tower = world.Wall(300,250,ids.Tower_img_dic,"wall",100000)



warrior_draw = DrawImage(warrior)
goblin_draw = DrawImage(goblin)
castle_draw = DrawImage(castle)
house_draw = DrawImage(house)
tower_draw = DrawImage(tower)
gold1_draw = DrawImage(gold1)
gold2_draw = DrawImage(gold2)
gold3_draw = DrawImage(gold3)

wood_draw = DrawImage(wood)

tree1_draw = DrawImage(tree1)
tree2_draw = DrawImage(tree2)
tree3_draw = DrawImage(tree3)
sheep_draw = DrawImage(sheep)

background = world.Background(0,0,ids.background_img_dic,"background",1000000)
background_draw = DrawImage(background)


World_Walls = [sheep,tree1,tree2,tree3,castle,house,tower,goblin]
World_Items = [gold1,gold2,gold3,wood]
World_objects_draw=[
                    (background,background_draw),
                    (warrior,warrior_draw),
                    (sheep,sheep_draw),
                    (goblin,goblin_draw),
                    (tree1,tree1_draw),
                    (tree2,tree2_draw),
                    (tree3,tree3_draw),
                    (castle,castle_draw),
                    (house,house_draw),
                    (tower,tower_draw),
                    (gold1,gold1_draw),
                    (gold2,gold2_draw),
                    (gold3,gold3_draw),
                    (wood,wood_draw),
                    ]
###################  map make #####################


################## init val and func ################
Item_count = 0
ratValue = 0
func_check = True


sheep.set_velocity(4,0)
sheep.set_state("right")
sheep.set_direction("R")
sheep.move_left_right(500)

goblin.set_velocity(4,4)
goblin.set_direction("R")
goblin.move_rectangle(340,340,440,440)
################## init val and func ################


###################  loop func #######################
def frame_loop(*args):
    
    ## global var in loop
    global goblin
    global sheep
    global warrior
    
    global lastTime
    global ratValue
    
    global Item_count
    global World_Items
    global World_objects_draw
    global World_Walls
    #################
    
    
    
    if lastTime%5 ==0: # 12frame / 1sec
        
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        
        
        
        sheep.move_left_right(500)
        goblin.move_rectangle(340,340,440,440)
        
        
        
        for obj,draw in World_objects_draw:
            update_draw(obj,draw)
        
        if game_com_codition():
            warrior.stop()
            say("!!미션성공!!")
            notify_server_game_completed()
            
            
        
    
        for wall in World_Walls:
            tree_checker(wall)
            if warrior.check_collision(wall):                                                                                                                    
                warrior.set_velocity(0,0)
                
        
        for item in World_Items:
            if warrior.check_collision(item):
                if item.get_type() == "gold":
                    warrior.gold_change(1)
                if item.get_type() =="wood":
                    warrior.wood_change(1)
                
                Item_count += 1
                World_Items.remove(item)
                World_objects_draw = [pair for pair in World_objects_draw if pair[0].get_id() != item.get_id()]
                
                
                
      
        
        window.sendXY(warrior.get_x(),warrior.get_y(),warrior.get_gold(),warrior.get_wood())
                
        if check_out(warrior):
            warrior.set_velocity(0,0)
            
        UserLoopCode()
        
    lastTime = lastTime+1 if lastTime <= float('inf') else 0    
    ratValue = window.requestAnimationFrame(create_proxy(frame_loop))
###################  loop func #######################

###################  key action func #######################
def controls(e):
    global warrior
    warrior.set_velocity(10,10)
    if e.code == 'KeyW':
        warrior.set_direction("U")
    elif e.code =='KeyS':
        warrior.set_direction("D")
    elif e.code == 'KeyA':
        warrior.set_direction("L")
        warrior.set_state("left")
    elif e.code == 'KeyD':
        warrior.set_direction("R")
        warrior.set_state("right")
    elif e.code == 'KeyX':
        warrior.attack(5)
###################  key action func #######################




###################  async loop func #######################
async def delay(): ## 반복문 넣은 거 비동기적 대기 가능!
    global warrior
    global func_check
    a = 0
    if not func_check:
        return
    if func_check:
        for i in range(10):
            warrior.attack(1)
            
            await asyncio.sleep(1) # 서버에서 넣어줘야함!
            
        while a <10:
            console.log(a)
            
            a +=1
              # 1초 동안 비동기적으로 대기
            # 근데 async를 while loop안에다 넣어줘야함
        func_check = False
###################  async loop func #######################



################### run function ############################

document.addEventListener('keydown',create_proxy(controls))
frame_loop()
loop = pwc.Loop()
loop.add_task("delay", delay)
loop.run()

UserInitCode()

################### run function ############################
