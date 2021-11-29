from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from mst import Mst, Vertex

class Gui:
    _tree = Mst()
    _circles = {}

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('Minimum Spanning Tree')
        self.window.geometry('1280x720')
        
        left_frame = Frame(self.window, relief='solid')
        right_frame = Frame(self.window, relief='solid')
        
        left_frame.pack(side='left', fill='both', expand=True)
        right_frame.pack(side='right', fill='both', expand=True)

        src_label = Label(right_frame, text="시작 정점")
        src_label.pack(pady=5)

        self.src_combobox = Combobox(right_frame, height=5, state='readonly')
        self.src_combobox.pack(pady=5)
        self.src_combobox.bind('<<ComboboxSelected>>', self.src_selected)

        dst_label = Label(right_frame, text="종료 정점")
        dst_label.pack(pady=5)

        self.dst_combobox = Combobox(right_frame, height=5, state='readonly')
        self.dst_combobox.pack(pady=5)
        self.dst_combobox.bind('<<ComboboxSelected>>', self.dst_selected)

        weight_label = Label(right_frame, text="가중치")
        weight_label.pack(pady=5)

        weight_validate_command = self.window.register(weight_validate)
        self.weight_entry = Entry(right_frame, validate='key', validatecommand=(weight_validate_command, '%P'))
        self.weight_entry.pack(pady=5)

        add_button = Button(right_frame, text='간선 추가', command=self.add_button_pressed)
        add_button.pack(pady=10)

        button_frame = Frame(right_frame)
        button_frame.pack(pady=10)

        half_button = Button(button_frame, text='중간 결과', command=self.half_button_pressed)
        result_button = Button(button_frame, text='완성 결과', command=self.result_button_pressed)

        half_button.pack(padx=5, side='left')
        result_button.pack(padx=5, side='right')

        upper_frame = Frame(left_frame, relief='solid')
        lower_frame = Frame(left_frame, relief='solid')
        
        upper_frame.pack(side='top', fill='both', expand=True)
        lower_frame.pack(side='bottom', fill='both', expand=True)
        
        input_label = Label(upper_frame, text='입력 영역')
        input_label.pack(pady=5)

        self.input_canvas = Canvas(upper_frame, relief='solid', bd=1)
        self.input_canvas.pack(fill='both', expand=True)
        self.input_canvas.bind('<Button-1>', self.mouse)
        
        prim_frame = Frame(lower_frame, relief='solid')
        kruskal_frame = Frame(lower_frame, relief='solid')
        
        prim_frame.pack(side='left', fill='both', expand=True)
        kruskal_frame.pack(side='right', fill='both', expand=True)
        
        prim_label = Label(prim_frame, text='Prim 영역')
        prim_label.pack(pady=5)
        self.prim_canvas = Canvas(prim_frame, relief='solid', bd=1)
        self.prim_canvas.pack(fill='both', expand=True)

        kruskal_label = Label(kruskal_frame, text='Kruskal 영역')
        kruskal_label.pack(pady=5)
        self.kruskal_canvas = Canvas(kruskal_frame, relief='solid', bd=1)
        self.kruskal_canvas.pack(fill='both', expand=True)

    def start(self) -> None:
        self.window.mainloop()

    def mouse(self, event: Event) -> None:
        canvas: Canvas = event.widget
        
        self._tree.add_vertex(event.x, event.y)

        src_vertexs = [str(v._value) for v in self._tree._vertex]
        dst_vertexs = [str(v._value) for v in self._tree._vertex]
        
        src_value = self.src_combobox.get()
        if src_value != "":
            dst_vertexs.remove(src_value)

        dst_value = self.dst_combobox.get()
        if dst_value != "":
            src_vertexs.remove(dst_value)
           
        self.src_combobox['values'] = src_vertexs
        self.dst_combobox['values'] = dst_vertexs

        v: Vertex = self._tree.get_vertex(self._tree._count - 1)

        circle_tuple = calc_circle(v._x, v._y, 15)
        circle = canvas.create_oval(circle_tuple[0], circle_tuple[1], circle_tuple[2], circle_tuple[3], fill='cyan')
        canvas.create_text(v._x, v._y, text=str(v._value))

        self._circles[str(v._value)] = circle

    def src_selected(self, event: Event):
        src: Combobox = event.widget
        
        dst_list = [str(v._value) for v in self._tree._vertex]
        dst_list.remove(src.get())

        self.dst_combobox['values'] = dst_list

    def dst_selected(self, event: Event):
        dst: Combobox = event.widget

        src_list = [str(v._value) for v in self._tree._vertex]
        src_list.remove(dst.get())

        self.src_combobox['values'] = src_list

    def add_button_pressed(self):
        src: str = self.src_combobox.get()
        dst: str = self.dst_combobox.get()
        weight: str = self.weight_entry.get()

        if src == '' or dst == '':
            messagebox.showerror('입력 오류', '정점을 입력해주세요.')

        elif weight == '':
            messagebox.showerror('입력 오류', '가중치를 입력해주세요.')

        else:
            # 간선 그리기 처리
            selected_src = self._tree.get_vertex_by_value(int(src))
            selected_dst = self._tree.get_vertex_by_value(int(dst))

            edge_id = self.input_canvas.create_line(selected_src._x, selected_src._y, selected_dst._x, selected_dst._y)
            
            # 간선 충돌 처리

            vertex_list = [v for v in self._tree._vertex]

            vertex_list.remove(selected_src)
            vertex_list.remove(selected_dst)

            if self.collision_detect(edge_id, vertex_list):
                pass
    
    def half_button_pressed(self):
        print('half')

    def result_button_pressed(self):
        print('result')

    def collision_detect(self, edge_id: int, vertex_list: list) -> bool:
        '''
        선분의 좌표와 정점 리스트를 제공, 충돌 처리 필요
        '''
        print('line segment coords:', self.input_canvas.coords(edge_id))

        overlapping = self.input_canvas.find_overlapping(*self.input_canvas.coords(edge_id))

        print('Overlapping objects:', overlapping)
        print('Edge id:', edge_id)

        # Overlapping canvas item type
        # filter with type?
        for id in overlapping:
            print(id, self.input_canvas.type(id))
        
        for v in vertex_list:
            print(v._x, v._y)

def weight_validate(input: str) -> bool:
    if input.isdigit() or input == "":
        return True
    else:
        return False

def calc_circle(x: int, y: int, r: int) -> tuple:
    x0 = x - r
    x1 = x + r
    y0 = y - r
    y1 = y + r

    return (x0, y0, x1, y1)