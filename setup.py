from setuptools import setup, find_packages


try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""


setup(
    name="pripple",
    version="0.1.0",
    author="TartAI Inc",
    author_email="dev@tart.ai.kr",
    description="Ripple wrapper for RWA and Payments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prap-team/pripple",
    project_urls={
        "Bug Tracker": "https://github.com/prap-team/pripple/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "xrpl-py",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-mock>"
        ]
    },
    include_package_data=True,
)

