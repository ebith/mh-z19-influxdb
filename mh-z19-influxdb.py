#!/usr/bin/env python3
import mh_z19
from influxdb import InfluxDBClient

homestats = InfluxDBClient(host='raspberrypi4bserver.local',database='homestats')

points = [
  {
    'measurement': 'sensor',
    'tags': { 'location': 'myRoom'},
    'fields': {
      'co2': mh_z19.read()['co2']
    }
  }
]
homestats.write_points(points)