""" Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="treescript-files",
    version="0.2.3",
    description="Obtains the relative path of all files in the TreeScript.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="DK96-OS",
    url="https://github.com/DK96-OS/treescript-files/",
    project_urls={
        "Issues": "https://github.com/DK96-OS/treescript-files/issues",
        "Source Code": "https://github.com/DK96-OS/treescript-files/"
    },
    license="GPLv3",
    packages=find_packages(exclude=['test', 'test.*']),
    entry_points={
        'console_scripts': [
            'treescript-files=treescript_files.__main__:main',
            'treescript_files=treescript_files.__main__:main',
        ],
    },
    python_requires='>=3.9',
    keywords=['treescript'],
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
