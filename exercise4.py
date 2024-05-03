# =============================================================================
# quad_zahl = []
# for k in range(1,11):
#     if k%2 != 0:
#         quad_zahl.append(k**2)
#     else:
#         quad_zahl.append(k)
# =============================================================================
        
quad_zahl = [k**2 if k%2 != 0 else k for k in range(1,11)]

print(quad_zahl)