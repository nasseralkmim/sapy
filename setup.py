from setuptools import setup

setup(name='sapy',
      version='0.1',
      description='matrix structural analysis',
      author='Nasser Alkmim',
      author_email='nasser.alkmim@gmail.com',
      url='https://github.com/nasseralkmim/sapy',
      license='MIT',
      packages=['sapy'],
      install_requires=[
          'numpy',
          'matplotlib'],
      zip_safe=False)
