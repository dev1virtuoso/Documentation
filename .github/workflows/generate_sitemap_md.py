import os

def generate_sitemap_md(directory, md_file):
    with open(md_file, 'w') as file:
        file.write("# Site Map\n\n")
        for root, _, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.relpath(os.path.join(root, file_name), directory)
                file_path = file_path.replace("\\", "/")
                file.write(f"- [{file_path}]({file_path})\n")

repository_directory = "."
sitemap_file_name = "sitemap.md"

generate_sitemap_md(repository_directory, sitemap_file_name)
