# Project card-title
# #images
# #Description
# #Description
import os

api = []
for i in range(5):
    Project = {
        "title": f"Title_1",
        "images": ["imgs/projects/" + i for i in os.listdir("./static/imgs/projects/")],
        "desc": "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderi.",
    }

    api.append(Project)

# f = os.walk("./static/imgs/").__next__()
# for i in os.listdir("./static/imgs/proj_1"):
#     print(i)
#
