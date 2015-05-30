"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from phase2 import Phase2XBlock


class Phase1XBlock(XBlock):
	"""
	TO-DO: document what your XBlock does.
	"""

	# Fields are defined on the class.	You can access them in your code as
	# self.<fieldname>.
	
	support = String(
		default="", scope=Scope.content
	)
	
	mainCourse = String(
		default="Systemes stochastiques", scope=Scope.content
	)
	note1 = Integer(
		default=0, scope=Scope.user_state,
	)
	note2 = Integer(
		default=0, scope=Scope.user_state,
	)
	note3 = Integer(
		default=0, scope=Scope.user_state,
	)
	rep1 = String(
		default="Optimisation d\'emploi du temps, optimisation de profil d\'ailes d\'avion, optimisation de tournees de vehicules", scope=Scope.user_state,
	)
	rep2 = String(
		default="C\'est un espace dans lequel on cherche une solution", scope=Scope.user_state,
	)
	rep3 = String(
		default="C\'est un espace de recherche qui a plusieurs optima locaux", scope=Scope.user_state,
	)
	rpp1 = String(
		default="C\'est un espace avec qui a plusieurs optima locaux", scope=Scope.user_state,
	)
	rpp2 = String(
		default="C\'est un espace", scope=Scope.user_state,
	)
	rpp3 = String(
		default="C\'est quelque chose", scope=Scope.user_state,
	)
	quest = String(
		default='', scope=Scope.user_state,
	)
	quest1 = String(
		default='', scope=Scope.user_state,
	)
	quest2 = String(
		default='', scope=Scope.user_state,
	)
	quest3 = String(
		default='', scope=Scope.user_state,
	)
	
	# TO-DO: delete count, and define your own fields.
	count = Integer(
		default=0, scope=Scope.user_state,
		help="A simple counter, to show something happening",
	)

	def resource_string(self, path):
		"""Handy helper for getting resources from our kit."""
		data = pkg_resources.resource_string(__name__, path)
		return data.decode("utf8")

	# TO-DO: change this view to display your data your own way.
	def student_view(self, context=None):
		"""
		The primary view of the Phase1XBlock, shown to students
		when viewing courses.
		"""
		html = self.resource_string("static/html/phase1.html")
		frag = Fragment(html.format(self=self))
		frag.add_css(self.resource_string("static/css/phase1.css"))
		frag.add_javascript(self.resource_string("static/js/src/phase1.js"))
		frag.initialize_js('Phase1XBlock')
		self.quest1 = "Donnez trois exemples de problemes d'optimisation."
		self.quest2 = "Qu'est-ce qu'un espace de recherche ?"
		self.quest3 = "Qu'est-ce qu'un espace de recherche multimodal ?"
		return frag
		
	@XBlock.json_handler
	def validate1(self, data, suffix=''):
		self.rep1 = data['rep1']
		self.rep2 = data['rep2']
		self.rep3 = data['rep3']
		print "Le field rep1 vaut :"
		
		return {"rep1": self.rep1}
		
		
	# TO-DO: change this handler to perform your own actions.  You may need more
	# than one handler, or you may not need any handlers at all.
	@XBlock.json_handler
	def increment_count(self, data, suffix=''):
		"""
		An example handler, which increments the data.
		"""
		# Just to show data coming in...
		assert data['hello'] == 'world'

		self.count += 1
		return {"count": self.count}

	# TO-DO: change this to create the scenarios you'd like to see in the
	# workbench while developing your XBlock.
	@staticmethod
	def workbench_scenarios():
		"""A canned scenario for display in the workbench."""
		return [
			("Phase1XBlock",
			 """<vertical_demo>
				<phase1/>
				</vertical_demo>
			 """),
		]
	@staticmethod
	def newpage():
		"""A canned scenario for display in the workbench."""
		return [
			("Phase2XBlock",
			 """<vertical_demo>
				<phase2/>
				</vertical_demo>
			 """),
		]
