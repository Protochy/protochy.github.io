import random

import numpy as np
from manim import *

COL = "#2a2c40"
config.background_color = COL


class RS(Scene):
    def construct(self):
        self.camera.background_color = COL  # set the background color to navy blue

        def func(t):
            return [t, np.exp(-t ** 2), 0]

        p = ParametricFunction(func, t_range=[-2, 2], fill_opacity=0)
        p.set_color_by_gradient([RED, BLUE, GREEN])
        numpl = NumberPlane(
            x_range=[-3, 3],
            y_range=[-2, 2],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            },
            axis_config={
                "include_numbers": True
            }
        )
        v = VGroup(numpl, p)
        v.scale(2)
        self.play(Create(numpl))

        self.play(Write(Dot(numpl.coords_to_point(0, 0))))
        self.play(Create(p))
        self.play(Write(numpl.get_riemann_rectangles(p, x_range=[-1, 1])))


class MyCamera(ThreeDCamera):
    def transform_points_pre_display(self, mobject, points):
        if getattr(mobject, "fixed", False):
            return points
        else:
            return super().transform_points_pre_display(mobject, points)


class MyThreeDScene(ThreeDScene):
    def __init__(self, camera_class=MyCamera, ambient_camera_rotation=None,
                 default_angled_camera_orientation_kwargs=None, **kwargs):
        super().__init__(camera_class=camera_class, **kwargs)


def make_fixed(*mobs):
    for mob in mobs:
        mob.fixed = True
        for submob in mob.family_members_with_points():
            submob.fixed = True


def tex_init(lcs):
    lcs.stdtex = TexTemplate()
    lcs.stdtex.add_to_preamble(r"""\usepackage{xcolor}
    \renewcommand{\c}[1]{\color{#1}}
    \def\mbb#1{\mathbb{#1}}
    \def\mfk#1{\mathfrak{#1}}

    \def\bN{\mbb{N}}
    \def\bC{\mbb{C}}
    \def\bR{\mbb{R}}
    \def\bQ{\mbb{Q}}
    \def\bZ{\mbb{Z}}
    \newcommand{\f}[2]{\frac{#1}{#2}}
    \newcommand{\sinf}[1]{\sum_{n =#1}^{\infty}}
    \newcommand{\linf}[1]{\lim_{x \to #1}^{\infty}}
    \newcommand{\deriv}[1]{\f{d}{d#1}}
    \newcommand{\vecD}[2]{\begin{bmatrix} 
        #1 \\
        #2
        \end{bmatrix}}

    \newcommand{\vecT}[3]{\begin{bmatrix} 
        #1 \\
        #2 \\ 
        #3
        \end{bmatrix}}
    \newcommand{\st}[1]{\sin(\theta)}    
    \newcommand{\ct}[1]{\cos(\theta)} 
    \newcommand{\x}[0]{\cdot} 
    \newcommand{\tu}[1]{\textup{#1}} 
    \colorlet{r}{red}
    \colorlet{o}{orange}
    \colorlet{c}{cyan}
    \colorlet{l}{lime}
    \colorlet{m}{magenta}
    \colorlet{b}{blue}
    \colorlet{y}{yellow}
    \colorlet{w}{white}
    \colorlet{p}{pink}

    \usepackage{tikz}
    \usetikzlibrary{fadings}
    \usepackage{pgffor}

    \pgfdeclarehorizontalshading{rainbow}{100bp}{%
      rgb(0bp)=(1,0,0);
      rgb(26bp)=(1,0,0);
      rgb(33bp)=(1,.5,0);
      rgb(40bp)=(1,1,0);
      rgb(47bp)=(0,1,0);
      rgb(54bp)=(0,1,0.5);
      rgb(61bp)=(0,1,1);
      rgb(68bp)=(1,0,1);
      rgb(75bp)=(.5,0,.5);
      rgb(100bp)=(.5,0,.5)}

    \newcommand\snow[2][]{%
      \begin{tikzfadingfrompicture}[name = fading letter]
        \node[text = transparent!0, inner xsep = 0pt, outer xsep = 0pt] {#2};
      \end{tikzfadingfrompicture}%
      \begin{tikzpicture}[baseline = (textnode.base)]
        \node[inner sep = 0pt, outer sep = 1pt] (textnode) {\phantom{#2}}; 
        \shade[path fading = fading letter, fading text, #1, fit fading = false]
        (textnode.south west) rectangle (textnode.north east);% 
      \end{tikzpicture}% 
    }

    \tikzset{fading text/.style = {shading=rainbow}}""")


