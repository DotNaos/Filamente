from manim import *  # or: from manimlib import *

from manim_slides import *
import numpy as np

myChemTemplate = TexTemplate(
                    tex_compiler="latex",
                    output_format='.dvi',
                    preamble=r"""
                        \usepackage{amsmath}
                        \usepackage{amssymb}
                        \usepackage{chemfig}
                        \setchemfig{atom sep=2em,angle increment=45,bond offset=2pt,double bond sep=2pt}
                    """
                    )

l_lactid_tex = '\chemfig{[:-30]HO-(<[:210]H)(<:[:-40]CH_{3})-[:30](=[2]O)(-[:-30]OH)}'
d_lactid_tex = '\chemfig{[:-30]HO-(<[:210]H_{3}C)(<:[:-40]H)-[:30](=[2]O)(-[:-30]OH)}'

IMG_HEIGHT = 5.5

class Filamente(Scene):
    def construct(self):
        # self.intro()
        # self.production()
        # self.extrusion()
        # self.recycling()
        self.lactid_acid()

    def next_page(self):
        self.next_slide()
        self.remove(*self.mobjects)

    def next_slide(self):
        pass

    def intro(self):
        # Title
        title = Tex(
            "Filamente")

        self.wait(1)

        self.play(Write(title))

        self.next_page()

        # 3D printing visualization
        height = 2
        layerheight = 0.2

        for i in range(0, int(height/layerheight)):
            layer = RoundedRectangle(height=layerheight, width=2, color=WHITE, corner_radius=0.1).shift(UP*layerheight*i - UP*height/2 + UP*layerheight/2)

            self.play(Write(layer), run_time=0.2)


        self.next_page()

        # Image of 3D printers
        fdm = ImageMobject("img/fdm.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add((fdm))
        self.wait()
        self.next_page()

        sla = ImageMobject("img/sla.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add((sla))
        self.wait()
        self.next_page()

        sls = ImageMobject("img/sls.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add((sls))
        self.wait()
        self.next_page()


    def production(self):
        # background white
        self.camera.background_color = WHITE
        raw = ImageMobject("img/PLA-Pellets.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add((raw))
        self.next_slide()

        # Addition of additives visualization

        # Bounds of points
        bounds = np.array([[-2, 2], [-2, 2]])

        # Generate random points
        count = 30

        points = np.random.rand(count, 3)
        for p in points:
            p[0] = p[0] * (bounds[0][1] - bounds[0][0]) + bounds[0][0]
            p[1] = p[1] * (bounds[1][1] - bounds[1][0]) + bounds[1][0]
            p[2] = 1

        # Generate random colors\
        colors = np.random.rand(count, 3)

        sizes = np.random.rand(count) * 0.1 + 0.05

        self.wait(1)

        # Show points
        for i in range(count):
            self.add(Dot(point=points[i], color=colors[i], radius=sizes[i]))
            self.wait(0.05)


        self.next_page()

        # Show not dried filament
        wet = ImageMobject("img/wet_filament.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add((wet))

        self.next_page()

    def extrusion(self):
        # Schema of extrusion
        extrusion = ImageMobject("img/Production.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add(extrusion)
        self.next_page()


        # Curling filament
        curling = ImageMobject("img/curling.jpg").scale_to_fit_height(IMG_HEIGHT)
        self.add(curling)
        self.next_page()


        extruder = ImageMobject("img/extruder.jpg").scale_to_fit_height(IMG_HEIGHT)
        cooling = ImageMobject("img/cooling.jpg").scale_to_fit_height(IMG_HEIGHT)

        group = Group(extruder, cooling)

        group.arrange(RIGHT, buff=0.5)

        self.add(group)

        self.next_page()

        coil = ImageMobject("img/coil.jpeg").scale_to_fit_width(7)
        quality = ImageMobject("img/quality.jpg").scale_to_fit_width(7)

        group2 = Group(coil, quality)

        group2.arrange(RIGHT, buff=0.5)

        self.add(group2)

        self.next_page()

    def recycling(self):
        # PET bottles
        pet = ImageMobject("img/pet.png").scale_to_fit_height(IMG_HEIGHT)
        self.add(pet)

        self.next_page()


    def attributes(self):
        pass

    def filaments(self):
        pass


    def lactid_acid(self):
        l_lactid = Tex(
            l_lactid_tex,
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        d_lactid = Tex(
            d_lactid_tex,
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        caption = Tex(
                "Lactic acid"
        ).next_to(l_lactid, DOWN)

        if 0:
            self.play(Write(l_lactid))
            self.play(Write(caption))
            self.wait()
        else:
            self.add(l_lactid)
            self.add(caption)
            self.wait()




        self.play(FadeOut(caption), run_time=1)
        self.play(Transform(l_lactid, d_lactid), run_time=3)
        self.wait()
        self.add(d_lactid)
        self.remove(l_lactid)

        # move to the right
        self.play(ApplyMethod(d_lactid.shift, RIGHT*3), run_time=1)

        l_lactid = Tex(
            l_lactid_tex,
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        # add lactic acid on the left
        self.play(Write(l_lactid.shift(LEFT*3)), run_time=1)

        l_caption = Tex(
            "L-lactic acid"
        ).next_to(l_lactid, DOWN)

        d_caption = Tex(
            "D-lactic acid"
        ).next_to(d_lactid, DOWN)

        self.play(Write(l_caption), Write(d_caption))

        self.wait(1)

    def polymerization(self):
        pass

