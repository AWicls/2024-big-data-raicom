import kagglehub

# Download latest version
path = kagglehub.dataset_download("pablomgomez21/drugs-a-b-c-x-y-for-decision-trees")

print("Path to dataset files:", path)
