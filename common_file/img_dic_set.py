
# warrior: 1152-6: 192-100
#tree 768-4 -180
#sheep 768-6 - 60
#gold 896-7 - 80
#goblin 1152-6-100

#hit-img가 0,0에서 그렸다고 생각하고 box를 그림!

knight_img_dic ={
    "default":
        {
            "frame":6,
            "f-width-full":1152,
            "f-width": 100,
            "f-height":100,
            "draw_width": 50,  # 실제 그릴 너비
            "draw_height": 50,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/right/w-right.png',
            
        },
    "left":{
            "frame":6,
            "f-width-full":1152,
            "f-width": 100,
            "f-height":100,
            "draw_width": 50,  # 실제 그릴 너비
            "draw_height": 50,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/left/w-left.png',
            
        },
    "right":{
            "frame":6,
            "f-width-full":1152,
            "f-width": 100,
            "f-height":100,
            "draw_width": 50,  # 실제 그릴 너비
            "draw_height": 50,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/right/w-right.png',
            
            
        },
    "attack-left":{
        "frame":6,
            "f-width-full":1152,
            "f-width": 150,
            "f-height":130,
            "draw_width": 75,  # 실제 그릴 너비
            "draw_height": 65,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/attack-left/w-a-left.png',
    },
    "attack-right":{
        "frame":6,
            "f-width-full":1152,
            "f-width": 190,
            "f-height":130,
            "draw_width": 75,  # 실제 그릴 너비
            "draw_height": 65,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/attack-right/w-a-right.png',
            
    },
    "attack-down":{
        "frame":6,
            "f-width-full":1152,
            "f-width": 150,
            "f-height":130,
            "draw_width": 60,  # 실제 그릴 너비
            "draw_height": 70,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/attack-down/w-a-down.png',
            
    },
    "attack-up":{
        "frame":6,
            "f-width-full":1152,
            "f-width": 150,
            "f-height":130,
            "draw_width": 60,  # 실제 그릴 너비
            "draw_height": 70,  # 실제 그릴 높이
            "hit_x":10,
            "hit_y":10,
            "hit_w":30,
            "hit_h":30,
            "img-url": '../../assets/knight/attack-up/w-a-up.png',
            
    },
    
}
sheep_img_dic = {
    "default":{
            "frame":6,
            "f-width-full":768,
            "f-width":100,
            "f-height":60,
            "draw_width": 100,  # 실제 그릴 너비
            "draw_height": 60,  # 실제 그릴 높이
            "hit_x":20,
            "hit_y":0,
            "hit_w":80,
            "hit_h":60,
            "img-url": '../../assets/objects/sheep/right/sheep-right.png',
        },
    "right":{
            "frame":6,
            "f-width-full":768,
            "f-width":100,
            "f-height":60,
            "draw_width": 100,  # 실제 그릴 너비
            "draw_height": 60,  # 실제 그릴 높이
            "hit_x":20,
            "hit_y":0,
            "hit_w":80,
            "hit_h":60,
            "img-url": '../../assets/objects/sheep/right/sheep-right.png',
        },
    "left":{
            "frame":6,
            "f-width-full":768,
            "f-width":100,
            "f-height":60,
            "draw_width": 100,  # 실제 그릴 너비
            "draw_height": 60,  # 실제 그릴 높이
            "hit_x":20,
            "hit_y":0,
            "hit_w":80,
            "hit_h":60,
            "img-url": '../../assets/objects/sheep/left/sheep-left.png',
        },
}

