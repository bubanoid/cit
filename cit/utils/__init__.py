from flask import g
from werkzeug.exceptions import Unauthorized
def admin_required(fn):
	def decorated(*args, **kw):
		if not g.user or not g.user.is_superuser:
			raise Unauthorized('Admin permissions required')
		return fn(*args, **kw)
	return decorated
