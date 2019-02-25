# -------------------------------------------------------------------------------
# Licence:
# Copyright (c) 2012-2019 Luzzi Valerio 
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#
# Name:        projection.py
# Purpose:
#
# Author:      Luzzi Valerio
#
# Created:     25/02/2019
# -------------------------------------------------------------------------------
from pyproj import *
from gecosistema_core import *

def ProjFrom(text):
    if val(text):
        return "+init=epsg:%s" % (text)
    if isstring(text) and text.lower().startswith("epsg:"):
        return "+init=%s" % (text)
    if isstring(text) and text.lower().startswith("init="):
        return "+%s" % (text)
    if isstring(text) and text.lower().startswith("+proj"):
        return text
    return ""


def Reproj(lon, lat, epsgfrom="epsg:4326", epsgto="epsg:32632"):
    try:
        epsgfrom = ProjFrom(epsgfrom)
        epsgto = ProjFrom(epsgto)
        p1 = Proj(epsgfrom)
        p2 = Proj(epsgto)
        if (p1 != p2):
            x, y = transform(p1, p2, lon, lat)
            return (x, y)
        return lon, lat
    except Exception as ex:
        print(ex)
        print("Proj Error", "Proj Error")
    return 0, 0


def ReProject(blon, blat, elon, elat, epsgfrom="epsg:4326", epsgto="epsg:32632"):
    blon, blat, elon, elat = float(blon), float(blat), float(elon), float(elat)
    blon, blat = Reproj(blon, blat, epsgfrom, epsgto)
    elon, elat = Reproj(elon, elat, epsgfrom, epsgto)
    return blon, blat, elon, elat