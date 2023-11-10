from enum import auto
from os import path

from mlgame.utils.enum import StringEnum
# game
WIDTH = 900
HEIGHT = 600
BG_COLOR = "#2B2B49"
PG_COLOR = "#B3E5FC"

# ball -> squid
# BALL_COLOR = "#FFEB3B"
SQUID_VEL = 10
SQUID_W = 50
SQUID_H = 70
SQUID_GROWTH_SCORE_STEP = 10
SQUID_GROWTH_SIZE_STEP=10
SQUID_GROWTH_VEL_STEP=3
SQUID_SIZE_MAX = 125
SQUID_SIZE_MIN = 20
SQUID_VEL_MAX = 25
SQUID_VEL_MIN = 10

ASSET_IMAGE_DIR = path.join(path.dirname(__file__), "../asset/img")
# food
class FoodTypeEnum(StringEnum):
    FOOD_1 = auto()
    FOOD_2 = auto()
    FOOD_3 = auto()
    GARBAGE_1 = auto()
    GARBAGE_2 = auto()
    GARBAGE_3 = auto()


FOOD_LV1_SIZE = 30
FOOD_LV2_SIZE = 40
FOOD_LV3_SIZE = 50

# path of assets
ASSET_PATH = path.join(path.dirname(__file__), "..", "asset")
LEVEL_PATH = path.join(path.dirname(__file__), "..", "levels")
SOUND_PATH = path.join(path.dirname(__file__), "..", "asset", "sounds")
MUSIC_PATH = path.join(path.dirname(__file__), "..", "asset", "music")

BG_PATH = path.join(ASSET_IMAGE_DIR, "background.png")
SQUID_PATH = path.join(ASSET_IMAGE_DIR, "squid.png")

IMG_ID_FOOD01_L = "food_01_L"
IMG_ID_FOOD02_L = "food_02_L"
IMG_ID_FOOD03_L = "food_03_L"
IMG_ID_FOOD01_R = "food_01_R"
IMG_ID_FOOD02_R = "food_02_R"
IMG_ID_FOOD03_R = "food_03_R"

FOOD01_L_PATH = path.join(ASSET_IMAGE_DIR, "food_01_L.png")
FOOD02_L_PATH = path.join(ASSET_IMAGE_DIR, "food_02_L.png")
FOOD03_L_PATH = path.join(ASSET_IMAGE_DIR, "food_03_L.png")
FOOD01_R_PATH = path.join(ASSET_IMAGE_DIR, "food_01_R.png")
FOOD02_R_PATH = path.join(ASSET_IMAGE_DIR, "food_02_R.png")
FOOD03_R_PATH = path.join(ASSET_IMAGE_DIR, "food_03_R.png")

GARBAGE01_PATH = path.join(ASSET_IMAGE_DIR, "garbage_01.png")
GARBAGE02_PATH = path.join(ASSET_IMAGE_DIR, "garbage_02.png")
GARBAGE03_PATH = path.join(ASSET_IMAGE_DIR, "garbage_03.png")

# TODO check url
BG_URL = BG_PATH
SQUID_URL = SQUID_PATH
FOOD01_L_URL = FOOD01_L_PATH
FOOD02_L_URL = FOOD02_L_PATH
FOOD03_L_URL = FOOD03_L_PATH
FOOD01_R_URL = FOOD01_R_PATH
FOOD02_R_URL = FOOD02_R_PATH
FOOD03_R_URL = FOOD03_R_PATH
GARBAGE01_URL = GARBAGE01_PATH
GARBAGE02_URL = GARBAGE02_PATH
GARBAGE03_URL = GARBAGE03_PATH
# BAR_URL = "https://raw.githubusercontent.com/PAIA/dont_touch/master/asset/image/bar.png"

