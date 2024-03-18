import js
from js import document, window, Image, console

class GameObject:
    _id_counter = 0
    
    def __init__(self, x, y, img_dic,type,hp):
        img_info = img_dic["default"]
        
        self._x = x
        self._y = y
        self._width = img_info["draw_width"]
        self._height = img_info["draw_height"]
        self._direction = "S"
        self._dx = 0
        self._dy = 0
        self._state = "default"
    
        self._img_dic = img_dic
        self._hit_x = img_info["hit_x"] + x 
        self._hit_y = img_info["hit_y"] + y 
        self._hit_w = img_info["hit_w"]
        self._hit_h = img_info["hit_h"]
        
        self._id = GameObject._id_counter  # 객체별 유니크 ID 할당
        GameObject._id_counter += 1
        self.motion_num = 0
        
        self._state_frames_remaining = 0  # 현재 상태가 유지되어야 하는 남은 프레임 수
        self._default_state = "default" # 객체의 기본 상태 저장
        
        self._type = type
        self._hp = hp

    def set_state_frame(self, state, frames=0):
        """특정 상태를 설정하고, 지정된 프레임 동안 유지"""
        self._state = state
        self._state_frames_remaining = frames  # 상태 유지 프레임 설정
    
    def update_state(self):
        """객체 상태 업데이트 - 매 프레임 호출 필요"""
        if self._state_frames_remaining > 0:
            self._state_frames_remaining -= 1  # 프레임 카운트 다운
            if self._state_frames_remaining == 0:
                self._state = self._default_state  # 프레임 완료 시 기본 상태로 복귀

    # Getter methods
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_direction(self):
        return self._direction

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def get_state(self):
        return self._state

    def get_img_dic(self):
        return self._img_dic

    def get_hit_x(self):
        return self._hit_x

    def get_hit_y(self):
        return self._hit_y

    def get_hit_w(self):
        return self._hit_w

    def get_hit_h(self):
        return self._hit_h

    def get_id(self):
        return self._id
    
    def get_type(self):
        return self._type

    def get_hp(self):
        return self._hp

    #init정리필요!
        
    
    def update_position(self):
        
        if self._direction == 'U':
            self._hit_y -= self._dy
            self._y -= self._dy
        elif self._direction == 'D':
            self._hit_y += self._dy
            self._y += self._dy
        elif self._direction == 'R':
            self._hit_x += self._dx
            self._x += self._dx
        elif self._direction == 'L':
            self._hit_x -= self._dx
            self._x -= self._dx
        elif self._direction == 'S':
            pass  # 정지 상태

    def set_direction(self,dir):
        self._direction = dir
        
    def set_velocity(self,dx,dy):
        self._dx = dx
        self._dy = dy
    
    def set_state(self,state):
        self._state = state
    
    def change_hp(self,deal):
        self._hp += deal
    
    def turn_left(self):
        direction_order = ['U', 'L', 'D', 'R']
        current_index = direction_order.index(self._direction)
        self._direction = direction_order[(current_index + 1) % 4]

    def turn_right(self):
        direction_order = ['U', 'R', 'D', 'L']
        current_index = direction_order.index(self._direction)
        self._direction = direction_order[(current_index + 1) % 4]
        
   
    def check_collision(self, other):
        
        
        # A의 오른쪽 경계가 B의 왼쪽 경계보다 오른쪽에 있는지 확인
        right_of_other_left = self._hit_w + self._hit_x >  other.get_hit_x()
        # A의 왼쪽 경계가 B의 오른쪽 경계보다 왼쪽에 있는지 확인
        left_of_other_right = self._hit_x <  other.get_hit_w() + other.get_hit_x()
        # A의 하단 경계가 B의 상단 경계보다 아래에 있는지 확인
        below_other_top = self._hit_h + self._hit_y > other.get_hit_y()
        # A의 상단 경계가 B의 하단 경계보다 위에 있는지 확인
        above_other_bottom =  self._hit_y <  other.get_hit_h() + other.get_hit_y()
        

        # 모든 조건이 참이면 충돌 발생
        if right_of_other_left and left_of_other_right and below_other_top and above_other_bottom:
            return True
        else:
            return False

        

