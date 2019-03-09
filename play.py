#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from random import randint
import pyganim
import os
import math

# Объявляем переменные
WIN_WIDTH = 1366  # Ширина создаваемого окна 1360
WIN_HEIGHT = 768  # Высота 768
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#ffffff"

PLATFORM_WIDTH = 63
PLATFORM_HEIGHT = 64
PLATFORM_COLOR = "#FF6262"
# ICON_DIRR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами
FPS = 60
MOVE_SPEED = 7
WIDTH = 220
HEIGHT = 355


DMG_HAND = 10
RANGE_SPACE = 250
CD_SPACE = 4

CD_SANYA_ULT = 800  # 1 sec   10=0.25 sec #800
CD_ILYA_ULT = 800                           #600
CD_SENYA_ULT = 1200                         #800
CD_GRISHA_ULT = 50                          #50
CD_DIMA_ULT = 1000              #1000
CD_MAX_ULT = 1000              #1000
CD_MAX_PASS = 2500             #2500
CD_IGOR_ULT = 1200             #200
CD_NEK_ULT = 700                #1000

COLOR = "#888888"
JUMP_POWER = 15
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров

BOOLET_WIDTH = 40
MED_WIDTH = 64

ANIMATION_SHOOT = [('detail/shot.png', 0.1)] #пуля
ANIMATION_SHIT = [('detail/shit.png', 0.1)] #пуля
ANIMATION_MED = [('detail/med_mina.png', 0.1)] #пуля

ANIMATION_SHOOT_STAS = [('detail/shot_stas.png', 0.1)] #стас
ANIMATION_SHOOT_STAS_D = [('detail/shot_stas_dawn.png', 0.1)] #стас

ANIMATION_SHOOT_P = [('detail/poisoned.png', 0.1)]
ANIMATION_SHOOT_EGG = [('detail/egg.png', 0.1)]
ANIMATION_SHIT_D = [('detail/d_shot1.png'),
                    ('detail/d_shot2.png'),
                    ('detail/d_shot3.png'),
                    ('detail/d_shot4.png')]
ANIMATION_SHIT_I = [('detail/i_shot1.png'),
                    ('detail/i_shot2.png'),
                    ('detail/i_shot3.png'),
                    ('detail/i_shot4.png')]
ANIMATION_ONIME_L = [('detail/onime_left1.png'),
                    ('detail/onime_left2.png'),
                    ('detail/onime_left3.png')]
ANIMATION_ONIME_R = [('detail/onime_right1.png'),
                    ('detail/onime_right2.png'),
                    ('detail/onime_right3.png')]
ANIMATION_SHOOT_M = [('detail/m_shot1.png', 0.1)] #пуля
#саня
SANYA_ANIMATION_RIGHT = [('detail/sanya_right1.png'),
                         ('detail/sanya_right2.png'),
                         ('detail/sanya_right3.png'),
                         ('detail/sanya_right4.png'),
                         ('detail/sanya_right5.png')]
SANYA_ANIMATION_LEFT = [('detail/sanya_left1.png'),
                        ('detail/sanya_left2.png'),
                        ('detail/sanya_left3.png'),
                        ('detail/sanya_left4.png'),
                        ('detail/sanya_left5.png')]


SANYA_ANIMATION_STAY = [('detail/sanya_stand.png', 0.1)]

SANYA_ANIMATION_STAY_RIGHT = [('detail/sanya_right1.png', 0.1)]
SANYA_ANIMATION_STAY_LEFT = [('detail/sanya_left1.png', 0.1)]

SANYA_ANIMATION_FIGHT_RIGHT = [('detail/sanya_fight_right.png', 0.1)]
SANYA_ANIMATION_FIGHT_LEFT = [('detail/sanya_fight_left.png', 0.1)]

SANYA_ANIMATION_LEFT_FLY  = [('detail/sanya_left_fly.png', 0.1)]
SANYA_ANIMATION_RIGHT_FLY = [('detail/sanya_right_fly.png', 0.1)]
#илья
ILYA_ANIMATION_RIGHT = [('detail/ilya_right1.png'),
                         ('detail/ilya_right2.png'),
                         ('detail/ilya_right3.png'),
                         ('detail/ilya_right4.png')]
ILYA_ANIMATION_LEFT = [('detail/ilya_left1.png'),
                        ('detail/ilya_left2.png'),
                        ('detail/ilya_left3.png'),
                        ('detail/ilya_left4.png')]


ILYA_ANIMATION_STAY = [('detail/ilya_stand.png', 0.1)]

ILYA_ANIMATION_STAY_RIGHT = [('detail/ilya_right1.png', 0.1)]
ILYA_ANIMATION_STAY_LEFT = [('detail/ilya_left1.png', 0.1)]

ILYA_ANIMATION_FIGHT_RIGHT = [('detail/ilya_fight_right.png', 0.1)]
ILYA_ANIMATION_FIGHT_LEFT = [('detail/ilya_fight_left.png', 0.1)]

ILYA_ANIMATION_ULT_RIGHT1 = [('detail/ilya_ult_right1.png', 0.1)]
ILYA_ANIMATION_ULT_RIGHT2 = [('detail/ilya_ult_right2.png', 0.1)]

ILYA_ANIMATION_ULT_LEFT1 = [('detail/ilya_ult_left1.png', 0.1)]
ILYA_ANIMATION_ULT_LEFT2 = [('detail/ilya_ult_left2.png', 0.1)]

#Сеня
SENYA_ANIMATION_RIGHT = [('detail/senya_right1.png'),
                         ('detail/senya_right2.png'),
                         ('detail/senya_right3.png'),
                         ('detail/senya_right4.png'),
                         ('detail/senya_right5.png'),
                         ('detail/senya_right6.png'),
                         ('detail/senya_right7.png'),
                         ('detail/senya_right8.png')]
SENYA_ANIMATION_LEFT = [('detail/senya_left1.png'),
                        ('detail/senya_left2.png'),
                        ('detail/senya_left3.png'),
                        ('detail/senya_left4.png'),
                        ('detail/senya_left5.png'),
                        ('detail/senya_left6.png'),
                        ('detail/senya_left7.png'),
                        ('detail/senya_left8.png')]


SENYA_ANIMATION_STAY = [('detail/senya_stand.png', 0.1)]

SENYA_ANIMATION_STAY_RIGHT = [('detail/senya_right1.png', 0.1)]
SENYA_ANIMATION_STAY_LEFT = [('detail/senya_left1.png', 0.1)]

SENYA_ANIMATION_FIGHT_RIGHT = [('detail/senya_fight_right.png', 0.1)]
SENYA_ANIMATION_FIGHT_LEFT = [('detail/senya_fight_left.png', 0.1)]

SENYA_ANIMATION_ULT1 = [('detail/senya_ult1.png', 0.1)]
SENYA_ANIMATION_ULT2 = [('detail/senya_ult2.png', 0.1)]

#гриша
GRISHA_ANIMATION_RIGHT = [('detail/grisha_right1.png'),
                         ('detail/grisha_right2.png'),
                         ('detail/grisha_right3.png'),
                         ('detail/grisha_right4.png')]
GRISHA_ANIMATION_LEFT = [('detail/grisha_left1.png'),
                        ('detail/grisha_left2.png'),
                        ('detail/grisha_left3.png'),
                        ('detail/grisha_left4.png')]


GRISHA_ANIMATION_STAY = [('detail/grisha_stand.png', 0.1)]

GRISHA_ANIMATION_STAY_RIGHT = [('detail/grisha_right1.png', 0.1)]
GRISHA_ANIMATION_STAY_LEFT = [('detail/grisha_left1.png', 0.1)]

GRISHA_ANIMATION_FIGHT_RIGHT = [('detail/grisha_fight_right.png', 0.1)]
GRISHA_ANIMATION_FIGHT_LEFT = [('detail/grisha_fight_left.png', 0.1)]

GRISHA_ANIMATION_ULT  = [('detail/grisha_ult.png', 0.1)]

#дима
DIMA_ANIMATION_RIGHT = [('detail/dima_right1.png'),
                         ('detail/dima_right2.png'),
                         ('detail/dima_right3.png'),
                         ('detail/dima_right4.png')]
DIMA_ANIMATION_LEFT = [('detail/dima_left1.png'),
                        ('detail/dima_left2.png'),
                        ('detail/dima_left3.png'),
                        ('detail/dima_left4.png')]


DIMA_ANIMATION_STAY = [('detail/dima_stand.png', 0.1)]

DIMA_ANIMATION_STAY_RIGHT = [('detail/dima_right1.png', 0.1)]
DIMA_ANIMATION_STAY_LEFT = [('detail/dima_left1.png', 0.1)]

DIMA_ANIMATION_FIGHT_RIGHT = [('detail/dima_fight_right.png', 0.1)]
DIMA_ANIMATION_FIGHT_LEFT = [('detail/dima_fight_left.png', 0.1)]

DIMA_ANIMATION_ULT_RIGHT1 = [('detail/dima_ult_right1.png', 0.1)]
DIMA_ANIMATION_ULT_RIGHT2 = [('detail/dima_ult_right2.png', 0.1)]

DIMA_ANIMATION_ULT_LEFT1 = [('detail/dima_ult_left1.png', 0.1)]
DIMA_ANIMATION_ULT_LEFT2 = [('detail/dima_ult_left2.png', 0.1)]

#миша
MISHA_ANIMATION_RIGHT = [('detail/misha_right1.png'),
                         ('detail/misha_right2.png'),
                         ('detail/misha_right3.png'),
                         ('detail/misha_right4.png')]
MISHA_ANIMATION_LEFT = [('detail/misha_left1.png'),
                        ('detail/misha_left2.png'),
                        ('detail/misha_left3.png'),
                        ('detail/misha_left4.png')]


MISHA_ANIMATION_STAY = [('detail/misha_stand.png', 0.1)]

MISHA_ANIMATION_STAY_RIGHT = [('detail/misha_right1.png', 0.1)]
MISHA_ANIMATION_STAY_LEFT = [('detail/misha_left1.png', 0.1)]

MISHA_ANIMATION_FIGHT_RIGHT = [('detail/misha_fight_right.png', 0.1)]
MISHA_ANIMATION_FIGHT_LEFT = [('detail/misha_fight_left.png', 0.1)]

MISHA_ANIMATION_ULT_RIGHT = [('detail/misha_ult_right1.png'),
                             ('detail/misha_ult_right2.png')]

MISHA_ANIMATION_ULT_LEFT = [('detail/misha_ult_left1.png'),
                            ('detail/misha_ult_left2.png')]

MISHA_ANIMATION_RIGHT_P = [('detail/misha_right1_p.png'),
                         ('detail/misha_right2_p.png'),
                         ('detail/misha_right3_p.png'),
                         ('detail/misha_right4_p.png')]
MISHA_ANIMATION_LEFT_P = [('detail/misha_left1_p.png'),
                        ('detail/misha_left2_p.png'),
                        ('detail/misha_left3_p.png'),
                        ('detail/misha_left4_p.png')]


MISHA_ANIMATION_STAY_RIGHT_P = [('detail/misha_right1_p.png', 0.1)]
MISHA_ANIMATION_STAY_LEFT_P = [('detail/misha_left1_p.png', 0.1)]

MISHA_ANIMATION_FIGHT_RIGHT_P = [('detail/misha_fight_right_p.png', 0.1)]
MISHA_ANIMATION_FIGHT_LEFT_P = [('detail/misha_fight_left_p.png', 0.1)]

MISHA_ANIMATION_ULT_RIGHT_P = [('detail/misha_ult_right1_p.png'),
                             ('detail/misha_ult_right2_p.png')]

MISHA_ANIMATION_ULT_LEFT_P = [('detail/misha_ult_left1_p.png'),
                            ('detail/misha_ult_left2_p.png')]

#Игорь
IGOR_ANIMATION_RIGHT = [('detail/igor_right2.png'),
                         ('detail/igor_right3.png'),
                         ('detail/igor_right4.png')]
IGOR_ANIMATION_LEFT = [('detail/igor_left2.png'),
                         ('detail/igor_left3.png'),
                         ('detail/igor_left4.png')]


IGOR_ANIMATION_STAY = [('detail/igor_stand.png', 0.1)]

IGOR_ANIMATION_STAY_RIGHT = [('detail/igor_right1.png', 0.1)]
IGOR_ANIMATION_STAY_LEFT = [('detail/igor_left1.png', 0.1)]

IGOR_ANIMATION_FIGHT_RIGHT = [('detail/igor_fight_right.png', 0.1)]
IGOR_ANIMATION_FIGHT_LEFT = [('detail/igor_fight_left.png', 0.1)]

IGOR_ANIMATION_ULT1 = [('detail/igor_ult1.png', 0.1)]
IGOR_ANIMATION_ULT2 = [('detail/igor_ult2.png', 0.1)]
IGOR_ANIMATION_ULT3 = [('detail/igor_ult3.png', 0.1)]
IGOR_ANIMATION_ULT4 = [('detail/igor_ult4.png', 0.1)]


IGOR_ANIMATION_ULT_RIGHT = [('detail/igor_ult_right.png', 0.1)]
IGOR_ANIMATION_ULT_LEFT = [('detail/igor_ult_left.png', 0.1)]

#некит
NIK_ANIMATION_RIGHT = [('detail/nik_right1.png'),
                         ('detail/nik_right2.png'),
                         ('detail/nik_right3.png'),
                         ('detail/nik_right4.png')]
NIK_ANIMATION_LEFT = [('detail/nik_left1.png'),
                        ('detail/nik_left2.png'),
                        ('detail/nik_left3.png'),
                        ('detail/nik_left4.png')]


NIK_ANIMATION_STAY = [('detail/nik_stand.png', 0.1)]

NIK_ANIMATION_STAY_RIGHT = [('detail/nik_right1.png', 0.1)]
NIK_ANIMATION_STAY_LEFT = [('detail/nik_left1.png', 0.1)]

NIK_ANIMATION_FIGHT_RIGHT = [('detail/nik_fight_right.png', 0.1)]
NIK_ANIMATION_FIGHT_LEFT = [('detail/nik_fight_left.png', 0.1)]

NIK_ANIMATION_ULT_RIGHT = [('detail/nik_ult_right.png', 0.1)]
NIK_ANIMATION_ULT_LEFT = [('detail/nik_ult_left.png', 0.1)]


#макс
MAX_ANIMATION_RIGHT = [('detail/max_right1.png'),
                         ('detail/max_right2.png'),
                         ('detail/max_right3.png'),
                         ('detail/max_right4.png')]
MAX_ANIMATION_LEFT = [('detail/max_left1.png'),
                        ('detail/max_left2.png'),
                        ('detail/max_left3.png'),
                        ('detail/max_left4.png')]


MAX_ANIMATION_STAY = [('detail/max_stand.png', 0.1)]

MAX_ANIMATION_STAY_RIGHT = [('detail/max_right1.png', 0.1)]
MAX_ANIMATION_STAY_LEFT = [('detail/max_left1.png', 0.1)]

MAX_ANIMATION_FIGHT_RIGHT = [('detail/max_fight_right.png', 0.1)]
MAX_ANIMATION_FIGHT_LEFT = [('detail/max_fight_left.png', 0.1)]

MAX_ANIMATION_ULT_RIGHT = [('detail/max_ult_right1.png'),
                             ('detail/max_ult_right2.png'),
                           ('detail/max_ult_right2.png')]

MAX_ANIMATION_ULT_LEFT = [('detail/max_ult_left1.png'),
                            ('detail/max_ult_left2.png'),
                          ('detail/max_ult_left2.png')]

#enemy
ENEMY_ANIMATION_RIGHT = [('enemy/enemy/enemy_right1.png'),
                         ('enemy/enemy/enemy_right2.png'),
                         ('enemy/enemy/enemy_right3.png')]
ENEMY_ANIMATION_LEFT = [('enemy/enemy/enemy_left1.png'),
                        ('enemy/enemy/enemy_left2.png'),
                        ('enemy/enemy/enemy_left3.png')]

ENEMY_ANIMATION_FIGHT_RIGHT = [('enemy/enemy/enemy_fight_right1.png', 0.1)]
ENEMY_ANIMATION_FIGHT_LEFT = [('enemy/enemy/enemy_fight_left1.png', 0.1)]

ENEMY_ANIMATION_STAY_RIGHT = [('enemy/enemy/enemy_right1.png', 0.1)]
ENEMY_ANIMATION_STAY_LEFT = [('enemy/enemy/enemy_left1.png', 0.1)]

ENEMY_ANIMATION_STAN = [('enemy/enemy/enemy_stun.png', 0.1)]

#enemy pistol
ENEMYPS_ANIMATION_RIGHT = [('enemy/enemypis/enemypis_right1.png'),
                         ('enemy/enemypis/enemypis_right2.png'),
                         ('enemy/enemypis/enemypis_right3.png')]
ENEMYPS_ANIMATION_LEFT = [('enemy/enemypis/enemypis_left1.png'),
                        ('enemy/enemypis/enemypis_left2.png'),
                        ('enemy/enemypis/enemypis_left3.png')]

ENEMYPS_ANIMATION_FIGHT_RIGHT1 = [('enemy/enemypis/enemypis_fight_right1.png', 0.1)]
ENEMYPS_ANIMATION_FIGHT_LEFT1 = [('enemy/enemypis/enemypis_fight_left1.png', 0.1)]

ENEMYPS_ANIMATION_FIGHT_RIGHT2 = [('enemy/enemypis/enemypis_fight_right2.png', 0.1)]
ENEMYPS_ANIMATION_FIGHT_LEFT2 = [('enemy/enemypis/enemypis_fight_left2.png', 0.1)]

ENEMYPS_ANIMATION_STAY_RIGHT = [('enemy/enemypis/enemypis_right1.png', 0.1)]
ENEMYPS_ANIMATION_STAY_LEFT = [('enemy/enemypis/enemypis_left1.png', 0.1)]
ENEMYPS_ANIMATION_STAN = [('enemy/enemypis/enemypis_stan.png', 0.1)]

#enemy automat
ENEMYAU_ANIMATION_RIGHT = [('enemy/enemyaut/enemyaut_right1.png'),
                         ('enemy/enemyaut/enemyaut_right2.png'),
                         ('enemy/enemyaut/enemyaut_right3.png')]
