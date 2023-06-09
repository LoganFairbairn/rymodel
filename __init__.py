# Copyright (c) 2021-2023 Logan Fairbairn
# logan-fairbairn@outlook.com
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# This file imports and registers all required modules for this add-on.

import bpy

# Import operators.
from .quick_operators import RyModel_Mirror, RyModel_ResetOrigin, RyModel_AddModifier, RyModel_CopyModifiers, RyModel_AutoSharpen, RyModel_CleanMesh, RyModel_RadialArray, RyModel_CurveToRope, RyModel_Cheshire, RyModel_HSWFModApply, RyModel_AddCutter, RyModel_HideCutters, RyModel_ShowCutters, RyModel_RemoveUnusedCutters, RyModel_AutoSeam

# Import user interface.
from .ui_main import MATLAYER_OT_open_rymodel_menu, ADDON_VERSION_NUMBER

bl_info = {
    "name": "RyModel",
    "author": "Logan Fairbairn (Ryver)",
    "version": (ADDON_VERSION_NUMBER[0], ADDON_VERSION_NUMBER[1], ADDON_VERSION_NUMBER[2]),
    "blender": (3, 5, 0),
    "location": "View3D > Sidebar > RyModel",
    "description": "Adds a quick access menu with a collection of batched and commonly used modeling operations.",
    "warning": "",
    "doc_url": "",
    "category": "Modeling",
}

# List of classes to be registered.
classes = (
    # Operators
    RyModel_Mirror,
    RyModel_ResetOrigin,
    RyModel_AddModifier,
    RyModel_CopyModifiers,
    RyModel_AutoSharpen,
    RyModel_CleanMesh,
    RyModel_RadialArray,
    RyModel_CurveToRope, 
    RyModel_Cheshire,
    RyModel_HSWFModApply,
    RyModel_AddCutter,
    RyModel_HideCutters, 
    RyModel_ShowCutters, 
    RyModel_RemoveUnusedCutters,
    RyModel_AutoSeam,

    # User Interface
    MATLAYER_OT_open_rymodel_menu
)

addon_keymaps = []

def register():
    # Register properties, operators and pannels.
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    km.keymap_items.new(MATLAYER_OT_open_rymodel_menu.bl_idname, 'D', 'PRESS', ctrl=True, shift=False)
    addon_keymaps.append(km)

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    # Remove add-on key mapping.
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    del addon_keymaps[:]

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()