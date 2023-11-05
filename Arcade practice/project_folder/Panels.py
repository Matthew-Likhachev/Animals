class RightPanel():
    def __init__(self, width=100, height=200, color=(255,0,0), window_width=1280,window_height = 720):
        self.width = width
        self.height = height
        self.color = color
        self.set_pos(window_width,window_height)
    def set_width(self, value):
        self.width = value
    def set_height(self, value):
        self.height = value
    def set_color(self, value):
        self.color = value
    def set_pos(self,window_width, window_height):
        '''
              координаты точек боковой панели
              ................2....3
              ......................
              ......................
              ................1....4
        '''
        self.x1 = window_width - self.width
        self.y1 = 0

        self.x2 = window_width - self.width
        self.y2 = window_height

        self.x3 = window_width
        self.y3 = window_height

        self.x4 = window_width
        self.y4 = 0
        self.menu_coords = (
            (self.x1, self.y1),  # 1
            (self.x2, self.y2),  # 2
            (self.x3, self.y3),  # 3
            (self.x4, self.y4)  # 4
        )
    def get_pos(self):
        return self.menu_coords
    def resize(self, width, height):
        self.set_pos(width, height)


#Панель где происходит отрисовка
class MainPanel():

    def __init__(self, width=1280, height=720,color= (255,255,255),window_width=1280, window_height=720):
        self.width= width
        self.height = height
        self.color = color
        #self.calculate_coords()
        self.set_pos(window_width, window_height)

    def set_pos(self,window_width, window_height):
        '''
            координаты точек боковой панели
            2................3....
            ......................
            ......................
            1................4....
        '''
        # высчитывание координат
        # Центр поля в get_window().width/2 и get_window().height/2   - половина размера окна
        # из него надо вычесть половину рабочего центрального окна
        self.x1 = window_width / 2 - self.width / 2
        self.y1 = window_height / 2 - self.height / 2

        self.x2 = window_width / 2 - self.width / 2
        self.y2 = window_height / 2 + self.height / 2

        self.x3 = window_width / 2 + self.width / 2
        self.y3 = window_height / 2 + self.height / 2

        self.x4 = window_width / 2 + self.width / 2
        self.y4 = window_height / 2 - self.height / 2

        self.panel_coords = (
            (self.x1, self.y1),  # 1
            (self.x2, self.y2),  # 2
            (self.x3, self.y3),  # 3
            (self.x4, self.y4)  # 4
        )
        #print(self.panel_coords)

    def get_pos(self):
        return self.panel_coords

