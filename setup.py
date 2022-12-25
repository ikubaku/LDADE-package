from setuptools import setup, find_packages


setup(
    name='LDADE',

    # TODO: NEED TO BE CHANGED LATER
    version='2022.10.25',

    author='Amritanshu Agrawal',
    author_email='aagrawa8@ncsu.edu',

    # TODO: NEED TO BE CHANGED LATER
    url='https://github.com/tonyfloatersu/LDADE-python-package',
    license='MIT',
    include_package_data=True,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    packages=find_packages(),
    package_dir={'LDADE': 'LDADE'},
    package_data={'LDADE': ['data/*']},

    python_requires='>=3.7',
    install_requires=["numpy", "scikit-learn"]
)
