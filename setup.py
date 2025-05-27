from pathlib import Path
import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-fill-in-blanks",  # Pip package name
    version="0.1.0",  # Initial version
    author="Your Name",  # Your Name
    author_email="your.email@example.com",  # Your Email
    description="Streamlit component for fill-in-the-blanks exercises",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/streamlit-fill-in-blanks",  # Optional: Your repo URL
    packages=setuptools.find_packages(),  # Should find 'fill_in_blanks_component'
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",  # Updated to a more modern Python
    install_requires=[
        "streamlit >= 1.0",  # Updated to a more modern Streamlit
        # Add other Python dependencies here if your component's Python side needs them
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",  # Or newer
            "playwright==1.48.0",  # Or newer
            "requests==2.31.0",  # Or newer
            "pytest-playwright-snapshot==1.0",  # Or newer
            "pytest-rerunfailures==12.0",  # Or newer
        ]
    },
)