class Hero(GameObject):
    def __init__(self, x, y,img_dic={},type="hero",hp=0):
        super().__init__(x, y,img_dic,type,hp)
        self._tot_attack = 0
        self._attack_frame = 0
        self.__num_gold = 0
        self.__num_wood = 0
    
    def gold_change(self,num):
        self.__num_gold += num
    def get_gold(self):
        return self.__num_gold
    
    def wood_change(self,num):
        self.__num_wood += num
        
    def get_wood(self):
        return self.__num_wood
    
    def update_position(self):
    
    
        if "attack" in self.get_state():
            return
        if self._direction == 'U':
            self._hit_y -= self._dy
            self._y -= self._dy
        elif self._direction == 'D':
            self._hit_y += self._dy
            self._y += self._dy
        elif self._direction == 'R':
            self._hit_x += self._dx
            self._x += self._dx
        elif self._direction == 'L':
            self._hit_x -= self._dx
            self._x -= self._dx
        elif self._direction == 'S':
            pass  # 정지 상태
        
    def is_attack_hit(self,obj):
        
        if "attack" in self.get_state() and self.check_collision(obj):
            console.log(obj.get_hp())
            obj.change_hp(-10)
            return True
        else:
            return False
    
    def attack(self, attack_num=1):
        # 공격 상태 설정 시 고려할 프레임 수
        total_frames_for_attack = 6 * attack_num
        before_direction = self._direction
        
        
        # 공격 방향에 따라 상태 설정
        if before_direction == "L":
            self._default_state = "left"
            self.set_state_frame("attack-left", total_frames_for_attack)
        elif before_direction == "R":
            self._default_state = "right"
            self.set_state_frame("attack-right", total_frames_for_attack)
        elif before_direction == "U":
            self.set_state_frame("attack-up", total_frames_for_attack)
        elif before_direction == "D":
            self.set_state_frame("attack-down", total_frames_for_attack)
            
    def stop(self):
        self._direction = "S"
    def go_left(self):
        self.set_state("left")
        self._direction = "L"
    def go_right(self):
        self.set_state("right")
        self._direction = "R"
    def go_down(self):
        self._direction = "D"
    def go_up(self):
        self._direction = "U"

class Wall(GameObject):
    def __init__(self, x, y,img_dic={},type="wall",hp=0):
        super().__init__(x, y,img_dic,type,hp)
    
    def move_left_right(self,X):
        if self._x > X-self._width and self._state == "right":
            self._direction = "L"
            self._state = "left"
        elif self._hit_x<0 and self._state =="left":
            self._direction = "R"
            self._state ="right"
    
    def move_rectangle(self,X1,Y1,X2,Y2):
        
        if self._x < X1 and self._y < Y1 and self._direction == "U":
            self._direction = "R"
            self._state = "right"
        elif self._x > X2 and self._direction == "R":
            self._direction = "D"
            self._state = "left"
        elif self._x > X2 and self._y>Y2 and self._direction == "D":
            self._direction = "L"
            self._state = "left"
        elif self._x<X1 and self._direction == "L":
            self._direction = "U"
            self._state = "right"
        
        
            
        

class Background(GameObject):
  def __init__(self, x, y,img_dic={},type="background",hp=0):
        super().__init__(x, y,img_dic,type,hp)



class Item(GameObject):
   def __init__(self, x, y,img_dic={},type="item",hp=0):
        super().__init__(x, y,img_dic,type,hp)
        
    
        
class Monster(GameObject):
    def __init__(self, x, y,img_dic={},type="monster",hp=0):
        super().__init__(x, y,img_dic,type,hp)


