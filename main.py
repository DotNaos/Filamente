from manim import *
from manim_slides import *


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

class Filamente(Slide):
    def construct(self):
        self.play(Write(Tex("Filamente")))

        self.lactid()



    def lactid(self):
        l_lactid = Tex(
            l_lactid_tex,
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        d_lactid = Tex(
            d_lactid_tex,
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        self.play(Write(l_lactid))
        self.wait()
        self.play(Transform(l_lactid, d_lactid), run_time=2)
