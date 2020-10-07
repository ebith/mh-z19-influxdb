# MH-Z19-InfluxDB

## Usage
```sh
sudo raspi-config # Interfacing Options => Serial(hardware)
sudo pip3 install pyserial influxdb

sudo systemctl enable (realpath  mh-z19-influxdb.service)
sudo systemctl enable --now (realpath mh-z19-influxdb.timer)
sudo systemctl enable --now (realpath  mh-z19-disable-auto-calibration.service)
```

## Zero calibration 
It should be execute while left outdoors for about 30 minutes.
```sh
sudo python3 -m mh_z19 --zero_point_calibration
```