ENEMYAU_ANIMATION_LEFT = [('enemy/enemyaut/enemyaut_left1.png'),
                        ('enemy/enemyaut/enemyaut_left2.png'),
                        ('enemy/enemyaut/enemyaut_left3.png')]

ENEMYAU_ANIMATION_FIGHT_RIGHT1 = [('enemy/enemyaut/enemyaut_fight_right1.png', 0.1)]
ENEMYAU_ANIMATION_FIGHT_LEFT1 = [('enemy/enemyaut/enemyaut_fight_left1.png', 0.1)]

ENEMYAU_ANIMATION_FIGHT_RIGHT2 = [('enemy/enemyaut/enemyaut_fight_right2.png', 0.1)]
ENEMYAU_ANIMATION_FIGHT_LEFT2 = [('enemy/enemyaut/enemyaut_fight_left2.png', 0.1)]

ENEMYAU_ANIMATION_STAY_RIGHT = [('enemy/enemyaut/enemyaut_right1.png', 0.1)]
ENEMYAU_ANIMATION_STAY_LEFT = [('enemy/enemyaut/enemyaut_left1.png', 0.1)]

ENEMYAU_ANIMATION_STAN = [('enemy/enemyaut/enemyaut_stan.png', 0.1)]

#turrel
TURREL_ANIMATION_FIGHT_RIGHT1 = [('enemy/turrel/turrel_right2.png', 0.1)]
TURREL_ANIMATION_FIGHT_LEFT1 = [('enemy/turrel/turrel_left2.png', 0.1)]

TURREL_ANIMATION_FIGHT_RIGHT2 = [('enemy/turrel/turrel_right3.png', 0.1)]
TURREL_ANIMATION_FIGHT_LEFT2 = [('enemy/turrel/turrel_left3.png', 0.1)]

TURREL_ANIMATION_STAY_RIGHT = [('enemy/turrel/turrel_right1.png', 0.1)]
TURREL_ANIMATION_STAY_LEFT = [('enemy/turrel/turrel_left1.png', 0.1)]

TURREL_ANIMATION_STAN = [('enemy/turrel/turrel_stan.png', 0.1)]

#zombe
ZOMBE_ANIMATION_RIGHT = [('enemy/zombe/zombe_right1.png'),
                         ('enemy/zombe/zombe_right2.png'),
                         ('enemy/zombe/zombe_right3.png')]
ZOMBE_ANIMATION_LEFT = [('enemy/zombe/zombe_left1.png'),
                        ('enemy/zombe/zombe_left2.png'),
                        ('enemy/zombe/zombe_left3.png')]

ZOMBE_ANIMATION_FIGHT_RIGHT = [('enemy/zombe/zombe_fight_right1.png', 0.1)]
ZOMBE_ANIMATION_FIGHT_LEFT = [('enemy/zombe/zombe_fight_left1.png', 0.1)]

ZOMBE_ANIMATION_STAY_RIGHT = [('enemy/zombe/zombe_right1.png', 0.1)]
ZOMBE_ANIMATION_STAY_LEFT = [('enemy/zombe/zombe_left1.png', 0.1)]

ZOMBE_ANIMATION_STAN = [('enemy/zombe/zombe_stan.png', 0.1)]

#mnogonozha
MNOGONOZA_ANIMATION_RIGHT = [('enemy/mnogonoza/mnogonoza_right1.png'),
                         ('enemy/mnogonoza/mnogonoza_right2.png'),
                         ('enemy/mnogonoza/mnogonoza_right3.png')]
MNOGONOZA_ANIMATION_LEFT = [('enemy/mnogonoza/mnogonoza_left1.png'),
                        ('enemy/mnogonoza/mnogonoza_left2.png'),
                        ('enemy/mnogonoza/mnogonoza_left3.png')]

MNOGONOZA_ANIMATION_FIGHT_RIGHT = [('enemy/mnogonoza/mnogonoza_fight_right1.png', 0.1)]
MNOGONOZA_ANIMATION_FIGHT_LEFT = [('enemy/mnogonoza/mnogonoza_fight_left1.png', 0.1)]

MNOGONOZA_ANIMATION_STAY_RIGHT = [('enemy/mnogonoza/mnogonoza_right1.png', 0.1)]
MNOGONOZA_ANIMATION_STAY_LEFT = [('enemy/mnogonoza/mnogonoza_left1.png', 0.1)]

MNOGONOZA_ANIMATION_STAN = [('enemy/mnogonoza/mnogonoza_stan.png', 0.1)]

# pudje
PUDJE_ANIMATION_RIGHT = [('enemy/pudje/pudje_right1.png'),
                         ('enemy/pudje/pudje_right2.png'),
                         ('enemy/pudje/pudje_right3.png')]
PUDJE_ANIMATION_LEFT = [('enemy/pudje/pudje_left1.png'),
                        ('enemy/pudje/pudje_left2.png'),
                        ('enemy/pudje/pudje_left3.png')]

PUDJE_ANIMATION_FIGHT_RIGHT1 = [('enemy/pudje/pudje_fight_right1.png', 0.1)]
PUDJE_ANIMATION_FIGHT_LEFT1 = [('enemy/pudje/pudje_fight_left1.png', 0.1)]

PUDJE_ANIMATION_FIGHT_RIGHT2 = [('enemy/pudje/pudje_fight_right2.png', 0.1)]
PUDJE_ANIMATION_FIGHT_LEFT2 = [('enemy/pudje/pudje_fight_left2.png', 0.1)]

PUDJE_ANIMATION_STAY_RIGHT = [('enemy/pudje/pudje_right1.png', 0.1)]
PUDJE_ANIMATION_STAY_LEFT = [('enemy/pudje/pudje_left1.png', 0.1)]

PUDJE_ANIMATION_STAN = [('enemy/pudje/pudje_stan.png', 0.1)]

# chikne
CHIKEN_ANIMATION_RIGHT = [('enemy/chiken/chiken_right1.png'),
                         ('enemy/chiken/chiken_right2.png')]
CHIKEN_ANIMATION_LEFT = [('enemy/chiken/chiken_left1.png'),
                        ('enemy/chiken/chiken_left2.png')]

#elit_enemy
ELITEN_ANIMATION_RIGHT = [('enemy/elit_enemy/elitenemy_right1.png'),
                         ('enemy/elit_enemy/elitenemy_right2.png'),
                         ('enemy/elit_enemy/elitenemy_right3.png')]
ELITEN_ANIMATION_LEFT = [('enemy/elit_enemy/elitenemy_left1.png'),
                        ('enemy/elit_enemy/elitenemy_left2.png'),
                        ('enemy/elit_enemy/elitenemy_left3.png')]

ELITEN_ANIMATION_FIGHT_RIGHT = [('enemy/elit_enemy/elitenemy_fight_right1.png', 0.1)]
ELITEN_ANIMATION_FIGHT_LEFT = [('enemy/elit_enemy/elitenemy_fight_left1.png', 0.1)]

ELITEN_ANIMATION_STAY_RIGHT = [('enemy/elit_enemy/elitenemy_right1.png', 0.1)]
ELITEN_ANIMATION_STAY_LEFT = [('enemy/elit_enemy/elitenemy_left1.png', 0.1)]

ELITEN_ANIMATION_STAN = [('enemy/elit_enemy/elitenemy_stan.png', 0.1)]

#enemy automat
ELITAU_ANIMATION_RIGHT = [('enemy/elit_automat/elitautomat_right1.png'),
                         ('enemy/elit_automat/elitautomat_right2.png'),
                         ('enemy/elit_automat/elitautomat_right3.png')]
ELITAU_ANIMATION_LEFT = [('enemy/elit_automat/elitautomat_left1.png'),
                        ('enemy/elit_automat/elitautomat_left2.png'),
                        ('enemy/elit_automat/elitautomat_left3.png')]

ELITAU_ANIMATION_FIGHT_RIGHT1 = [('enemy/elit_automat/elitautomat_fight_right1.png', 0.1)]
ELITAU_ANIMATION_FIGHT_LEFT1 = [('enemy/elit_automat/elitautomat_fight_left1.png', 0.1)]

ELITAU_ANIMATION_FIGHT_RIGHT2 = [('enemy/elit_automat/elitautomat_fight_right2.png', 0.1)]
ELITAU_ANIMATION_FIGHT_LEFT2 = [('enemy/elit_automat/elitautomat_fight_left2.png', 0.1)]

ELITAU_ANIMATION_STAY_RIGHT = [('enemy/elit_automat/elitautomat_right1.png', 0.1)]
ELITAU_ANIMATION_STAY_LEFT = [('enemy/elit_automat/elitautomat_left1.png', 0.1)]

ELITAU_ANIMATION_RIGHT_KUV = [('enemy/elit_automat/elitautomat_right_kuvirok.png', 0.1)]
ELITAU_ANIMATION_LEFT_KUV = [('enemy/elit_automat/elitautomat_left_kuvirok.png', 0.1)]

ELITAU_ANIMATION_STAN = [('enemy/elit_automat/elitautomat_stan.png', 0.1)]

# ZOLOTOV
ZOLOTOV_ANIMATION_RIGHT = [('enemy/zolotov/zolotov_right1.png'),
                         ('enemy/zolotov/zolotov_right2.png'),
                         ('enemy/zolotov/zolotov_right3.png'),
                        ('enemy/zolotov/zolotov_right4.png')]
ZOLOTOV_ANIMATION_LEFT = [('enemy/zolotov/zolotov_left1.png'),
                        ('enemy/zolotov/zolotov_left2.png'),
                        ('enemy/zolotov/zolotov_left3.png'),
                        ('enemy/zolotov/zolotov_left4.png')]

ZOLOTOV_ANIMATION_FIGHT_RIGHT = [('enemy/zolotov/zolotov_fight_right.png', 0.1)]
ZOLOTOV_ANIMATION_FIGHT_LEFT = [('enemy/zolotov/zolotov_fight_left.png', 0.1)]

ZOLOTOV_ANIMATION_STAY_RIGHT = [('enemy/zolotov/zolotov_right1.png', 0.1)]
ZOLOTOV_ANIMATION_STAY_LEFT = [('enemy/zolotov/zolotov_left1.png', 0.1)]

# ZOLOTOV
STAS_ANIMATION_RIGHT = [('enemy/zolotov/zolotov_right1.png'),
                         ('enemy/zolotov/zolotov_right2.png'),
                         ('enemy/zolotov/zolotov_right3.png'),
                        ('enemy/zolotov/zolotov_right4.png')]
STAS_ANIMATION_LEFT = [('enemy/zolotov/zolotov_left1.png'),
                        ('enemy/zolotov/zolotov_left2.png'),
                        ('enemy/zolotov/zolotov_left3.png'),
                        ('enemy/zolotov/zolotov_left4.png')]

STAS_ANIMATION_FIGHT_RIGHT = [('enemy/zolotov/zolotov_fight_right.png', 0.1)]
STAS_ANIMATION_FIGHT_LEFT = [('enemy/zolotov/zolotov_fight_left.png', 0.1)]

STAS_ANIMATION_STAY_RIGHT = [('enemy/zolotov/zolotov_right1.png', 0.1)]
STAS_ANIMATION_STAY_LEFT = [('enemy/zolotov/zolotov_left1.png', 0.1)]

# STAS
STAS_ANIMATION_RIGHT = [('enemy/stas/stas_right1.png'),
                         ('enemy/stas/stas_right2.png')]
STAS_ANIMATION_LEFT = [('enemy/stas/stas_left1.png'),
                        ('enemy/stas/stas_left2.png')]

STAS_ANIMATION_FIGHT_RIGHT1 = [('enemy/stas/stas_fight_right1.png', 0.1)]
STAS_ANIMATION_FIGHT_LEFT1 = [('enemy/stas/stas_fight_left1.png', 0.1)]

STAS_ANIMATION_FIGHT_RIGHT2 = [('enemy/stas/stas_fight_right2.png', 0.1)]
STAS_ANIMATION_FIGHT_LEFT2 = [('enemy/stas/stas_fight_left2.png', 0.1)]

STAS_ANIMATION_FIGHT_RIGHT3 = [('enemy/stas/stas_fight_right3.png', 0.1)]
STAS_ANIMATION_FIGHT_LEFT3 = [('enemy/stas/stas_fight_left3.png', 0.1)]

# PUTIN
PUTIN_ANIMATION_RIGHT = [('enemy/putin/putin_right1.png'),
                         ('enemy/putin/putin_right2.png')]
PUTIN_ANIMATION_LEFT = [('enemy/putin/putin_left1.png'),
                        ('enemy/putin/putin_left2.png')]

PUTIN_ANIMATION_FIRED_RIGHT = [('enemy/putin/putin_right_fired1.png'),
                               ('enemy/putin/putin_right_fired2.png')]
PUTIN_ANIMATION_FIRED_LEFT = [('enemy/putin/putin_left_fired1.png'),
                              ('enemy/putin/putin_left_fired2.png')]

PUTIN_ANIMATION_FIGHT_RIGHT = [('enemy/putin/putin_right_fired3.png', 0.1)]
PUTIN_ANIMATION_FIGHT_LEFT = [('enemy/putin/putin_left_fired3.png', 0.1)]





