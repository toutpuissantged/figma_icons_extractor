
from asyncio import constants
from hashlib import new
from importlib.resources import path
import json
import os
from tokenize import String
json
import time

class SVG_PATH_EXTRACTOR : 
  def __init__(self) -> None:
    self.path_list = []
    self.folder_path = ""
    self.svg_map = []
    self.current_dir = os.path.dirname(os.path.abspath(__file__))
    self.folders_path = os.path.join(self.current_dir, "icons","linear")
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
    return '{"name" : "'+name+'", "path" : "'+dir.replace('\\','/')+'"}, \n'
    
  def list_svg_path_from_folder(self ) -> list:
    svg_path_list = []
    folder_path = self.folders_path
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
    #print(formated)
    return formated

  def save_output_to_file(self, file_path, content) -> None:
    with open(file_path, "w") as f:
      f.write(content)
    pass  

  def main(self) -> None:
    self.list_svg_path_from_folder()

class ExecutionTime :
  def __init__(self) -> None:
    self.start_time = 0
    self.end_time = 0
    self.execution_time = 0
    pass

  def start(self) -> None:
    self.start_time = time.time()
    pass

  def end(self) -> None:
    self.end_time = time.time()
    self.execution_time = self.end_time - self.start_time
    pass

  def get_execution_time(self) -> float:
    return self.execution_time

execution_time = ExecutionTime()
execution_time.start()
extractor = SVG_PATH_EXTRACTOR() 
extractor.main()
execution_time.end()
print("Execution Time : ", execution_time.get_execution_time())

