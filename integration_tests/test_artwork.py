#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Test the Artwork against live data in redis to ensure the Artwork data is valid/behaves."""


from megacosm.generators import Artwork
#from pprint import pprint

import unittest2 as unittest

import redis
from config import IntegrationTestConfiguration


class TestArtworkIntegration(unittest.TestCase):
    """ Test Artwork Integration """
    def setUp(self):
        "Create Redis Connection"
        self.redis = redis.from_url(IntegrationTestConfiguration.REDIS_URL)

    def tearDown(self):
        """Tear stuff Down."""
        #self.redis.flushall()

    def test_kinds(self):
        """ Test all the kinds, subkinds, and their templates """
        for kind in self.redis.lrange('artwork_kind', 0, -1):
            print "kind: "+kind
            for template in self.redis.lrange('artwork'+kind+'_template', 0, -1):
                #print "template: "+template
                artwork = Artwork(self.redis, {'kind':kind, 'template':template})
                self.assertEqual(kind, str(artwork.kind))

                self.assertNotIn('{', str(artwork))
                self.assertNotIn('}', str(artwork))
                self.assertNotIn('params', str(artwork))
            for subkind in self.redis.lrange('artwork'+kind+'_subkind', 0, -1):
                #print "template: "+template
                artwork = Artwork(self.redis, {'kind':kind, 'subkind':subkind})
                self.assertEqual(kind, str(artwork.kind))
                self.assertNotIn(kind, str(artwork))
                self.assertIn(subkind, str(artwork))

                self.assertNotIn('{', str(artwork))
                self.assertNotIn('}', str(artwork))
                self.assertNotIn('params', str(artwork))
