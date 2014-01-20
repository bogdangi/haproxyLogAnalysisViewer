from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='haproxyLogAnalysisViewer',
      version=version,
      description="The haproxy log analysis viewer",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='haproxy log analysis viewer',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='girman.in.ua',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
