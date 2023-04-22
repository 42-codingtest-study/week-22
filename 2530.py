# hour, mnt, scd = map(int, input().split())
# need_scd = int(input())

# def stom():
#     global scd, mnt
#     if scd // 60 :
#         mnt += (scd // 60)
#         scd %= 60

# def mtoh():
#     global mnt, hour
#     if mnt // 60 :
#         hour += (mnt // 60)
#         if hour // 24 :
#             hour %= 24
#         mnt %= 60

# scd += need_scd
# stom()
# mtoh()

# print(hour, mnt, scd, sep=' ') 

hour, mnt, scd = map(int, input().split())
need_scd = int(input())

scd += need_scd
mnt += scd // 60
hour += mnt // 60

print(hour % 24, mnt % 60, scd % 60)