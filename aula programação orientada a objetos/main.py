velocida = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RANDAR_RANGER = 1

if velocida > RADAR_1:
    print('passou da velocida')
    if local_carro >= (LOCAL_1 - RANDAR_RANGER) and \
        local_carro <= (LOCAL_1 + RANDAR_RANGER):
        print('carro multado em radar 1')