class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/platform1.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Shipi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/platform2.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Svaston(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/platform3.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Mina(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/platform4.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT

class Barikada(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/platform1.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Salo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/platform5.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class DOOR(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((138, 310))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("blocks/the_door.png")
        self.rect = pygame.Rect(x, y, 138, 310)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):

        self.hp = 120
        self.max_hp = self.hp
        self.speed = 4
        self.dmg = 10
        self.mele = True
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 150

        self.cooldown_punch = 35
        self.cooldown_shot = 0
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.ii_save = True
        self.stuned = False

        self.agression = True

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ENEMY_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ENEMY_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ENEMY_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ENEMY_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()
        self.cooldown = 0
        self.timer = pygame.time.Clock()

        # стоим налево
        self.boltAnimRightStay = pyganim.PygAnimation(ENEMY_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ENEMY_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStuned = pyganim.PygAnimation(ENEMY_ANIMATION_STAN)
        self.boltAnimStuned.play()


    def update(self, platforms, xplayer, yplayer, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.dmg_deal = 0

        if self.cooldown > 0:
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStuned.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:
                if self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.play()
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))
                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:

                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10
            elif self.cooldown <= self.cooldown_punch - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))

        if self.ii_save:
            if self.left and xplayer > self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = False
                self.right = True
                self.ii_save = False
            if self.right and xplayer < self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = True
                self.right = False
                self.ii_save = False

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Enemy_pistol(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 100
        self.max_hp = self.hp
        self.speed = 4
        self.watch = 200
        self.dmg = 10
        self.mele = False
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 600

        self.cooldown_punch = 0
        self.cooldown_shot = 140
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.agression = True
        self.ii_save = True
        self.stuned = False

        self.cooldown = 0

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ENEMYPS_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ENEMYPS_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо1
        self.boltAnimRightFight = pyganim.PygAnimation(ENEMYPS_ANIMATION_FIGHT_RIGHT1)
        self.boltAnimRightFight.play()

        # бьем влево1
        self.boltAnimLeftFight = pyganim.PygAnimation(ENEMYPS_ANIMATION_FIGHT_LEFT1)
        self.boltAnimLeftFight.play()

        # бьем вправо2
        self.boltAnimRightFight2 = pyganim.PygAnimation(ENEMYPS_ANIMATION_FIGHT_RIGHT2)
        self.boltAnimRightFight2.play()

        # бьем влево2
        self.boltAnimLeftFight2 = pyganim.PygAnimation(ENEMYPS_ANIMATION_FIGHT_LEFT2)
        self.boltAnimLeftFight2.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ENEMYPS_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ENEMYPS_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(ENEMYPS_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        if self.cooldown > 0:
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:

                if self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))
                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
            elif self.cooldown <= self.cooldown_shot - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight2.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight2.blit(self.image, (0, 0))

        if self.ii_save:
            if self.left and xplayer > self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = False
                self.right = True
                self.ii_save = False
            if self.right and xplayer < self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = True
                self.right = False
                self.ii_save = False

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Enemy_automat(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 100
        self.max_hp = self.hp
        self.speed = 4
        self.watch = 200
        self.dmg = 10
        self.mele = False
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 600

        self.cooldown_punch = 0
        self.cooldown_shot = 25
        self.cooldown_reload = 220

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.bullets = 3
        self.cooldown = 0
        self.reload = 0

        self.timer = pygame.time.Clock()

        self.agression = True
        self.ii_save = True
        self.stuned = False

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ENEMYAU_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ENEMYAU_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ENEMYAU_ANIMATION_FIGHT_RIGHT1)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ENEMYAU_ANIMATION_FIGHT_LEFT1)
        self.boltAnimLeftFight.play()

        # бьем вправо2
        self.boltAnimRightFight2 = pyganim.PygAnimation(ENEMYAU_ANIMATION_FIGHT_RIGHT2)
        self.boltAnimRightFight2.play()

        # бьем влево2
        self.boltAnimLeftFight2 = pyganim.PygAnimation(ENEMYAU_ANIMATION_FIGHT_LEFT2)
        self.boltAnimLeftFight2.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ENEMYAU_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()
        # self.boltAnimRightStay.blit(self.image, (0, 0))

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ENEMYAU_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(ENEMYAU_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)

        if self.cooldown > 0:  # 25
            self.cooldown -= SECOND

        if self.reload > 0:
            self.reload -= SECOND
            if self.reload <= 0:
                self.reload = 0
                self.bullets = 3

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:
                if self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))
                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    if self.bullets > 0:
                        self.bullets -= 1
                        self.boltAnimLeftFight.blit(self.image, (0, 0))
                        self.cooldown = self.cooldown_shot
                        shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                        entities.add(shot1)
                        bad_bullets.append(shot1)
                    elif self.reload == 0:
                        self.boltAnimLeftFight.blit(self.image, (0, 0))  # -- reload
                        self.reload = self.cooldown_reload
                    else:
                        self.boltAnimLeftFight.blit(self.image, (0, 0))

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    if self.bullets > 0:
                        self.bullets -= 1
                        self.boltAnimRightFight.blit(self.image, (0, 0))
                        self.cooldown = self.cooldown_shot
                        shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                        entities.add(shot1)
                        bad_bullets.append(shot1)
                    elif self.reload == 0:
                        self.boltAnimRightFight.blit(self.image, (0, 0))  # -- reload
                        self.reload = self.cooldown_reload
                    else:
                        self.boltAnimRightFight.blit(self.image, (0, 0))
            elif self.cooldown <= self.cooldown_shot - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight2.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight2.blit(self.image, (0, 0))

        if self.ii_save:
            if self.left and xplayer > self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = False
                self.right = True
                self.ii_save = False
            if self.right and xplayer < self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = True
                self.right = False
                self.ii_save = False

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Turrel(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 100
        self.speed = 0
        self.watch = 200
        self.dmg = 10
        self.mele = False
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 1400

        self.cooldown_punch = 0
        self.cooldown_shot = 75
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = 220
        self.height = 180

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.bullets = 4
        self.cooldown = 0
        self.reload = 0
        self.timer = pygame.time.Clock()

        self.agression = True
        self.stuned = False

        self.image.set_colorkey(pygame.Color(COLOR))

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(TURREL_ANIMATION_FIGHT_RIGHT1)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(TURREL_ANIMATION_FIGHT_LEFT1)
        self.boltAnimLeftFight.play()

        # бьем вправо2
        self.boltAnimRightFight2 = pyganim.PygAnimation(TURREL_ANIMATION_FIGHT_RIGHT2)
        self.boltAnimRightFight2.play()

        # бьем влево2
        self.boltAnimLeftFight2 = pyganim.PygAnimation(TURREL_ANIMATION_FIGHT_LEFT2)
        self.boltAnimLeftFight2.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(TURREL_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(TURREL_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(TURREL_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)

        if self.cooldown > 0:
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:

                if self.left:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))

                if self.right:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))

                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + WIDTH * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + WIDTH * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
            elif self.cooldown <= self.cooldown_shot - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight2.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight2.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Zombe(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 120
        self.speed = 4
        self.dmg = 10
        self.mele = True
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 150
        self.agr = 600

        self.cooldown_punch = 20
        self.cooldown_shot = 0
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.agression = True
        self.stuned = False

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ZOMBE_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ZOMBE_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ZOMBE_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ZOMBE_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()
        self.cooldown = 0
        self.timer = pygame.time.Clock()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ZOMBE_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ZOMBE_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(ZOMBE_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.agr_x_1 = self.rect.x - self.agr
        self.agr_x_2 = self.rect.x + self.agr

        self.dmg_deal = 0
        if self.cooldown > 0:
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:

                if self.left and xplayer >= self.agr_x_1 and xplayer <= self.rect.x:
                    self.xvel = -2 * self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))
                elif self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))
                if self.right and xplayer <= self.agr_x_2 and xplayer >= self.rect.x:
                    self.xvel = 2 * self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))
                elif self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))

                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:

                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10

            elif self.cooldown <= self.cooldown_punch - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Mnogonoza(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 200
        self.speed = 4
        self.dmg = 20
        self.mele = True
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 150
        self.agr = 600

        self.cooldown_punch = 20
        self.cooldown_shot = 0
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.agression = True
        self.stuned = False

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in MNOGONOZA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in MNOGONOZA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(MNOGONOZA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(MNOGONOZA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()
        self.cooldown = 0
        self.timer = pygame.time.Clock()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(MNOGONOZA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(MNOGONOZA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(MNOGONOZA_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.agr_x_1 = self.rect.x - self.agr
        self.agr_x_2 = self.rect.x + self.agr

        self.dmg_deal = 0
        if self.cooldown > 0:
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:

                if self.left and xplayer >= self.agr_x_1 and xplayer <= self.rect.x:
                    self.xvel = -3 * self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))
                elif self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))
                if self.right and xplayer <= self.agr_x_2 and xplayer >= self.rect.x:
                    self.xvel = 3 * self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))
                elif self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))

                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:

                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10

            elif self.cooldown <= self.cooldown_punch - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Pudje(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 350
        self.speed = 3
        self.watch = 200
        self.dmg = 30
        self.mele = False
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 600
        self.atack_zone_mele = 150

        self.cooldown_punch = 60
        self.cooldown_shot = 500
        self.cooldown_reload = 0

        self.stoped = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.agression = True
        self.stuned = False
        self.cooldown = 0


        self.image.set_colorkey(pygame.Color(COLOR))
        anim_del=0.25

        boltAnim = []
        for anim in PUDJE_ANIMATION_RIGHT:
            boltAnim.append((anim, anim_del))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in PUDJE_ANIMATION_LEFT:
            boltAnim.append((anim, anim_del))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(PUDJE_ANIMATION_FIGHT_RIGHT1)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(PUDJE_ANIMATION_FIGHT_LEFT1)
        self.boltAnimLeftFight.play()

        # стреляем вправо
        self.boltAnimRightFight2 = pyganim.PygAnimation(PUDJE_ANIMATION_FIGHT_RIGHT2)
        self.boltAnimRightFight2.play()

        # стреляем влево
        self.boltAnimLeftFight2 = pyganim.PygAnimation(PUDJE_ANIMATION_FIGHT_LEFT2)
        self.boltAnimLeftFight2.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(PUDJE_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(PUDJE_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(PUDJE_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.dmg_deal = 0
        self.STOTED = False
        if self.cooldown > 0:
            self.cooldown -= SECOND
        if self.stoped > 0:
            self.stoped -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:

            if self.cooldown <= 0:
                # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.STOTED = True
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight2.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    self.stoped = self.cooldown_punch
                    shot1 = poisoned_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.STOTED = True
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight2.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    self.stoped = self.cooldown_punch
                    shot1 = poisoned_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
            if self.stoped <= 0:
                if self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))

                if self.left and xplayer > self.rect.x - self.atack_zone_mele and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.STOTED = True
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.stoped = self.cooldown_punch
                    self.dmg_deal = self.dmg

                elif self.right and xplayer < self.rect.x + self.atack_zone_mele and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.STOTED = True
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.stoped = self.cooldown_punch
                    self.dmg_deal = self.dmg
            elif not self.STOTED:
                if self.left:
                    self.xvel = 0  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = 0  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))
            elif self.STOTED:
                if self.left:
                    self.xvel = 0  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight2.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = 0  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight2.blit(self.image, (0, 0))
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Chicken(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 300
        self.speed = 4
        self.watch = 200
        self.dmg = 10
        self.mele = False
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.cooldown_punch = 0
        self.cooldown_shot = 40
        self.cooldown_reload = 220

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        # self.onGround = False  # На земле ли я?
        self.width = 220
        self.height = 180

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.bullets = 5
        self.cooldown = 0
        self.reload = 0
        self.stuned = False

        self.timer = pygame.time.Clock()

        self.agression = True

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in CHIKEN_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in CHIKEN_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()


    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.atack_zone = int((yplayer - self.rect.y) / 2.7)

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)

        if self.cooldown > 0:  # 25
            self.cooldown -= SECOND

        if self.reload > 0:
            self.reload -= SECOND
            if self.reload <= 0:
                self.reload = 0
                self.bullets = 5

        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))

        if self.cooldown <= 0:
            # по исксу зона ударов                           #по игрику
            if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                    yplayer >= self.agr_y_1:  # and yplayer<=self.agr_y_2:
                self.xvel = -self.speed
                self.image.fill(pygame.Color(COLOR))
                if self.bullets > 0:
                    self.bullets -= 1
                    self.boltAnimLeft.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = egg_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
                elif self.reload == 0:
                    self.boltAnimLeft.blit(self.image, (0, 0))  # -- reload
                    self.reload = self.cooldown_reload
                else:
                    self.boltAnimLeft.blit(self.image, (0, 0))

            if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                    yplayer >= self.agr_y_1:
                self.xvel = self.speed
                self.image.fill(pygame.Color(COLOR))
                if self.bullets > 0:
                    self.bullets -= 1
                    self.boltAnimRight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = egg_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
                elif self.reload == 0:
                    self.boltAnimRight.blit(self.image, (0, 0))  # -- reload
                    self.reload = self.cooldown_reload
                else:
                    self.boltAnimRight.blit(self.image, (0, 0))

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True


class Elit_Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 150
        self.max_hp = self.hp
        self.speed = 4
        self.dmg = 20
        self.mele = True
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 150

        self.cooldown_punch = 35
        self.cooldown_shot = 0
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.agression = True
        self.ii_save = True
        self.stuned = False

        self.kuvirok = False
        self.kuvirok_left = False
        self.kuvirok_right = False
        self.kuvirok_time = 0

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ELITEN_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ELITEN_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ELITEN_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ELITEN_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()
        self.cooldown = 0
        self.timer = pygame.time.Clock()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ELITEN_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ELITEN_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим налево
        self.boltAnimStan = pyganim.PygAnimation(ELITEN_ANIMATION_STAN)
        self.boltAnimStan.play()

    def update(self, platforms, xplayer, yplayer, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.dmg_deal = 0
        if self.cooldown > 0:
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if self.cooldown <= 0:
                if self.left:
                    self.xvel = -self.speed  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.play()
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if self.right:
                    self.xvel = self.speed  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))
                    # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:

                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_punch
                    if self.damagelvl_y >= yplayer and self.damagelvl_y <= yplayer + HEIGHT:
                        self.dmg_deal = 10
            elif self.cooldown <= self.cooldown_punch - int(self.cooldown / 2):
                if self.left:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))
                if self.right:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))

        if self.ii_save:
            if self.left and xplayer > self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = False
                self.right = True
                # self.ii_save = False
            if self.right and xplayer < self.rect.x and self.hp <= self.max_hp * 0.5:
                self.left = True
                self.right = False
                # self.ii_save = False

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Elit_automat(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 120
        self.max_hp = self.hp
        self.speed = 4
        self.watch = 200
        self.dmg = 10
        self.mele = False
        self.boss = False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 600

        self.cooldown_punch = 0
        self.cooldown_shot = 25
        self.cooldown_reload = 200


        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = WIDTH
        self.height = HEIGHT

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.bullets = 4
        self.cooldown = 0
        self.reload = 0

        self.kuvirok = False
        self.kuvirok_left = False
        self.kuvirok_right = False
        self.kuvirok_time = 0
        self.kuvirok_reload = 0
        # self.timer = pygame.time.Clock()

        self.agression = True
        self.ii_save = True
        self.stuned = False

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ELITAU_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ELITAU_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ELITAU_ANIMATION_FIGHT_RIGHT1)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ELITAU_ANIMATION_FIGHT_LEFT1)
        self.boltAnimLeftFight.play()

        # бьем вправо2
        self.boltAnimRightFight2 = pyganim.PygAnimation(ELITAU_ANIMATION_FIGHT_RIGHT2)
        self.boltAnimRightFight2.play()

        # бьем влево2
        self.boltAnimLeftFight2 = pyganim.PygAnimation(ELITAU_ANIMATION_FIGHT_LEFT2)
        self.boltAnimLeftFight2.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ELITAU_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()
        # self.boltAnimRightStay.blit(self.image, (0, 0))

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ELITAU_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # стоим направо222
        self.boltAnimRightKuv = pyganim.PygAnimation(ELITAU_ANIMATION_RIGHT_KUV)
        self.boltAnimRightKuv.play()
        # self.boltAnimRightStay.blit(self.image, (0, 0))

        # стоим налево222
        self.boltAnimLeftKuv = pyganim.PygAnimation(ELITAU_ANIMATION_LEFT_KUV)
        self.boltAnimLeftKuv.play()

        # стоим налево222
        self.boltAnimStan = pyganim.PygAnimation(ELITAU_ANIMATION_STAN)
        self.boltAnimStan.play()
    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)

        if self.kuvirok_time > 0:
            self.kuvirok_time -= SECOND

        if self.cooldown > 0:  # 25
            self.cooldown -= SECOND

        if self.stuned:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStan.blit(self.image, (0, 0))
        else:
            if not self.kuvirok:
                if self.reload > 0:
                    self.reload -= SECOND
                    if self.reload <= 0:
                        self.reload = 0
                        self.bullets = 4

                if self.cooldown <= 0:
                    if self.left:
                        self.xvel = -self.speed  # Лево = x- n
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimLeft.blit(self.image, (0, 0))

                    if self.right:
                        self.xvel = self.speed  # Право = x + n
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimRight.blit(self.image, (0, 0))
                        # по исксу зона ударов                           #по игрику
                    if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                            yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        if self.bullets > 0:
                            self.bullets -= 1
                            self.boltAnimLeftFight.blit(self.image, (0, 0))
                            self.cooldown = self.cooldown_shot
                            shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                            entities.add(shot1)
                            bad_bullets.append(shot1)
                        elif self.reload == 0:
                            self.boltAnimLeftFight2.blit(self.image, (0, 0))  # -- reload
                            self.reload = self.cooldown_reload
                        else:
                            self.boltAnimLeftStay.blit(self.image, (0, 0))

                    if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                            yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        if self.bullets > 0:
                            self.bullets -= 1
                            self.boltAnimRightFight.blit(self.image, (0, 0))
                            self.cooldown = self.cooldown_shot
                            shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                            entities.add(shot1)
                            bad_bullets.append(shot1)
                        elif self.reload == 0:
                            self.boltAnimRightFight2.blit(self.image, (0, 0))  # -- reload
                            self.reload = self.cooldown_reload
                        else:
                            self.boltAnimRightStay.blit(self.image, (0, 0))
                elif self.cooldown <= self.cooldown_shot - int(self.cooldown / 2):
                    if self.left:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimLeftStay.blit(self.image, (0, 0))
                    if self.right:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimRightStay.blit(self.image, (0, 0))

                if self.ii_save:
                    if self.left and xplayer > self.rect.x and self.hp <= self.max_hp * 0.5:
                        self.kuvirok_left = True
                        self.kuvirok = True
                        self.ii_save = False
                        self.kuvirok_time = 50
                    if self.right and xplayer < self.rect.x and self.hp <= self.max_hp * 0.5:
                        self.kuvirok_right = True
                        self.kuvirok = True
                        self.ii_save = False
                        self.kuvirok_time = 50
            else:
                if self.kuvirok_left and self.kuvirok_time > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftKuv.blit(self.image, (0, 0))
                    self.xvel = -5 * self.speed
                elif self.kuvirok_right and self.kuvirok_time > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightKuv.blit(self.image, (0, 0))
                    self.xvel = 5 * self.speed
                elif self.kuvirok_left:
                    self.left = False
                    self.right = True
                    self.kuvirok = False
                    self.reload = 0
                    self.bullets = 4
                elif self.kuvirok_right:
                    self.left = True
                    self.right = False
                    self.kuvirok = False
                    self.reload = 0
                    self.bullets = 4

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


###############################################################################################3
###############################БОСЫ############################################################3
###############################################################################################3

class Zolotov_BOS(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):

        self.hp = 1500
        self.max_hp = self.hp
        self.speed = 4
        self.dmg = 10
        self.mele = False
        self.boss = True
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 150

        self.cooldown_punch = 35
        self.cooldown_shot = 0
        self.cooldown_reload = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = 200
        self.height = 280

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right

        self.ii_save = True
        self.stuned = False

        self.agression = True
        self.lets_shoot = False
        self.shooted = 0
        self.shotEND = False
        self.time_shoot_wait = 120
        self.etalon_time_shoot_wait = 120
        self.etalon_speed = 4

        self.damaged = 0

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in ZOLOTOV_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ZOLOTOV_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ZOLOTOV_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ZOLOTOV_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()
        self.cooldown = 0
        self.timer = pygame.time.Clock()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ZOLOTOV_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()
        # self.boltAnimRightStay.blit(self.image, (0, 0))

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ZOLOTOV_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.dmg_deal = 0
        if hero.chosen in [3,6,8]:
            if self.hp < self.max_hp * 0.15:
                self.speed = self.etalon_speed * 2
                self.time_shoot_wait = int(self.etalon_time_shoot_wait / 3)
            elif self.hp < self.max_hp * 0.65:
                self.speed = self.etalon_speed * 1.5
                self.time_shoot_wait = int(self.etalon_time_shoot_wait / 2)
        else:
            if self.hp < self.max_hp * 0.3:
                self.speed = self.etalon_speed * 3
                self.time_shoot_wait = int(self.etalon_time_shoot_wait / 3)
            elif self.hp < self.max_hp * 0.65:
                self.speed = self.etalon_speed * 2
                self.time_shoot_wait = int(self.etalon_time_shoot_wait / 2)

        if self.lets_shoot:
            if self.shooted > 0:
                self.shooted -= SECOND
                if self.left and not self.shotEND:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
                    self.shotEND = True
                if self.right and not self.shotEND:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
                    self.shotEND = True
            else:
                self.lets_shoot = False
                self.shotEND = False

        else:
            if self.left:
                self.xvel = -self.speed  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.play()
                self.boltAnimLeft.blit(self.image, (0, 0))

            if self.right:
                self.xvel = self.speed  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, hero, SECOND)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, hero, SECOND)

    def collide(self, xvel, yvel, platforms, hero, SECOND):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True
                    self.lets_shoot = True
                    self.shooted = self.time_shoot_wait
                    self.xvel = 0

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True
                    self.lets_shoot = True
                    self.shooted = self.time_shoot_wait
                    self.xvel = 0

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        if self.damaged > 0:
            self.damaged -= SECOND
        else:
            if pygame.sprite.collide_rect(self, hero):
                if xvel > 0:  # если движется вправо
                    # self.rect.right = hero.rect.left  # то не движется вправо
                    self.damaged = 40
                    if not hero.unkill:
                        hero.hp -= 3
                        if hero.chosen == 7:
                            self.hp -= 3

                if xvel < 0:  # если движется влево
                    # self.rect.left = hero.rect.right  # то не движется влево
                    self.damaged = 40
                    if not hero.unkill:
                        hero.hp -= 3
                        if hero.chosen == 7:
                            self.hp -= 3


