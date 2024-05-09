import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["tkinter", "PIL", "PIL.ImageTk", "PIL.Image", "PIL.ImageFile", "os"]
include_files = []

setup(
    name="Bryan's Image Converter",
    version="1.0",
    description="A simple image converter",
    options={
        "build_exe": {
            "includes": includes,
            "include_files": include_files,
        }
    },
    executables=[Executable("main.py", base=base)],
)