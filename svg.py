
from asyncio import constants
from hashlib import new
from importlib.resources import path
import json
import os
from tokenize import String
json

class SVG_PATH_EXTRACTOR : 
  def __init__(self) -> None:
    self.path_list = []
    self.folder_path = ""
    self.svg_map = []
    self.current_dir = os.path.dirname(os.path.abspath(__file__))
    self.save_file = os.path.join(self.current_dir, "svg_path_map.json")
    pass

  def extract_svg_path_from_file(self, file_path) -> str:
    try  : 
      with open(file_path, "r") as f:
        svg_path = f.read()
      return svg_path
    except :
      print("FileNotFoundError : ", file_path)
      return ""

  def make_json_object( self, name , dir) -> None:
    return '{"'+name+'": "'+dir.replace('\\','/')+'"}, \n'
    
  def list_svg_path_from_folder(self, folder_path) -> list:
    svg_path_list = []
    svg_json = "["
    for file in os.listdir(folder_path):
      svg_dir = os.path.join(folder_path, file)
      for svg_file in os.listdir(svg_dir):
        svg_path_list.append(os.path.join(svg_dir, svg_file))
        svg_name = svg_file.split(".")[0]
        svg_rel_path = os.path.relpath(os.path.join(svg_dir, svg_file), os.path.join(self.current_dir, "icons"))
        self.svg_map.append({
          "name": svg_name,
          "path": svg_rel_path
        })
        svg_json += self.make_json_object(svg_name, svg_rel_path)
      #print(file)
      if file.endswith(".svg"):
        svg_path_list.append(os.path.join(folder_path, file))
    formated = svg_json+"]"
    self.save_output_to_file(self.save_file, formated)
    print(formated)
    return formated

  def save_output_to_file(self, file_path, content) -> None:
    with open(file_path, "w") as f:
      f.write(content)
    pass


current_dir = os.path.dirname(os.path.abspath(__file__))
folders_path = os.path.join(current_dir, "icons","linear")
extractor = SVG_PATH_EXTRACTOR() 
svg_path_list = extractor.list_svg_path_from_folder(folders_path)

