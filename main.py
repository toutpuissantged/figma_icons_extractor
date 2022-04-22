from importlib.resources import path
import os , shutil
import json
import regex

current_dir = os.path.dirname(os.path.abspath(__file__))

#load data from json file
def load_data_from_json():
  data_dir = os.path.join(current_dir, "data")
  with open(os.path.join(data_dir, "data.json"), "r") as f:
    data = json.load(f)
  return data

folders_path = os.path.join(current_dir, "icons")
new_folders_names = load_data_from_json()

def old_folders_name (id):
    return "Figma(" + str(id)+ ")"

def search_int_in_string(string):
  #print("string : ", string)
  try:
    return regex.search(r'\d+', string).group()
  except:
    return 0

def rename_folders(folders_path, new_folders_names):
    for folder in os.listdir(folders_path):
        if folder.startswith("Figma"):
            old_name = folder
            try : 
              new_name = new_folders_names[int(search_int_in_string(folder))]
              os.rename(os.path.join(folders_path, old_name), os.path.join(folders_path, new_name))
            except IndexError:
              print("IndexError : ", folder)

def move_svg_files():
  svg_dir = os.sep+"vuesax"+os.sep+"linear"+os.sep
  for folder in os.listdir(folders_path):
    old_svg_dir = os.path.join(folders_path, folder+svg_dir)
    new_svg_dir = os.path.join(folders_path, folder)
    #print(old_svg_dir)
    if os.path.isdir(old_svg_dir):
      #print(old_svg_dir)
      for svg_file in os.listdir(old_svg_dir):
        shutil.move(os.path.join(old_svg_dir, svg_file), new_svg_dir)

    remove_path = os.path.join(new_svg_dir, "vuesax","linear")
    remove_path_second = os.path.join(new_svg_dir, "vuesax")
    if os.path.exists(remove_path):
      os.rmdir(remove_path)
    if os.path.exists(remove_path_second):
      os.rmdir(remove_path_second)
    else :
      #print("no svg dir")
      pass
    

rename_folders(folders_path, new_folders_names)
move_svg_files()
print("done")