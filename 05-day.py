# 5- kun: List (Royxat) va Dict)

# 1. List - Royxat (tartiblangan, bir nechta narsa)

print("--- List (Royxat)---")
ismlar = ["Amin", "Ali", "Vali", "Guli"]

print(ismlar)       # Butun royxatni chiqaradi
print(ismlar[0])   # Birinchi element (Amin)
print(ismlar[-1])   # Oxirgi element (Guli)
print(len(ismlar))  # Nechta element borligi (4)

# 2. Dict - Lugat (kalit: qiymat juftligi)

print("--- Dict (Lugat) ---")
talaba = {
    "ism": "Amin",
    "yosh": 25,
    "shahar": "Toshkent"
}    

print(talaba)           # Butun lugatni chiqaradi
print(talaba["ism"])    # "Ism" kalitidagi qiymat (Amin)
print(talaba["yosh"])   # "yosh" kalitidagi qiymat (25)
