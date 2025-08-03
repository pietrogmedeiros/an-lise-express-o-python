from setuptools import setup, find_packages

setup(
    name="emotion-analyzer",
    version="1.0.0",
    description="Sistema de análise de expressões faciais para monitoramento de bem-estar",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.8.0",
        "tensorflow>=2.13.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "streamlit>=1.25.0",
        "plotly>=5.15.0",
        "scikit-learn>=1.3.0",
        "pillow>=10.0.0",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'emotion-analyzer=main:main',
        ],
    },
)