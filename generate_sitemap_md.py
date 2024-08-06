import os

def generate_sitemap_md(directory, md_file):
    with open(md_file, 'w') as file:
        file.write("# Site Map\n\n")
        file_list = []
        
        for root, _, files in os.walk(directory):
            if root.endswith('.git') or '.git' in root:
                continue
            for file_name in files:
                if not file_name.startswith('.') and file_name != '.DS_Store':
                    full_path = os.path.join(root, file_name)
                    if not os.path.basename(full_path).startswith('.'):
                        file_list.append(full_path)

        file_list.sort()

        for idx, file_path in enumerate(file_list, start=1):
            rel_path = os.path.relpath(file_path, directory).replace("\\", "/")
            depth = rel_path.count('/')
            indent = "  " * depth
            file.write(f"{indent}{idx}. [{rel_path}]({rel_path})\n")

repository_directory = "."
sitemap_file_name = "sitemap.md"

generate_sitemap_md(repository_directory, sitemap_file_name)