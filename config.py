import os
dirname = os.path.dirname(__file__)

functionTrue=False

browserClose = True

headlessmode = False

execution_mode = "docker" #docker #local
docker_port = "http://localhost:4444/wd/hub"

browser = "chrome"
local = "core_local"
testSuite = "Sanity"