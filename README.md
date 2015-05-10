GMachine
===

序
---

簡單說就是我需要一個比較簡單的方式操作 docker machine, 目前是把docker machine 當做 tls ca & ssh key 的產生器, 
預計修改driver 讓 gmachine 直接支援原生 api


擴充docker machine

1. 支援 指定 machine 上傳, 下載 檔案
2. 支援 指定 machine fabric 命令
3. 擴充 python interface, 讓 python 也可以直接操錯 docker machine
4. 擴充 python interface 取淂 machine 的 docker client ( 使用 docker.io & https )



