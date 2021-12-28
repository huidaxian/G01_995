from re import A
from flask import Flask, jsonify
from flask_cors import CORS
from flask_cors import cross_origin
from flask import request
from db import AccessData
import pymysql
from pymysql.cursors import Cursor
# 创建一个WSGI对象，并指定名字，一般使用文件名。__name__
app = Flask("myweb")
CORS(app, supports_credentials=True)

# route()方法用于设定路由；类似spring路由配置
@app.route('/data/carPurpose.json',methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service():
    access = AccessData()
    carinf=request.form.to_dict()
    print(carinf)
    res = access.queryPurpose(carinf["cid"])

    data = {}
    data["purposes"]={
        "type": "pie",
        "title": {
            "text": "购车目的饼状图"
        },
        "legend": {
            "position": "middle"
        },
        "bgColor": "#00000000",
        "labels": [
            "购物",
            "自驾游",
            "通勤",
            "长途",
            "越野",
            "接送孩子",
            "约会"
        ],
        "datasets": [
            {
                "data": [23,56,18,45,89,26,67]
            }
        ]
    }
    if res:
      data["purposes"]["datasets"][0]["data"].clear()
      for i in res[0] :
        data["purposes"]["datasets"][0]["data"].append(i)
      del(data["purposes"]["datasets"][0]["data"][0])
    return jsonify(data)

@app.route('/data/options.json', methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service2():
    
    access = AccessData()
    user_info = request.form.to_dict()
    print(user_info)
    data = {}
    car=access.queryCar()
    data["cars"]=[]
    for carinf in car:
      data["cars"].append(
        {
          "value":carinf[0],
          "label":carinf[1]
        }
      )
      
    return jsonify(data)


@app.route('/data/users.json',methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service3():
    user_info = request.form.to_dict()
    print(user_info)
    data = {}
    access = AccessData()
    res=access.queryUserByName(user_info["username"])
    if res:
      data["password"]=res[0][3]
      data["status"]=res[0][4]
    return jsonify(data)


@app.route('/data/update.json',methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service10():
  access=AccessData()
  info = request.form.to_dict()
  access.updateUserByName(info["username"],info["password"])
  data={}
  return jsonify(data)


@app.route('/data/fuelAnalysis.json',methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service4():
    
    access = AccessData()
    car = request.form.to_dict()
    fuel1=access.queryCarByID(car["car1"])
    fuel2=access.queryCarByID(car["car2"])
    print(car)
    data = {}
    data["fuel"]={
        "type": "ring",
        "title": {
          "text": "油耗对比表"
        },
        "showValue": "true",
        "legend": {
          "position": "bottom",
          "bottom": 40
        },
        "bgColor": "#00000000",
        "labels": ["本车", "react"],
        "datasets": [
          {
            "data": [500, 500]
          }
        ]
      }
    if fuel1 and fuel2:
      data["fuel"]["labels"]=[fuel1[0][1],fuel2[0][1]]
      data["fuel"]["datasets"][0]={
        "data":[fuel1[0][4],fuel2[0][4]]
      }
    return jsonify(data)
    
@app.route('/data/hotSalesArea.json',methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service5():
    user_info = request.form.to_dict()
    print(user_info)
    data = {}
    data["salesAreaBarChart"]={
        "type": "bar",
        "title": {
          "text": "热点地区销售图"
        },
        "bgColor": "#00000000",
        "labels": ["北京", "天津", "上海", "重庆", "广州", "江苏", "香港"],
        "datasets": [
          {
            "data": [334, 278, 190, 235, 260, 200, 141]
          }
        ]
    }
    data["salesAreaPieChart"]={
        "type": "pie",
        "title": {
          "text": "销售地区占比饼状图"
        },
        "legend": {
          "position": "left"
        },
        "bgColor": "#00000000",
        "labels": ["北京", "天津", "上海", "重庆", "广州", "江苏", "香港"],
        "datasets": [
          {
            "data": [334, 278, 190, 235, 260, 200, 141]
          }
        ]
      }
    return jsonify(data)
@app.route('/data/priceComparison.json', methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service6():
    carinf = request.form.to_dict()
    print(carinf)
    
    access = AccessData()
    price1=access.queryCarByID(int(carinf["car1"]))[0][3].split("-")[0].split("万")[0].strip()
    price2=access.queryCarByID(int(carinf["car2"]))[0][3].split("-")[0].split("万")[0].strip()
    #price=carinf[2]
    #print(price)
    print(price1)
    print(price2)
    data = {}
    data["prices"]={
        "type": "ring",
        "title": {
          "text": "价格对比"
        },
        "showValue": "true",
        "legend": {
          "position": "bottom",
          "bottom": 40
        },
        "bgColor": "#00000000",
        "labels": ["车型一", "车型二"],
        "datasets": [
          {
            "data": [float(price1), float(price2)]
          }
        ]
      }
    return jsonify(data)
@app.route('/data/salesComparison.json', methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service7():
    info = request.form.to_dict()
    print(info)
    data = {}
    sale=[
      [334, 278, 190, 235, 260, 200, 141, 342, 234, 546, 657, 123],
      [174, 245, 567, 123, 455, 234, 64, 386, 230, 179, 365, 626],
      [324, 457, 723, 542, 82, 79, 313, 323, 437, 531, 235, 678],
      [124, 468, 120, 236, 241, 316, 531, 224, 153, 212, 341, 256]
    ]
    data["salesPieChart"]={
        "type": "pie",
        "title": {
          "text": "不同种车类销售占比图"
        },
        "legend": {
          "position": "left"
        },
        "bgColor": "#00000000",
        "labels": ["SUV", "轿车", "跑车", "MPV"],
        "datasets": [
          {
            "data": [334, 278, 190, 235]
          }
        ]
    }
    data["salesLineChart"]= {
        "type": "line",
          "title": {
            "text": "XX类车月销售趋势图"
          },
          "bgColor": "#00000000",
          "labels": [
            "1月",
            "2月",
            "3月",
            "4月",
            "5月",
            "6月",
            "7月",
            "8月",
            "9月",
            "10月",
            "11月",
            "12月"
          ],
          "datasets": [
            {
              "label":"aodi",
              "data": [334, 278, 190, 235, 260, 200, 141, 342, 234, 546, 657, 123]
            }
          ]
    }
    data["cars"]=[
      {
        "value":1,
        "label":"显示"
      },
      {
        "value":0,
        "label":"不显示"
      }
      

    ]
    num=data["salesLineChart"]["datasets"]=[]
    if 'car1' in info.keys():
      if int(info["car1"]):
        num.append({
          "label":"SUV",
          "data":sale[0]
        })
      if int(info["car2"]):
        num.append({
          "label":"轿车",
          "data":sale[1]
        })
      if int(info["car3"]):
        num.append({
          "label":"跑车",
          "data":sale[2]
        })
      if int(info["car4"]):
        num.append({
          "label":"MPV",
          "data":sale[3]
        })
    return jsonify(data)



@app.route('/data/salesTrend.json', methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service8():
    user_info = request.form.to_dict()
    access = AccessData()
    res=access.querySale_year(user_info["cid"])
    car=access.queryCarByID(user_info["cid"])
    print(user_info)
    data = {} 
    data["salesTrendChart"]={
        "type": "bar",
        "title": {
          "text": "xxxx车型近五年销量趋势图"
        },
        "bgColor": "#00000000",
        "labels": ["2017", "2018", "2019", "2020", "2021（半年）"],
        "datasets": [
          {
            "label": "xxxx车型",
            "data": [134, 178, 185, 210, 180]
          }
        ]
      }
    if res:
      data["salesTrendChart"]["datasets"][0]["data"]=[res[0][0],res[0][1],res[0][2],res[0][3],res[0][4]]
      data["salesTrendChart"]["title"]["text"]="“"+car[0][1]+"”"+"近五年销量趋势图"
      data["salesTrendChart"]["datasets"][0]["label"]=car[0][1]


    return jsonify(data) 
@app.route('/data/scoreAnalysis.json', methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service9():
    info = request.form.to_dict()
    print(info)
    access = AccessData()
    res=access.queryCarByID(info["cid"])
    
    data = {}
    data["scores"]=[
        3.7,
        3.5,
        3.0,
        2.5,
        3.5,
        2.7,
        4.0
    ]
    if res:
       data["scores"]=[res[0][5],res[0][6],res[0][7],res[0][4],res[0][8],res[0][9],res[0][10]]

    return jsonify(data)
@app.route('/data/admin.json', methods=["get", "post"])
@cross_origin(supports_credentials=True)
def method_service11():
    info = request.form.to_dict()
    print(info)
    access = AccessData()
    res=access.queryUser()
    data={}
    data["data"]=[]
    for i, j in enumerate(res):
      if(j[4]=="normal"):
        data["data"].append(
          {
            "no": str(i),
            "company": j[1],
            "username": j[2],
            "password": j[3],
            "valid": True,
          }
        )
      else:
        data["data"].append(
          {
            "no": str(i+1),
            "company": j[1],
            "username": j[2],
            "password": j[3],
            "valid": False,
          }
        )
    return jsonify(data)


if __name__ == '__main__':
        app.run(port=9898)
