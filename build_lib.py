Import("env")

print("building lib")

import shutil
import os

origin = os.path.join(os.getcwd(), r"src\openMosfetEspNow.cpp")
destination = os.path.join(os.getcwd(), r"dist\src\openMosfetEspNow.cpp")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)

origin = os.path.join(os.getcwd(), r"src\openMosfetEspNow.h")
destination = os.path.join(os.getcwd(), r"dist\src\openMosfetEspNow.h")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)

origin = os.path.join(os.getcwd(), r"src\clientModule.cpp")
destination = os.path.join(os.getcwd(), r"dist\examples\client\clientModule.ino")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)

# origin = os.path.join(os.getcwd(), r"src\serverModule.cpp")
# destination = os.path.join(os.getcwd(), r"dist\examples\server\serverModule.ino")
# os.makedirs(os.path.dirname(destination), exist_ok=True)
# shutil.copy(origin, destination)

origin = os.path.join(os.getcwd(), r"src\asyncServerModule.cpp")
destination = os.path.join(os.getcwd(), r"dist\examples\asyncServer\asyncServerModule.ino")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)

origin = os.path.join(os.getcwd(), r"library.properties")
destination = os.path.join(os.getcwd(), r"dist\library.properties")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)

origin = os.path.join(os.getcwd(), r"library.properties")
destination = os.path.join(os.getcwd(), r"dist\library.properties")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)

origin = os.path.join(os.getcwd(), r"README.library.md")
destination = os.path.join(os.getcwd(), r"dist\README.md")
os.makedirs(os.path.dirname(destination), exist_ok=True)
shutil.copy(origin, destination)