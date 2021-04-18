# DataV GeoJSON 格式数据

提供国家级/省级/市级/区级行政区 GeoJSON 格式数据

本项目使用[2020 年 6 月中华人民共和国县以上行政区划代码](http://www.mca.gov.cn//article/sj/xzqh/2020/202006/202008310601.shtml)进行数据爬取

```txt
├─code 存储行政区及代码
├─geojson 不含子区域
│ ├─city 城市
│ ├─county 区县
│ └─province 省份
└─geojson_full 含子区域
├─city 城市
└─province 区县
```