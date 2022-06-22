from manim import *

#NEWTON METHOD
class Tester(Scene):
    def construct(self):

        def f(x):
            return -(x-1)*(x+1)

        def df(x):
            return -2 * x

        def newton_f(x):
            return x - (f(x)/df(x))
            pass

        def iterate(p, d, speed, func, dfunc, newton_func):
            #Draw Line
            a = [k.get_value()- (newton_func(k.get_value())-k.get_value()), 2*func(k.get_value())]
            mid = [k.get_value(), func(k.get_value())]
            b = [newton_func(k.get_value()),0]

            l= Line(ax.coords_to_point(a[0],a[1]), ax.coords_to_point(b[0],b[1]))
            l2= Line(ax.coords_to_point(mid[0],mid[1]), ax.coords_to_point(b[0],b[1]))
            l3 = DashedLine(ax.coords_to_point(b[0],b[1]), ax.coords_to_point(b[0],func(b[0])), dashed_ratio=0.5)
            l4 = Line(ax.coords_to_point(b[0],b[1]), ax.coords_to_point(b[0],func(b[0])))
            self.play(Create(l), run_time = 1/speed)
            self.wait(0.5/speed)
            #Move Point To Next Iteration
            self.play(k.animate.set_value(b[0]), MoveAlongPath(d, l2), run_time=1/speed)

            #Move Point Down
            self.play(Write(l3), run_time = 0.5/speed)
            self.play(MoveAlongPath(d,l4))

            #Remove Lines
            self.play(FadeOut(l), FadeOut(l3), run_time = 0.5/speed)
            self.wait(0.5/speed)
            #

        k = ValueTracker(0.4)


        #xn = DecimalNumber().set_value(k.get_value())

        text = MathTex(r"f(x) = -x^2+1").shift(3*RIGHT+3*UP)
        ax = Axes(x_range=(-1,3),y_range=(-1,2)).add_coordinates()

        iteration = MathTex(r"x_n=").shift(3*RIGHT+2*UP)
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False,
            color=GREEN
        )
        decimal.add_updater(lambda d: d.next_to(iteration, RIGHT))
        decimal.add_updater(lambda d: d.set_value(k.get_value()))

        iteration.set_color_by_tex("x", GREEN)

        #DOT
        dot = Dot(ax.coords_to_point( k.get_value(), f(k.get_value())), color=GREEN)

        func = ax.plot(lambda x:f(x), color=BLUE, x_range=[-1,1.5])


        self.play(Write(ax), Write(func), Write(text), Write(iteration), Write(dot), Write(decimal))

        self.wait(1)

        #iterate
        iterate(k.get_value(), dot, 1, f, df, newton_f)
        iterate(k.get_value(), dot, 2, f, df, newton_f)
        iterate(k.get_value(), dot, 2, f, df, newton_f)
        #hi

        #self.play(Create(l))
        self.wait(1)


        # ANIMATE RANDO
        #self.play(k.animate.set_value(b[0]), run_time=1.5)


        self.wait(1)
        self.wait(2)
