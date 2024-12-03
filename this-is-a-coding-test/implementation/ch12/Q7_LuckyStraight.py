# 321p, 럭키 스트레이트

n = list(map(int, input()))
half = int(len(n) / 2)

left = sum(n[:half])
right = sum(n[half:])

if left == right: print("LUCKY")
else: print("READY")