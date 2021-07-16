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

from openstack.tests.functional import base


class BaseSharedFileSystemTest(base.BaseFunctionalTest):

    min_microversion = None

    def setUp(self):
        super(BaseSharedFileSystemTest, self).setUp()
        self.require_service('shared-file-system',
                             min_microversion=self.min_microversion)

    def create_share(self, **kwargs):
        share = self.conn.share.create_share(**kwargs)
        self.addCleanup(self.conn.share.delete_share, share.id,
                        ignore_missing=True)
        self.assertIsNotNone(share.id)
        return share