class ThreeFunc(MyThreeDScene):
    def construct(self):
        tex_init(self)

        self.camera.background_color = COL

        def func(u, v):
            return np.array([
                u,
                v,
                np.exp(-(u ** 2 + v ** 2))
            ])

        s = Surface(
            func,
            u_range=[-2, 2],
            v_range=[-2, 2]
        )
        s.set_fill_by_checkerboard(GREEN, GREEN_A)

        axes = ThreeDAxes()

        surface = VGroup(axes, s)

        # Group together axes and surface
        def create_prisms(n):
            prisms = []
            du = 4 / n
            dv = 4 / n

            for i in range(n):
                for j in range(n):
                    x = -2 + i * du
                    y = -2 + j * dv
                    z = func(x, y)[2]
                    p = Prism(dimensions=[du, dv, z])
                    p.set_color(MAROON)
                    p.move_to([x, y, z / 2])
                    prisms.append(p)
            return VGroup(*prisms)

        tex = MathTex("{{f(x,y)}} = {{ e^{-(x^2 + y^2)} }}", tex_template=self.stdtex).to_edge(UP, buff=0.4)
        tex[2].set_color(YELLOW)
        texN = MathTex(
            "{{ \\int_{-2}^2 \\int_{-2}^2 }} {{ f(x,y) \\, }} {{ \\tu{d}x \\, \\tu{d}y }} {{ \\approx \\sum_{i=0}^{n-1} \\sum_{j=0}^{m-1} f(x_i,y_j) \\Delta A }}",
            tex_template=self.stdtex)
        texN[0].set_color("#bfff00")

        texN[6].set_color(LIGHT_PINK)
        texN.to_edge(UP * 2).to_edge(UP, buff=0.4)
        self.set_camera_orientation(0.8 * np.pi / 2, -0.45 * np.pi)

        # self.add_fixed_in_frame_mobjects(tex)
        box = SurroundingRectangle(tex, color=YELLOW, buff=SMALL_BUFF)
        box2 = SurroundingRectangle(texN, color=YELLOW, buff=SMALL_BUFF)
        make_fixed(tex, texN, box, box2)
        self.prisms = create_prisms(2)
        total = VGroup(surface, self.prisms)
        total.scale(2)
        self.add(surface)
        self.set_camera_orientation(frame_center=[0, 0, 1])
        self.add(box)
        self.begin_ambient_camera_rotation()

        # Start off with 2 rects
        self.n_var = MathTex("{{ n = m = }}", 2).to_edge(DOWN, buff=0.4).to_edge(RIGHT)
        self.n_var[1].set_color(ORANGE)
        make_fixed(self.n_var)
        addRects = AnimationGroup(ApplyMethod(surface.set_opacity, 0.2), AnimationGroup(
            LaggedStart(*[Write(p) for p in self.prisms], ReplacementTransform(box, box2), Write(self.n_var),
                        TransformMatchingTex(tex, texN))), lag_ratio=1, run_time=3)
        self.play(addRects)
        self.add_fixed_in_frame_mobjects(texN)
        self.wait()

        colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK]

        def reRiemann(n):
            total.remove(self.prisms)
            total.scale(0.5)
            prismsnw = create_prisms(n)
            total.add(prismsnw)
            total.scale(2)
            n_var1 = MathTex("{{ n = m = }}", n).to_edge(DOWN, buff=0.4).to_edge(RIGHT)
            random_color = random.choice(colors)
            n_var1[1].set_color(random_color)
            make_fixed(n_var1)
            self.play(FadeTransform(self.prisms, prismsnw), TransformMatchingTex(self.n_var, n_var1))
            self.n_var = n_var1

        # Update the prisms within the total VGroup
        reRiemann(4)
        self.wait()
        reRiemann(8)
        self.wait()
        reRiemann(20)
        # self.wait()
        reRiemann(30)
        self.wait(3)
    #  self.move_camera()


