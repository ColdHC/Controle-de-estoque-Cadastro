import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("contro.py", base=base)
]

buildOptions = dict(
        packages = ["PyQt5"],
        includes = [],
        include_files = ["650x5000px.png","Rockwell.ttc","31x41px PDF Ícon_Prancheta 1 (1).png","241x411Px.png","498x600px.png","787x826px (1).png","795x233px.png","879x826px.png","1000x1000px.png","cadastro.ui","ÍCONE-96x96px.ico","listar_dados.ui","Logo wild BRANCA.png","Logo Wild haze Vapes-01 (1).png","Logo wild PRETA.png","menu_editar.ui","pdfsalvo.ui"],
        excludes = []
)




setup(
    name = "contro",
    version = "1.9",
    description = "",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
