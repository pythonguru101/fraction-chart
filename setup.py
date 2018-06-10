# coding: utf-8
import setuptools


setuptools.setup(
      name='fraction-chart',
      version='0.1',
      description='Push plot chart to fraction site',
      author="Fraction", author_email="pythonguru101@gmail.com",
      license="MIT",
      zip_safe=False,
      platforms='any',
      py_modules=['fraction_chart'],
      include_package_data=True,
      install_requires=[
            'requests',
      ],
      url='https://github.com/pythonguru101/fraction-chart/',
)
