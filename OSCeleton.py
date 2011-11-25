#! /usr/bin/env python

"""
   Written by: Robbie Clemons
   Email: RobClemons@gmail.com
   Project: pyOSCeleton
   Licensed under GNU GPLv3
   Released February 2011

   This document provides the Point, Skeleton, and OSCeleton classes which
   are meant to recieve and contain skeleton data from OSCeleton.
   
"""

# Copyright (C) 2011 Robbie Clemons
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>

import OSC
from math import sqrt

HEAD = 'head'
NECK = 'neck'
LEFT_COLLAR = 'l_collar'
RIGHT_COLLAR = 'r_collar'
LEFT_SHOULDER = 'l_shoulder'
RIGHT_SHOULDER = 'r_shoulder'
LEFT_ELBOW = 'l_elbow'
RIGHT_ELBOW = 'r_elbow'
LEFT_WRIST = 'l_wrist'
RIGHT_WRIST = 'r_wrist'
LEFT_HAND = 'l_hand'
RIGHT_HAND = 'r_hand'
LEFT_FINGERTIP = 'l_fingertip'
RIGHT_FINGERTIP = 'r_fingertip'
TORSO = 'torso'
LEFT_HIP = 'l_hip'
RIGHT_HIP = 'r_hip'
LEFT_KNEE = 'l_knee'
RIGHT_KNEE = 'r_knee'
LEFT_ANKLE = 'l_ankle'
RIGHT_ANKLE = 'r_ankle'
LEFT_FOOT = 'l_foot'
RIGHT_FOOT = 'r_foot'

class Point(object):
    """Holds a 3 dimensional point.
    
    Point has 3 properties which are the coordinates x, y and z.
    """
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x, y, z):
        """Initialize Point object.
        
        Accepts the x, y and z coordinates in that order.
        
        Usage:
        
            >>> point1 = Point(1, 2, 3)
            >>> point1.x
            1
            >>> point1.z
            3
        """
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        """Return a string in the format (x, y, z)"""
        s = "(%f, %f, %f)" % (self.x, self.y, self.z)
        return s
        
    def __eq__(self, other):
        """Test whether two Points' x, y and z coordinates are equal
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point2 = Point(1, 2, 5)
        >>> point1 == point2
        False
        >>> point3 = Point(1, 2, 3)
        >>> point1 == point3
        True
"""
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
            
    def __add__(self, other):
        """Add Point objects' coordinates together
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point2 = Point(1, 2, 5)
        >>> point1 + point2
        (2.000000, 4.000000, 8.000000)
        """
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)
        
    def __sub__(self, other):
        """Subtract Point objects' coordinates
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point2 = Point(1, 2, 5)
        >>> point1 - point2
        (0.000000, 0.000000, -2.000000)
        """
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)
    
    def copy(self):
        """Returns a new Point with the same coordinates
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point0 = point1.copy()
        >>> point0
        (1.000000, 2.000000, 3.000000)
        """
        return Point(self.x, self.y, self.z)
        
    def vals(self):
        """Returns a list containg the x, y and z coordinates
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point1.vals()
        [1, 2, 3]
        """
        return [self.x, self.y, self.z]
        
    def magnitude(self):
        """Calculate vector magnitude of Point
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point1.magnitude()
        3.7416573867739413
        """
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
            
    def normalize(self):
        """Normalize Point's x, y and z coordinates in place
        
        Usage:
        
        >>> point1 = Point(1, 2, 3)
        >>> point1
        (1.000000, 2.000000, 3.000000)
        >>> point1.normalize()
        >>> point1
        (0.267261, 0.534522, 0.801784)
        """
        mag = self.magnitude()
        self.x = self.x / mag
        self.y = self.y / mag
        self.z = self.z / mag

class Skeleton:
    """Holds a user's joint positions
    
    Skeleton.joints is a dictionary whose keys are joint labels
    and its values are the joint's Point.
    
    Skeleton.orient is a dictionary whose keys are joint labels
    and its values are the joint's orientation data.
    
    Skeleton.id is the user's number    
    """
    
    def __init__(self, user):
        """Initialize Skeleton.
        
        Requires the user's number
        """
        self.id = user
        self.joints = {}
        self.orient = {}

    def __contains__(self, wanted):
        """Test whether Skeleton.joints contains everything passed to it.
        
        Usage:
        
        >>>if (HEAD, NECK) in skeleton:
        >>>    print "skeleton contains HEAD and NECK"
        """
        return set(wanted) <= set(self.joints)
        
    def __setitem__(self, key, value):
        """Maps to Skeleton.joints"""
        self.joints[key] = value
        
    def __getitem__(self, key):
        """Maps to Skeleton.joints"""
        return self.joints[key]
        
    def copy_joints(self):
        """Returns a new dictionary with the same joints data"""
        joints = {}
        for jointName, pnt  in self.joints.items():
            joints[jointName] = pnt.copy()
        return joints
        
    def clear(self):
        """Maps to Skeleton.joints"""
        self.joints.clear()
        self.orient.clear()

