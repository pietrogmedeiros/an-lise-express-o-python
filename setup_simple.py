#!/usr/bin/env python3
"""
Setup simplificado para o sistema de detecção facial
"""

from setuptools import setup

setup(
    name="detector-facial-simples",
    version="2.0.0",
    description="Sistema simples de detecção facial sem dependências complexas",
    author="Seu Nome",
    python_requires=">=3.6",
    install_requires=[
        "opencv-python>=4.5.0",
    ],
    py_modules=["detector_simples", "run_simple", "instalar_opencv"],
    entry_points={
        'console_scripts': [
            'detector-facial=detector_simples:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Multimedia :: Video :: Capture",
    ],
)
