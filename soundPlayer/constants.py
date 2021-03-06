# 定数
PLAYER_DEFAULT_SPEAKER = -101

# ソースタイプ
PLAYER_SOURCETYPE_FILE = 201
PLAYER_SOURCETYPE_STREAM = 202
PLAYER_SOURCETYPE_NUL = 203
PLAYER_SOURCETYPE_PATH = 204
PLAYER_SOURCETYPE_URL = 205

# 設定読み出し定数
PLAYER_CONFIG_DEVICE = 301
PLAYER_CONFIG_ID = 302
PLAYER_CONFIG_SOURCE = 303
PLAYER_CONFIG_SOURCETYPE = 304
PLAYER_CONFIG_SPEED = 305
PLAYER_CONFIG_KEY = 306
PLAYER_CONFIG_FREQ = 307
PLAYER_CONFIG_AMPVOL = 308
PLAYER_CONFIG_VOLUME = 309
PLAYER_CONFIG_AMP = 310

# ステータス
PLAYERSTATUS_STATUS_OK = 401
PLAYERSTATUS_STATUS_FAILD = 402
PLAYER_STATUS_PLAYING = 403
PLAYER_STATUS_PAUSED = 404
PLAYER_STATUS_STOPPED = 405
PLAYER_STATUS_END = 406
PLAYER_STATUS_LOADING = 407
PLAYER_STATUS_DEVICEERROR = 408
PLAYER_STATUS_OVERREWIND = 409

# 命令送信
PLAYER_SEND_INIT = 501
PLAYER_SEND_FILE = 502 #ファイルからストリーム生成
PLAYER_SEND_URL = 503 #URLからストリーム生成
PLAYER_SEND_PLAY = 504
PLAYER_SEND_PAUSE = 505
PLAYER_SEND_SPEED = 506
PLAYER_SEND_KEY = 507
PLAYER_SEND_FREQ = 508
PLAYER_SEND_GETPOSITION = 509
PLAYER_SEND_SETPOSITION = 510
PLAYER_SEND_EXIT = 511
PLAYER_SEND_GETSTATUS = 512
PLAYER_SEND_GETLENGTH = 513
PLAYER_SEND_SETNETTIMEOUT = 514
PLAYER_SEND_SETHLSDELAY = 515
PLAYER_SEND_VOLUME = 516
PLAYER_SEND_AUTOCHANGE = 517
PLAYER_SEND_FREE = 518
PLAYER_SEND_STOP = 519
PLAYER_SEND_GETREPEAT = 520
PLAYER_SEND_SETREPEAT = 521
PLAYER_SEND_NEWPLAYER = 522
PLAYER_SEND_DEVICE = 523
PLAYER_SEND_IS_DEVICEOK = 524
