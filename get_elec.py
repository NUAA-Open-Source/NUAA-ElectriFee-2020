# -*- coding: UTF-8 -*-

from sensitive_data import card_url
import requests
import re
import ast


def get_elec(aid, account, roomid, room, area, areaname, buildingid, building):
    """
    Get Electricity bill
    """
    form_data = 'jsondata={{+"query_elec_roominfo":+{{+"aid":"{}",+"account":+"{}","room":+{{+"roomid":+"{}",+"room":+"{}"+}},++"floor":+{{+"floorid":+"",+"floor":+""+}},+"area":+{{+"area":+"{}",+"areaname":+"{}"+}},+"building":+{{+"buildingid":+"{}",+"building":+"{}"+}}+}}+}}&funname=synjones.onecard.query.elec.roominfo&json=true'.format(
        aid, account, roomid, room, area, areaname, buildingid, building)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    return_data = requests.post(
        card_url, data=form_data.encode('utf-8'), headers=headers).text

    if return_data == "系统异常!":
        print("[+] Error! {}".format("系统异常!"))
        exit(0)

    elec_dict = ast.literal_eval(return_data)

    elec_msg = elec_dict["query_elec_roominfo"]["errmsg"]

    return elec_msg
