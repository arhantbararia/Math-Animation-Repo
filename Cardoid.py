from manim import *

class Cardioid(Scene):

def construct(self):

plane = PolarPlane(

azimuth_units="PI radians",

size=6,

azimuth_label_scale=0.7,

radius_config={"number_scale_value": 0.5},

).add_coordinates()

self.add(plane)

graph = ParametricFunction(

lambda t : np.array([1.2*np.cos(t)*(1+np.cos(t)), 1.2*np.sin(t)*(1+np.cos(t)), 0]),

t_range = np.array([0, TAU]),

)

self.play(

Create(graph),

rate_func = smooth,

run_time = 3

)

self.wait(1)

cardioid = Tex(r"This is"," Cardioid." "\\\\",

"$r = a\\cdot(1+\\mathrm{cos}(\\theta))$"

)

cardioid.set_color_by_tex('Cardioid',BLUE)

cardioid.to_edge(UP+LEFT)

self.play(

Write(cardioid),

Indicate(graph),

run_time = 3

)

self.wait(2)
