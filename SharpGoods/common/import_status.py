# *- coding:utf8 *-


def import_status(msg_key, sta_key, code_key=None):
    from SharpGoods.config import messages, status, status_code
    if code_key:
        msg, sta, code = eval("messages.{0}, status.{1}, status_code.{2}".format(msg_key, sta_key, code_key))
        return {"message": msg, "status": sta, "status_code": code}
    else:
        msg, sta = eval("messages.{0}, status.{1}".format(msg_key, sta_key))
        return {"message": msg, "status": sta}


if __name__ == "__main__":
    print import_status("ERROR_MESSAGE_WRONG_TELCODE", "SHARPGOODS_ERROR", "ERROR_WRONG_TELCODE")