class OSCeleton:
    """Starts a server instance and processes each event the server receives.
    
    OSCeleton.server is a OSC.OSCServer instance.
    
    OSCeleton.users is a dictionary whose keys are user ids and
    its' values are Skeleton objects.
    
    OSCeleton.frames is a counter that is incremented every time all of a user's
    recognized joints have been received by the server.
    
    OSCeleton.lost_users is a list containing recently lost users.
    """
    
    users = {}
    _users = {}
    frames = 0
    lostUsers = []
    realWorld = False
    
    def __init__(self, port = 7110):
        """Initialize OSCeleton.
        
        Accepts the optional argument of the port for the server to listen on.
        
        Creates the server and registers the callbacks.
        """
        self.server = OSC.OSCServer(('127.0.0.1', port))
        self.server.addMsgHandler("/new_user", self.new_user_callback)
        self.server.addMsgHandler("/lost_user", self.lost_user_callback)
        self.server.addMsgHandler("/new_skel", self.new_skeleton_callback)
        self.server.addMsgHandler("/joint", self.joint_callback)
        self.server.addMsgHandler("/orient", self.orient_callback)
        self.server.addMsgHandler("default", self.do_nothing_callback)
    
    def new_user_callback(self, path, types, args, src):
        """Create user"""
        print "New user %d" % args[0]
        self._users[args[0]] = Skeleton(args[0])
        
    def lost_user_callback(self, path, types, args, src):
        """Remove user"""
        print "User %d has been lost" % args[0]
        try:
            del self._users[args[0]]
            self.lostUsers.append(args[0])
            del self.users[args[0]]
        except KeyError:
            pass
            
    def do_nothing_callback(self, path, types, args, src):
        """Does absolutely nothing"""
        
    def new_skeleton_callback(self, path, types, args, src):
        """Prints that a new skeleton is being tracked"""
        print "Calibration complete, now tracking User %d" % args[0]
        
    def joint_callback(self, path, types, args, src):
        """Add joint to a users skeleton"""
        #add new user if they haven't been added already
        if args[1] not in self._users:
            self._users[args[1]] = Skeleton(args[1])

        #start a new frame and save the old one in users if we already have joint
        if str(args[0]) in self._users[args[1]].joints:
            if args[1] not in self.users:
                self.users[args[1]] = Skeleton(args[1])
            self.users[args[1]].joints = self._users[args[1]].copy_joints()
            self.users[args[1]].orient = self._users[args[1]].orient.copy()
            self._users[args[1]].clear()
            self.frames += 1
        #convert to mm in real world measurements
        if self.realWorld:
            x = 1280 - args[2] * 2560
            y = 960 - args[3] * 1920
            z = -args[4] * 1280
            self._users[args[1]][str(args[0])] = Point(x, y, z)
        else:
            x, y, z = args[2:]
            self._users[args[1]][str(args[0])] = Point(x, y, z)

    def orient_callback(self, path, types, args, src):
        """Add join orientation to a users skeleton"""
        #add new user if they haven't been added already
        if args[1] not in self._users:
            self._users[args[1]] = Skeleton(args[1])
        x = args[2:5]
        y = args[5:8]
        z = args[8:]
        self._users[args[1]].orient[str(args[0])] = [x, y, z]
        
    def get_users(self):
        """Return a list of users
        
        Usage: 
        
        >>> osc.get_users()
        [1, 2]
        """
        return self._users.keys()
        
    def get_new_skeletons(self):
        """Return a list of new skeletons
        
        Usage:
        
        >>> for skel in osc.get_new_skeletons():
        >>>     for jointName, point in skel.joints.items():
        >>>         print "joint = " + str(jointName)
        >>>         print "position = " + str(point)
        """
        tmp = self.users.values()
        self.users.clear()
        return tmp
        
    def run(self):
        """Wait for and catch event"""
        self.server.handle_request()

