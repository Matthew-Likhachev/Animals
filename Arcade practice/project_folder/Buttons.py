import random, time
import arcade

class Button:
    """ Text based, put under the images, excluding actual text as icon above will speak for function of the button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 face_color=arcade.color.BLUE_VIOLET,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2,
                 text = "Кнопка"):

        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height
        self.text = text

    def draw(self):
        # draw the actual GUI of the button

        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.face_color)

        arcade.draw_text(start_x=self.center_x - len(self.text)*5,
                         start_y=self.center_y, # midlle of the button
                         width=self.width,
                         #height=self.height, #не нужно, т.к. есть start_y
                         text=self.text)

        # if the button is pressed, make it the highlught color, if it isn't, make it the shadow color
        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # bottom horizontal line under button
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

    def check_mouse_coords(self,x,y,is_clicked):
        # print("y is ", y, type (y))
        # print("center y is ", self.center_y, type (self.center_y))
        # print("self.height  is ",  self.height, type ( self.height))
        # print("###")
        #
        # print("x is ", x, type(x))
        # print("center x is ", self.center_x, type(self.center_x))
        # print("self.width  is ", self.width, type(self.width))
        # print()
        # print()
        if x > self.center_x + self.width / 2:
            self.on_release()
            return
        if x < self.center_x - self.width / 2:
            self.on_release()
            return
        if y > self.center_y + self.height / 2:
            self.on_release()
            return
        if y < self.center_y - self.height / 2:
            self.on_release()
            return
        if is_clicked:
            self.on_press()
        else:
            self.on_release()
    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False
    def on_resize(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y


class ChangeColorButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
    def draw(self):
        super().draw()
    def on_press(self):
        self.action()
        super().on_press()
    def on_release(self):
        super().on_release()
    def resize(self, coords):
        self.center_x = coords[0][0]+ (coords[2][0]-coords[0][0])/2
        self.center_y = coords[1][1]-self.height
        super().on_resize(self.center_x, self.center_y)
    def check_mouse_coords(self,x,y,is_clicked):
        super().check_mouse_coords(x,y,is_clicked)
    def action(self):
        arcade.set_background_color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

class CreateCellButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        #переменная для вкл/выкл спавна  клеток
        self.is_activated_action = False
        self.start_color = self.face_color

    def draw(self):
        super().draw()

    def on_press(self):
        super().on_press()
        self.action()


    def on_release(self):
        super().on_release()

    def resize(self, coords):
        self.center_x = coords[0][0] + (coords[2][0] - coords[0][0]) / 2
        self.center_y = coords[1][1] - 100.0 - self.height
        super().on_resize(self.center_x, self.center_y)

    def check_mouse_coords(self, x, y, is_clicked):
        super().check_mouse_coords(x, y, is_clicked)

    def action(self):
        #arcade.set_background_color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

        #включение и выключение режима активации
        self.is_activated_action= not self.is_activated_action
        print(self.is_activated_action)
        #смена цвета
        if self.is_activated_action:
            self.face_color=(0,255 ,0)
        else:
            self.face_color= self.start_color


        #Создание клетки
#
# class Button_Chng_Color(arcade.gui.UIFlatButton):
#     def on_click(self, event: arcade.gui.UIOnClickEvent):
#         self.target.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     def set_parameters(self,right_panel_coords,width,height):
#         right_panel_width=right_panel_coords[3][0]-right_panel_coords[0][0]
#         right_panel_height = right_panel_coords[1][1]-right_panel_coords[0][1]
#         #Кнопка смены цвета
#         self.btn_width = width
#         self.btn_height = height
#         self.btn_x = right_panel_coords[0][0]+right_panel_width/2-self.btn_width/2
#         self.btn_y = right_panel_coords[0][1]+right_panel_height-50-self.btn_height/2
#
#         self.x = self.btn_x
#         super().y = self.btn_y
#         super().width=self.btn_width
#         super().height = self.btn_height
#     def resize(self):
#         super().x = self.btn_x
#         super().y = self.btn_y
#         super().width = self.btn_width
#         super().height = self.btn_height
#     def set_target(self,target):
#         self.target = target
