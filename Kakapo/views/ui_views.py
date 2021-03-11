from Kakapo.controller.util import import_devices
from Kakapo import app


@app.route('/devices')
def device():

    devices = import_devices()
    return {"devices": devices}
