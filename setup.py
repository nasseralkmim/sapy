from setuptools import setup

setup(name='sapy',
      version='0.1',
      description='matrix structural analysis',
      author='Nasser Alkmim',
      author_email='nasser.alkmim@gmail.com',
      url='https://github.com/nasseralkmim/sapy',
      download_url='https://github.com/nasseralkmim/sapy/releases/tag/0.1',
      license='MIT',
      packages=['sapy'],
      install_requires=[
          'numpy',
          'matplotlib'],
      zip_safe=False)
