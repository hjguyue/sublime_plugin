# Date: Sun Mar  9 16:29:02 2014
# Author: Jun Hu

import sublime, sublime_plugin
import time

class HeadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "# Date: " + time.ctime() + "\n# Author: Jun Hu\n\n")
