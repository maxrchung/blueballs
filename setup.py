from cx_Freeze import setup, Executable



setup(name = 'BlueBalls', 
      version='2', 
      description='',
      executables = [Executable('BlueBalls.py',base="WIN32GUI")])
