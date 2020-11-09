"""

link: https://leetcode-cn.com/problems/validate-ip-address

problem: 检查字符是否为IPv4或者IPv6格式

solution: 模拟

"""
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def check_v4(k: str) -> bool:
            if k == "":
                return False
            t = 0
            for c in k:
                if c not in "0123456789":
                    return False
                t = t * 10 + int(c)
            if t > 255 or k[0] == '0' and len(k) != 1:
                return False
            return True

        def check_ipv4() -> bool:
            l = IP.split(".")
            if len(l) != 4:
                return False
            return all([check_v4(k) for k in l])

        def check_v6(k: str) -> bool:
            if k == "" or len(k) > 4:
                return False
            for c in k:
                if c not in "0123456789abcdefABCDEF":
                    return False
            return True

        def check_ipv6() -> bool:
            l = IP.split(":")
            if len(l) != 8:
                return False
            return all([check_v6(k) for k in l])

        if check_ipv4():
            return "IPv4"
        elif check_ipv6():
            return "IPv6"
        return "Neither"
