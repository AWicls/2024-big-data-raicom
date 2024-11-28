import kagglehub

# Download latest version
path = kagglehub.dataset_download("meeraajayakumar/spotify-user-behavior-dataset")

print("Path to dataset files:", path)