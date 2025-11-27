import os
directory_path="/web tech/day-1"
content=os.listdir(directory_path)
print(content)

import pyjokes
print(pyjokes.get_joke())