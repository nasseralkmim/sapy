from setuptools import setup

setup(name='sapy',
      version='0.1',
      description='matrix structural analysis',
      url='nasseralkmim.github.io',
      author='Nasser Alkmim',
      author_email='nasser.alkmim@gmail.com',
      license='MIT',
      packages=['sapy'],
      install_requires=[
          'numpy',
          'matplotlib',
          'networkx',
          'scipy'
      ],
      zip_safe=False)
