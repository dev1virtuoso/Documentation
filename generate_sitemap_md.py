import os

def generate_sitemap_md(directory, md_file):
    with open(md_file, 'w') as file:
        file.write("# Site Map\n\n")
        for root, _, files in os.walk(directory):
            # 排除特定文件或目录
            if root.endswith('.git') or '.git' in root:
                continue
            for file_name in files:
                if not file_name.startswith('.') and file_name != '.DS_Store':  
                    full_path = os.path.join(root, file_name)
                    if not os.path.basename(full_path).startswith('.'):
                        file_path = os.path.relpath(full_path, directory)
                        file_path = file_path.replace("\\", "/")
                        file.write(f"- [{file_path}]({file_path})\n")

repository_directory = "."
sitemap_file_name = "sitemap.md"

generate_sitemap_md(repository_directory, sitemap_file_name)