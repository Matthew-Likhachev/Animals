import  arcade

from .Panels import MainPanel, RightPanel

from .Animals import OrganismInspector

from .Buttons import ChangeColorButton, CreateCellButton



class Window(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_start()
    def run(self):
        super().run()

    def setup_start(self):
        ###базовые данные

        #позиция курсора
        self.mouse_x = 0
        self.mouse_y = 0
        arcade.set_background_color(arcade.csscolor.AQUA)
        arcade.get_window().set_minimum_size(width=500,height=500)

        self.create_panels()
        self.create_buttons()
        self.create_organisms()
    def create_organisms(self):
        self.org_insp = OrganismInspector(panel_borders= self.main_panel.get_pos())
        self.org_insp.create_cells(1)


    def create_panels(self):
        # размеры окон
        self.main_panel_width = 1280
        self.main_panel_height = 720
        self.main_panel_color = (255,255,255)
        #print(f"arcade.get_window().width {arcade.get_window().width},  arcade.get_window().height {arcade.get_window().height}")
        self.main_panel = MainPanel(width=self.main_panel_width, height=self.main_panel_height, color= self.main_panel_color, window_width=arcade.get_window().width, window_height = arcade.get_window().height)

        self.right_panel_width = 200
        self.right_panel_height = arcade.get_window().height
        self.right_panel_color = arcade.color.GRAY
        #размеры окна (нулевое окно)- arcade.get_display_size(0)[0], arcade.get_display_size(0)[1]
        self.right_panel = RightPanel(self.right_panel_width,self.right_panel_height , self.right_panel_color,window_width= arcade.get_display_size(0)[0], window_height =arcade.get_display_size(0)[1])

    def create_buttons(self):
        self.chng_clr_btn = ChangeColorButton(center_x=500, center_y=500, width=120, height=50, text="NEW COLOR!")                              # Кнопка смены цвета
        self.create_cell_btn = CreateCellButton(center_x=-500, center_y=300, width=120, height=50, text="Create Cell", face_color=(255,0,0))    # Кнопка создания клетки
        # print(f"color: {self.chng_clr_btn.center_y}")
        # print(f"Cell: {self.create_cell_btn.center_y}")

    def on_draw(self):
        arcade.start_render()

        #draw main panel
        arcade.draw_polygon_filled(self.main_panel.get_pos(), self.main_panel.color)

        #draw cells
        for cell in self.org_insp.get_cells():
            arcade.draw_circle_filled(cell.x_pos, cell.y_pos, cell.radius, cell.color)

        #draw right panel
        arcade.draw_polygon_filled(self.right_panel.get_pos(), self.right_panel.color)
        self.chng_clr_btn.draw()
        self.create_cell_btn.draw()



    def on_update(self, delta_time):
        self.org_insp.update()

    def on_resize(self, width: float, height: float):
        super().on_resize(width, height)

        # resize right panel
        self.right_panel.resize(width,height)
        #print(self.right_panel.)
        #self.main_panel.resize(width,height)

        self.org_insp.resize(self.main_panel.get_pos())

        self.chng_clr_btn.resize(self.right_panel.get_pos())
        self.create_cell_btn.resize(self.right_panel.get_pos())



    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_x = x
        self.mouse_y = y
        #print( self.mouse_x,  self.mouse_y)
        self.chng_clr_btn.check_mouse_coords(self.mouse_x, self.mouse_y, False)
        self.create_cell_btn.check_mouse_coords(self.mouse_x, self.mouse_y, False)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.chng_clr_btn.check_mouse_coords(self.mouse_x, self.mouse_y, False)
        self.create_cell_btn.check_mouse_coords(self.mouse_x, self.mouse_y, False)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.chng_clr_btn.check_mouse_coords(self.mouse_x, self.mouse_y, True)
        self.create_cell_btn.check_mouse_coords(self.mouse_x, self.mouse_y, True)
        if self.create_cell_btn.is_activated_action :
            self.org_insp.create_cell()