tree_img_dic = {
    "default":{
            "frame":4,
            "f-width-full":768,
            "f-width": 192,
            "f-height": 180,
            "draw_width": 100,  # 실제 그릴 너비
            "draw_height": 110,  # 실제 그릴 높이
            "hit_x":30,
            "hit_y":60,
            "hit_w":45,
            "hit_h":50,
            "img-url": '../../assets/objects/tree/Tree.png',
    }
}
goblin_img_dic = {
     "default":
        {
            "frame":6,
            "f-width-full":1152,
            "f-width": 192,
            "f-height":100,
            "draw_width": 60,  # 실제 그릴 너비
            "draw_height": 60,  # 실제 그릴 높이
            "hit_x":0,
            "hit_y":0,
            "hit_w":60,
            "hit_h":60,
            "img-url": '../../assets/goblin/right/g-right.png',
            
        },
    "left":{
            "frame":6,
            "f-width-full":1152,
            "f-width": 192,
            "f-height":100,
            "draw_width": 60,  # 실제 그릴 너비
            "draw_height": 60,  # 실제 그릴 높이
            "hit_x":0,
            "hit_y":0,
            "hit_w":60,
            "hit_h":60,
            "img-url": '../../assets/goblin/left/g-left.png',
            
        },
    "right":{
            "frame":6,
            "f-width-full":1152,
            "f-width": 192,
            "f-height":100,
            "draw_width": 60,  # 실제 그릴 너비
            "draw_height": 60,  # 실제 그릴 높이
            "hit_x":0,
            "hit_y":0,
            "hit_w":60,
            "hit_h":60,
            "img-url": '../../assets/goblin/right/g-right.png',
        }
}
Castle_img_dic = {
    "default":{
        "frame":1,
        "f-width-full":195,
        "f-width":195,
        "f-height":288,
        "draw_width": 100,  # 실제 그릴 너비
        "draw_height": 100,  # 실제 그릴 높이
        "hit_x":0,
        "hit_y":0,
        "hit_w":100,
        "hit_h":100,
        "img-url":'../../assets/Buildings/Castle/Castle_Blue.png',
    }
}
House_img_dic = {
      "default":{
        "frame":1,
        "f-width-full":108,
        "f-width":108,
        "f-height":142,
        "draw_width": 50,  # 실제 그릴 너비
        "draw_height": 70,  # 실제 그릴 높이
        "hit_x":0,
        "hit_y":20,
        "hit_w":50,
        "hit_h":50,
        "img-url":'../../assets/Buildings/House/House_Blue.png',
    }
}
Tower_img_dic ={
     "default":{
        "frame":1,
        "f-width-full":115,
        "f-width":115,
        "f-height":173,
        "draw_width": 50,  # 실제 그릴 너비
        "draw_height": 100,  # 실제 그릴 높이
        "hit_x":0,
        "hit_y":50,
        "hit_w":50,
        "hit_h":50,
        "img-url":'../../assets/Buildings/Tower/Tower_Blue.png',
    }
}
background_img_dic={
     "default":{
        "frame":1,
        "f-width-full":3300,
        "f-width":3300,
        "f-height":3300,
        "draw_width": 500,  # 실제 그릴 너비
        "draw_height": 500,  # 실제 그릴 높이
        "hit_x":0,
        "hit_y":0,
        "hit_w":500,
        "hit_h":500,
        "img-url":'../../assets/background/grid_tile.png',
    }
}
gold_img_dic={
    "default":{
        "frame":7,
        "f-width-full":896,
        "f-width":100,
        "f-height":80,
        "draw_width": 50,  # 실제 그릴 너비
        "draw_height": 50,  # 실제 그릴 높이
        "hit_x":0,
        "hit_y":0,
        "hit_w":50,
        "hit_h":50,
        "img-url":'../../assets/objects/gold/G_Spawn.png',
    }
}
wood_img_dic={
    "default":{
        "frame":7,
        "f-width-full":896,
        "f-width":100,
        "f-height":100,
        "draw_width": 60,  # 실제 그릴 너비
        "draw_height": 60,  # 실제 그릴 높이
        "hit_x":0,
        "hit_y":0,
        "hit_w":60,
        "hit_h":60,
        "img-url":'../../assets/objects/wood/W_Spawn.png'
    }
}