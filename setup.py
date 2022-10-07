import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipath",
    version="0.0.2",
    author="daohu527",
    author_email="daohu527@gmail.com",
    description="Apollo path and simple map making tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daohu527/ipath",
    project_urls={
        "Bug Tracker": "https://github.com/daohu527/ipath/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=[
        'protobuf',
        'matplotlib',
        'record_msg',
    ],
    entry_points={
        'console_scripts': [
            'ipath = ipath.main:main',
        ],
    },
    python_requires=">=3.6",
)
