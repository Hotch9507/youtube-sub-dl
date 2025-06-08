from datetime import datetime, timedelta

# 你的 Cookie 字符串（从文件复制）
raw_cookie = """
VISITOR_INFO1_LIVE=Cw8vsSc8vIA; VISITOR_PRIVACY_METADATA=CgJISxIEGgAgZg%3D%3D; LOGIN_INFO=AFmmF2swRQIhAL2WpQ1WX1fSaSZOPgMsR3GlxIxsUlmAbKhk4eeHuBz7AiAhI4OnGvheZ9W1A80WgwBDPw92F7IYki1KtB4bq_FVYg:QUQ3MjNmeV9pVERLU3JYLV9UbXozc01tQUxybVNOQ0N0REw3bzI5d05ZQUh0MHJSU1N0dTgzV2xJLWRxS2YxZHJoUnJxaWZkcG9YSk95UHRSZmV2b0FjZnU1MU5Bd2xicm0zRndZNGZlaU1ZdlZlQ3dkVU0tcThpeGFKMDUzVDhVNmxiYnZ2dHVqOWk2ZS1iTmxja2M0UmVVV3cwSTVpc3pR; PREF=tz=Asia.Shanghai&f7=150&f3=18&f5=30000; SID=g.a000xggUaP-Bx2bs-SZnJz2V_mkO76p9fJT_FWxmczRVpLkDn00n54RJ66Ur2VIeY5RLph6CugACgYKAfISARISFQHGX2MiryNDIrGmM0-PXiMxrOFr_RoVAUF8yKqX63hkGYK6_ZmKKNFsOqGt0076; __Secure-1PSID=g.a000xggUaP-Bx2bs-SZnJz2V_mkO76p9fJT_FWxmczRVpLkDn00n7SWOYlQKxOSA3aUiWspYoQACgYKAa8SARISFQHGX2Mi9jX2wFowLgzIvWy9ZQUCVhoVAUF8yKorDv7cFuJJUOJwqC39geJQ0076; __Secure-3PSID=g.a000xggUaP-Bx2bs-SZnJz2V_mkO76p9fJT_FWxmczRVpLkDn00ntp03OOBWjxhvJZYMV9gVcgACgYKAR4SARISFQHGX2MiD33h4gC6LxzjRjlLDWva6xoVAUF8yKqPsCJdi7NPJ8r36mInDC1-0076; HSID=ACLv3Sdt-JCUB0MrT; SSID=A2ndIoOwUt5ECUzbJ; APISID=faencS2hSAd5_kfd/AL4Qq2uTMky5j-dfR; SAPISID=UkrpzYsPTXRKuB3A/AOQYh2B5FfJEyyYI9; __Secure-1PAPISID=UkrpzYsPTXRKuB3A/AOQYh2B5FfJEyyYI9; __Secure-3PAPISID=UkrpzYsPTXRKuB3A/AOQYh2B5FfJEyyYI9; YSC=YQ-LG-G_jxs; __Secure-ROLLOUT_TOKEN=CM_R6fzcjJ_NmwEQl53utIKxigMY-fOI1drgjQM%3D; __Secure-1PSIDTS=sidts-CjEB5H03PyJbyGptwERSlLkI5XE4nGtISYFtHOnH5FPd-jwqrJjsPHTLTkfap9fVn8StEAA; __Secure-3PSIDTS=sidts-CjEB5H03PyJbyGptwERSlLkI5XE4nGtISYFtHOnH5FPd-jwqrJjsPHTLTkfap9fVn8StEAA; CONSISTENCY=AKreu9sWNUGsNzG3Gie3CIcg0zig5jj-SimOonE8WouO1A6v0HN22VwKSstwL_9BhQGk9WAhIAaqESzAAxN1Y8WSYNQbP5ZY_j_7W9pjGiPVaizkWl1I_gxL_D4V0gQOk-Y59cUlxzy3KJfSMkpkY5LZ; ST-tladcw=session_logininfo=AFmmF2swRQIgUuCWOxSKjLkAt-M7AKJEZnCw-76_vDcUEUMCJXrnyUECIQCMeIK6XbjJRmb-4Mzk7OHdGHNVeRQ0GdVbSosO9td3aA%3AQUQ3MjNmeXJWaEY3TjN5YkVEVVJoenlod3NnVktYV1NpclRWZkxFc3BTbWZidGdQS3dFeEh0RTlxMDl0cG1uN2VLSFR4ZGUyclRIY1FyNE9pUGdIQ0hfa2F4c2V4T0NTVEZMSV9JRWFHby1hdnA1ak9iTERiYXFOUDVicmc1NWVONDdmQkM2dlBLd1BYb0NxVGo4eS13ZW1rcFZjakktbENR; ST-xuwub9=session_logininfo=AFmmF2swRQIgUuCWOxSKjLkAt-M7AKJEZnCw-76_vDcUEUMCJXrnyUECIQCMeIK6XbjJRmb-4Mzk7OHdGHNVeRQ0GdVbSosO9td3aA%3AQUQ3MjNmeXJWaEY3TjN5YkVEVVJoenlod3NnVktYV1NpclRWZkxFc3BTbWZidGdQS3dFeEh0RTlxMDl0cG1uN2VLSFR4ZGUyclRIY1FyNE9pUGdIQ0hfa2F4c2V4T0NTVEZMSV9JRWFHby1hdnA1ak9iTERiYXFOUDVicmc1NWVONDdmQkM2dlBLd1BYb0NxVGo4eS13ZW1rcFZjakktbENR; SIDCC=AKEyXzWdhxaB-Vykja3TfiPC2TfrBniHGgJH6Fpc7qh1IKU1I6iofptxX6ExEEFUE_Egrqlqn6I; __Secure-1PSIDCC=AKEyXzWJl68pza9uhIPtZugInVkItIOyZmSbLUzg3TiMPJe9ZvTAb1A2Y2G2C61NcSkCDpzEMdM; __Secure-3PSIDCC=AKEyXzXx_7xrAQ3Bi2JkHHjVEYwk9a_W2VX7uurvKI0DbJjniyA8wVBOBRmiMOMZ5aOIOiKn6Q
""".strip()

# 你要下载的站点域名
domain = ".youtube.com"
path = "/"
secure = "FALSE"
expires = int((datetime.now() + timedelta(days=180)).timestamp())

# 输出文件名
output_file = "cookies/cookies.txt"

# 构建 cookies.txt 格式内容
lines = ["# Netscape HTTP Cookie File"]
for pair in raw_cookie.split(";"):
    if "=" not in pair:
        continue
    name, value = pair.strip().split("=", 1)
    # 忽略空值
    if not value:
        continue
    line = f"{domain}\tTRUE\t{path}\t{secure}\t{expires}\t{name}\t{value}"
    lines.append(line)

# 写入文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"✅ 已生成 cookies.txt 文件，可用于 yt-dlp")
