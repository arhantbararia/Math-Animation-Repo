from manimlib.imports import *
import math
import numpy as np

class integral(GraphScene):
    CONFIG = {
            "x_max" : 20,
            "y_max" : 10,
            "y_axis_height" : 5,
            "init_dx" : 0.5,
        }


    def construct(self):
        self.show_function_graph()


    
    def show_function_graph(self):
        self.setup_axes(animate = True)

        #math functions


        def func(x):
                                                                    
            return (2.71**(0.1*x))*np.sin(x)

        
        #graph 
        graph = self.get_graph(func , x_min = -1 , x_max = 20 )

        graph.set_color(YELLOW)
        kwargs = {
            "x_min" : 5, 
            "x_max" : 15,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
        }
        
        self.play(ShowCreation(graph), runtime = 5)
        self.wait(1)

       
   
        riemann_rectangles_list = self.get_riemann_rectangles_list(
                                graph,
                                6,
                                max_dx=self.init_dx,
                                power_base=2,
                                start_color=PURPLE,
                                end_color=ORANGE,
                                 **kwargs
        )
        
        self.play(ShowCreation(riemann_rectangles_list[0]))
        self.wait()

        for r in range(1, len(riemann_rectangles_list)):
            self.play(ReplacementTransform(riemann_rectangles_list[r-1], riemann_rectangles_list[r]))


        
        self.wait(2)
       
        self.play(*[Uncreate(item) for item in riemann_rectangles_list])
        self.play(Uncreate(graph))
        self.play(*[FadeOut(i) for i in self.axes])
        self.wait(4)
        

        group_dots = VGroup(*[Dot() for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)

        for dot in group_dots: 
            self.play(FadeIn(dot))
        
        self.wait()
    
