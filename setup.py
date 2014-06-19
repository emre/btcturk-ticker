from setuptools import setup

setup(
    name='btcturk-ticker',
    version='0.1',
    packages=['btcturk_ticker'],
    url='http://github.com/emre/btcturk-ticker',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='btcturk ticker',
    entry_points={
        'console_scripts': [
            'btcturk = btcturk_ticker.ticker:main',
        ],
    },
    install_requires=[
        'requests',
    ],
)
