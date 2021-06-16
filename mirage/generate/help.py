# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from mirage.flow import Workflow

class DjangoModelMakeFlow(Workflow):

    def main(self):

        datatypes = """

Data Type:         Rerating Fields:

 string              CharField
 auto                AutoField
 auto64              BigAutoField
 int64               BigIntegerField
 binary              BinaryField
 bool                BooleanField
 char                CharField
 date                DateField
 datetime            DateTimeField
 decimal             DecimalField
 duration            DurationField
 interval            DurationField
 email               EmailField
 file                FileField
 path                FilePathFields
 float               FloatField
 image               ImageField
 int                 IntegerField
 integer             IntegerField
 ip                  GenericIPAddressField
 nullbool            NullBooleanField
 pint                PositiveIntegerField
 slug                SlugField
 text                TextField
 time                TimeField
 url                 URLField
 uuid                UUIDField"

"""
        print(datatypes)
