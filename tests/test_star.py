#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Fully test this module's functionality through the use of fixtures."

from megacosm.generators import Star
import unittest2 as unittest

import fakeredis
import fixtures
from config import TestConfiguration

class TestStar(unittest.TestCase):

    def setUp(self):
        self.redis = fakeredis.FakeRedis()
        fixtures.star.import_fixtures(self)

    def tearDown(self):
        self.redis.flushall()

    def test_creation(self):
        """  """

        star = Star(self.redis)
        self.assertEqual('Krojel', str(star.name))
        self.assertEqual('Krojel', str(star))
