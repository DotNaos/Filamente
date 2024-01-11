from manim import *
from mol2chemfigPy3 import mol2chemfig

myChemTemplate = TexTemplate(
                    tex_compiler="latex",
                    output_format='.dvi',
                    preamble=r"""
                        \usepackage{amsmath}
                        \usepackage{amssymb}
                        \usepackage{chemfig}
                        \usepackage{mol2chemfig}
                        \setchemfig{atom sep=2em,angle increment=45,bond offset=2pt,double bond sep=2pt}
                    """
                    )

class kadir(Scene):
    def construct(self):

        a = mol2chemfig('CN1C=NC2=C1C(=O)N(C(=O)N2C)C', inline=True, aromatic=False)

        chem = Tex(
            a,
            tex_template=myChemTemplate
        ).set_stroke(width=3)

        self.play(Write(chem))
        self.wait()
