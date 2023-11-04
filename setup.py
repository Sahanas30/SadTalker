from setuptools import setup

setup(
    name='SadTalker',
    version='0.1.0',
    description='SadTalker API',
    author='Cedro3',
    author_email='cedro3@gmail.com',
    packages=['SadTalker'],
    install_requires=[
        'torch==1.12.1+cu113',
        'torchvision==0.13.1+cu113',
        'torchaudio==0.12.1',
    ]
)
