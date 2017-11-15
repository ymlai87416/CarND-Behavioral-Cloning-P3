from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\ymlai\Anaconda3\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ymlai\Anaconda3\tcl\tk8.6"
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = ["IPython", "tcl", "tk", "sqlite3", "ipykernel", "jupyter_client", "jupyter_core", "pydoc_data", "tkinter", "ipython_genutils", "ipywidgets"],
    includes = ["atexit", 'numpy.core._methods', 'numpy.lib.format', "pygments.lexers.python", "pygments.formatters.html", "sip"],
    include_files = [
        r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\1033\mkl_msg.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\libimalloc.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_avx.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_avx2.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_avx512.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_avx512_mic.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_ilp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_intelmpi_ilp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_intelmpi_lp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_lp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_mpich2_ilp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_mpich2_lp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_msmpi_ilp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_blacs_msmpi_lp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_cdft_core.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_core.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_def.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_intel_thread.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_mc.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_mc3.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_pgi_thread.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_rt.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_scalapack_ilp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_scalapack_lp64.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_sequential.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_tbb_thread.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_avx.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_avx2.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_avx512.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_avx512_mic.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_cmpt.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_def.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_mc.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_mc2.dll",
    r"C:\Users\ymlai\Anaconda3\pkgs\mkl-2017.0.4-h6d528fc_0\Library\bin\mkl_vml_mc3.dll",
    r"C:\Users\ymlai\Anaconda3\Library\bin\libjpeg.dll",
    r"C:\Users\ymlai\Anaconda3\Library\bin\libiomp5md.dll"
    ]
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(r'C:\GitProjects\CarND-Behavioral-Cloning-P3\train_data_editor\main.py', base=base, targetName = 'trainsetEditor.exe')
]

setup(name='self driving - behavior cloning train set editor',
      version = '1.0',
      description = 'self driving - behavior cloning train set editor',
      options = dict(build_exe = buildOptions),
      executables = executables)
