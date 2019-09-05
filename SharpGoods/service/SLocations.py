# *- coding:utf8 *-
from SharpGoods.service.SBase import SBase, close_session
from SharpGoods.models.model import Locations


class SLocations(SBase):
    def __init__(self):
        super(SLocations, self).__init__()

    @close_session
    def get_all(self, usid):
        all_location = self.session.query(
            Locations.LOid,
            Locations.LOname,
            Locations.LOtelphone,
            Locations.LOno,
            Locations.LOdetail,
            Locations.LOprovince,
            Locations.LOcity,
            Locations.LOarea,
            Locations.LOisedit
        ).filter(
            Locations.USid == usid, Locations.LOisedit != 303
        ).all()
        return all_location

    @close_session
    def update_locations_by_loid(self, loid, new_location):
        self.session.query(Locations).filter_by(
            LOid=loid).update(new_location)

    @close_session
    def get_location_by_loid(self, loid):
        return self.session.query(
            Locations.LOid,
            Locations.LOname,
            Locations.LOtelphone,
            Locations.LOno,
            Locations.LOdetail,
            Locations.LOprovince,
            Locations.LOcity,
            Locations.LOarea,
            Locations.LOisedit
        ).filter(Locations.LOid == loid).first()