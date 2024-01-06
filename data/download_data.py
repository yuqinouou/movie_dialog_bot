import os
import urllib.request

# URL for downloading the dataset
URL = "http://www.cs.cornell.edu/~cristian/data/cornell_movie_dialogs_corpus.zip"

# Function to download and extract the dataset
def download_dataset():
    # Create a directory to store the dataset
    os.makedirs("cornell_movie_dialogs_corpus", exist_ok=True)

    # Download the dataset zip file
    print("Downloading the Cornell Movie Dialogs Corpus dataset...")
    urllib.request.urlretrieve(URL, "cornell_movie_dialogs_corpus.zip")

    # Extract the dataset
    print("Extracting the dataset...")
    import zipfile
    with zipfile.ZipFile("cornell_movie_dialogs_corpus.zip", "r") as zip_ref:
        zip_ref.extractall("./")

    print("Dataset downloaded and extracted successfully!")

# Run the script
if __name__ == "__main__":
    download_dataset()