from distutils.core import setup


with open('README.rst') as file:
    long_description = file.read()


setup(name='libgravatar',
      version='0.2.1',
      author='Pablo SEMINARIO',
      author_email='pabluk@gmail.com',
      url='https://github.com/pabluk/libgravatar',
      license='GNU General Public License v3 (GPLv3)',
      description='A library that provides a Python 3 interface for the Gravatar API.',
      long_description=long_description,
      packages=['libgravatar'],
      provides=['libgravatar (0.2.1)'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
      ],
)
