import kagglehub

# Download latest version
path = kagglehub.dataset_download("greenwing1985/housepricing")

print("Path to dataset files:", path)