import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

SRC_REPO="Object_detection"
__VERSION__="0.0.0"
AUTHOR_USER_NAME="arun73822"
AUTHOR_USER_EMAIL="arun73822@gmail.com"
REPO_NAME="Object_Detection_Yolov5"

setuptools.setup(name=SRC_REPO,
                 version=__VERSION__,
                 description="A Sample Object Detection",
                 long_description=long_description,
                 author=AUTHOR_USER_NAME,
                 author_email=AUTHOR_USER_EMAIL,
                 url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
                 project_url={
                    "Bug_Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
                package_dir={"":"src"},
                packages=setuptools.find_packages(where="src")
)