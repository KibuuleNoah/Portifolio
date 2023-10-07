# Project card-title
# #images
# #Description
# #Description
import os

GUI_PRO = []
NON_GUI = []

projects = {
    "PERSONAL DB": ["per_db", "lorem.....", "mobile development"],
    "HANDWRITTEN": ["hand_rec", "loremsent....", "machine learning"],
    "NOTES BOOK": ["notes", "loremPara.....", "python scripting"],
    "USD<-->UGX": ["curr", "loremPara....", "web scrabbing"],
}
for proj_title in projects:
    Project = {
        "title": proj_title,
        "images": [
            "imgs/projects/" + img
            for img in os.listdir("./static/imgs/projects/")
            if img.startswith(projects[proj_title][0])
        ],
        "cat": projects[proj_title][-1],
        "desc": projects[proj_title][1],
    }

    GUI_PRO.append(Project)

certs = list(os.walk("./static/certs/"))[-1][-1]

# print(PROJECTS_JSON)