class Stas_BOS(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 1500
        self.previos_hp = 1500
        self.max_hp = 1500

        self.speed = 4
        self.watch = 200
        self.dmg = 30
        self.mele = False
        self.boss = True #False
        self.putin = False

        self.dmg_deal = 0

        self.atack_zone = 600
        self.atack_zone_mele = 150

        self.cooldown_punch = 60
        self.cooldown_shot = 300
        self.cooldown_reload = 0

        self.stoped = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = 200
        self.height = 280
        self.lost_hp = 0

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right
        self.stadion = 0

        self.meteors = 5

        self.agression = True
        self.stuned = False

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in STAS_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in STAS_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(STAS_ANIMATION_FIGHT_RIGHT1)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(STAS_ANIMATION_FIGHT_LEFT1)
        self.boltAnimLeftFight.play()
        self.cooldown = 0
        self.timer = pygame.time.Clock()

        # стоим направо 2
        self.boltAnimRightFight2 = pyganim.PygAnimation(STAS_ANIMATION_FIGHT_RIGHT2)
        self.boltAnimRightFight2.play()

        # стоим налево 2
        self.boltAnimLeftFight2 = pyganim.PygAnimation(STAS_ANIMATION_FIGHT_LEFT2)
        self.boltAnimLeftFight2.play()

        # стоим направо 3
        self.boltAnimRightFight3 = pyganim.PygAnimation(STAS_ANIMATION_FIGHT_RIGHT3)
        self.boltAnimRightFight3.play()

        # стоим налево 3
        self.boltAnimLeftFight3 = pyganim.PygAnimation(STAS_ANIMATION_FIGHT_LEFT3)
        self.boltAnimLeftFight3.play()

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND):

        self.damagelvl_y = int(self.rect.y + self.height * 0.3) #int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.dmg_deal = 0

        if hero.chosen in [3, 6, 8]:
            pass
        else:
            if self.left and xplayer > self.rect.x + 1000:
                self.left = False
                self.right = True
            if self.right and xplayer < self.rect.x - 1000:
                self.left = True
                self.right = False
            self.atack_zone = 750

        if self.previos_hp > self.hp:
            self.lost_hp = self.previos_hp - self.hp + self.lost_hp
            self.previos_hp = self.hp

        if self.cooldown > 0:
            self.cooldown -= SECOND
        if self.stoped > 0:
            self.stoped -= SECOND

        if self.lost_hp > 0:
            if self.lost_hp > 200:
                self.image.fill(pygame.Color(COLOR))
                if self.left:
                    self.boltAnimLeftFight2.blit(self.image, (0, 0))
                else:
                    self.boltAnimRightFight3.blit(self.image, (0, 0))
                for bul in range(self.meteors):
                    if hero.chosen in [3, 6, 8]:
                        self.meteors += 1
                        x_random = randint(xplayer - 1000, xplayer + 1000)
                    else:
                        self.meteors += 2
                        x_random = randint(xplayer - 800, xplayer + 800)
                    y_random = randint(-1000, -400)
                    shot1 = dead_shot_dawn(x_random, y_random, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)
                self.lost_hp = 0
                self.stadion = 0
            if self.lost_hp > 50 and self.stadion == 0:
                self.stadion = 2
                if self.left and xplayer > self.rect.x:
                    self.left = False
                    self.right = True
                if self.right and xplayer < self.rect.x:
                    self.left = True
                    self.right = False
                self.cooldown = self.cooldown_shot
            elif self.lost_hp > 150 and self.stadion == 2:
                self.stadion = 3
                if self.left and xplayer > self.rect.x:
                    self.left = False
                    self.right = True
                if self.right and xplayer < self.rect.x:
                    self.left = True
                    self.right = False
                self.cooldown = self.cooldown_shot

        if self.stoped <= 0:
            if self.left:
                self.xvel = -self.speed  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if self.right:
                self.xvel = self.speed  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

        if self.cooldown <= 0:
            # по исксу зона ударов                           #по игрику
            if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                    yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftFight2.blit(self.image, (0, 0))
                self.cooldown = self.cooldown_shot
                self.stoped = self.cooldown_punch
                shot1 = dead_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                entities.add(shot1)
                bad_bullets.append(shot1)

            if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                    yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightFight2.blit(self.image, (0, 0))
                self.cooldown = self.cooldown_shot
                self.stoped = self.cooldown_punch
                shot1 = dead_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                entities.add(shot1)
                bad_bullets.append(shot1)
        if self.stoped <= 0:
            if self.left and xplayer > self.rect.x - self.atack_zone_mele and xplayer < self.rect.x and \
                    yplayer + HEIGHT >= self.agr_y_1+100 and yplayer <= self.agr_y_2:
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftFight.blit(self.image, (0, 0))
                self.stoped = self.cooldown_punch
                self.dmg_deal = self.dmg

            elif self.right and xplayer < self.rect.x + self.atack_zone_mele and xplayer > self.rect.x and \
                    yplayer + HEIGHT >= self.agr_y_1+100 and yplayer <= self.agr_y_2:
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightFight.blit(self.image, (0, 0))
                self.stoped = self.cooldown_punch
                self.dmg_deal = self.dmg

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Putin_BOS(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        self.hp = 2500
        self.previos_hp = 2500
        self.max_hp = 2500

        self.speed = 4
        self.watch = 200
        self.dmg = 30
        self.mele = False
        self.boss = True
        self.putin = True

        self.exploud_dmg = 40
        self.dmg_deal = 0

        self.atack_zone = 600
        self.atack_zone_mele = 300

        self.cooldown_punch = 60
        self.cooldown_shot = 300
        self.cooldown_reload = 0

        self.stoped = 0

        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.width = 200
        self.height = 280
        self.lost_hp = 0

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, self.width, self.height)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.left = left
        self.right = right
        self.stadion = 0
        self.stuned = False

        self.agression = True
        self.cooldown = 0
        self.boom_time = 0
        self.mina_standart_cd = 500
        self.mina_cd = self.mina_standart_cd

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in PUTIN_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in PUTIN_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        boltAnim = []
        for anim in PUTIN_ANIMATION_FIRED_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRightF = pyganim.PygAnimation(boltAnim)
        self.boltAnimRightF.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in PUTIN_ANIMATION_FIRED_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeftF = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeftF.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(PUTIN_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(PUTIN_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        self.speed_time = 0
        self.stadia = 0

    def update(self, platforms, xplayer, yplayer, hero, entities, bad_bullets, SECOND, mins):


        if hero.chosen in [3, 6, 8]:
            self.mina_standart_cd = 500
            self.atack_zone = 600
        else:
            self.mina_standart_cd = 400
            self.atack_zone = 1000

        self.damagelvl_y = int(self.rect.y + self.height * 0.3)
        self.agr_y_1 = int(self.rect.y - self.height * 0.3)
        self.agr_y_2 = int(self.rect.y + self.height)
        self.dmg_deal = 0


        if self.hp<1500 and self.stadia == 0:
            self.speed = self.speed * 4
            self.speed_time = 1000
            self.stadia = 1
        if self.speed_time>0:
            self.speed_time -= SECOND
        elif self.speed_time<=0:
            self.speed = 4

        if self.hp<500 and self.stadia == 1:
            self.speed = self.speed * 5
            self.speed_time = 1500
            self.stadia = 1
        if self.speed_time>0:
            self.speed_time -= SECOND
        elif self.speed_time<=0:
            self.speed = 5

        if self.previos_hp > self.hp and self.boom_time == 0:
            self.lost_hp = self.previos_hp - self.hp + self.lost_hp
            self.previos_hp = self.hp

        if self.cooldown > 0:
            self.cooldown -= SECOND

        # мины
        if self.mina_cd > 0:
            self.mina_cd -= SECOND
        else:
            self.mina_cd = self.mina_standart_cd
            sh = Mina(self.rect.x, self.rect.y + self.height - PLATFORM_HEIGHT)
            entities.add(sh)
            mins.append(sh)

        if self.boom_time > 0:
            self.boom_time -= SECOND
            if self.boom_time <= 0:
                if self.left and xplayer > self.rect.x and xplayer < self.rect.x + self.atack_zone_mele and \
                        yplayer + HEIGHT >= self.rect.y and yplayer <= self.rect.y + self.height:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    if not hero.unkill:
                        hero.hp -= self.exploud_dmg
                elif self.right and xplayer < self.rect.x and xplayer > self.rect.x - self.atack_zone_mele and \
                        yplayer + HEIGHT >= self.rect.y and yplayer <= self.rect.y + self.height:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    if not hero.unkill:
                        hero.hp -= self.exploud_dmg
                elif self.left:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                self.boom_time = 0
            # красный путин
            elif self.left:
                self.xvel = -self.speed  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftF.blit(self.image, (0, 0))

            elif self.right:
                self.xvel = self.speed  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightF.blit(self.image, (0, 0))

            elif self.cooldown <= 0:
                # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

        if self.lost_hp > 0:
            if self.lost_hp > 200:
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftF.blit(self.image, (0, 0))
                self.lost_hp = 0
                self.boom_time = 200

        if self.boom_time <= 0:
            if self.left:
                self.xvel = -self.speed  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if self.right:
                self.xvel = self.speed  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if self.cooldown <= 0:
                # по исксу зона ударов                           #по игрику
                if self.left and xplayer > self.rect.x - self.atack_zone and xplayer < self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, True, False)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

                if self.right and xplayer < self.rect.x + self.atack_zone and xplayer > self.rect.x and \
                        yplayer + HEIGHT >= self.agr_y_1 and yplayer <= self.agr_y_2:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                    self.cooldown = self.cooldown_shot
                    shot1 = bad_shot(int(self.rect.x + self.width * 0.5), self.damagelvl_y, False, True)
                    entities.add(shot1)
                    bad_bullets.append(shot1)

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.right = False
                    self.left = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.left = False
                    self.right = True

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 1
        self.hp = 100
        self.DMG_ABILITY = 50
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT)) #((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0

        #        Анимация движения вправо
        boltAnim = []
        for anim in SANYA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in SANYA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(SANYA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(SANYA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(SANYA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(SANYA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(SANYA_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #летим налево
        self.boltAnimFlyLeft = pyganim.PygAnimation(SANYA_ANIMATION_LEFT_FLY)
        self.boltAnimFlyLeft.play()

        #летим вправо
        self.boltAnimFlyRight = pyganim.PygAnimation(SANYA_ANIMATION_RIGHT_FLY)
        self.boltAnimFlyRight.play()

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive, get_damage):

        if self.can_fly>0:
            if self.can_fly == 150:
                self.rect = pygame.Rect(self.rect.x, self.rect.y, HEIGHT, WIDTH)
            self.can_fly -= SECOND
            if look_right:
                self.xvel = 2*MOVE_SPEED

                self.image = pygame.Surface((HEIGHT, WIDTH))
                self.image.set_colorkey(pygame.Color(COLOR))
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimFlyRight.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -2*MOVE_SPEED

                self.image = pygame.Surface((HEIGHT, WIDTH))
                self.image.set_colorkey(pygame.Color(COLOR))
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimFlyLeft.blit(self.image, (0, 0))
            if self.can_fly<=0:
                self.rect = pygame.Rect(self.rect.x, self.rect.y, WIDTH, HEIGHT)
            self.yvel = 0

        elif look_left or look_right:
            self.image = pygame.Surface((WIDTH, HEIGHT))
            self.image.set_colorkey(pygame.Color(COLOR))
            self.unkill = False
            get_damage.clear()
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
            if not self.onGround:
                self.yvel += GRAVITY
        else:
            get_damage.clear()
            if not self.onGround:
                self.yvel += GRAVITY
        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo, alive, get_damage)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo, alive, get_damage)

    def collide(self, xvel, yvel, platforms, ships, mins, salo, alive, get_damage):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s) and not self.unkill:
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl

        if self.can_fly>0:
            for en in alive:
                if pygame.sprite.collide_rect(self, en):
                    if xvel > 0:  # если движется вправо
                        if en not in get_damage:
                            en.hp -= self.DMG_ABILITY
                            get_damage.append(en)

                    if xvel < 0:  # если движется влево
                        if en not in get_damage:
                            en.hp -= self.DMG_ABILITY
                            get_damage.append(en)

                    if yvel > 0:  # если падает вниз
                        if en not in get_damage:
                            en.hp -= self.DMG_ABILITY
                            get_damage.append(en)

                    if yvel < 0:  # если движется вверх
                        if en not in get_damage:
                            en.hp -= self.DMG_ABILITY
                            get_damage.append(en)

class Player_Ilya(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 4
        self.hp = 100
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0

        self.shit = False

        #        Анимация движения вправо
        boltAnim = []
        for anim in ILYA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ILYA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(ILYA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(ILYA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(ILYA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(ILYA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()


        #начинаем срать вправо
        self.boltAnimULTright1 = pyganim.PygAnimation(ILYA_ANIMATION_ULT_RIGHT1)
        self.boltAnimULTright1.play()

        #срем вправо
        self.boltAnimULTright2 = pyganim.PygAnimation(ILYA_ANIMATION_ULT_RIGHT2)
        self.boltAnimULTright2.play()

        # начинаем срать налево
        self.boltAnimULTleft1 = pyganim.PygAnimation(ILYA_ANIMATION_ULT_LEFT1)
        self.boltAnimULTleft1.play()

        # срем налево
        self.boltAnimULTleft2 = pyganim.PygAnimation(ILYA_ANIMATION_ULT_LEFT2)
        self.boltAnimULTleft2.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(ILYA_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #летим

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive, get_damage, good_bullets, entities):


        if self.can_fly>=0:
            self.can_fly -= SECOND
            self.xvel = 0
            if look_left:
                if self.can_fly<=100:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTleft2.blit(self.image, (0, 0))
                    if not self.shit:
                        shot1 = good_shot(int(self.rect.x + WIDTH * 0.5), int(self.rect.y + HEIGHT * 0.3), True, False)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.shit = True

                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTleft1.blit(self.image, (0, 0))
            elif look_right:
                if self.can_fly<=100:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTright2.blit(self.image, (0, 0))
                    if not self.shit:
                        shot1 = good_shot(int(self.rect.x + WIDTH * 0.5), int(self.rect.y + HEIGHT * 0.3), False, True)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.shit = True
                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTright1.blit(self.image, (0, 0))

        else:

            if look_right:
                self.xvel = MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s):
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl


class Player_Senya(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 5
        self.hp = 120
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0
        self.BABAH = False
        self.ult_dmg = 100
        self.stun_time = 0

        #        Анимация движения вправо
        boltAnim = []
        for anim in SENYA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in SENYA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(SENYA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(SENYA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(SENYA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(SENYA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(SENYA_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        # начинаем играть
        self.boltAnimULT1 = pyganim.PygAnimation(SENYA_ANIMATION_ULT1)
        self.boltAnimULT1.play()

        # играем
        self.boltAnimULT2 = pyganim.PygAnimation(SENYA_ANIMATION_ULT2)
        self.boltAnimULT2.play()

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive, get_damage, entities):

        radius = 550
        if self.can_fly>0:
            self.can_fly -= SECOND
            if self.can_fly <= 70:
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULT2.blit(self.image, (0, 0))
                if self.can_fly <=0:
                    self.BABAH = True
                    self.can_fly = 0
            else:
                if left and up:
                    self.xvel = -5

                if right  and up:
                    self.xvel = 5
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULT1.blit(self.image, (0, 0))
        else:
            if look_right:
                self.xvel = MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if self.BABAH:
            for a in alive:
                if (a.rect.x+a.width/2-self.rect.x)**2+(a.rect.y-self.rect.y)**2<=radius**2:
                    a.stuned = True
                    a.hp -= self.ult_dmg
            for m in mins:
                if (m.rect.x+m.width/2-self.rect.x)**2+(m.rect.y-self.rect.y)**2<=radius**2:
                    entities.remove([m])
                    mins.remove(m)
            self.BABAH = False
            self.stun_time = 150
            rand_music = randint(1,21)
            pygame.mixer.music.load('music/senya/' + str(rand_music) + '.mp3')
            if rand_music == 1:
                pygame.mixer.music.play(start = 41.5)
            elif rand_music == 2:
                pygame.mixer.music.play(start=25)
            elif rand_music == 3:
                pygame.mixer.music.play(start=30)
            elif rand_music == 5:
                pygame.mixer.music.play(start=20)
            elif rand_music == 6:
                pygame.mixer.music.play(start=68)
            elif rand_music == 11:
                pygame.mixer.music.play(start=10.5)
            elif rand_music == 16:
                pygame.mixer.music.play(start=32)
            else:
                pygame.mixer.music.play()
        if self.stun_time>0:
            self.stun_time -= SECOND
        elif self.stun_time<0:
            self.stun_time = 0
            for a in alive:
                a.stuned = False


        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s):
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl

class Player_Grisha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 3
        self.hp = 100
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0
        self.cur_hp = 100
        self.speed_on = 0

        self.speed = MOVE_SPEED

        #        Анимация движения вправо
        boltAnim = []
        for anim in GRISHA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in GRISHA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(GRISHA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(GRISHA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(GRISHA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(GRISHA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(GRISHA_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #летим
        self.boltAnimULT = pyganim.PygAnimation(GRISHA_ANIMATION_ULT)
        self.boltAnimULT.play()

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive,
               get_damage, good_bullets):

        if self.cur_hp>self.hp:
            self.speed_on = 150
            self.cur_hp = self.hp
        if self.speed_on>0:
            self.speed_on -= SECOND
            self.speed = MOVE_SPEED * 2
        else:
            self.speed = MOVE_SPEED

        if self.unkill:

            if left:
                self.xvel = -1  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULT.blit(self.image, (0, 0))

            elif right:
                self.xvel = 1  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULT.blit(self.image, (0, 0))

            else:
                self.xvel = 0  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULT.blit(self.image, (0, 0))
        else:
            if look_right:
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -self.speed  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = self.speed  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s) and not self.unkill:
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl

class Player_Dima(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 2
        self.hp = 100
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0

        self.shit = False

        #        Анимация движения вправо
        boltAnim = []
        for anim in DIMA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in DIMA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(DIMA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(DIMA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(DIMA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(DIMA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()


        #начинаем срать вправо
        self.boltAnimULTright1 = pyganim.PygAnimation(DIMA_ANIMATION_ULT_RIGHT1)
        self.boltAnimULTright1.play()

        #срем вправо
        self.boltAnimULTright2 = pyganim.PygAnimation(DIMA_ANIMATION_ULT_RIGHT2)
        self.boltAnimULTright2.play()

        # начинаем срать налево
        self.boltAnimULTleft1 = pyganim.PygAnimation(DIMA_ANIMATION_ULT_LEFT1)
        self.boltAnimULTleft1.play()

        # срем налево
        self.boltAnimULTleft2 = pyganim.PygAnimation(DIMA_ANIMATION_ULT_LEFT2)
        self.boltAnimULTleft2.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(DIMA_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #летим

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive, good_bullets, entities):


        if self.can_fly>=0:
            self.can_fly -= SECOND
            self.xvel = 0
            if look_left:
                if self.can_fly<=100:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTleft2.blit(self.image, (0, 0))
                    if not self.shit:
                        shot1 = dima_good_shot(int(self.rect.x), int(self.rect.y + HEIGHT * 0.4),
                                               True, False)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.shit = True

                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTleft1.blit(self.image, (0, 0))
            elif look_right:
                if self.can_fly<=100:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTright2.blit(self.image, (0, 0))
                    if not self.shit:
                        shot1 = dima_good_shot(int(self.rect.x + WIDTH * 0.6), int(self.rect.y + HEIGHT * 0.4),
                                               False, True)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.shit = True
                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTright1.blit(self.image, (0, 0))

        else:

            if look_right:
                self.xvel = MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s):
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl

class Player_Misha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 6
        self.hp = 100
        self.cur_hp = 100
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = randint(20,350)
        self.bullets = 5
        self.shoot = False
        self.WARN = False

        #        Анимация движения вправо
        boltAnim = []
        for anim in MISHA_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in MISHA_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(MISHA_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(MISHA_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(MISHA_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(MISHA_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(MISHA_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #        Анимация ульты вправо
        boltAnim = []
        for anim in MISHA_ANIMATION_ULT_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimULTRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimULTRight.play()

        #        Анимация ульты влево
        boltAnim = []
        for anim in MISHA_ANIMATION_ULT_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimULTLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimULTLeft.play()


        #    ПАСИВА    Анимация движения вправо
        boltAnim = []
        for anim in MISHA_ANIMATION_RIGHT_P:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight_p = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight_p.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in MISHA_ANIMATION_LEFT_P:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft_p = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft_p.play()

        # стоим направо
        self.boltAnimRightStay_p = pyganim.PygAnimation(MISHA_ANIMATION_STAY_RIGHT_P)
        self.boltAnimRightStay_p.play()

        # стоим налево
        self.boltAnimLeftStay_p = pyganim.PygAnimation(MISHA_ANIMATION_STAY_LEFT_P)
        self.boltAnimLeftStay_p.play()

        # бьем вправо
        self.boltAnimRightFight_p = pyganim.PygAnimation(MISHA_ANIMATION_FIGHT_RIGHT_P)
        self.boltAnimRightFight_p.play()

        # бьем влево
        self.boltAnimLeftFight_p = pyganim.PygAnimation(MISHA_ANIMATION_FIGHT_LEFT_P)
        self.boltAnimLeftFight_p.play()

        #        Анимация ульты вправо
        boltAnim = []
        for anim in MISHA_ANIMATION_ULT_RIGHT_P:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimULTRight_p = pyganim.PygAnimation(boltAnim)
        self.boltAnimULTRight_p.play()

        #        Анимация ульты влево
        boltAnim = []
        for anim in MISHA_ANIMATION_ULT_LEFT_P:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimULTLeft_p = pyganim.PygAnimation(boltAnim)
        self.boltAnimULTLeft_p.play()

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive,
               get_damage, entities, good_bullets):

        if self.bullets == 5:
            self.WARN = False
        if self.bullets < 5 and not self.WARN:
            self.cur_hp = self.hp
            self.WARN = True
        if self.WARN:
            plus_blullets = self.cur_hp-self.hp
            if plus_blullets>0:
                self.bullets += int((plus_blullets)/10)
                if int((plus_blullets)/10)>0:
                    self.cur_hp = self.hp
            elif plus_blullets<0:
                self.cur_hp = self.hp

        if self.unkill:
            if self.can_fly >= 0 and self.shoot and self.bullets > 0:
                self.can_fly -= SECOND
                self.xvel = 0
                if look_left:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTLeft_p.blit(self.image, (0, 0))
                    if self.can_fly <= 0:
                        shot1 = misha_good_shot(int(self.rect.x + WIDTH * 0.35), int(self.rect.y + HEIGHT * 0.7), True,
                                                False)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.bullets -= 1
                        if self.hp > 80:
                            self.can_fly = randint(100, 350)
                        elif self.hp > 60:
                            self.can_fly = randint(80, 300)
                        elif self.hp > 40:
                            self.can_fly = randint(60, 250)
                        elif self.hp > 20:
                            self.can_fly = randint(40, 150)
                        else:
                            self.can_fly = randint(20, 100)
                elif look_right:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTRight_p.blit(self.image, (0, 0))
                    if self.can_fly <= 0:
                        shot1 = misha_good_shot(int(self.rect.x + WIDTH * 0.5), int(self.rect.y + HEIGHT * 0.7), False,
                                                True)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.bullets -= 1
                        if self.hp > 80:
                            self.can_fly = randint(100, 350)
                        elif self.hp > 60:
                            self.can_fly = randint(80, 300)
                        elif self.hp > 40:
                            self.can_fly = randint(60, 250)
                        elif self.hp > 20:
                            self.can_fly = randint(40, 150)
                        else:
                            self.can_fly = randint(20, 100)

            else:

                if look_right:
                    self.xvel = MOVE_SPEED
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay_p.blit(self.image, (0, 0))
                if look_left:
                    self.xvel = -MOVE_SPEED
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay_p.blit(self.image, (0, 0))
                if up and look_left:
                    if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                        self.yvel = -JUMP_POWER
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft_p.blit(self.image, (0, 0))

                if up and look_right:
                    if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                        self.yvel = -JUMP_POWER
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight_p.blit(self.image, (0, 0))

                if left:
                    self.xvel = -MOVE_SPEED  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft_p.blit(self.image, (0, 0))

                if right:
                    self.xvel = MOVE_SPEED  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight_p.blit(self.image, (0, 0))

                if look_left and not (left or right):
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay_p.blit(self.image, (0, 0))

                if look_right and not (left or right):
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay_p.blit(self.image, (0, 0))

                if look_left and fight:
                    if self.yvel > 0:
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimLeftFight_p.blit(self.image, (0, 0))
                    else:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimLeftFight_p.blit(self.image, (0, 0))

                if look_right and fight:
                    if self.yvel > 0:
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimRightFight_p.blit(self.image, (0, 0))
                    else:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimRightFight_p.blit(self.image, (0, 0))

        else:

            if self.can_fly >= 0 and self.shoot and self.bullets>0:
                self.can_fly -= SECOND
                self.xvel = 0
                if look_left:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTLeft.blit(self.image, (0, 0))
                    if self.can_fly<=0:
                        shot1 = misha_good_shot(int(self.rect.x + WIDTH * 0.35), int(self.rect.y + HEIGHT * 0.7), True, False)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.bullets -= 1
                        if self.hp > 80:
                            self.can_fly = randint(100,350)
                        elif self.hp > 60:
                            self.can_fly = randint(80, 300)
                        elif self.hp > 40:
                            self.can_fly = randint(60, 250)
                        elif self.hp > 20:
                            self.can_fly = randint(40, 150)
                        else:
                            self.can_fly = randint(20, 100)
                elif look_right:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTRight.blit(self.image, (0, 0))
                    if self.can_fly <= 0:
                        shot1 = misha_good_shot(int(self.rect.x + WIDTH * 0.5), int(self.rect.y + HEIGHT * 0.7), False, True)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.bullets -= 1
                        if self.hp > 80:
                            self.can_fly = randint(100, 350)
                        elif self.hp > 60:
                            self.can_fly = randint(80, 300)
                        elif self.hp > 40:
                            self.can_fly = randint(60, 250)
                        elif self.hp > 20:
                            self.can_fly = randint(40, 150)
                        else:
                            self.can_fly = randint(20, 100)

            else:

                if look_right:
                    self.xvel = MOVE_SPEED
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))
                if look_left:
                    self.xvel = -MOVE_SPEED
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))
                if up and look_left:
                    if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                        self.yvel = -JUMP_POWER
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if up and look_right:
                    if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                        self.yvel = -JUMP_POWER
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))

                if left:
                    self.xvel = -MOVE_SPEED  # Лево = x- n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeft.blit(self.image, (0, 0))

                if right:
                    self.xvel = MOVE_SPEED  # Право = x + n
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRight.blit(self.image, (0, 0))

                if look_left and not (left or right):
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftStay.blit(self.image, (0, 0))

                if look_right and not (left or right):
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightStay.blit(self.image, (0, 0))

                if look_left and fight:
                    if self.yvel > 0:
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimLeftFight.blit(self.image, (0, 0))
                    else:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimLeftFight.blit(self.image, (0, 0))

                if look_right and fight:
                    if self.yvel > 0:
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimRightFight.blit(self.image, (0, 0))
                    else:
                        self.xvel = 0
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s)  and not self.unkill:
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl
class Player_Igor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 7
        self.hp = 100
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0

        self.shit = False

        #        Анимация движения вправо
        boltAnim = []
        for anim in IGOR_ANIMATION_RIGHT:
            boltAnim.append((anim, 0.2))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in IGOR_ANIMATION_LEFT:
            boltAnim.append((anim, 0.2))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(IGOR_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(IGOR_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(IGOR_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(IGOR_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()


        #УЛЬТЫ1
        self.boltAnimULT1 = pyganim.PygAnimation(IGOR_ANIMATION_ULT1)
        self.boltAnimULT1.play()
        # УЛЬТЫ2
        self.boltAnimULT2 = pyganim.PygAnimation(IGOR_ANIMATION_ULT2)
        self.boltAnimULT2.play()
        # УЛЬТЫ3
        self.boltAnimULT3 = pyganim.PygAnimation(IGOR_ANIMATION_ULT3)
        self.boltAnimULT3.play()
        # УЛЬТЫ4
        self.boltAnimULT4 = pyganim.PygAnimation(IGOR_ANIMATION_ULT4)
        self.boltAnimULT4.play()


        # ультуем налево
        self.boltAnimULTleft = pyganim.PygAnimation(IGOR_ANIMATION_ULT_LEFT)
        self.boltAnimULTleft.play()

        # ультуем право
        self.boltAnimULTright = pyganim.PygAnimation(IGOR_ANIMATION_ULT_RIGHT)
        self.boltAnimULTright.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(IGOR_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #летим

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive, get_damage, good_bullets, entities):


        if self.can_fly>0:
            self.can_fly -= SECOND
            self.xvel = 0
            if look_left:
                if self.can_fly<=80:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTleft.blit(self.image, (0, 0))
                    if not self.shit:
                        shot1 = igor_shot(int(self.rect.x), int(self.rect.y + HEIGHT * 0.4), True, False)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.shit = True

                elif self.can_fly<=110:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT4.blit(self.image, (0, 0))
                elif self.can_fly<=140:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT3.blit(self.image, (0, 0))
                elif self.can_fly<=170:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT2.blit(self.image, (0, 0))
                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT1.blit(self.image, (0, 0))

            elif look_right:
                if self.can_fly<=80:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULTright.blit(self.image, (0, 0))
                    if not self.shit:
                        shot1 = igor_shot(int(self.rect.x + WIDTH * 0.7), int(self.rect.y + HEIGHT * 0.4), False, True)
                        entities.add(shot1)
                        good_bullets.append(shot1)
                        self.shit = True

                elif self.can_fly <= 110:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT4.blit(self.image, (0, 0))
                elif self.can_fly <= 140:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT3.blit(self.image, (0, 0))
                elif self.can_fly <= 170:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT2.blit(self.image, (0, 0))
                else:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimULT1.blit(self.image, (0, 0))


        else:

            if look_right:
                self.xvel = MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s):
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl

class Player_Nik(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 8
        self.hp = 100
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.can_fly = 0

        self.shit = False

        #        Анимация движения вправо
        boltAnim = []
        for anim in NIK_ANIMATION_RIGHT:
            boltAnim.append((anim, 0.2))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in NIK_ANIMATION_LEFT:
            boltAnim.append((anim, 0.2))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(NIK_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(NIK_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(NIK_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(NIK_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        # ультуем налево
        self.boltAnimULTleft = pyganim.PygAnimation(NIK_ANIMATION_ULT_LEFT)
        self.boltAnimULTleft.play()

        # ультуем право
        self.boltAnimULTright = pyganim.PygAnimation(NIK_ANIMATION_ULT_RIGHT)
        self.boltAnimULTright.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(NIK_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #летим

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive, get_damage, good_bullets, entities):


        if self.can_fly>0:
            self.can_fly -= SECOND
            self.xvel = 0
            if self.can_fly<=0:
                if look_left:
                    if self.can_fly<=80:
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimULTleft.blit(self.image, (0, 0))
                        shot1 = nik_shot(int(self.rect.x), int(self.rect.y - HEIGHT * 0.2), True, False)
                        entities.add(shot1)
                        good_bullets.append(shot1)

                elif look_right:
                        self.image.fill(pygame.Color(COLOR))
                        self.boltAnimULTright.blit(self.image, (0, 0))
                        shot1 = nik_shot(int(self.rect.x + WIDTH * 0.7), int(self.rect.y - HEIGHT * 0.2), False, True)
                        entities.add(shot1)
                        good_bullets.append(shot1)

        else:

            if look_right:
                self.xvel = MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s):
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl

class Player_Max(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.chosen = 9
        self.hp = 100
        self.cur_hp = 100
        self.can_fly = 0
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        self.BOOM = None
        self.eat = None
        self.unkill = False
        self.shoot = False
        self.WARN = False
        self.its_heal_time = CD_MAX_PASS

        #        Анимация движения вправо
        boltAnim = []
        for anim in MAX_ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in MAX_ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # стоим направо
        self.boltAnimRightStay = pyganim.PygAnimation(MAX_ANIMATION_STAY_RIGHT)
        self.boltAnimRightStay.play()

        # стоим налево
        self.boltAnimLeftStay = pyganim.PygAnimation(MAX_ANIMATION_STAY_LEFT)
        self.boltAnimLeftStay.play()

        # бьем вправо
        self.boltAnimRightFight = pyganim.PygAnimation(MAX_ANIMATION_FIGHT_RIGHT)
        self.boltAnimRightFight.play()

        # бьем влево
        self.boltAnimLeftFight = pyganim.PygAnimation(MAX_ANIMATION_FIGHT_LEFT)
        self.boltAnimLeftFight.play()

        #стоим
        self.boltAnimStay = pyganim.PygAnimation(MAX_ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #        Анимация ульты вправо
        boltAnim = []
        for anim in MAX_ANIMATION_ULT_RIGHT:
            boltAnim.append((anim, 0.2))
        self.boltAnimULTRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimULTRight.play()

        #        Анимация ульты влево
        boltAnim = []
        for anim in MAX_ANIMATION_ULT_LEFT:
            boltAnim.append((anim, 0.2))
        self.boltAnimULTLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimULTLeft.play()

    def update(self, left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive,
               get_damage, entities, good_bullets):

        if self.its_heal_time>0:
            self.its_heal_time -= SECOND
            if self.its_heal_time<=0:
                if self.hp<100:
                    self.hp += 1
                    self.its_heal_time = CD_MAX_PASS


        if self.can_fly > 0:
            self.can_fly -= SECOND
            self.xvel = 0
            if look_left:
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULTLeft.blit(self.image, (0, 0))
                if self.can_fly<=0:
                    shot1 = med_mina(int(self.rect.x), int(self.rect.y + HEIGHT * 0.7))
                    entities.add(shot1)
                    good_bullets.append(shot1)
                    self.can_fly = 0
            elif look_right:
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimULTRight.blit(self.image, (0, 0))
                if self.can_fly <= 0:
                    shot1 = med_mina(int(self.rect.x + WIDTH * 0.75), int(self.rect.y + HEIGHT * 0.7))
                    entities.add(shot1)
                    good_bullets.append(shot1)
                    self.can_fly = 0


        else:

            if look_right:
                self.xvel = MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))
            if look_left:
                self.xvel = -MOVE_SPEED
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))
            if up and look_left:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if up and look_right:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRight.blit(self.image, (0, 0))

            if look_left and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimLeftStay.blit(self.image, (0, 0))

            if look_right and not (left or right):
                self.xvel = 0
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimRightStay.blit(self.image, (0, 0))

            if look_left and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimLeftFight.blit(self.image, (0, 0))

            if look_right and fight:
                if self.yvel > 0:
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))
                else:
                    self.xvel = 0
                    self.image.fill(pygame.Color(COLOR))
                    self.boltAnimRightFight.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, ships, mins, salo)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, ships, mins, salo)

    def collide(self, xvel, yvel, platforms, ships, mins, salo):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

        for s in ships:
            if pygame.sprite.collide_rect(self, s)  and not self.unkill:
                if xvel > 0:  # если движется вправо
                    self.hp = 0

                if xvel < 0:  # если движется влево
                    self.hp = 0

                if yvel > 0:  # если падает вниз
                    self.hp = 0

                if yvel < 0:  # если движется вверх
                    self.hp = 0

        for m in mins:

            if pygame.sprite.collide_rect(self, m):
                if xvel > 0:  # если движется вправо
                    self.BOOM = m

                if xvel < 0:  # если движется влево
                    self.BOOM = m

                if yvel > 0:  # если падает вниз
                    self.BOOM = m

                if yvel < 0:  # если движется вверх
                    self.BOOM = m

        for sl in salo:
            if pygame.sprite.collide_rect(self, sl):
                if xvel > 0:  # если движется вправо
                    self.eat = sl

                if xvel < 0:  # если движется влево
                    self.eat = sl

                if yvel > 0:  # если падает вниз
                    self.eat = sl

                if yvel < 0:  # если движется вверх
                    self.eat = sl



class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2 - WIDTH - PLATFORM_WIDTH, -t + WIN_HEIGHT / 2 - HEIGHT / 10 - PLATFORM_HEIGHT

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH) - PLATFORM_WIDTH, l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT) - PLATFORM_HEIGHT, t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)


class good_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.dmg = 30

        self.speed = 5

        self.damaged = None
        self.stop = False
        self.image = pygame.Surface((BOOLET_WIDTH, BOOLET_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, BOOLET_WIDTH, BOOLET_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHIT)
        self.boltAnimShoot.play()

    def update(self, platforms, alive, get_damage):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, alive, get_damage)

    def collide(self, xvel, platforms, alive, get_damage):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
        for i in alive:
            if pygame.sprite.collide_rect(self, i):
                if xvel > 0:  # если движется вправо
                    self.rect.right = i.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True
                    self.damaged = i
                    i.stuned = True
                    get_damage.append(i)

                if xvel < 0:  # если движется влево
                    self.rect.left = i.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
                    self.damaged = i
                    i.stuned = True
                    get_damage.append(i)

class dima_good_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.dmg = 35

        self.speed = 8

        self.damaged = None
        self.stop = False
        self.image = pygame.Surface((BOOLET_WIDTH, BOOLET_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, BOOLET_WIDTH, BOOLET_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        boltAnim = []
        for anim in ANIMATION_SHIT_D:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimShoot = pyganim.PygAnimation(boltAnim)
        self.boltAnimShoot.play()

    def update(self, platforms, alive, get_damage):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, alive, get_damage)

    def collide(self, xvel, platforms, alive, get_damage):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
        for i in alive:
            if pygame.sprite.collide_rect(self, i):
                if xvel > 0 and i not in get_damage:  # если движется вправо
                    #self.rect.right = i.rect.left  # то не движется вправо
                    #self.boom = True
                    #self.stop = True
                    #self.damaged = i
                    i.hp -= self.dmg
                    get_damage.append(i)

                if xvel < 0 and i not in get_damage:  # если движется влево
                    #self.rect.left = i.rect.right  # то не движется влево
                    #self.boom = True
                    #self.stop = True
                    #self.damaged = i
                    i.hp -= self.dmg
                    get_damage.append(i)

class misha_good_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.dmg = 20

        self.speed = 10

        self.damaged = None
        self.stop = False
        self.image = pygame.Surface((BOOLET_WIDTH, BOOLET_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, BOOLET_WIDTH, BOOLET_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHOOT_M)
        self.boltAnimShoot.play()

    def update(self, platforms, alive,hero):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, alive,hero)

    def collide(self, xvel, platforms, alive, hero):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
        for i in alive:
            if pygame.sprite.collide_rect(self, i):
                if xvel > 0:  # если движется вправо
                    self.rect.right = i.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True
                    self.damaged = i
                    if hero.hp<=95:
                        hero.hp += 5
                    else:
                        hero.hp = 100

                if xvel < 0:  # если движется влево
                    self.rect.left = i.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
                    self.damaged = i
                    if hero.hp <= 95:
                        hero.hp += 5
                    else:
                        hero.hp = 100

class med_mina(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        #self.left = left
        #self.right = right
        self.boom = False
        self.dmg = 0

        self.speed = 8

        self.damaged = None
        self.stop = False
        self.image = pygame.Surface((MED_WIDTH, MED_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, MED_WIDTH, MED_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_MED)
        self.boltAnimShoot.play()

        self.onGround = True

    def update(self, platforms, alive, get_damage):

        self.boltAnimShoot.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, alive, get_damage)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, alive, get_damage)



    def collide(self, xvel, yvel, platforms, alive, get_damage):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

            for i in alive:
                if pygame.sprite.collide_rect(self, i):

                        self.rect.left = i.rect.right  # то не движется влево
                        self.boom = True
                        self.stop = True
                        self.damaged = i
                        get_damage.append(i)

class igor_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.dmg = 80

        self.speed = 8

        self.damaged = None
        self.stop = False
        self.image = pygame.Surface((50, 50))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, 50, 50)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        boltAnim = []
        for anim in ANIMATION_SHIT_I:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimShoot = pyganim.PygAnimation(boltAnim)
        self.boltAnimShoot.play()


    def update(self, platforms, alive, get_damage):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, alive, get_damage)

    def collide(self, xvel, platforms, alive, get_damage):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
        for i in alive:
            if pygame.sprite.collide_rect(self, i):
                if xvel > 0:  # если движется вправо
                    self.rect.right = i.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True
                    self.damaged = i

                if xvel < 0:  # если движется влево
                    self.rect.left = i.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
                    self.damaged = i

class nik_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.dmg = 10
        self.onGround = True
        self.speed = 9

        self.damaged = None
        self.stop = False
        self.image = pygame.Surface((220, 315))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, 220, 315)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        boltAnim = []
        for anim in ANIMATION_ONIME_L:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimShootL = pyganim.PygAnimation(boltAnim)
        self.boltAnimShootL.play()

        boltAnim = []
        for anim in ANIMATION_ONIME_R:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimShootR = pyganim.PygAnimation(boltAnim)
        self.boltAnimShootR.play()


    def update(self, platforms, alive, get_damage):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShootL.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShootR.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, alive, get_damage)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, alive, get_damage)

    def collide(self, xvel, yvel, platforms, alive, get_damage):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
        for i in alive:
            if pygame.sprite.collide_rect(self, i):
                if xvel > 0:  # если движется вправо
                    self.rect.right = i.rect.left  # то не движется вправо
                    self.boom = True
                    self.stop = True
                    self.damaged = i
                    i.stuned = True
                    get_damage.append(i)

                if xvel < 0:  # если движется влево
                    self.rect.left = i.rect.right  # то не движется влево
                    self.boom = True
                    self.stop = True
                    self.damaged = i
                    i.stuned = True
                    get_damage.append(i)


class bad_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.damaged = False

        self.dmg = 20
        self.speed = 7

        self.image = pygame.Surface((BOOLET_WIDTH, BOOLET_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, BOOLET_WIDTH, BOOLET_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHOOT)
        self.boltAnimShoot.play()

    def update(self, platforms, hero):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, hero)

    def collide(self, xvel, platforms, hero):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
        if pygame.sprite.collide_rect(self, hero):
            if xvel > 0:  # если движется вправо
                self.rect.right = hero.rect.left  # то не движется вправо
                self.boom = True
                self.damaged = True

            if xvel < 0:  # если движется влево
                self.rect.left = hero.rect.right  # то не движется влево
                self.boom = True
                self.damaged = True

class poisoned_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.damaged = False

        self.dmg = 35
        self.speed = 7
        boolet_width = 60
        self.image = pygame.Surface((boolet_width, boolet_width))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, boolet_width, boolet_width)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHOOT_P)
        self.boltAnimShoot.play()

    def update(self, platforms, hero):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, hero)

    def collide(self, xvel, platforms, hero):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
        if pygame.sprite.collide_rect(self, hero):
            if xvel > 0:  # если движется вправо
                self.rect.right = hero.rect.left  # то не движется вправо
                self.boom = True
                self.damaged = True

            if xvel < 0:  # если движется влево
                self.rect.left = hero.rect.right  # то не движется влево
                self.boom = True
                self.damaged = True


class egg_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.damaged = False
        self.onGround = False
        boolet_width = 60
        self.dmg = 50
        self.image = pygame.Surface((boolet_width, boolet_width))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, boolet_width, boolet_width)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHOOT_EGG)
        self.boltAnimShoot.play()

    def update(self, platforms, hero):

        self.image.fill(pygame.Color(COLOR))
        self.boltAnimShoot.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += int(self.yvel)

        self.collide(self.xvel, self.yvel, platforms, hero)

        # self.rect.x += self.xvel
        # self.collide(self.xvel, platforms, hero)

    def collide(self, xvel, yvel, platforms, hero):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает
                    self.boom = True

        if pygame.sprite.collide_rect(self, hero):
            if yvel > 0:  # если падает вниз
                self.rect.bottom = p.rect.top  # то не падает вниз
                self.onGround = True  # и становится на что-то твердое
                self.yvel = 0  # и энергия падения пропадает
                self.boom = True
                self.damaged = True


class dead_shot_dawn(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.damaged = False
        self.onGround = False
        self.speed = 0.1

        self.dmg = 15
        self.image = pygame.Surface((BOOLET_WIDTH, BOOLET_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, BOOLET_WIDTH, BOOLET_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHOOT_STAS_D)
        self.boltAnimShoot.play()

    def update(self, platforms, hero):

        self.image.fill(pygame.Color(COLOR))
        self.boltAnimShoot.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += self.speed

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += int(self.yvel)

        self.collide(self.xvel, self.yvel, platforms, hero)

    def collide(self, xvel, yvel, platforms, hero):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает
                    self.boom = True

        if pygame.sprite.collide_rect(self, hero):
            if yvel > 0:  # если падает вниз
                self.rect.bottom = p.rect.top  # то не падает вниз
                self.onGround = True  # и становится на что-то твердое
                self.yvel = 0  # и энергия падения пропадает
                self.boom = True
                self.damaged = True


class dead_shot(pygame.sprite.Sprite):
    def __init__(self, x, y, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.left = left
        self.right = right
        self.boom = False
        self.damaged = False

        self.dmg = 25
        self.speed = 7
        self.image = pygame.Surface((BOOLET_WIDTH, BOOLET_WIDTH))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, BOOLET_WIDTH, BOOLET_WIDTH)  # прямоугольный объект
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным

        self.boltAnimShoot = pyganim.PygAnimation(ANIMATION_SHOOT_STAS)
        self.boltAnimShoot.play()

    def update(self, platforms, hero):
        if self.left:
            self.xvel = -self.speed  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        if self.right:
            self.xvel = self.speed  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimShoot.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.collide(self.xvel, platforms, hero)

    def collide(self, xvel, platforms, hero):
        for p in platforms:

            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                    self.boom = True

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                    self.boom = True
        if pygame.sprite.collide_rect(self, hero):
            if xvel > 0:  # если движется вправо
                self.rect.right = hero.rect.left  # то не движется вправо
                self.boom = True
                self.damaged = True

            if xvel < 0:  # если движется влево
                self.rect.left = hero.rect.right  # то не движется влево
                self.boom = True
                self.damaged = True


def sanya_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT] and  hero.can_fly<= 0:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT] and hero.can_fly<= 0:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            shoot_coldow = CD_SANYA_ULT
            hero.unkill = True
            hero.can_fly = 150

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            shoot_coldow = CD_SANYA_ULT
            hero.unkill = True
            hero.can_fly = 150

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, get_damage)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive)
        for i in bad_bullets:
            i.update(platforms, hero)

        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal
                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))
            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))

        if curret_key == random_key:
            get_key = True
        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        screen.blit(textsurface, (50, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/sanya.mp3')
            pygame.mixer.music.play()

        if get_key:
            screen.blit(key, (115, 5))

        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH/2) > DOOR_X and hero.rect.x + int(WIDTH/2) < DOOR_X + 138 and\
                hero.rect.y + int(HEIGHT/2) > DOOR_Y and hero.rect.y + int(HEIGHT/2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break

def ilya_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    timer_stun = 150
    stop_it=0
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT]:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            shoot_coldow = CD_ILYA_ULT
            hero.can_fly = 150
            hero.shit = False

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            shoot_coldow = CD_ILYA_ULT
            hero.can_fly = 150
            hero.shit = False

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, get_damage, good_bullets, entities)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive, get_damage)
        for i in bad_bullets:
            i.update(platforms, hero)

        if get_damage:
            timer_stun -= SECOND
            if timer_stun<=0:
                timer_stun = 150
                for gd in get_damage:
                    gd.hp -= 10
                    gd.stuned = False
                get_damage.clear()
                stop_it = 0
            elif timer_stun<=50 and stop_it==1:
                for gd in get_damage:
                    gd.hp -= 10
                stop_it += 1
            elif timer_stun<=100 and stop_it==0:
                for gd in get_damage:
                    gd.hp -= 10
                stop_it +=1


        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    if e.left and look_left and not e.boss:
                        e.hp = e.hp - DMG_HAND*1.2
                    elif e.right and look_right and not e.boss:
                        e.hp = e.hp - DMG_HAND*1.2
                    else:
                        e.hp = e.hp - DMG_HAND

                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal

                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))

            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))


        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/ilya.mp3')
            pygame.mixer.music.play()

        if curret_key == random_key:
            get_key = True

        screen.blit(textsurface, (50, 0))
        if get_key:
            screen.blit(key, (115, 5))



        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break


