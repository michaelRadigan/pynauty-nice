import os
from setuptools import setup, Extension
from setuptools.command.install import install as Install
import glob
from subprocess import check_call, check_output


# Note that the original module name is pynauty, we're going to distibute this as pynauty-nice
# mainly in the interest of not accidentally stepping on anyone's toes
MODULENAME = 'pynauty-nice'
MODULE='pynauty'



VERSION = '0.1.6'

description = 'Automorphism and isomorphism of graphs'
long_description = '''
Package for testing isomorphism of graphs and computing their automorphism group. 

pynauty-nice is a pynauty fork in an effort to ease installation. Pynauty is a python wrapper around nauty, distributed under the GNU GPLv3. Nauty is an isomorphism finder, written in C, distributed under the APACHE 2.0 licence. Previously, the two would have to be dowloaded separately from their respective websites, unpacked, built and symbolically linked. Given that that in this direction the licences are compatible and allow it, I've decided to redistribute them together.

There is no change to the underlying pynauty package, written by Peter Dobsan: pdobsan@gmail.com.

I've put myself down as the author of pynauty-nice, despite not being the author of pynauty, please get in contact if you think that this is wrong.
Contact me at michael@radigan.co.uk.
'''
author = 'Michael Radigan'
author_email = 'michael@radigan.co.uk'
url = 'https://github.com/michaelRadigan/pynauty-nice'
license = 'GNU General Public License v3'
platforms = ['Linux', 'Unix', 'OS X']
classifiers = [
    'Environment :: Console',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: C',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
]

pynauty_dir = 'src'
package_dir = {MODULE: pynauty_dir}
packages = [MODULE]

install_requires = []
real_path = os.path.dirname(os.path.realpath(__file__))

scripts=['Makefile']
nautypath = os.path.join(real_path, 'nauty')

data_files= [
    (nautypath, [file for file in glob.iglob('nauty/*')]),
    (real_path, [file for file in glob.iglob('pynauty/*')]),
]


def pre():
    check_call('./nauty/configure')
    check_call(['make', '-C', nautypath])

class MyInstall(Install):
    def run(self):
        pre()
        Install.run(self)

nauty_dir = 'nauty'  # nauty's source directory
if not os.access(nauty_dir, os.R_OK | os.X_OK):
    print("Can't find nauty_dir: %s" % nauty_dir)
    raise SystemExit(1)

ext_pynauty = Extension(
    name=MODULE + '.nautywrap',
    sources=[pynauty_dir + '/' + 'nautywrap.c'],
    extra_compile_args=['-O4', '-fPIC'],
    extra_objects=[nauty_dir + '/' + 'nauty.o',
                   nauty_dir + '/' + 'nautil.o',
                   nauty_dir + '/' + 'naugraph.o',
                   nauty_dir + '/' + 'schreier.o',
                   nauty_dir + '/' + 'naurng.o'
                   ],
    include_dirs=[nauty_dir, pynauty_dir]
)
ext_modules = [ext_pynauty]

setup(name=MODULENAME,
      version=VERSION,
      description=description, 
      long_description=long_description,
      author=author, 
      author_email=author_email, 
      url=url,
      platforms=platforms,
      license=license,
      package_dir=package_dir,
      packages=packages,
      scripts=scripts,
      data_files=data_files,
      ext_modules=ext_modules,
      classifiers=classifiers,
      cmdclass={
        'install': MyInstall,
      },
      )
      