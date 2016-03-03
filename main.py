__author__ = 'Fares'

import os

# Each wesbite you crawl is a separate project(folder)

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project "+ directory)
        os.makedirs(directory)
