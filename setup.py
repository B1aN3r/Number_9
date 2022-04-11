from setuptools import setup

setup(
    name="click-example-complex",
    version="1.0",
    py_modules=['main'],
    install_requires=[
        'Click',
        'datetime',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts':[
        'pizda=main:cli'
      ]
    },
)