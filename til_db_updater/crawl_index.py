import git
import os
import re
from settings import REPO_URL, REPO_DIR

def pull_repo():
    til_repo = git.cmd.Git(REPO_DIR)
    til_repo.pull()

def crawl_index():
    file_list = []
    pull_repo()
    for file in os.listdir(REPO_DIR):
        if os.path.isdir(REPO_DIR+"/"+file):
            for readme in os.listdir(REPO_DIR+"/"+file):
                if readme=="README.md":
                    path = REPO_DIR+"/"+file;
                    f = open(path+"/"+readme)
                    pattern = re.compile(r"\[(.+)\](.+)")
                    lines = f.readlines()
                    for line in lines:
                        m = pattern.search(line)
                        if m:
                            try:
                                file_path = path+m.group(2)[2:-1]
                                file_name = m.group(2)[2:-1].split("/")[-1]
                                file_context = open(file_path).readlines()
                                file_list.append([file_name, "/"+file+m.group(2)[2:-1], file_context])
                            except:
                                pass
    return file_list