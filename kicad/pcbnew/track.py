# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# (C) 2018 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>

from kicad._native import _pcbnew


class Track(object):
    def __init__(self, track):
        assert isinstance(track, _pcbnew.TRACK)
        self._obj = track

    def get_native(self):
        """Get native object from the low level API

        :return: :class:`pcbnew.TRACK`
        """
        return self._obj

    def __eq__(self, other):
        if not isinstance(self, other.__class__):
            return False

        if not isinstance(self._obj, other._obj.__class__):
            return False

        if self._obj == other._obj:
            return True
        # TODO: SWIG has no working equal operator for objects pointing to the same object!
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "kicad.pcbnew.Track({})".format(self._obj)
