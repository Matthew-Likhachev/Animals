
import random

class OrganismInspector():
    def __init__(self, panel_borders):
        self.cell_list = []
        self.main_panel_borders = panel_borders
    def create_cell(self):
        cell_posx=random.randint(0,1280)
        cell_posy=random.randint(0,720)
        cell_changex = random.randint(-6,6)
        cell_changey = random.randint(-6,6)
        cell_radius=18
        cell_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.cell_list.append(Cell(cell_posx, cell_posy, cell_changex,cell_changey, cell_radius, cell_color))

    def get_cells(self):
        return self.cell_list
    def resize(self, new_panel_borders):
        self.main_panel_borders = new_panel_borders
        print(self.main_panel_borders)
    def update(self):
        self.check_colisions()

        for cell in self.cell_list:
            cell.update()

            # print(self.panel_borders)
            '''
            #self.panel_borders = [[x1,y1], [x2,y2], [x3, y3], [x4,y4]]

                  координаты точек боковой панели
                  2................3....
                  ......................
                  ......................
                  1................4....
            '''
            if (cell.x_pos < self.main_panel_borders[0][0] or cell.x_pos > self.main_panel_borders[3][0]):
                cell.change_x *= -1
                #self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if (cell.y_pos < self.main_panel_borders[0][1] or cell.y_pos > self.main_panel_borders[1][1]):
                cell.change_y *= -1
                #self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def check_colisions(self):
        # прохдимся по каждой клетке
        for cell1_iter in range(len(self.cell_list)):
            #прохдимся по каждой клетке ДО начальной
            for cell2_iter in range(0,cell1_iter):
                xdif = abs(self.cell_list[cell1_iter].x_pos - self.cell_list[cell2_iter].x_pos)
                ydif = abs(self.cell_list[cell1_iter].y_pos - self.cell_list[cell2_iter].y_pos)
                sum_radius = self.cell_list[cell1_iter].radius**2+self.cell_list[cell2_iter].radius**2
                #Коллизия шаров (расстояние между клетками меньше суммы их радиусов)
                if xdif**2+ydif**2<sum_radius:
                    #print("Сработало условие")
                    self.cell_list[cell1_iter].change_y *= -1
                    self.cell_list[cell1_iter].change_x *= -1

                    self.cell_list[cell2_iter].change_y *= -1
                    self.cell_list[cell2_iter].change_x *= -1

            #прохдимся по каждой клетке ПОСЛЕ начальной
            for cell2_iter in range(cell1_iter,len(self.cell_list)):
                xdif = abs(self.cell_list[cell1_iter].x_pos - self.cell_list[cell2_iter].x_pos)
                ydif = abs(self.cell_list[cell1_iter].y_pos - self.cell_list[cell2_iter].y_pos)
                sum_radius = self.cell_list[cell1_iter].radius ** 2 + self.cell_list[cell2_iter].radius
                #Коллизия шаров (расстояние между клетками меньше суммы их радиусов)
                if xdif ** 2 + ydif ** 2 < sum_radius:
                    self.cell_list[cell1_iter].change_y *= -1
                    self.cell_list[cell1_iter].change_x *= -1

                    self.cell_list[cell2_iter].change_y *= -1
                    self.cell_list[cell2_iter].change_x *= -1
            #cell.check_colision(x,y)
class Cell():  # arcade.draw_circle_filled()
    def __init__(self, x_pos, y_pos, change_x, change_y, radius, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.change_x = change_x
        self.change_y = change_y

    def update(self):
        self.x_pos += self.change_x
        self.y_pos += self.change_y


