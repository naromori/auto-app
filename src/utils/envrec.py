# import os


#     @staticmethod
#     def find_env(path: str = "./") -> str | None:
#         print(f"Going into path: {path}")
#         search_target = "cacert.pem"
#         path_list: list[str] = []
#         rec_list: list[str] = []
#         for file in os.listdir(path):
#             full_path = path + file
#             if os.path.isdir(full_path):
#                 print(f"Found dir: {full_path}")
#                 rec_list = EnvRec.find_env(full_path)
#             if file == search_target:
#                 path_list.append(full_path)
#         path_list.extend(rec_list)
#         return path_list
            

import os
import fnmatch
from typing import List

class EnvRec():

    @staticmethod
    def find_env(path: str = "./", search_target: str = ".env") -> List[str]:

        matched_files: List[str] = []
        
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                
                if os.path.isdir(full_path):
                    matched_files.extend(EnvRec.find_env(full_path, search_target))

                if fnmatch.fnmatch(item, search_target):
                    matched_files.append(full_path)
                    
        except PermissionError:
            print(f"Permission denied: {path}")
        except OSError as e:
            print(f"Error accessing {path}: {e}")
        
        return matched_files