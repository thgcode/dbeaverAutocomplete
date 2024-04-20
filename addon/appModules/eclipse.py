#eclipseAutocomplete autocomplete addon for Eclipse and Dbeaver
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import api
import controlTypes
from nvdaBuiltin.appModules import eclipse as base_eclipse
try:
	from nvdaBuiltin.appModules.eclipse import AutocompletionListItem
except ImportError:
	AutocompletionListItem = None

class AppModule(base_eclipse.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
		# Autocompletion items are placed outside the main eclipse window
		if (
				AutocompletionListItem is not None and
				AutocompletionListItem not in clsList and
				obj.role == controlTypes.Role.LISTITEM
				and obj.parent.parent.parent.role == controlTypes.Role.DIALOG
				and obj.parent.parent.parent.simpleParent == api.getDesktopObject()
				and obj.parent.parent.parent.parent.simpleNext.role in (
					controlTypes.Role.BUTTON,
					controlTypes.Role.TOGGLEBUTTON
				)
			):
				clsList.insert(0, AutocompletionListItem)
