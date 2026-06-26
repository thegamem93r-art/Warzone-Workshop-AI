bl_info = {
    "name": "Warzone Workshop AI",
    "blender": (4, 0, 0),
    "version": (0, 1, 0),
    "location": "View3D > Sidebar > Warzone Workshop AI",
    "description": "AI-powered Blender assistant for 3D modeling and design",
    "author": "Warzone Workshop",
    "url": "https://github.com/thegamem93r-art/Warzone-Workshop-AI",
    "category": "3D View",
    "support": "COMMUNITY",
    "doc_url": "https://github.com/thegamem93r-art/Warzone-Workshop-AI/wiki",
    "tracker_url": "https://github.com/thegamem93r-art/Warzone-Workshop-AI/issues",
}

import sys
import os

# Add addon directory to path for imports
addon_dir = os.path.dirname(__file__)
if addon_dir not in sys.path:
    sys.path.append(addon_dir)

import bpy
from . import panels, operators, preferences


def register():
    """Register all addon classes and properties"""
    preferences.register()
    operators.register()
    panels.register()
    print("✓ Warzone Workshop AI registered successfully")


def unregister():
    """Unregister all addon classes and properties"""
    panels.unregister()
    operators.unregister()
    preferences.unregister()
    print("✓ Warzone Workshop AI unregistered")


if __name__ == "__main__":
    register()
