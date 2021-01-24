#!/usr/bin/env python
import math

class ObjectDetector

  PtoP_ANGLE_COSINE = 0.999

  self.ptop_distance_list
  self.object_list

  def GetObject2D(self, distance_list):
      #各点と右となりの点との
      for index in range(len(distance_list)):
        #for dist1, dist2 in distance_list:
        dist1 = distance_list[index]
        dist2 = distance_list[index+1]
        tmp = (dist1*dist1) + (dist2*dist2) - (2*dist1*dist*PtoP_ANGLE_COSINE)
        tmp = math.sqrt(tmp)
        ptop_distance_list.append(tmp)
        
      return ptop_distance_list