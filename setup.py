from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

description = 'The haproxy log analysis viewer'

long_description = """{0}
{1}


LICENSE
=======

{2}
""".format(
    open('README.rst').read(),
    open('CHANGES.rst').read(),
    open('LICENSE').read(),
)

setup(name='haproxyLogAnalysisViewer',
      version=version,
      description=description,
      long_description=long_description,
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='haproxy log analysis viewer',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='girman.in.ua',
      license='GPL v3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'haproxy_log_analysis',
          'tornado',
      ],
      entry_points={
          'console_scripts': [
              'haproxyLogAnalysisViewer = haproxyloganalysisviewer.main:console_script',
              ],
          },
      )
