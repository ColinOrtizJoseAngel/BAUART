class Config:
    SECRET_KEY = 'b#Qsf*7AWTX7Vp45'

class DevelopmentConfig(Config):
    DEBUG = True

config={
    'development':DevelopmentConfig
}