# import ipdb
import re

class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 < len(value) and not hasattr(self, 'name'):
            self._name = value
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        all_visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]

        if all_visitors:
            best = max(all_visitors, key=lambda visitor: all_visitors.count(visitor))
            return best
        else:
            return None

class Trip:

    all = []

    def is_valid_format(self, date_string):
        pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)$"
        return re.match(pattern, date_string)
    
    def __init__(self, visitor, national_park, start_date, end_date):

        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.__class__.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value
        else: 
            raise Exception("visitor must be type 'Visitor")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if isinstance(value, NationalPark):
            self._national_park = value
        else: 
            raise Exception("visitor must be type 'NationalPark'")
        
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) > 6 and self.is_valid_format(value):
            self._start_date = value
        else: 
            raise Exception("start date must be type 'string' in format 'September 1st'")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) > 6 and self.is_valid_format(value):
            self._end_date = value
        else: 
            raise Exception("end date must be type 'string' in format 'September 1st'")

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) < 16:
            self._name = value
        else: 
            raise Exception("name must be type 'string' and at least 7 characters long")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        return len([trip.visitor for trip in Trip.all if trip.national_park == park])


# n1 = NationalPark("Yosemite")
# n2 = NationalPark("Yellow Stone")

# v1 = Visitor("Steven")
# v2 = Visitor("Rachel")

# t1 = Trip(v1, n1,"September 1st", "September 1st")
# t2 = Trip(v2, n2, "September 1st", "September 1st")

# #test if dates are mutable
# t1.start_date("September 2nd")
# t2.end_date("September 2nd")

# ipdb.set_trace()