def senya_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        # timer.tick(FPS)
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT]:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and shoot_coldow <= 0:
            shoot_coldow = CD_SENYA_ULT
            hero.can_fly = 220

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level


        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, get_damage, entities)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive)
        for i in bad_bullets:
            i.update(platforms, hero)

        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal

                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))
            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))

        if curret_key == random_key:
            get_key = True

        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        screen.blit(textsurface, (50, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/senya.mp3')
            pygame.mixer.music.play()
        if get_key:
            screen.blit(key, (115, 5))

        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break

def grisha_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.KEYUP and e.key == pygame.K_LSHIFT:
                if shoot_coldow<=0:
                    shoot_coldow = CD_GRISHA_ULT
                hero.unkill = False
            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT] and coldown_punch <= 0:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT] and coldown_punch <= 0:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and shoot_coldow<=0:
            hero.unkill = True


        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, get_damage,good_bullets)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive)
        for i in bad_bullets:
            i.update(platforms, hero)

        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal

                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))
            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))

        if curret_key == random_key:
            get_key = True

        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("/blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("/blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        screen.blit(textsurface, (50, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/grisha.mp3')
            pygame.mixer.music.play()
        if get_key:
            screen.blit(key, (115, 5))

        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break

def dima_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        # timer.tick(FPS)
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT]:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            shoot_coldow = CD_DIMA_ULT
            hero.can_fly = 150
            hero.shit = False

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            shoot_coldow = CD_DIMA_ULT
            hero.can_fly = 150
            hero.shit = False

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, good_bullets, entities)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive, get_damage)
        for i in bad_bullets:
            i.update(platforms, hero)

        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal
                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))
            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                    get_damage.clear()
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))


        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        if curret_key == random_key:
            get_key = True

        screen.blit(textsurface, (50, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/dima.mp3')
            pygame.mixer.music.play()
        if get_key:
            screen.blit(key, (115, 5))

        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break


def misha_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        # timer.tick(FPS)
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.KEYUP and e.key == pygame.K_LSHIFT:
                hero.shoot = False

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT]:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            hero.shoot = True

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            hero.shoot = True

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive,
               get_damage, entities, good_bullets)  # , play_move_left) # передвижение

        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive, hero)
        for i in bad_bullets:
            i.update(platforms, hero)

        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal

                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))
            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))


        if curret_key == random_key:
            get_key = True

        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        screen.blit(textsurface, (50, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/misha.mp3')
            pygame.mixer.music.play()
        if get_key:
            screen.blit(key, (115, 5))

        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.unkill:
            timeF-=SECOND
            if timeF<=0:
                hero.unkill = False

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level

        if hero.hp <= 0:
            chance=randint(0,9)
            if chance == 7:
                hero.hp = 1
                hero.unkill = True
                hero.bullets = 5
                timeF=350
            else:
                break


def igor_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    timer_stun = 150
    stop_it=0
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    while 1:  # Основной цикл программы
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT]:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            shoot_coldow = CD_IGOR_ULT
            hero.can_fly = 200
            hero.shit = False

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            shoot_coldow = CD_IGOR_ULT
            hero.can_fly = 200
            hero.shit = False

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, get_damage, good_bullets, entities)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive, get_damage)
        for i in bad_bullets:
            i.update(platforms, hero)

        if get_damage:
            timer_stun -= SECOND
            if timer_stun<=0:
                timer_stun = 150
                for gd in get_damage:
                    gd.hp -= 10
                    gd.stuned = False
                get_damage.clear()
                stop_it = 0
            elif timer_stun<=50 and stop_it==1:
                for gd in get_damage:
                    gd.hp -= 10
                stop_it += 1
            elif timer_stun<=100 and stop_it==0:
                for gd in get_damage:
                    gd.hp -= 10
                stop_it +=1


        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    if e.left and look_left and not e.boss:
                        e.hp = e.hp - DMG_HAND*1.2
                    elif e.right and look_right and not e.boss:
                        e.hp = e.hp - DMG_HAND*1.2
                    else:
                        e.hp = e.hp - DMG_HAND

                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal
                    e.hp -= e.dmg_deal
                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))

            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))


        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/igor.mp3')
            pygame.mixer.music.play()

        if curret_key == random_key:
            get_key = True

        screen.blit(textsurface, (50, 0))
        if get_key:
            screen.blit(key, (115, 5))



        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break

