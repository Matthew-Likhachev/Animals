from threading import Thread
import random, time

class OrganismInspector():
    def __init__(self, panel_borders):
        self.cell_list = []
        self.main_panel_borders = panel_borders
    def create_cell(self):
        cell_posx=random.randint(0,1280)
        cell_posy=random.randint(0,720)
        cell_changex = random.randint(-6,6)
        cell_changey = random.randint(-6,6)
        cell_radius=random.randint(10,50)
        #cell_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cell_color = (255,0,0)
        self.cell_list.append(Cell(cell_posx, cell_posy, cell_changex,cell_changey, cell_radius, cell_color))
    def create_cells(self,amount):
        for i in range(amount):
            self.create_cell()
        # for cell in self.cell_list:
        #     cell.change_x = 0
        #     cell.change_y = 0
        # self.cell_list[0].change_x = -6
        # self.cell_list[0].change_y = 8
        # self.cell_list[0].radius =200


    def get_cells(self):
        return self.cell_list
    def resize(self, new_panel_borders):
        self.main_panel_borders = new_panel_borders
        print(self.main_panel_borders)
    def update(self):
        if self.cell_list:
            self.check_colisions()
        #print(len(self.cell_list))
        #print(len(self.cell_list[0:len(self.cell_list)//2]))


        # threads_arr = []
        # size = 10
        # for i in range(len(self.cell_list)//size):
        #     threads_arr.append(Thread(target=self.check_colisions_test, args=(self.cell_list[i*size : i*size+size],)))
        # # t1 = Thread(target=self.check_colisions_test, args=([self.cell_list[0:len(self.cell_list)//2]]))
        # # t2 = Thread(target=self.check_colisions_test, args=([self.cell_list[len(self.cell_list)//2:]]))
        # for th in threads_arr:
        #     th.start()
        # for th in threads_arr:
        #     th.join()
        # # t1.start()
        # # t2.start()
        # # #self.check_colisions_test()
        # # t1.join()
        # # t2.join()



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
            if (cell.x_pos + cell.radius < self.main_panel_borders[0][0] or cell.x_pos + cell.radius> self.main_panel_borders[3][0]):
                cell.change_x *= -1
                #self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if (cell.y_pos + cell.radius < self.main_panel_borders[0][1] or cell.y_pos + cell.radius > self.main_panel_borders[1][1]):
                cell.change_y *= -1
                #self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def check_colisions_all_with_all(self):
        # Переменная  для проверки прохода
        first_time = True
        self.cell_list[0].chng_color((255, 0, 0))

        for cell1_iter in range(len(self.cell_list)):
            for cell2_iter in range(len(self.cell_list)):
                    if self.cell_list[cell1_iter] == self.cell_list[cell2_iter]:
                        continue

                    # Если проходимся первый раз - красим всех в красный
                    if first_time:
                        self.cell_list[cell2_iter].color = (255, 0, 0)

                    xdif = abs(self.cell_list[cell1_iter].x_pos - self.cell_list[cell2_iter].x_pos)
                    ydif = abs(self.cell_list[cell1_iter].y_pos - self.cell_list[cell2_iter].y_pos)
                    sum_radius = self.cell_list[cell1_iter].radius + self.cell_list[cell2_iter].radius
                    # Коллизия шаров (расстояние между клетками меньше суммы их радиусов)
                    if xdif ** 2 + ydif ** 2 <= sum_radius ** 2:
                        self.cell_list[cell2_iter].chng_color((255, 255, 0))
                        self.cell_list[cell1_iter].chng_color((255, 255, 0))
                        # self.cell_list[cell1_iter].change_y *= -1
                        # self.cell_list[cell1_iter].change_x *= -1
                        #
                        # self.cell_list[cell2_iter].change_y *= -1
                        # self.cell_list[cell2_iter].change_x *= -1

            if first_time:
                first_time = False
    def check_colisions_test(self, small_cell_list):
        for cell1_iter in range(len(small_cell_list)):
            for cell2_iter in range(len(self.cell_list)):
                # if self.cell_list[cell1_iter] == self.cell_list[cell2_iter]:
                #     continue

                xdif = abs(self.cell_list[cell1_iter].x_pos - self.cell_list[cell2_iter].x_pos)
                ydif = abs(self.cell_list[cell1_iter].y_pos - self.cell_list[cell2_iter].y_pos)
                sum_radius = self.cell_list[cell1_iter].radius ** 2 + self.cell_list[cell2_iter].radius ** 2
                # Коллизия шаров (расстояние между клетками меньше суммы их радиусов)
                if xdif ** 2 + ydif ** 2 < sum_radius:
                    # print("Сработало условие")
                    # self.cell_list[cell1_iter].change_y *= -1
                    # self.cell_list[cell1_iter].change_x *= -1
                    #
                    # self.cell_list[cell2_iter].change_y *= -1
                    # self.cell_list[cell2_iter].change_x *= -1


                    self.cell_list[cell2_iter].color = (255,255,0)
                else:
                    self.cell_list[cell2_iter].color = (255,0,0)

    def check_colisions(self):
        #Переменная  для проверки прохода
        first_time = True
        self.cell_list[0].chng_color((255, 0, 0))
        # прохдимся по каждой клетке
        for cell1_iter in range(len(self.cell_list)):
            #прохдимся по каждой следующей клетке, не учитывая уже пройденные
            for cell2_iter in range(cell1_iter+1, len(self.cell_list)):

                # if self.cell_list[cell1_iter] == self.cell_list[cell2_iter]:
                #     continue

                #Если проходимся первый раз - красим всех в красный
                if first_time:
                    self.cell_list[cell2_iter].color = (255, 0, 0)
                xdif = abs(self.cell_list[cell1_iter].x_pos - self.cell_list[cell2_iter].x_pos)
                ydif = abs(self.cell_list[cell1_iter].y_pos - self.cell_list[cell2_iter].y_pos)
                sum_radius = self.cell_list[cell1_iter].radius+self.cell_list[cell2_iter].radius
                #Коллизия шаров (расстояние между клетками меньше суммы их радиусов)
                if xdif**2+ydif**2<=sum_radius**2:
                    self.cell_list[cell2_iter].chng_color((255, 255, 0))
                    self.cell_list[cell1_iter].chng_color((255, 255, 0))
                    # self.cell_list[cell1_iter].change_y *= -1
                    # self.cell_list[cell1_iter].change_x *= -1
                    #
                    # self.cell_list[cell2_iter].change_y *= -1
                    # self.cell_list[cell2_iter].change_x *= -1

            if first_time:
                first_time = False

        
class Cell():  # arcade.draw_circle_filled()
    def __init__(self, x_pos, y_pos, change_x, change_y, radius, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.change_x = change_x
        self.change_y = change_y
    def chng_color(self, color):
        self.color = color
    def update(self):
        self.x_pos += self.change_x
        self.y_pos += self.change_y


