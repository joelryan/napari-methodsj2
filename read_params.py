

from tkinter import dialog


dialog_dic={"Image dimensions":[],"Objective":[]}

def get_item_info(blurb_title,settings):
    for i in range(0, len(settings)):
        if settings[i].get("Dialog_Box") == blurb_title:
            dialog_dic[blurb_title].append(settings[i])
    return dialog_dic



def get_blurb_info(blurb_title,settings):
    setting_list=[]
    dialog_dic=get_item_info(blurb_title,settings)
    for setting_box in dialog_dic[blurb_title]:
        if setting_box.get("Dialog_Type")== "addChoice":
            setting_list.append(setting_box["attributes"])
        else:
            setting_list.append(setting_box['Setting'])
    return setting_list
