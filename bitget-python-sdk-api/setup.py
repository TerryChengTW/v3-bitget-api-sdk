from setuptools import setup, find_packages

setup(
    name='bitget_sdk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests', 'websocket-client'],
    description='Official Bitget SDK from cloned repo',
    author='TerryChengTW',
    author_email='terrydev.tw@gmail.com',
    url='https://github.com/TerryChengTW/v3-bitget-api-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
