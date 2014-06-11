# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.image.v1 import image

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'checksum': '1',
    'container_format': '2',
    'copy_from': '3',
    'disk_format': '4',
    'id': IDENTIFIER,
    'is_public': '5',
    'location': '6',
    'min_disk': '7',
    'min_ram': '8',
    'name': '9',
    'owner': '10',
    'properties': '11',
    'protected': '12',
    'size': '13',
    'status': '14',
    'created_at': '2014-06-15 14:18:37.794540',
    'updated_at': '2014-06-16 14:18:37.794540',
}


class TestImage(testtools.TestCase):

    def test_basic(self):
        sot = image.Image()
        self.assertEqual('image', sot.resource_key)
        self.assertEqual('images', sot.resources_key)
        self.assertEqual('/images', sot.base_path)
        self.assertEqual('image', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = image.Image(EXAMPLE)
        self.assertEqual(EXAMPLE['checksum'], sot.checksum)
        self.assertEqual(EXAMPLE['container_format'], sot.container_format)
        self.assertEqual(EXAMPLE['copy_from'], sot.copy_from)
        self.assertEqual(EXAMPLE['disk_format'], sot.disk_format)
        self.assertEqual(IDENTIFIER, sot.id)
        self.assertEqual(EXAMPLE['is_public'], sot.is_public)
        self.assertEqual(EXAMPLE['location'], sot.location)
        self.assertEqual(EXAMPLE['min_disk'], sot.min_disk)
        self.assertEqual(EXAMPLE['min_ram'], sot.min_ram)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['owner'], sot.owner)
        self.assertEqual(EXAMPLE['properties'], sot.properties)
        self.assertEqual(EXAMPLE['protected'], sot.protected)
        self.assertEqual(EXAMPLE['size'], sot.size)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)
