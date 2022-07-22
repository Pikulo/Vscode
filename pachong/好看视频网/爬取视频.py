# -*- encoding=utf-8 -*-
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/7/28  17:06

import json
import requests
import urllib.request,urllib.error  #制定URL，获取网页数据
# 数据抓取
base_url = 'https://haokan.baidu.com/web/video/feed?tab=yunying_vlog&act=pcFeed&pd=pc&num=20&shuaxin_id=1627468867238' #开发者模式修改

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'referer': 'https://haokan.baidu.com/tab/yingshi_new',
    'cookie': 'BIDUPSID=E6E33034140D097458A17C9329AFFE53; PSTM=1595849750; BDUSS=J4SHN5LTlFcjNVYk9VaUVkQldYSDhITn5WN2c0aWd1ZDRsejhoYTJnWmhER3hnRVFBQUFBJCQAAAAAAAAAAAEAAACqhUNebG15b3VkbwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGF~RGBhf0RgUH; BDUSS_BFESS=J4SHN5LTlFcjNVYk9VaUVkQldYSDhITn5WN2c0aWd1ZDRsejhoYTJnWmhER3hnRVFBQUFBJCQAAAAAAAAAAAEAAACqhUNebG15b3VkbwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGF~RGBhf0RgUH; MCITY=-%3A; __yjs_duid=1_6c69158c19a5ca6cb2231a93b1e765541620397512732; BAIDUID_BFESS=183FC4B781E8678DF0E386505DADCBBE:FG=1; H_PS_PSSID=34303_33764_34279_34004_34093_34106_34094_26350_34241; delPer=0; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=11641593850693087963; BDSFRCVID=WU_OJexroG0YKNnH0jSPM3RvN3qMFyTTDYLEJs2qYShnrsPVJeC6EG0PtoWQkz--EHtdogKKXgOTHwuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJAjoCP5tDt3fP36q6_ahtFhqxby26nkaNO9aJ5nJD_bOxjT5x6q-Ttg-U7iKhvA5jnT_Jb-QpP-HJAC0678Wt4Ljp38aUR0BDrpKl0MLUOWbb0xynoDXMtj3xnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFleP7HhPP_hmTa54cbb4o2WbCQQM5r8pcN2b5oQT84yPTXBTOBLaRuoMoKBDOa8qQw3hOUWfAkyl-Hblcg2IoHQMJCWJ5TMl5jDh3Mhp-uMpCLexQ7bIny0hvcyn3cShn65fjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f6LDtJCt3D; BCLID_BFESS=11641593850693087963; BDSFRCVID_BFESS=WU_OJexroG0YKNnH0jSPM3RvN3qMFyTTDYLEJs2qYShnrsPVJeC6EG0PtoWQkz--EHtdogKKXgOTHwuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJAjoCP5tDt3fP36q6_ahtFhqxby26nkaNO9aJ5nJD_bOxjT5x6q-Ttg-U7iKhvA5jnT_Jb-QpP-HJAC0678Wt4Ljp38aUR0BDrpKl0MLUOWbb0xynoDXMtj3xnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFleP7HhPP_hmTa54cbb4o2WbCQQM5r8pcN2b5oQT84yPTXBTOBLaRuoMoKBDOa8qQw3hOUWfAkyl-Hblcg2IoHQMJCWJ5TMl5jDh3Mhp-uMpCLexQ7bIny0hvcyn3cShn65fjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f6LDtJCt3D; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1627463746,1627464043,1627464057,1627464061; PC_TAB_LOG=video_details_page; COMMON_LID=cdc7d82a85cca3864b8096c341b93bff; BAIDUID=435E631FCAFF7743DA7E9D3915CEB22B:FG=1; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1627468589; ab_sr=1.0.1_NTA3NGJjZTc2YWM5MjU0ODg4YWYxMTJkN2Q3MmMxYjc1M2QxNDA4NTY4NjU2NzU1YjBkZGVkZjM0MTZmOWVmZTc2YmEyYWUzOTE0MTI3NmI1OWQwZmVkNjJkNmU4ZjViYmE5YjZiMzczNGRmMGMwN2M5NGM5ZTI4MTk0N2U5MWMyN2VlYThlMmYxNzg4NjFhNzVkNDM5NjQyYzRlMzlhMA==; reptileData=%7B%22data%22%3A%22ccce3870144a556bde6604975a39f051a79eb43523b2d2056b11115036c69bfcbca746afeeeae6ec09aec75e034cdf28742367dca276d915abd13679ffb8940bf121c7b139c89fe71b3758b8d784ab14ca6874590411ced15f6aa4f70ed3aad560282a0bb3885b2c16e8db7d37fa9303757cd2fbf279d238ab11c108ee5befb6%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%221a69c9dc%22%7D'
}
response = requests.get(base_url,headers=headers) # 第一次请求

# request=urllib.request.Request(base_url,headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
# # print(response.status_code) # 200说明能访问
data = response.text
# print(data)

# 数据解析，json loads转换为python格式
json_data = json.loads(data)
print(json_data)
json_list = json_data['data']['response']['videos']
# print(json_list)
'''
for data in json_list:
    video_title = data['title']+'.mp4'
    video_url = data['play_url']
    print(video_title,video_url)

    print('正在下载')
    # 第二次请求
    video_data = requests.get(video_url,headers=headers).content # 二进制
    with open(r'./视频/'+video_title,'wb') as f:
        f.write(video_data)
        print('下载完成\n')
    break
'''





