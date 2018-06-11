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
      classifiers=[
          'Development Status :: 1 - Development/Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='https://github.com/pythonguru101/fraction-chart/',
)
