# import necessary libs
from manim import *
import numpy as np
from math import sin, pi


# Develop the graphs

class Intergral(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_min=0,
            y_max=10,
            y_axis_config={"tick_frequency": 1},
            y_labeled_nums=np.arange(0, 10, 1),
            x_min=0,
            x_max=10,
            x_axis_config={"tick_frequency": 1},
            x_labeled_nums=np.arange(0, 10, 1),
            **kwargs
        )
    #define construction
    def construct(self):
        self.show_function_graph()

    #Define function
    def show_function_graph(self):
        self.setup_axes(animate=True)
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5
        #Kurve der Funktion darstellen
        graph=self.get_graph(func,x_min=0.3,x_max=9.2)
        graph.set_color(YELLOW)
        self.play(ShowCreation(graph),run_time=3)
        self.wait(1)
        text1 = Tex('$\int_{2}^{8} f(x) \,dx$ = 30').set_color(WHITE).scale(1.0)
        text1.next_to(text1, 6 * UP)
        self.play(Write(text1))
        self.wait(1)

        #Define rectangle function
        def rect(x):
            return x
        recta=self.get_graph(rect,x_min=-1,x_max=5)
        #Riemanregel darstellen
        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.5,
            "stroke_width" : 0.5,
        }
        self.graph=graph

        iteraciones=6
        self.rect_list = self.get_riemann_rectangles_list(
            graph,iteraciones,start_color=PURPLE,end_color=ORANGE,**kwargs
        )
        flat_rects=self.get_riemann_rectangles(
            self.get_graph((lambda  x :0),dx=1,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs)
        )
        rects=self.rect_list[0] #define the size of rectangles - bigger number smaller rectangle
        self.transform_between_riemann_rects(
            flat_rects,rects,
            replace_mobject_with_target_in_scene=True,
            run_time=0.9
        )
        on_screen_n = Variable(10, Text("n"), num_decimal_places=0)
        on_screen_n.next_to(on_screen_n, 11*RIGHT)

        #Gesamtfläche der Rechecke berechnen
        a = 2
        b = 8
        dx = (b - a) / 10
        xi = a
        sum = 0
        for i in range(0, 10 + 1):
            sum = sum + func(xi)
            xi = xi + dx
        Riemannsum = sum * dx
        Diff=Riemannsum-30
        on_screen_Riemann = Variable(Riemannsum, Text("Gesamtfläche der Rechtecke"), num_decimal_places=2)

        on_screen_Riemann.next_to(on_screen_Riemann,1.5*DOWN+ 3 * RIGHT).scale(0.3)

        # Difference
        on_screen_Diff = Variable(Diff, Text("Fehler"), num_decimal_places=2)

        on_screen_Diff.next_to(on_screen_Diff, 5 * DOWN + 4 * RIGHT).scale(0.5)
        self.play(Write(on_screen_n))
        self.play(Write(on_screen_Riemann))
        self.play(Write(on_screen_Diff))
        self.wait(0, 9)
        self.remove(self, on_screen_n)
        self.remove(self, on_screen_Riemann)
        self.remove(self, on_screen_Diff)



        for r in range(1,6):
            self.transform_between_riemann_rects(
                    self.rect_list[r-1],self.rect_list[r],dx=1,
                    replace_mobject_with_target_in_scene = True,
                run_time=0.9
                )
            # Gesamtfläche der Rechecke berechnen
            n = (2 ** r) * 10
            a = 2
            b = 8
            dx = (b - a) / n
            xi = a
            sum = 0
            for i in range(0, n + 1):
                sum = sum + func(xi)
                xi = xi + dx
            #Gesamtfläche der Rechecke
            Riemannsum = sum * dx
            on_screen_Riemann = Variable(Riemannsum, Text("Gesamtfläche der Rechecke"), num_decimal_places=2)
            on_screen_Riemann.next_to(on_screen_Riemann, 1.5*DOWN+3* RIGHT).scale(0.3)
            # Fehler
            Diff = Riemannsum - 30
            on_screen_Diff = Variable(Diff, Text("Fehler"), num_decimal_places=2)
            on_screen_Diff.next_to(on_screen_Diff, 5 * DOWN + 4* RIGHT).scale(0.5)
            # n
            on_screen_n = Variable(n, Text("n"), num_decimal_places=0)
            on_screen_n.next_to(on_screen_n, 11 * RIGHT)

            self.play(Write(on_screen_n))
            self.play(Write(on_screen_Riemann))
            self.play(Write(on_screen_Diff))
            self.wait(0, 9)
            self.remove(self, on_screen_n)
            self.remove(self, on_screen_Riemann)
            self.remove(self, on_screen_Diff)


