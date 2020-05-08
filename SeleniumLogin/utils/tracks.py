'''
Function:
	以不同的方式生成滑块轨迹
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-08
'''
import numpy as np


'''滑块轨迹生成器'''
class TrackGenerator():
	def __init__(self):
		self.info = 'generate tracks for slider captcha'
	@staticmethod
	def getTracksByAcceleration(distance):
		tracks = []
		offset = 0
		turning_point = distance * 0.8
		delta_t = 0.2
		v_start = 0
		while offset < distance:
			if offset < turning_point: a = 2
			else: a = -3
			v_end = v_start + a * delta_t
			delta_dis = v_start * delta_t + 0.5 * a * delta_t * delta_t
			offset += round(delta_dis)
			tracks.append(round(delta_dis))
			v_start = v_end
		tracks[-1] -= (offset - distance)
		return tracks
	@staticmethod
	def getTracksByExpfunc(distance):
		tracks = []
		offset = 0
		for i in np.arange(0.2, 12, 0.2):
			delta_dis = round((1 - pow(2, -10 * i / 12)) * distance) - offset
			tracks.append(delta_dis)
			offset += delta_dis
		return tracks