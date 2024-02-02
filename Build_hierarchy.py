import os
import glob
import argparse
from nltk.corpus import wordnet as wn
import nltk



def extract_and_place(synset_id, base_directory, tar_files_dir):
    # Get the synset from the synset ID
    synset = wn.synset_from_pos_and_offset('n', int(synset_id[1:]))

    # Get the hierarchy of the synset (hypernyms) and reverse it
    hierarchy = synset.hypernym_paths()[0]

    # Extract the folder names from the synsets
    path_components = [h.lemmas()[0].name() for h in hierarchy]

    # Construct the folder path
    folder_path = os.path.join(base_directory, *path_components)

    # Create the folder if it does not exist
    os.makedirs(folder_path, exist_ok=True)

    # Extract the tar file to the folder
    tar_file_path = os.path.join(tar_files_dir, f"{synset_id}.tar")
    os.system(f"tar -xf {tar_file_path} -C {folder_path}")

def main(tar_files_dir, base_dir):
    # Create the base directory if it does not exist
    os.makedirs(base_dir, exist_ok=True)

    # Assuming you have a list of synset IDs from the image names
    for tar_file in glob.glob(os.path.join(tar_files_dir, '*.tar')):
        # Extract the synset ID from the tar file name
        synset_id = os.path.basename(tar_file).split('.')[0]
        extract_and_place(synset_id, base_dir, tar_files_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract images into a structured hierarchy based on WordNet synsets.')
    parser.add_argument('tar_files_dir', type=str, help='Directory containing the tar files')
    parser.add_argument('base_dir', type=str, help='Base directory where the extracted images will be stored')

    args = parser.parse_args()

    nltk.download('wordnet')

    main(args.tar_files_dir, args.base_dir)
