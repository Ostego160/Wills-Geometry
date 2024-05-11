from tkinter import *
from geometry import *

class Gui:
    def __init__(self, window: Tk) -> None:
        """
        Constructor for the Gui Class that creates the content for the window
        :param window:
            The window to populate
        """
        self.window = window

        # Radio buttons
        self.frame_func = Frame(self.window)
        self.label_operation = Label(self.frame_func, text='Select Function to Graph:\t')
        self.radio_var = IntVar()
        self.radio_var.set(0)
        self.radio_f0 = Radiobutton(self.frame_func, text='No Function', variable=self.radio_var, value=0)
        self.radio_f1 = Radiobutton(self.frame_func, text='Func 1', variable=self.radio_var, value=1)
        self.radio_f2 = Radiobutton(self.frame_func, text='Func 2', variable=self.radio_var, value=2)
        self.radio_f3 = Radiobutton(self.frame_func, text='Func 3', variable=self.radio_var, value=3)
        self.label_operation.pack()
        self.radio_f0.pack(side=LEFT)
        self.radio_f1.pack(side=LEFT)
        self.radio_f2.pack(side=LEFT)
        self.radio_f3.pack(side=LEFT)

        self.frame_func.pack()

        # Dimensions
        self.frame_dimensions = Frame(self.window)
        self.label_instructions1 = Label(self.frame_dimensions, text='Geometry Dimensions:')

        self.label_w = Label(self.frame_dimensions, text='W:')
        self.entry_w = Entry(self.frame_dimensions, width=8)
        self.label_h = Label(self.frame_dimensions, text='H:')
        self.entry_h = Entry(self.frame_dimensions, width=8)
        self.label_d = Label(self.frame_dimensions, text='D:')
        self.entry_d = Entry(self.frame_dimensions, width=8)
        self.label_instructions1.pack()
        self.label_w.pack(padx=5, side=LEFT)
        self.entry_w.pack(padx=5, side=LEFT)
        self.label_h.pack(padx=5, side=LEFT)
        self.entry_h.pack(padx=5, side=LEFT)
        self.label_d.pack(padx=5, side=LEFT)
        self.entry_d.pack(padx=5, side=LEFT)

        self.frame_dimensions.pack()

        # Angles
        self.frame_angle = Frame(self.window)
        self.label_instructions2 = Label(self.frame_angle, text='Enter Rotation Angles:')

        self.var_theta = StringVar()
        self.var_phi = StringVar()

        self.label_theta = Label(self.frame_angle, text='Theta:')
        self.entry_theta = Entry(self.frame_angle, width=8, textvariable=self.var_theta)
        self.label_phi = Label(self.frame_angle, text='Phi:')
        self.entry_phi = Entry(self.frame_angle, width=8, textvariable=self.var_phi)
        self.label_instructions2.pack()
        self.label_theta.pack(padx=5, side=LEFT)
        self.entry_theta.pack(padx=5, side=LEFT)
        self.label_phi.pack(padx=5, side=LEFT)
        self.entry_phi.pack(padx=5, side=LEFT)

        self.var_theta.set(str(math.pi/3))
        self.var_phi.set(str(math.pi/4))

        self.frame_angle.pack()

        # Rotations
        self.frame_rotation = Frame(self.window)
        self.label_instructions3 = Label(self.frame_rotation, text='Click buttons to rotate:')

        self.button_rotate1 = Button(self.frame_rotation, text='<-', command=self.rotate_left)
        self.button_rotate2 = Button(self.frame_rotation, text='->', command=self.rotate_right)
        self.label_instructions3.pack()
        self.button_rotate1.pack(padx=20, side=LEFT)
        self.button_rotate2.pack(padx=20, side=LEFT)
        self.frame_rotation.pack()

        #Message Label
        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text='\nEnter dimensions of the geometry to graph.')
        self.label_message.pack()
        self.frame_message.pack()

        # Graph button
        self.frame_button  = Frame(self.window)
        self.button_graph  = Button(self.frame_button, text='GRAPH', command=self.create_geometry)
        self.button_graph.pack(pady=10)
        self.frame_button.pack()

        self.frame_geometry = Frame(self.window)
        self.canvas_geometry = Canvas(self.window, width=512, height=512, bg='white')
        self.canvas_geometry.pack()
        self.frame_geometry.pack()

        #Geometry Definition
        self.geometry = None

    def verify_dimensions(self) -> bool:
        """
        Method to verify the input fields
        :return:
        """
        w = self.entry_w.get()
        h = self.entry_h.get()
        d = self.entry_d.get()

        theta = self.var_theta.get()
        phi = self.var_phi.get()

        if w == '' or h == '' or d == '' or theta == '' or phi == '':
            self.label_message.config(text=f'\nAll fields must be entered.')
            return False

        try:
            w, h, d = int(w), int(h), int(d)
            theta, phi = float(theta), float(phi)
        except:
            self.label_message.config(text=f'\nAll fields must be numbers.')
            return False

        if w <= 0 or h <= 0 or d <= 0:
            self.label_message.config(text=f'\nAll fields must be greater than zero.')
            return False

        if w > 40 or h > 40 or d > 40:
            self.label_message.config(text=f'\nFields cannot exceed 40.')
            return False

        return True

    def verify_theta(self) -> bool:
        try:
            float(self.var_theta.get())
        except:
            self.label_message.config(text=f'\nTheta angle must be number.')
            return False

        return True

    def create_geometry(self) -> None:
        """
        Method to create the 3D Geometry
        :return:
        """
        self.canvas_geometry.delete('all')

        if self.verify_dimensions():
            self.label_message.config(text=f'\nProcessing Geometry...')

            func_num = self.radio_var.get()

            w = self.entry_w.get()
            h = self.entry_h.get()
            d = self.entry_d.get()

            theta = self.entry_theta.get()
            phi = self.entry_phi.get()

            c_width  = self.canvas_geometry.winfo_reqwidth()
            c_height = self.canvas_geometry.winfo_reqheight()

            self.geometry = Geometry(w, h, d)
            self.geometry.reformat_and_set_scalar(6)
            self.geometry.apply_function(func_num)
            self.geometry.rotate(float(theta), float(phi))
            self.geometry.z_sort()
            self.geometry.draw_to_canvas(self.canvas_geometry, c_width / 2,c_height / 2 - c_height / 6)
            self.label_message.config(text=f'\nGeometry Processed.')

    def rotate_left(self) -> None:
        if self.verify_theta():
            theta = float(self.var_theta.get())
            theta += math.pi/10
            self.var_theta.set(str(theta))

    def rotate_right(self) -> None:
        if self.verify_theta():
            theta = float(self.var_theta.get())
            theta -= math.pi/10
            self.var_theta.set(str(theta))
