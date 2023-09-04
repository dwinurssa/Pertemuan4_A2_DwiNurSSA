N = str(input())

if N == ("[] ()"):
    print("Pemain A menang")
elif N == ("() []"):
    print("Pemain B menang")
elif N == ("[] 8<"):
    print("Pemain B menang")
elif N == ("8< []"):
    print("Pemain A menang")
elif N == ("() 8<"):
    print("Pemain A menang")
elif N == ("8< ()"):
    print("Pemain B menang")
elif N == ("8< 8<"):
    print("Draw")
elif N == ("[] []"):
    print("Draw")
elif N == ("() ()"):
    print("Draw")
else :
    print("Input tidak terdaftar")