import os
import yaml
from jinja2 import Environment, FileSystemLoader

jinja_path = input("Jinja file: ")
yaml_path = input("YAML file: ")

with open(yaml_path) as f:
    data = yaml.safe_load(f)

# Load templates from the master file's folder so {% include %} works
env = Environment(loader=FileSystemLoader(os.path.dirname(jinja_path) or "."))
template = env.get_template(os.path.basename(jinja_path))

with open("output.txt", "w") as f:
    f.write(template.render(data))

print("Wrote output.txt")
