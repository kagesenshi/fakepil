from setuptools import setup, find_packages
import os

version = '1.1.7'

setup(name='PIL',
      version=version,
      description="Fake PIL",
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='WTFPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Pillow',
      ],
      entry_points='',
)
