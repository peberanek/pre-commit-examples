"""Example source code to demonstrate pre-commit hooks."""

from string import digits
import sys
from string import ascii_letters

# """
# -----BEGIN RSA PRIVATE KEY-----  # gitleaks:allow
# MIICXQIBAAKBgQCNONE9CpPmxWddL+nS2pthNdaQDSjeWVFkZxDbNi7VcskIAdk6
# jn3JCM2pf+GNAhE43BZ3x/IGvp8LbbnXB7mltZU/IeyqCVLRvv6GLxXVdQjmuyhk
# XS0EQVMulsJaLUW0ncLZqX+XOHASJRLObpLoyB/h3Ge/nuIfT54zHonc7wIDAQAB
# AoGAKFJIq70RbZp/YMQFZwazxpWwpYCcYp/t9VTYIz7dMGSNsZOVinqUv4mb7wFs
# TO6CLFHquFiGahaTIpg5r4OtJYp23E1K9Qn5i3Vjn0Rcm6tk+Dmyry6lE9Vk4WGC
# 6RgD98V0C1whYidoSiAdC7Bnt6IEQ7hOmTKo54+yXN+cnEECQQD6Rwkl+UmrBMTW
# zKJRDXntdgyvsX1Nv9LCXcZ87br5YBOXIpmeABJ+iWBFcKmyr5MoPml74KrG19OR
# e8EFK9pdAkEAkHNws4GEo0bcp6IC12moJLugYjehGsA7F/U0WpC6alVE9dQCGD0b
# UQQdkLt7x8V0WxgBrB/12k9T1Wu2sj8XuwJBAINwHvvUab3o6T8thOkwPKJa5tq2
# Seo1HYh6Gy2s5A7nSCKNR0PVIeFWYDrXqidvUcdGz7sBCG8ZFcFHztzaZPkCQHRF
# d6IFzs3ebB5CuibKVR28KQzl2je+I9LU/J8pf+O3XxrA3C7GgQZlWab2Qlw7A72P
# RUlXMH3Y/JH9ccFoJ6ECQQCgrjx1BsNoLYIpHcs0jz6M9M2ityLf8qg0VLOktizC
# kqUJTY6eMTbJMLh+KkbicLB5n12ds2swJrDCCWPfZ2BI
# -----END RSA PRIVATE KEY-----
# """

def main():
    print(
        ascii_letters + digits
    )

if __name__ == "__main__":
    main()
