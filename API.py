# Project card-title
# #images
# #Description
# #Description
import os

PROJECTS_JSON = {"MOB_APP": [], "ML": []}

projects = {
    "PERSONAL DB": ["per_db", "lorem.....", "MOB_APP"],
    "HANDWRITTEN": ["hand_rec", "loremsent....", "ML"],
}
for proj_title in projects:
    Project = {
        "title": proj_title,
        "images": [
            "imgs/projects/" + img
            for img in os.listdir("./static/imgs/projects/")
            if img.startswith(projects[proj_title][0])
        ],
        "desc": projects[proj_title][1],
    }

    PROJECTS_JSON[projects[proj_title][2]].append(Project)

certs = list(os.walk("./static/certs/"))[-1][-1]
