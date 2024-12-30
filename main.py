from pathlib import Path 
for file_path in Path.cwd().glob("*.py"):
    new_path = Path('new')/file_path.name
    file_path.replace(new_path)
    
