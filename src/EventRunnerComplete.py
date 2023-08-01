# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'EventRunnerComplete'
)


class EventRunnerComplete(object):
	"""Event Runner Complete Interface"""

	@abstractmethod
	def __call__(
		self,
		event: str,
		headers: dict = None,
		body=None,
	):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))
