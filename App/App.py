#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import wcferry as sdk


def main():
    print(dir(sdk))                     # 查看SDK支持的方法和属性
    help(sdk.WxSetTextMsgCb)            # 查看某方法的情况
    help(sdk.WxMessage)                 # 查看消息结构
    WxMsgTypes = sdk.WxGetMsgTypes()    # 获取消息类型
    print(WxMsgTypes)                   # 查看消息类型

    # 初始化SDK，如果成功，返回0；否则失败
    status = sdk.WxInitSDK()
    if status != 0:
        print("初始化失败")
        exit(-1)

    print("初始化成功")

    time.sleep(2)
    print("发送文本消息......")
    sdk.WxSendTextMsg("filehelper", "", "message from WeChatFerry...")

    time.sleep(2)
    print("发送图片消息......")
    sdk.WxSendImageMsg("filehelper", "test.jpg")

    # 接收消息。先定义消息处理回调
    def OnTextMsg(msg: sdk.WxMessage):
        if msg.self == 1:  # 忽略自己发的消息
            return 0

        s = ""
        msgType = WxMsgTypes.get(msg.type, '未知消息类型')
        if msg.source == 0:
            s += f"收到来自好友[{msg.wxId}]的{msgType}消息："
        else:
            s += f"收到来自群[{msg.roomId}]的[{msg.wxId}]的{msgType}消息："

        s += f"\r\n{msg.content}"
        if msg.type != 0x01:
            s += f"\r\n{msg.xml}"

        print(f"\n{s}")

        return 0

    print("Message: 接收通知中......")
    sdk.WxSetTextMsgCb(OnTextMsg)  # 设置回调，接收消息
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