class VF(Scene):
    def construct(self):
        tex_init(self)
        self.camera.background_color = COL
        npl = NumberPlane()

        t = ValueTracker(0)

        def func(pos, dt):
            return np.sin(pos[1] + dt) * RIGHT + np.cos(pos[0] + dt) * UP

        vector_field = always_redraw(
            lambda: ArrowVectorField(lambda pos: func(pos, t.get_value())).scale(2)
        )

        mtx = MathTex(r"f: {{ \mathbb{R}^2 \to \mathbb{R}^2 }}").to_edge(UP, buff=0.4)
        mtx[1].set_color(ORANGE)
        box = SurroundingRectangle(mtx, color=WHITE, buff=SMALL_BUFF).set_fill(color=BLACK, opacity=1)
        self.play(Create(npl), Write(vector_field), Create(box), Write(mtx))
        self.play(t.animate.set_value(2 * PI), run_time=5, rate_func=rate_functions.ease_in_out_cubic)
        self.wait()


class PictureScene(ThreeDScene):
    def construct(self):
        # Number plane
        npl = NumberPlane()

        # Vectors
        vector_1 = Vector([2, 1]).set_color(YELLOW)
        vector_2 = Vector([3, -1]).set_color("#AFEEEE")

        # Angle indicator
        angle = Angle(vector_2, vector_1, radius=0.5, color=RED)
        theta_label = MathTex("\\theta").next_to(angle, RIGHT, buff=0.12).set_color("#da70d6")

        # Projection
        vector_1_np = np.array([2, 1, 0])
        vector_2_np = np.array([3, -1, 0])
        dot_product = np.dot(vector_1_np, vector_2_np)
        magnitude_squared = np.dot(vector_2_np, vector_2_np)
        projection = (dot_product / magnitude_squared) * vector_2_np
        projection_vector = Vector(projection).set_color(ORANGE)

        # Dashed Line
        dashed_line = DashedLine(vector_1.get_end(), projection_vector.get_end(), dash_length=0.1).set_color(GRAY)

        # Labels
        a_label = MathTex(r"\vec{a}").next_to(vector_1.get_end(), UP,buff=0.2).set_color(YELLOW)
        b_label = MathTex(r"\vec{b}").next_to(vector_2.get_end(), RIGHT,buff=0.2).set_color("#AFEEEE")

        # Projection label
        proj_label_text = "\\text{proj}_{\\vec{b}} \\vec{a}"
        angle_of_projection = np.arctan2(projection[1], projection[0])
        proj_label = MathTex(proj_label_text).next_to(projection_vector, DOWN, buff=-0.1).rotate(
            angle_of_projection).set_color(ORANGE)

        # Group and scale
        v = VGroup(npl, vector_1, vector_2, projection_vector, dashed_line, angle, theta_label, a_label, b_label,
                   proj_label)
        v.scale(1.5)

        # Add to scene
        self.add(v)


class CrossProductScene(ThreeDScene):
    def construct(self):
        # Set the camera position
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        # Create the 3D axes
        axes = ThreeDAxes()

        # Create the first vector (lime color)
        vec1 = Arrow3D(start=[0, 0, 0], end=[0.75, 1.5, 0], color="#32CD32")
        vec1_label = MathTex("\\vec{a}").set_color("#32CD32")
        vec1_label.next_to(vec1.get_end(), direction=DOWN+RIGHT,buff=0.3)

        # Create the second vector (pink color)
        vec2 = Arrow3D(start=[0, 0, 0], end=[1, 1, 2], color=PINK)
        vec2_label = MathTex("\\vec{b}").set_color(PINK)
        vec2_label.next_to(vec2.get_end(), direction=UP+LEFT,buff=0.6)

        # Calculate the cross product of the two vectors
        cross_product = np.cross([0.75, 1.5, 0], [1, 1, 2])
        vec3 = Arrow3D(start=[0, 0, 0], end=cross_product, color=ORANGE)
        vec3_label = MathTex("\\vec{a} \\times \\vec{b}").set_color(ORANGE)
        vec3_label.next_to(vec3.get_end(), direction=RIGHT)

        # Create a plane spanned by vec1 and vec2
        plane = Polygon([0, 0, 0], vec1.get_end(), vec1.get_end() + vec2.get_end(), vec2.get_end(), color=BLUE)
        plane.set_opacity(0.4)  # Set the transparency

        # Add the plane first so it's in the background
        self.add(axes, plane, vec1, vec2, vec3)

        # Add text labels with fixed orientation in 3D space
        self.add_fixed_orientation_mobjects(vec1_label, vec2_label, vec3_label)