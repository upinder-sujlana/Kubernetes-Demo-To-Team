from flask import Flask
import os
import logging as logger
logger.basicConfig(level="DEBUG")

#----------------------------------------------------------------------------
__author__     = 'Upinder Sujlana'
__copyright__  = 'Copyright 2020, Docker & K8S demo for hyperflex team'
__version__    = '1.0.4'
__maintainer__ = 'Upinder Sujlana'
__email__      = 'usujlana@cisco.com'
__status__     = 'prod'
#----------------------------------------------------------------------------
#Do not forget below
app = Flask(__name__)
#----------------------------------------------------------------------------
@app.route("/")
def hello():
    if 'POD_NAME' in os.environ:
        return {'pod_hostname': os.environ['POD_NAME'], 'pod_podip': os.environ['POD_PODIP'] }
    else:
        return "Had issues getting the POD details. Still hi from inside the container"
#----------------------------------------------------------------------------
if __name__ == "__main__":
    logger.debug("Starting Flask Server")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
