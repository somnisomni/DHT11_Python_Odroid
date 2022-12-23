from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dht11-odroid",
    version="0.1.0",
    author="somni",
    author_email="me@somni.one",
    description="Pure Python library for reading DHT11 sensor on ODROID (based on 'szazo/DHT11_Python' and 'unims77/odroid_c1_dht11')",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/somnisomni/DHT11_Python_Odroid",
    packages=find_packages(),
    install_requires=["odroid-wiringpi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
