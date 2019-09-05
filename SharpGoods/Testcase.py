# *- coding:utf8 *-
import urllib2
import json
HTTP_HOST = "h878.cn"
HTTP_SERVER = "https"
HTTP_HEADER = {'Content-Type': 'application/json'}
ERROR_CODE = 0
title = "======={0}======="
def test_user_login():
    try:
        api_login = "/sharp/goods/users/login"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"UStelphone\":\"17706441101\",\n\t\"USpassword\":\"123\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_user_register():
    try:
        api_login = "/sharp/goods/users/register"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"UStelphone\":\"17806441101\",\n\t\"USpassword\":\"123\",\n\t\"UScode\":\"661824\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status_code" not in jsonResult:
            return False
        status = jsonResult["status_code"]
        if status != 405102:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_user_update_pwd():
    try:
        api_login = "/sharp/goods/users/update_pwd?token=123"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"USpasswordold\":\"123\",\n\t\"USpasswordnew\":\"123\",\n\t\"UStelphone\":\"17706441101\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_user_update_personal():
    try:
        api_login = "/sharp/goods/users/update_info?token=123"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"USsex\":\"男\",\n\t\"USname\":\"昵称\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_user_get_personal():
    try:
        api_login = "/sharp/goods/users/all_info?token=123"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        req = urllib2.Request(url_login)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_product_get_all():
    try:
        api_login = "/sharp/goods/product/get_all"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        req = urllib2.Request(url_login)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_product_get_abo():
    try:
        prid = "040a78f0-2c50-402e-969c-d26072659ae3"
        api_login = "/sharp/goods/product/get_info_by_id?PRid={0}".format(prid)
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        req = urllib2.Request(url_login)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_product_get_other_brand():
    try:
        prid = "040a78f0-2c50-402e-969c-d26072659ae3"
        api_login = "/sharp/goods/product/get_control_brand?token=123&PRid={0}".format(prid)
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"BRcolor\":\"玫瑰金\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

def test_product_get_pbid():
    try:
        prid = "040a78f0-2c50-402e-969c-d26072659ae3"
        api_login = "/sharp/goods/product/get_pbid_by_all_brand?token=123&PRid={0}".format(prid)
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"BRno\":\"进阶版\",\n\t\"BRcolor\":\"玫瑰金\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

if __name__ == '__main__':
    if not test_user_login():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_user_register():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_user_update_pwd():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_user_update_personal():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_user_get_personal():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_product_get_all():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_product_get_abo():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
    if not test_product_get_other_brand():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)

