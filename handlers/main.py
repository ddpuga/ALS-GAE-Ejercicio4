#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

class MainHandler(webapp2.RequestHandler):

    def post(self):
        kilometros = self.request.get("edKm", "0")
        tiempo = self.request.get("edTime", "0")
        consumo = self.request.get("edCons", "0")


        if len(kilometros.strip()) == 0 or isFloat(kilometros) == False:
            kilometros = 0
        if len(tiempo.strip()) == 0 or isFloat(tiempo) == False:
            tiempo = 0
        if len(consumo.strip()) == 0 or isFloat(consumo) == False:
            consumo = 0

        vel_media = 0
        if float(tiempo) != 0:
            vel_media = float(kilometros) / float(tiempo)

        consumo_total = float(consumo)*float(kilometros) /100.0

        self.response.write("Tu velocidad media ha sido de " + str(vel_media) + " km/h" + " y tu consumo total ha sido de " +
                            str(consumo_total) + " litros")




app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
