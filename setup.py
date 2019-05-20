from setuptools import setup, find_packages

setup(name="catalog_restful_api",
      packages=find_packages(),
      install_requires=[
          'flask',
      ],
      extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    })