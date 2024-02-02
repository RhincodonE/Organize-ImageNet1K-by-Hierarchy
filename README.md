# Organize-ImageNet1K-by-Hierarchy# Build_hierarchy.py

## Prerequisites
Before running `Build_hierarchy.py`, ensure you have the following installed:
- Python 3.x
- NLTK (Natural Language Toolkit)
- WordNet dataset for NLTK
- Plotly library

You can install NLTK and download the WordNet dataset by running:

pip install nltk

python -c "import nltk; nltk.download('wordnet')"


## Build_hierarchy.py
`Build_hierarchy.py` is a Python script designed to extract images from `.tar` files and organize them into a structured hierarchy based on WordNet synsets. It creates a directory structure that reflects the hypernym paths (categorization hierarchy) of each image's synset ID, facilitating organized storage and easy retrieval of images based on their semantic relationships.


### Usage
To use 'Build_hierarchy.py', you need to provide two arguments:

"tar_files_dir": The directory containing the .tar files. Basically, it is the folder where you store the extracted Imagenet.tar. In the directory, there will be 1000 tar files looks like "synid.tar". You can download the Imagenet dataset at https://www.image-net.org/

"base_dir": The base directory where the extracted images will be organized and stored.

### Command
Run the script from the command line as follows:
python Build_hierarchy.py <tar_files_dir> <base_dir>

This command will extract images from .tar files located in "./ILSVRC2012_img_train" and organize them into a structured hierarchy within "./Imgs".

### How It Works
1.The script reads .tar files from the specified tar_files_dir.

2.For each .tar file, it extracts the synset ID from the file name.

3.It queries the WordNet database to determine the hypernym path for each synset ID.

4.Based on the hypernym paths, it creates a nested directory structure within base_dir.

5.It extracts the images from each .tar file into their corresponding directory in the hierarchy.

## Visualize_hierarchy.py

### Usage
To visualize a directory hierarchy, you need run the previous script to build hierarchy first and then, provide one argument:

"root_dir": The root directory for building the hierarchy visualization.

### Command
Run the script from the command line as follows:

python visualize_hierarchy.py <root_dir>

### Example

python visualize_hierarchy.py ./MyDirectory

This command will generate an interactive treemap visualization for the directory hierarchy starting from ./MyDirectory.

### How it works

1.The script recursively explores the directory structure starting from the specified root_dir.

2.It collects information about directories and subdirectories, including their names and relationships.

3.Using the Plotly library, it creates an interactive treemap visualization, where each rectangle represents a directory, and its size reflects the number of files and subdirectories it contains.

4.You can interact with the treemap by zooming in/out, hovering over rectangles for details, and exploring the directory structure interactively.

