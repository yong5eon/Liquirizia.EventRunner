# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'EventRunner',
)


class EventRunner(object):
	"""Event Runner Interface"""

	@abstractmethod
	def __init__(self, event: str, headers: dict = None):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	@abstractmethod
	def run(self, body=None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
