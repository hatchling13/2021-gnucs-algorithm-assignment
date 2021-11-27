from tkinter import *
from tkinter.ttk import *

from mst import Mst, Vertex

class Gui:
    _tree = Mst()

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('Minimum Spanning Tree')
        self.window.geometry('1280x720')
        
        #------------------------------------------------------
        left_frame = Frame(self.window, relief='solid')
        right_frame = Frame(self.window, relief='solid')
        
        left_frame.pack(side='left', fill='both', expand=True)
        right_frame.pack(side='right', fill='both', expand=True)

        #------------------------------------------------------
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

        #------------------------------------------------------
        upper_frame = Frame(left_frame, relief='solid')
        lower_frame = Frame(left_frame, relief='solid')
        
        upper_frame.pack(side='top', fill='both', expand=True)
        lower_frame.pack(side='bottom', fill='both', expand=True)
        
        #------------------------------------------------------
        canvas = Canvas(upper_frame, relief='solid', bd=2)
        canvas.pack(fill='both', expand=True)
        canvas.bind('<Button-1>', self.mouse)
        
        #------------------------------------------------------
        prim_frame = Frame(lower_frame, relief='solid')
        kruskal_frame = Frame(lower_frame, relief='solid')
        
        prim_frame.pack(side='left', fill='both', expand=True)
        kruskal_frame.pack(side='right', fill='both', expand=True)
        
        #------------------------------------------------------
        self.prim_canvas = Canvas(prim_frame, relief='solid')
        self.prim_canvas.pack(fill='both', expand=True)

        self.kruskal_canvas = Canvas(kruskal_frame, relief='solid')
        self.kruskal_canvas.pack(fill='both', expand=True)

    def start(self) -> None:
        self.window.mainloop()

    def mouse(self, event: Event) -> None:
        canvas: Canvas = event.widget
        
        self._tree.add_vertex(event.x, event.y)

        src_vertexs = [str(v._value) for v in self._tree._vertex]
        dst_vertexs = [str(v._value) for v in self._tree._vertex]

        #---------------------------------------------------
        # 반대쪽에서 선택한 항목 제거
        # 이미 선택되어있을 때 -1 뜨는 것 제어
        #---------------------------------------------------
        src_current: int = self.src_combobox.current()
        if src_current != -1:
            dst_vertexs.remove(src_vertexs[src_current])
        else:
            print(src_current)

        dst_current: int = self.dst_combobox.current()
        if dst_current != -1:
            src_vertexs.remove(dst_vertexs[dst_current])
        else:
            print(src_current)

        #---------------------------------------------------
           
        self.src_combobox['values'] = src_vertexs
        self.dst_combobox['values'] = dst_vertexs

        v: Vertex = self._tree.get_vertex(self._tree._count - 1)

        circle = calc_circle(v._x, v._y, 15)
        canvas.create_oval(circle[0], circle[1], circle[2], circle[3], fill='cyan')
        canvas.create_text(v._x, v._y, text=str(v._value))

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