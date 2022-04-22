import os , shutil

import regex

new_folders_names = [
    "money",
    "video_audio_image",
    "emails_messages",
    "design_tools",
    "content_edit",
    "notification",
    "call",
    "business",
    "crypto_compagny",
    "type_paragraph_character",
    "arrow",
    "location",
    "school_learning",
    "grid",
    "Programming",
    "settings",
    "archive",
    "building",
    "weather",
    "user",
    "delivery",
    "shop",
    "essential",
    "time",
    "astrology",
    "files",
    "car",
    "security",
    "crypto_currency",
    "support_like_question",
    "computer_device_electronic",
]

svg_dir = os.sep+"vuesax"+os.sep+"linear"+os.sep
current_dir = os.path.dirname(os.path.abspath(__file__))
folders_path = os.path.join(current_dir, "icons")

def old_folders_name (id):
    return "Figma(" + str(id)+ ")"

def rename_folders(folders_path, new_folders_names):
    for folder in os.listdir(folders_path):
        if folder.startswith("Figma"):
            old_name = folder
            new_name = new_folders_names[int(regex.search(r'\d+', folder).group())]
            os.rename(os.path.join(folders_path, old_name), os.path.join(folders_path, new_name))

def move_svg_files():
  svg_dir = os.sep+"linear"+os.sep
  for folder in os.listdir(folders_path):
    old_svg_dir = os.path.join(folders_path, folder+svg_dir)
    new_svg_dir = os.path.join(folders_path, folder)
    print(old_svg_dir)
    if os.path.isdir(old_svg_dir):
      #print(old_svg_dir)
      for svg_file in os.listdir(old_svg_dir):
        shutil.move(os.path.join(old_svg_dir, svg_file), new_svg_dir)
      os.rmdir(os.path.join(new_svg_dir, "linear"))
      os.rmdir(os.path.join(new_svg_dir, "vuesax"))
    else :
      print("no svg dir")
    

#rename_folders(folders_path, new_folders_names)
move_svg_files()