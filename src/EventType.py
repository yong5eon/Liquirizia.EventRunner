# -*- coding: utf-8 -*-

from abc import ABC, abstractproperty

__all__ = (
	'EventType'
)


class EventType(object):
	"""Event Type Interface"""

	@abstractproperty
	def event(self):
		raise NotImplementedError('{} must be implemented event property'.format(self.__class__.__name__))