def nik_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    timer_stun = 150
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    heal = True
    while 1:  # Основной цикл программы
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT]:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT]:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            shoot_coldow = CD_NEK_ULT
            hero.can_fly = 50
            hero.shit = False

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            shoot_coldow = CD_NEK_ULT
            hero.can_fly = 50
            hero.shit = False

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins,
                    salo, SECOND, alive, get_damage, good_bullets, entities)  # , play_move_left) # передвижение
        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive, get_damage)
        for i in bad_bullets:
            i.update(platforms, hero)

        if get_damage:
            timer_stun -= SECOND
            if timer_stun<=0:
                timer_stun = 150
                for gd in get_damage:
                    gd.stuned = False
                get_damage.clear()


        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    if not get_key:
                        e.hp = e.hp - DMG_HAND*1.1
                    else:
                        e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal
                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))

            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))

        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/nik.mp3')
            pygame.mixer.music.play()

        if curret_key == random_key:
            get_key = True
            if heal and hero.hp<=90:
                hero.hp += 10
            elif heal and hero.hp>90:
                hero.hp = 100
            heal = False

        screen.blit(textsurface, (50, 0))
        if get_key:
            screen.blit(key, (115, 5))



        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level
        if hero.hp <= 0:
            break


def max_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg, coldown_punch,
                can_bit, shoot_coldow,
                restart, left, right, up, look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    curret_key = 0
    get_key = False
    paf = DOOR(DOOR_X, DOOR_Y)
    entities.add(paf)
    exite = 0
    stop_ext = True
    timer_stun = 150
    stop_it = 0
    while 1:  # Основной цикл программы
        # timer.tick(FPS)
        SECOND = timer.tick(FPS) / 10
        atak_zone = 0
        fight = False
        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                fight = False
                can_bit = True
            if e.type == pygame.KEYUP and e.key == pygame.K_F12:
                stop_ext = True

            if e.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            up = True

        if keys[pygame.K_LEFT] and hero.can_fly<=0:
            left = True
            look_left = True
            look_right = False

        if keys[pygame.K_RIGHT] and hero.can_fly<=0:
            right = True
            look_right = True
            look_left = False

        if keys[pygame.K_DOWN]:
            right = False
            left = False
            up = False

        if keys[pygame.K_ESCAPE]:
            restart = True

        if keys[pygame.K_F12] and stop_ext:
            exite += 1
            stop_ext = False

        if exite == 3:
            next_level = True
            return next_level

        if coldown_punch > 0:
            coldown_punch -= SECOND
        if shoot_coldow > 0:
            shoot_coldow -= SECOND

        if keys[pygame.K_SPACE] and can_bit and coldown_punch <= 0:
            coldown_punch = CD_SPACE
            fight = True
            can_bit = False
            if not up:
                left = False
                right = False

        if keys[pygame.K_LSHIFT] and look_left and shoot_coldow <= 0:
            shoot_coldow = CD_MAX_ULT
            #hero.shoot = True
            hero.can_fly = 200

        if keys[pygame.K_LSHIFT] and look_right and shoot_coldow <= 0:
            shoot_coldow = CD_MAX_ULT
            #hero.shoot = True
            hero.can_fly = 200

        if restart:
            break
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        if fight and look_right:
            atak_zone = hero.rect.x + int(WIDTH / 2) + RANGE_SPACE

        if fight and look_left:
            atak_zone = hero.rect.x + int(WIDTH / 2) - RANGE_SPACE

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, look_left, look_right, fight, ships, mins, salo, SECOND, alive,
               get_damage, entities, good_bullets)  # , play_move_left) # передвижение

        for i in alive:
            if i.mele:
                i.update(platforms, hero.rect.x, hero.rect.y, SECOND)
            elif i.putin:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND, mins)
            else:
                i.update(platforms, hero.rect.x, hero.rect.y, hero, entities, bad_bullets, SECOND)

        for i in good_bullets:
            i.update(platforms, alive, get_damage)
        for i in bad_bullets:
            i.update(platforms, hero)

        if get_damage:
            timer_stun -= SECOND
            if stop_it == 5:
                for gd in get_damage:
                    gd.stuned = True
                    timer_stun = 150
                stop_it += 1
            elif stop_it<5:
                if timer_stun<=0:
                    timer_stun = 150
                    for gd in get_damage:
                        gd.hp -= 15
                        gd.stuned = False
                    stop_it = 5
                elif timer_stun<=25 and stop_it==4:
                    for gd in get_damage:
                        gd.hp -= 15
                    stop_it += 1
                elif timer_stun<=50 and stop_it==3:
                    for gd in get_damage:
                        gd.hp -= 15
                    stop_it +=1
                elif timer_stun<=75 and stop_it==2:
                    for gd in get_damage:
                        gd.hp -= 15
                    stop_it +=1
                elif timer_stun<=100 and stop_it==1:
                    for gd in get_damage:
                        gd.hp -= 15
                    stop_it +=1
                elif timer_stun<=125 and stop_it==0:
                    for gd in get_damage:
                        gd.hp -= 15
                    stop_it +=1
            else:
                if timer_stun<=0:
                    stop_it = 0
                    timer_stun = 150
                    for gd in get_damage:
                        gd.hp -= 15
                        gd.stuned = False
                    get_damage.clear()



        for e in entities:
            if e in alive:
                if hero.rect.x <= e.rect.x + int(
                        e.width / 2) <= atak_zone and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                if atak_zone <= e.rect.x + int(
                        e.width / 2) <= hero.rect.x + WIDTH and e.rect.y + e.height > hero.rect.y and e.rect.y < hero.rect.y + HEIGHT and fight:
                    e.hp = e.hp - DMG_HAND
                for gb in good_bullets:
                    if gb.boom and gb.damaged == e:
                        e.hp = e.hp - gb.dmg
                        entities.remove([gb])
                        good_bullets.remove(gb)
                if e.hp <= 0:
                    alive.remove(e)
                    entities.remove([e])
                    curret_key += 1
                    if curret_key == random_key:
                        get_key = True
                screen.blit(e.image, camera.apply(e))
                if not hero.unkill:
                    hero.hp -= e.dmg_deal
                    if hero.chosen == 7:
                        e.hp -= 3
                if e.boss:
                    image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    image.fill(pygame.Color(PLATFORM_COLOR))
                    image = pygame.image.load("detail/hp_bos.png")
                    screen.blit(image, (300, 10))
                    cur_HP = e.hp/e.max_hp * 700
                    pygame.draw.rect(screen, (255,0,0), (305, 13, cur_HP, 49))
            elif e in bad_bullets:
                if e.boom and e.damaged:
                    if not hero.unkill:
                        hero.hp -= e.dmg
                    entities.remove([e])
                    bad_bullets.remove(e)
                elif e.boom and not e.damaged:
                    entities.remove([e])
                    bad_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in good_bullets:
                if e.boom and e.stop:
                    entities.remove([e])
                    good_bullets.remove(e)
                else:
                    screen.blit(e.image, camera.apply(e))
            elif e in mins:
                if hero.BOOM == e:
                    if not hero.unkill:
                        hero.hp -= 50
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                    hero.BOOM = None
                elif hero.rect.x <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= atak_zone and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                elif atak_zone <= e.rect.x + int(
                        PLATFORM_WIDTH / 2) <= hero.rect.x + WIDTH and e.rect.y + PLATFORM_HEIGHT > hero.rect.y \
                        and e.rect.y < hero.rect.y + HEIGHT and fight:
                    screen.blit(e.image, camera.apply(e))
                    entities.remove([e])
                    mins.remove(e)
                screen.blit(e.image, camera.apply(e))
            elif e in salo:
                if hero.eat == e:
                    if hero.hp > 90:
                        hero.hp = 100
                        entities.remove([e])
                        salo.remove(e)
                    elif hero.hp <= 90:
                        hero.hp += 10
                        entities.remove([e])
                        salo.remove(e)
                screen.blit(e.image, camera.apply(e))
            else:
                screen.blit(e.image, camera.apply(e))

        if curret_key == random_key:
            get_key = True

        image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        image.fill(pygame.Color(PLATFORM_COLOR))
        image = pygame.image.load("blocks/stats.png")
        screen.blit(image, (0, 0))

        key = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        key.fill(pygame.Color(PLATFORM_COLOR))
        key = pygame.image.load("blocks/key.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(hero.hp), False, (0, 0, 0))

        screen.blit(textsurface, (50, 0))

        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load('music/max.mp3')
            pygame.mixer.music.play()
        if get_key:
            screen.blit(key, (115, 5))

        pygame.display.update()  # обновление и вывод всех изменений на экран

        if hero.unkill:
            timeF-=SECOND
            if timeF<=0:
                hero.unkill = False

        if hero.rect.x + int(WIDTH / 2) > DOOR_X and hero.rect.x + int(WIDTH / 2) < DOOR_X + 138 and \
                hero.rect.y + int(HEIGHT / 2) > DOOR_Y and hero.rect.y + int(HEIGHT / 2) < DOOR_Y + 310 and get_key:
            next_level = True
            return next_level

        if hero.hp <= 0:
            break

def initz_hero(chosen , x, y):
    if chosen == 1:
        hero = Player(x, y)
    elif chosen == 2:
        hero = Player_Dima(x, y)
    elif chosen == 3:
        hero = Player_Grisha(x, y)
    elif chosen == 4:
        hero = Player_Ilya(x, y)
    elif chosen == 5:
        hero = Player_Senya(x, y)
    elif chosen == 6:
        hero = Player_Misha(x, y)
    elif chosen == 7:
        hero = Player_Igor(x, y)
    elif chosen == 8:
        hero = Player_Nik(x, y)
    elif chosen == 9:
        hero = Player_Max(x, y)
    return hero


def initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y):
    if chosen == 1:
        next_level = sanya_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg,
                                 coldown_punch, can_bit,
                                 shoot_coldow, restart, left, right, up, look_left, look_right, ships, mins, salo,
                                 random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 2:
        next_level = dima_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                                bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                look_left, look_right, ships, mins, salo, random_key, get_damage,  DOOR_X, DOOR_Y)
    elif chosen == 3:
        next_level = grisha_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg,
                                 coldown_punch, can_bit,
                                 shoot_coldow, restart, left, right, up, look_left, look_right, ships, mins, salo,
                                 random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 4:
        next_level = ilya_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg,
                                 coldown_punch, can_bit,
                                 shoot_coldow, restart, left, right, up, look_left, look_right, ships, mins, salo,
                                 random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 5:
        next_level = senya_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive, bg,
                                coldown_punch, can_bit,
                                shoot_coldow, restart, left, right, up, look_left, look_right, ships, mins, salo,
                                random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 6:
        next_level = misha_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo,random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 7:
        next_level = igor_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo,random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 8:
        next_level = nik_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo,random_key, get_damage, DOOR_X, DOOR_Y)
    elif chosen == 9:
        next_level = max_plays(timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)
    return next_level

