# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/__init__.py
# Compiled at: 2018-04-23 20:27:04
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface import capabilities as caps
from .blocks import Blocks

def get_capabilities():
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10996, product_ids=[
                              2304], model_name=[
                              'Lightpad BLOCK', 'BLOCKS']), 
       caps.PORTS_KEY: [
                      caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]),
                      caps.outport(props=[caps.NOTES_CC, caps.SCRIPT])], 
       caps.TYPE_KEY: 'blocks'}


def create_instance(c_instance):
    return Blocks(c_instance=c_instance)
