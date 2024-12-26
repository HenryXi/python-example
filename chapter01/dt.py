import json
import time
import requests

def post(db):
    print('db:'+db)
    url = 'https://api-datum.dt.mi.com/platform/resource/mysql/table/import'
    headers = {
        'X-DP-Workspace':'14809',
        'Content-Type': 'application/json',
        'Cookie':'Hm_lvt_c3e3e8b3ea48955284516b186acf0f4e=1716289368; Hm_lpvt_c3e3e8b3ea48955284516b186acf0f4e=1716289368; _utm_data={"mtm":"","device_id":""}; deviceId=xmdevice_p2vm1cops51zfm9g; mishopDeviceId=Bg0BePDzVneUW+STg4615YOOvDN8X3tfSk184SK3K/jskOIPHqnrtegmk1zFXDf8JaQksQm+u7cXiDWFJ16PdKA==; iplocale=zh_CN; userId=127039988; i.mi.com_istrudev=true; _aegis_cas_p=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3MjI4MjMyMTgsImRlcGlkIjoiK1x1MDAxYkxpMVx1MDAwMXtjbV9cXFx1MDAxYSFcdTAwMTVUXG5cdTAwMDAiLCJhdWQiOiJkdC5taS5jb20iLCJjIjowLCJkZXRhaWwiOiJlt6FaujcrkNGygfdmWz17XHUwMDA2XHUwMDExyXmp0c10LIHaZ1o-lNPRj5tcdTAwN2ZcdTAwMTWz9Fx1MDAwYlwidEguXC8zTNS3V0osXHUwMDA2NdTPqmvBRFbXnCGTYGOLXHUwMDAx76dcdTAwMDWGltHyuiixpmT1tJqGeD9cL1wiPrLhzjnhYruo3b1JhsDAmMmsoFx1MDAxMm8yglXtXHUwMDBloXSZwzZlXHUwMDE5qCyJ11x1MDAxYVx1MDAwNbXMkOTnb69DXHUwMDdmXWKfO_3rn603XHUwMDA3wNSt8XKbIfuCJ6-4XHUwMDFl52F5MjpFh4aMxdD3fKruc504sTAwXHUwMDEyQfiYl63PXFxTqNwjU3FcdTAwMGZj1rE5XHUwMDFjxVx1MDA3ZoVaeXbk_4CgsXGK89dIefZcdTAwMDMsuOa5fkpNO3UhJjsjtnxN5lx1MDAxONFccnuTO6hecDbEldy3lqLliJxcdTAwMDAghumtXHUwMDAy8tRlOVjOxfBkg2L_vzZC81XwIVxuXHUwMDA2XHUwMDE4VLMykSOQZnWSMHyxh2Uks7clwjexOrpl2slcdTAwMTW2O8dVXHUwMDFibYwkuqaYha2sOjxHZ7N9m5HkTlx1MDAwNK5cdTAwMTdcdTAwMTfi2Mc_lVx1MDAxYVx1MDAxOWzFXlx1MDAwMV5qjVx1MDAxOdNmdnBcdTAwMTg6MVx1MDAxMFxmupnEuYyZ7oCUXHUwMDAz2N-oXHUwMDFjhlxc7dD6Q1xyY6uarGzGui6fuiTUg691a22rVXLg03F1zFWrmsJESrVPnSvRsULIXC-lfFx0SlWcxlxcfYvacL2QyOjM5UEn_t6Ablx1MDAxNb7pPlx1MDAxN3N1I7TGO755c1j2e1xcYlx1MDAwZVxmWOJUZVx1MDA3Zlx1MDAwM_tcYnquR_tOXHUwMDFk6W96VDzqtoBcdTAwMTWkZuNYLtxiJGo8xo-_z4C_tz_H25lcIk5vcX1LXHUwMDA1pktg3PaLioWDcO1cdMhTrLfqiLjqqVx1MDAwZlx1MDAwNc7g705Ha2BtXHUwMDAzl9zYLHvEe5hcdTAwMDKkX8hcIjo4o9JfuvGdXHUwMDE1Z4_2pVx1MDAxNcXmQ3ZcbtZljUq530HPQlx1MDAwNCqTXHUwMDE5j7WlWNpcdTAwMWZ5aJSzWqrd-MBcdTAwMDNcZo5cdTAwMTBcdTAwMWLUXHUwMDFhIVJfSvLiXHUwMDE0gPKKXHUwMDAy_ug5roNKXHUwMDAxaq2O4YYxTthcdTAwMTT7JpnDLELUXHUwMDE4bTX4W-dAx3V3XrJ2e45cdTAwMDDv7Vx1MDAwMt589lrSYoGdMuP8XHUwMDEzqjqXc-pcdTAwMThcdTAwMDLjpdhMxFx0qohcdTAwMWFLY049Iiwic3ViIjoieGl4aWFveW9uZyIsInQiOiJmYWxzZSIsInV0IjoiXHUwMDAzP1x1MDAwNk1cdEJWUSIsImV4cCI6MTcyMzA4NjAxOCwiZCI6IjYyYjQzMWFiZTQyOWQ2MGE1ZjM1NGI5M2RjM2EzN2EwIiwiaXNzIjoiTUktSU5GT1NFQyIsImwiOiIlXHUwMDFhOFx1MDAxMVZcbiIsInR5cCI6ImNhcyJ9.aVxLRerYEXO-2FO0xYUY9Wy4beBY59dh3fAJEoQo_zM0MrDRAQQ45-1AhD7PXEBnJujBM253x8FJyOAtW4QNDA; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjM2MTg2NjIsImlhdCI6MTcyMzAxMzg2MiwidXNlciI6InhpeGlhb3lvbmcifQ.1aCcB_riC-WZ9-hf5RuCdwS4I9qG6OV7xRxp0SIJNY8'
    }
    json_data = genTableNameJson(db)
    # print(json_data)
    response = requests.post(url, data=json_data, headers=headers)
    print(response.text)


def genTableNameJson(db):
    mysqlImportDTOList = []
    for i in range(1,401):
        table_info={
            "table":"table"+str(i),
            "database":"device",
            "catalog": db
        }
        mysqlImportDTOList.append(table_info)

    data={
        "catalog": db,
        "permissions": "ro",
        "mysqlImportDTOList":mysqlImportDTOList
    }
    return json.dumps(data)
    


def main():
    for i in range(1,5):
        post('mysql_14809_device'+str(i))


if __name__ == "__main__":
    main()