from setuptools import setup, find_packages


setup(
    name="pripple",
    version="0.1.0",
    author="TartAI Inc",
    author_email="dev@tart.ai.kr",
    description="Ripple wrapper for RWA and Payments",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prap-team/pripple",
    project_urls={
        "Bug Tracker": "https://github.com/prap-team/pripple/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 다른 라이선스 사용 가능
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
    ],
)