def main():
    pygame.init()  # Инициация PyGame
    screen = pygame.display.set_mode(
        DISPLAY)  # Создаем окошко  screen = pygame.display.set_mode(DISPLAY,pygame.FULLSCREEN)
    pygame.display.set_caption("GAME_3")  # Пишем сверху
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(pygame.Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    #Sound1 = pygame.mixer.Sound('detail/soundtrack.mp3')
    #pygame.mixer.music.load('detail/soundtrack.mp3')
    pygame.mixer.music.load('music/start.mp3')
    pygame.mixer.music.play()
    #sound0 = pygame.mixer.Sound('music/soundtrack.mp3')
    #sound1 = pygame.mixer.Sound('music/level up.mp3')
    #sound2 = pygame.mixer.Sound('music/horror.mp3')
    #sound3 = pygame.mixer.Sound('music/soundtrack chill.mp3')
    #pygame.mixer.music.stop()

    ###             MENU
    next_level = False
    while not next_level:
        win = pygame.display.set_mode((1280, 720))
        back_fon = pygame.image.load('detail/esm_presents.png')
        win.blit(back_fon, (0, 0))


        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                next_level = True
            if e.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

    next_level = False
    while not next_level:
        win = pygame.display.set_mode((1280, 720))
        back_fon = pygame.image.load('detail/start_screen.png')
        win.blit(back_fon, (0, 0))

        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                next_level = True
            if e.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

    next_level = False
    y=0
    while not next_level:
        win = pygame.display.set_mode((1280, 720))
        if y==0:
            back_fon = pygame.image.load('detail/menu_1.png')
            win.blit(back_fon, (0, 0))
        if y==1:
            back_fon = pygame.image.load('detail/menu_2.png')
            win.blit(back_fon, (0, 0))

        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                if y==0:
                    y=1
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                if y == 1:
                    y = 0
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                if y == 1:
                    next_level = True
            if e.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

    next_level = False
    y = 0
    x = 0
    chosen = 0
    last_chosen = 0

    pygame.mixer.music.load('music/chose.mp3')
    pygame.mixer.music.play(start=2.5)
    while not next_level:
        win = pygame.display.set_mode((1280, 720))
        if y == 0 and x == 0:
            back_fon = pygame.image.load('detail/chose_0_0.png')
            win.blit(back_fon, (0, 0))
            chosen = randint(1,9)
            rand = True

        if y == 0 and x == 1:
            back_fon = pygame.image.load('detail/chose_1_0.png')
            win.blit(back_fon, (0, 0))
            chosen = 1
            rand = False

        if y == 0 and x == 2:
            back_fon = pygame.image.load('detail/chose_2_0.png')
            win.blit(back_fon, (0, 0))
            chosen = 2
            rand = False

        if y == 0 and x == 3:
            back_fon = pygame.image.load('detail/chose_3_0.png')
            win.blit(back_fon, (0, 0))
            chosen = 3
            rand = False

        if y == 0 and x == 4:
            back_fon = pygame.image.load('detail/chose_4_0.png')
            win.blit(back_fon, (0, 0))
            chosen = 9
            rand = False

        if y == 1 and x == 0:
            back_fon = pygame.image.load('detail/chose_0_1.png')
            win.blit(back_fon, (0, 0))
            chosen = 4
            rand = False

        if y == 1 and x == 1:
            back_fon = pygame.image.load('detail/chose_1_1.png')
            win.blit(back_fon, (0, 0))
            chosen = 5
            rand = False

        if y == 1 and x == 2:
            back_fon = pygame.image.load('detail/chose_2_1.png')
            win.blit(back_fon, (0, 0))
            chosen = 6
            rand = False

        if y == 1 and x == 3:
            back_fon = pygame.image.load('detail/chose_3_1.png')
            win.blit(back_fon, (0, 0))
            chosen = 7
            rand = False

        if y == 1 and x == 4:
            back_fon = pygame.image.load('detail/chose_4_1.png')
            win.blit(back_fon, (0, 0))
            chosen = 8
            rand = False

        if chosen!=last_chosen and not rand:
            last_chosen = chosen
            if chosen == 1:
                pygame.mixer.music.load('music/sanya.mp3')
                pygame.mixer.music.play(start=2.5)
            elif chosen == 2:
                pygame.mixer.music.load('music/dima.mp3')
                pygame.mixer.music.play()
            elif chosen == 3:
                pygame.mixer.music.load('music/grisha.mp3')
                pygame.mixer.music.play(start=1)
            elif chosen == 4:
                pygame.mixer.music.load('music/ilya.mp3')
                pygame.mixer.music.play()
            elif chosen == 5:
                pygame.mixer.music.load('music/senya.mp3')
                pygame.mixer.music.play(start=61)
            elif chosen == 6:
                pygame.mixer.music.load('music/misha.mp3')
                pygame.mixer.music.play()
            elif chosen == 7:
                pygame.mixer.music.load('music/igor.mp3')
                pygame.mixer.music.play(start=15.5)
            elif chosen == 8:
                pygame.mixer.music.load('music/nik.mp3')
                pygame.mixer.music.play()
            elif chosen == 9:
                pygame.mixer.music.load('music/max.mp3')
                pygame.mixer.music.play()

        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                if y == 1:
                    y = 0
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                if y == 0:
                    y = 1
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                if x > 0:
                    x -= 1
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                if x < 4:
                    x += 1
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and chosen!=0:
                next_level = True
            if e.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

    ###             MENU
    next_level = False
    while not next_level:
        win = pygame.display.set_mode((1280, 720))
        back_fon = pygame.image.load('detail/uprav.png')
        win.blit(back_fon, (0, 0))

        for e in pygame.event.get():  # Обрабатываем события

            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                next_level = True
            if e.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
    # LEVEL 1.1
    next_level = False
    while not next_level:
        restart = False
        #pygame.mixer.music.load('music/soundtrack.mp3')
        #pygame.mixer.music.play()


        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объектыLEVEL 3.3
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = [] # получили урон и больше не будут, до ...


        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-   H                        -                                D     - ",
            "---------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0,1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'B':
                    en = Zolotov_BOS(x,y, True,False)
                    #en = Stas_BOS(x,y, True,False)
                    #en = Putin_BOS(x, y, True, False)
                    entities.add(en)
                    alive.append(en)



                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive)>0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms, alive,
                                bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-          --                                                     - ",
            "- D        --                                                     - ",
            "-------------                                                     - ",
            "-                                                                 - ",
            "-                                     s                           - ",
            "-                    ---              --                          - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                            --                  --               - ",
            "-H                          E--xxxxxxxxxxxxxxxxxx--E        ss    - ",
            "-------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera, platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 2.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                        s        - ",
            "-                                      -                 -        - ",
            "-                                      -                 -        - ",
            "-                                      -                 -       x- ",
            "-                                      -                 -      --- ",
            "-                                      -D     E E       x-        - ",
            "-                                      -------------------        - ",
            "-      E   E    - x                                      -        - ",
            "------------------------                                 -x       - ",
            "-                       -                                 --      - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                 - ",
            "-                                                                x- ",
            "-                               --                              --- ",
            "- H                            x--       ss                     --- ",
            "-------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 3.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "- H                                                                 - ",
            "---------                                                           - ",
            "-        -                                           - P          D - ",
            "-          -                   s                     ---------------- ",
            "-            -                szs                                   - ",
            "-              -               s                                    - ",
            "-                -                              -                   - ",
            "-                  -                          -                     - ",
            "-                  -                        -                       - ",
            "-                  -                      -                         - ",
            "-                  - x x x     P        -          x x x x          - ",
            "-------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 3.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                    s                                              - ",
            "-                    --           --                       -        - ",
            "-                          z                               -         - ",
            "-                                                          -        - ",
            "-                                                          -         - ",
            "-             s                          s              D  -        - ",
            "-             --           --            --             ---          - ",
            "- H           --        A  --         P  -- x x x x x x---          - ",
            "-------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 3.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                     --            --                              - ",
            "-              --     --  H     D   --       --                     - ",
            "-                     ----------------                              - ",
            "-                                                        s          - ",
            "-        --                              z              --          - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                 s                                                 - ",
            "-s                                                                  - ",
            "----                                                             ---- ",
            "----         E  x      A             E           x     P         ---- ",
            "--------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 4.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                             -      - ",
            "-                                                             -      - ",
            "-                                                             -      - ",
            "-    --                                                       -      - ",
            "-H   --                                                       -      - ",
            "-------                                                       -      - ",
            "-                                                             f      - ",
            "-                                                             f      - ",
            "-                                                             f      - ",
            "-                           xx                  xx            f      - ",
            "- s s                       --                  --            f      - ",
            "- s s              m    R   --         m    R   --            f    D - ",
            "--------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 4.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                     -",
            "-                                                                     -",
            "-                                                                     -",
            "-               -           -                     -                   -",
            "-               -  E   -                  - E     -                   -",
            "-               --------                  ---------                   -",
            "-                                                               z     -",
            "-                                  -                                  -",
            "-                                                                     -",
            "-                                                                     -",
            "-           s                                   s                     -",
            "-                            -                                        -",
            "-                                                                     -",
            "- H                                                                   -",
            "----               -              f             -                     -",
            "-                                                                     -",
            "-            -             -              -                           -",
            "-                                                             f     D -",
            "----                                                   -            ---",
            "----                                                                  -",
            "----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx---",
            "--------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 4.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-  H                      R             r        s                   - ",
            "------                   ---    -      ---       -      -            - ",
            "-    -                                                               - ",
            "-    -                                                            D  - ",
            "-    -                                                            ---- ",
            "-    -                                                           -   - ",
            "-    -                                                         -     - ",
            "-    -                     s            s                    -       - ",
            "-    -                                                     -         - ",
            "-    -                                                   -           - ",
            "-    -                                                 -             - ",
            "-    -                                               -               - ",
            "-    -              E            P           A     -                 - ",
            "-    -                          x                -                   - ",
            "--------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 5
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/zolotov.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "- s                                                                 - ",
            "- s                                                                 - ",
            "- s                                                                 - ",
            "- s                                                                 - ",
            "- s                                                                 - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-             H                                       B        D    - ",
            "---------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                if col == 'B':
                    en = Zolotov_BOS(x, y, True, False)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 6
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack chill.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "z                                                                     ",
            "-                                                                   - ",
            "-                                                       x      D    - ",
            "-               ----------------------------------------------------- ",
            "-                                                                   - ",
            "-    -                   z                                          - ",
            "- ---                                                                 - ",
            "-   -                                                                - ",
            "-     -                                                              - ",
            "-       -                                                            - ",
            "-         -                                                          - ",
            "-           -                                                        - ",
            "--------------------------------------------------------             - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                   x- ",
            "-                                                               ------ ",
            "-                                                               -    - ",
            "-                                                             -      - ",
            "-                                                            -       - ",
            "-                                                           -        - ",
            "-                                                          -         - ",
            "-                 x         x           x        x      x -          - ",
            "-            ----------------------------------------------------------",
            "-                                                                    - ",
            "-                                                                    - ",
            "---                                                                  - ",
            "- --                                                                 - ",
            "-  --                                                                - ",
            "-ssss-                                                               - ",
            "-sssss                                                               - ",
            "-sssss                                                               - ",
            "-sssssx           x          x                         x       H     - ",
            "----------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 6.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack chill.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-  H           s         s      s        s         D                 - ",
            "------         -         -      -        f       -----     -         - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                  - - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                             -       - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                - ",
            "-      -----------------------------------------------               - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                            -       - ",
            "-                                                                    - ",
            "-              E                        A                 P          - ",
            "-x                                                                   - ",
            "--------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 6.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack chill.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-  H                                                                 - ",
            "------                                                               - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                    s                                               - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                         s          - ",
            "-                                    xx                              - ",
            "-                                    --                              - ",
            "-  r     E                   A       --  r       m                D  - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 8.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack chill.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                     --                                            - ",
            "-                     --                                            - ",
            "-                     --                                            - ",
            "-                     --                                            - ",
            "-                     --                                            - ",
            "-                     --                                             - ",
            "-                     --    D                                        - ",
            "-                     -------------------------------                - ",
            "-                     --                           ----              - ",
            "- s                   --                                             - ",
            "- s                   ff                                             - ",
            "- s                   ff                                     --------- ",
            "- s                   ff                                     -       - ",
            "-                     ff                                   ----       - ",
            "-                     ff                                   -          - ",
            "-                     ff                               ----          - ",
            "-                   ----                               -            - ",
            "-                 -   --                            ----           - ",
            "-               -     --                            -                - ",
            "-  H          -       --     E   P     A          ---                - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 9.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/soundtrack chill.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                   E          s                                     - ",
            "-                   -----                                            - ",
            "-                   -   -                                            - ",
            "-               -----   -                                            - ",
            "-           E   -       -                                            - ",
            "-           -----       -                      s                   - ",
            "-           -           -                     --                     - ",
            "- H     ----            -    m     m      R   --    A          D   - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 9.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-  H                                   D                   -         - ",
            "-------         ------           -----------------                   - ",
            "-     -         -    -           -               -                   - ",
            "-     -    s    -    -           -               --                  - ",
            "-     -         -    -           -               -                 - - ",
            "-     -         -    -           -               -                   - ",
            "-     -    s    -    -           -               -                   - ",
            "-     -         -    -           -               -                   - ",
            "-     -         -    -           -               -                   - ",
            "-     -    s    -    -           -               -            -       - ",
            "-     -         -    -           -               -                   - ",
            "-     -         -    -           -               -                   - ",
            "-     -         -    -           -       E       - -                 - ",
            "-     -    s    f    -           -               -                   - ",
            "-     -         f    -           fffffffffffffffff                   - ",
            "-     -         f    -           fffffffffffffffff                   - ",
            "-     -         f    -           fffffffffffffffff                   - ",
            "-     -         f    -           fffffffffffffffff           -       - ",
            "-     -         f    -           fffffffffffffffff                   - ",
            "-     - s s s s -    -           fffffffffffffffff                   - ",
            "-     -         -    -           -fffffffffffffff-                   - ",
            "-     - s s s s - x  -           -fffffffffffffff-                   -",
            "----------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 9.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                         -                         - ",
            "-                                         -                         - ",
            "-                                         -                         - ",
            "- H                                       -                          - ",
            "-               s            Z            -                          - ",
            "----------------------------------        -                          - ",
            "-                                         -                          - ",
            "-                                         -                          - ",
            "-                                         -                          - ",
            "-                                         -                          - ",
            "-                                         -                          - ",
            "-       s                                 -                          - ",
            "-                                         f            s             - ",
            "-                                         f                          - ",
            "-                                         f                      D   - ",
            "-                       s                 f                    ------- ",
            "-                                         f                          - ",
            "-                                         f                          - ",
            "-     Z     -     Z          -      Z     -           T       Z      - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 10.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-           C                                                      - ",
            "-H                                                                   - ",
            "-----                                                               - ",
            "-    -                z                                              - ",
            "-      -                                                             - ",
            "-        -                                                           - ",
            "-          -                     C                                   - ",
            "-            -                                                       - ",
            "-              -                                   x  ssss           - ",
            "-                -    s                            -------           - ",
            "-                  -                                                 - ",
            "-                    -                                               - ",
            "-                      -                                             - ",
            "-                        --                                          - ",
            "-                           -                                     D  - ",
            "-                             -    T     x      T               ------ ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 10.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                       -           - ",
            "-                                                       -           - ",
            "-                                                       -           - ",
            "-                                                       -           - ",
            "-     -          s         s           s           H    -           - ",
            "- -----         ff        ff           ff          ------            - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                s                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-      M               Z                   Z                   D     - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 10.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-  D                    M    M                  -                     - ",
            "- ------------------------------------------------                   - ",
            "-                                                                    - ",
            "-                      C                                             - ",
            "-                                                       s            - ",
            "-                                                      --            - ",
            "-                                                      ---            - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                         s                                     s    - ",
            "-                      ------           ------                -------- ",
            "-                      -    -           -    -                -      - ",
            "-  H                   -    -      Z    -    -      T         -      - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 11.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                s                                             H    - ",
            "- ----------------                        --------------------------- ",
            "-                f                        -                          - ",
            "-                f                        -                          - ",
            "-                f                        -                          - ",
            "-                f                        -                          - ",
            "-                f                        -                          - ",
            "-                f           Z            -                          - ",
            "-                -                 s      -                          - ",
            "-                --------------------------                          - ",
            "-              z -                        f                          - ",
            "-                                         f                         - ",
            "-                                         f                         - ",
            "-                                         f                          - ",
            "-                                         f                          - ",
            "-    M                       M            f                          - ",
            "-                                         -          m   R      D    - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 11.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/horror.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "- D                       m                                          - ",
            "---------------           -----                                      - ",
            "-             -             -               -                        - ",
            "-  s ss s                   -               -                        - ",
            "-                           -    M          -                        - ",
            "-        Z                - ---------------------                    - ",
            "-                       -                         -                  - ",
            "-                     -                             -               s- ",
            "-    Z      Z      -                                 -              - ",
            "--------------------                                    -            - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                   -- ",
            "-                                                                  --- ",
            "-                                  -                              ---- ",
            "-                                 ---                            ----- ",
            "-  H                 mmmmmmmmmmm -----mmmmmmm                  ------- ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 11.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/stas.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                               s    - ",
            "-                                                               s    - ",
            "-                                                               s    - ",
            "-                                                               s    - ",
            "-                                                               s    - ",
            "-                                                               s    - ",
            "-                             ----                              s    - ",
            "-                                                               s    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-         H                                          B           D   - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'B':
                    en = Stas_BOS(x,y,True,False)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 12.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                 C                                  - ",
            "-                                                                    - ",
            "-               s                                    s               - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                     -                        -                     - ",
            "-                     --                      --                     - ",
            "-                     - -                    - -     E               - ",
            "-  H                  -  -         M        -  -                D    - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 12.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-  H                                ssssssss                         - ",
            "--------------------fffffff------------------------------------------- ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-     A       P                           -        -       E         - ",
            "-------------------------------------------        ------------------- ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                       Z                                   T        - ",
            "-  D                                                                 -",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 12.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                -                                  - ",
            "-                                -                                  - ",
            "-                                -                                  - ",
            "-   H                     s      -                                  - ",
            "-------------           ----------                                  - ",
            "-                                                                    - ",
            "-                                               s                    - ",
            "-                                              ------                - ",
            "-                                              -                     - ",
            "-                        P                    -                      - ",
            "-                                             -                      - ",
            "-   E                 -------------    A      -                      - ",
            "-----------------------           -----------                        - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                          x       xx- ",
            "-                                                    ----------------- ",
            "-                                                                    - ",
            "-                          s                                         - ",
            "-  D                       -            M                 Z          - ",
            "--------------     T       -------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 14.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "- H                                                                  - ",
            "-----                                                                - ",
            "-                                                     s              - ",
            "-                                                     s              - ",
            "-                                                     s       z      - ",
            "-                                                     s              - ",
            "-                                                     s              - ",
            "-                                                     -              - ",
            "-   Z       Z    Z    Z    Z    Z   Z                 -              - ",
            "-                                                     -        D     - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 14.2
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                 s                          s                       - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                          --       S              S            D    - ",
            "-                         ---------------------------------------------",
            "-                      ------                                        - ",
            "-  H                ----------                                       - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 14.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                 -                                                 - ",
            "-                 -                                                 - ",
            "-                 -                                                 - ",
            "- H           R   -                                                - ",
            "-----         -----                                                 - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                   --------------                   - ",
            "-                S                  -            -                   - ",
            "-                                ss -            -                   - ",
            "-------------------------------------            -----               - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                         r                          - ",
            "-                                        ---                        - ",
            "-                                        - -                         - ",
            "-                                        - -                         - ",
            "-                                        - -                        - ",
            "-  D                 L                   - -s s     S                - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 15.1
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                    - ",
            "-                                                                    - ",
            "- H                                                                  - ",
            "------------------------------------------------------               - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-    z                                                        z      - ",
            "-                                                                    - ",
            "-    z                                                               - ",
            "-                               L                   s                - ",
            "-            -      m                     m                          - ",
            "-    z       --------------------------------------------------------- ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-    z                                                               - ",
            "-                                                    s               - ",
            "-                                L                                   - ",
            "-             m             m             m               -          - ",
            "-----------------------------------------------------------          - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                     s              - ",
            "-                                                                    - ",
            "-  D                m             L         m                   xxxx - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 15.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-            -----                   -         ----                 - ",
            "-            -   -                                                  - ",
            "-            -   -      H   D                        -              - ",
            "-            -   -      ------                                       - ",
            "-            -   -      -    -                              s        - ",
            "-            -   -      -    -                                       - ",
            "-   s        -   -      -    -                            ---        - ",
            "-            -   -      -    -                                       - ",
            "-            -   -      -    -                                        - ",
            "-            -   --------    ---------------------                   - ",
            "-            -------------------------------------                 - - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                         s          - ",
            "-                                                          ---       - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-         r                       A     A     A                      - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break

    # LEVEL 15.3
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/level up.mp3')
        pygame.mixer.music.play()
        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "----------------------------------------------------------------------",
            "-               -          -       -             -           -      - ",
            "-               f          f       f             f           f      - ",
            "-               f          f       f             f           f      - ",
            "-               f          f       f             f           f       - ",
            "-               f          f       f             f           f       - ",
            "-               f          f       f             f           f       - ",
            "-               f          f   H   f             f           f       - ",
            "----ffff---------------------------------ffff------------------ffff--- ",
            "-         f        f        -         f         -         f          - ",
            "-         f        f        -         f         -         f          - ",
            "-         f        f        -         f         -         f          - ",
            "-         f        f        -         f         -         f          - ",
            "-         f        f        -         f         -         f          - ",
            "-         f        f        -         f         -         f          - ",
            "-------------ffff--------------ffff----------------------------------- ",
            "-                  -                     -               -           - ",
            "-                  -                     f               f           - ",
            "-                  -                     f               f           - ",
            "-                  -                     f               f           - ",
            "-                  -                     f               f           - ",
            "-                  -                     f               f           - ",
            "-                  -                     f               f           - ",
            "---ffff------fffff--ffff--------------------------------------ffff---- ",
            "-          -             -             -           -                 - ",
            "-          -             f             -           f                 - ",
            "-          -             f             -           f                 - ",
            "-          -             f             -           f                 - ",
            "-          -             f             -           f                 - ",
            "-          -             f             -           f                 - ",
            "-          -             f             -           f                 - ",
            "--ffff------ffff---------------ffff------ffff------------------ffff--- ",
            "-        -         -        -        f        -        f      f      - ",
            "-        f         -        f        f        -        f      f      - ",
            "-        f         -        f        f        -        f      f      - ",
            "-        f         -        f        f        -        f      f      - ",
            "-        f         -        f        f        -        f      f      - ",
            "-        f         -        f        f        -        f      f      - ",
            "-        f         -        f        f        -        f      f      - ",
            "-----------------------ffff--ffff-------ffff------ffff----------ffff-- ",
            "-         f          -             -            -         -          - ",
            "-         f          f             -            -         -          - ",
            "-         f          f             -            -         -          - ",
            "-         f          f             -            -         -          - ",
            "-         f          f             -            -         -          - ",
            "-         f          f             -            -         -          - ",
            "-         f          f             -            -         -          - ",
            "--ffff----------ffff---------------------------------ffff--ffff--ffff- ",
            "-      f       -       f       -       f      f     f     -     -     - ",
            "-      f       -       f       -       f      f     f     -     -     - ",
            "-      f       -       f       -       f      f     f     -     -     - ",
            "-      f       -       f       -       f      f     f     -     -     - ",
            "-      f       -       f       -       f      f     f     -     -     - ",
            "-      f       -       f       -       f      f     f     -     -     - ",
            "-      -       -       -       -       -      f     f     -     -     - ",
            "-ffff---ffff---------------ffff-ffff------ffff-ffff--ffff--ffff--ffff- ",
            "-     -     f      f     -     -    -    -    -    -     -     -     - ",
            "-     -     f      f     -     -    -    -    -    -     -     -     - ",
            "-     -     f      f     -     -    -    -    -    -     -     -     - ",
            "-     -     f      f     -     -    -    -    -    -     -     -     - ",
            "-     -     f      f     -     -    -    -    -    -     -     -     - ",
            "-     -     f      f     -     - D  -    -    -    -     -     -     - ",
            "---------------------------------------------------------------------- "]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen == 1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break
    # LEVEL 16
    next_level = False
    while not next_level:
        restart = False
        pygame.mixer.music.load('music/putin.mp3')
        pygame.mixer.music.play()

        left = right = False  # по умолчанию - стоим
        up = False
        look_left = False
        look_right = False
        coldown_punch = 0
        can_bit = True

        alive = []
        entities = pygame.sprite.Group()  # Все объекты
        platforms = []  # то, во что мы будем врезаться или опираться
        ships = []  # то, что нас будет убивать при касании
        mins = []  # мины
        salo = []  # сало
        get_damage = []  # получили урон и больше не будут, до ...

        for i in alive:
            entities.add(i)

        level = [
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                   - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                        zsss              sss z                     - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                                                                    - ",
            "-                   H                                   B        D   - ",
            "----------------------------------------------------------------------",
            "-------------------------------------------------------------------"]

        timer = pygame.time.Clock()
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                if col == "f":
                    pf = Platform(x, y)
                    entities.add(pf)
                if col == "x":
                    sh = Shipi(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "z":
                    sh = Svaston(x, y)
                    entities.add(sh)
                    ships.append(sh)
                if col == "m":
                    sh = Mina(x, y)
                    entities.add(sh)
                    mins.append(sh)
                if col == "s" and chosen ==1:
                    sl = Salo(x, y)
                    entities.add(sl)
                    salo.append(sl)
                if col == 'D':
                    DOOR_X = x
                    DOOR_Y = y - 245
                if col == 'H':
                    hero = initz_hero(chosen, x, y)
                    entities.add(hero)
                if col == 'E':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'P':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_pistol(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'A':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Enemy_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'R':
                    en = Turrel(x, y, True, False)
                    entities.add(en)
                    alive.append(en)
                if col == 'r':
                    en = Turrel(x, y, False, True)
                    entities.add(en)
                    alive.append(en)
                if col == 'Z':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Zombe(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'M':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Mnogonoza(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'C':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Chicken(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'T':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Pudje(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'S':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_Enemy(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'L':
                    lft = randint(0, 1)
                    if lft == 1:
                        lft = True
                    else:
                        lft = False
                    en = Elit_automat(x, y, lft, not lft)
                    entities.add(en)
                    alive.append(en)
                if col == 'B':
                    en = Putin_BOS(x,y, True,False)
                    entities.add(en)
                    alive.append(en)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
        total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

        camera = Camera(camera_configure, total_level_width, total_level_height)
        good_bullets = []
        bad_bullets = []

        shoot_coldow = 0
        ##
        if len(alive) > 0:
            random_key = randint(1, len(alive))
        else:
            random_key = 0
        next_level = initz_plays(chosen, timer, hero, entities, good_bullets, bad_bullets, screen, camera,
                                 platforms,
                                 alive,
                                 bg, coldown_punch, can_bit, shoot_coldow, restart, left, right, up,
                                 look_left, look_right, ships, mins, salo, random_key, get_damage, DOOR_X, DOOR_Y)

        if next_level:
            break
    ############################################
    next_level = False
    y = 0
    pygame.mixer.music.load('music/final.mp3')
    pygame.mixer.music.play()
    while not next_level:
        win = pygame.display.set_mode((1280, 720))
        back_fon = pygame.image.load('detail/final.png')
        win.blit(back_fon, (50, y))
        y -= 5

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
