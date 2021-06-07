from manimlib.imports import *

import numpy as np



class Interference(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "x_axis_width": 9,
        "x_tick_frequency": 0.5,
        "y_min": -2,
        "y_max": 3,
        "y_axis_height": 6,
        "y_tick_frequency": 1
        
    }

    def construct(self):
        self.setup_axes(animate = True)
        

        curve = []

        for b in range(2 , 20 , 1):

            curve.append(ParametricFunction(lambda t : np.array([2*np.cos(b*t)*np.cos(t), 
                                            2*np.cos(b*t)*np.sin(t) , 0]) , color = PINK , t_min = 0 , t_max = 2*PI))
            

        self.play(ShowCreation(curve[0]))

        for i in range(1 ,18):
            self.play(ReplacementTransform(curve[i-1], curve[i]))

        self.wait()
        
        self.play(Uncreate(curve[17]))
        self.play(*[FadeOut(i) for i in self.axes])

        group_dots = VGroup(*[Dot() for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)

        for dot in group_dots: 
            self.play(FadeIn(dot))
        
        self.wait()
