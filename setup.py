from setuptools import setup

setup(name='jupyter_MyVBScript_kernel',
      version='0.0.1',
      description='Minimalistic vbscript kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyVBScript-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyVBScript-kernel/tarball/0.0.1',
      packages=['jupyter_MyVBScript_kernel'],
      scripts=['jupyter_MyVBScript_kernel/install_MyVBScript_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'wscript','cscript','VBScript','JScript'],
      include_package_data=True
      )
