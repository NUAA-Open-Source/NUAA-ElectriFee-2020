# -*- coding: UTF-8 -*-

from sensitive_data import card_url
import requests
import re

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
    
    elec_data = eval(return_data)

    if elec_data['query_elec_roominfo']['retcode'] != "0":
        print("[+] Error! {}".format(elec_data['query_elec_roominfo']['errmsg']))

    elec_num = re.search(pattern=r'\d+.\d+|\d+', string=elec_data['query_elec_roominfo']['errmsg'])
    return elec_num.group()
