from setuptools import setup, find_packages

setup(
    name="sysinfo",
    version="1.0.0",
    author="Alejandro",
    url="https://github.com/toncode-git/sysinfo",
    description="Interactive program that interacts with the OS",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "sysinfo=sysinfo.path:main"
        ]
    },
    python_requires=">=3.8"
)