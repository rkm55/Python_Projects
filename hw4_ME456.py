# HW 4 ME 456
# Ryan Melander
# --------------------
# Problem 7.1a
ply = [0, 90, 0, 90]   # ply = [0/90/0/90]s
ply.reverse()
# lamina properties
E1 = 180    # GPa
E2 = 10
N = len(ply)
Ex = [0]*int(N)
# Ex for all layers
for i in range(N):
    if ply[i] == 0:
        Ex[i] = E1
    elif ply[i] == 90:
        Ex[i] = E2
# Calculate Ef
Ef = 0
for i in range(N):
    Ef = (8/pow(N*2, 3))*Ex[i]*(3*pow(i+1, 2) - 3*(i+1) + 1) + Ef
print(Ef)   # Ef = 126.875
