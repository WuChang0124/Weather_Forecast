import urllib.request as request
import urllib.error as error
import json
import urllib

class WeatherQuery:
    def __init__(self, api_key):
        self.api_url = 'http://apis.juhe.cn/simpleWeather/query'
        self.api_key = api_key

    def query_weather(self, city):
        params_dict = {
            "city": city,
            "key": self.api_key,
        }
        params = urllib.parse.urlencode(params_dict)
        try:
            req = request.Request(self.api_url, params.encode())
            response = request.urlopen(req)
            content = response.read()
            if content:
                try:
                    result = json.loads(content)
                    error_code = result['error_code']
                    if error_code == 0:
                        temperature = result['result']['realtime']['temperature']
                        humidity = result['result']['realtime']['humidity']
                        info = result['result']['realtime']['info']
                        direct = result['result']['realtime']['direct']
                        power = result['result']['realtime']['power']
                        return f"{info}\n{temperature}\n{humidity}\n{direct}\n{power}"
                    else:
                        return f"请求失败: {result['error_code']} {result['reason']}"
                    
                        
                except Exception as e:
                    return f"解析结果异常：{e}"
            else:
                return "请求异常"
        except error.HTTPError as err:
            return str(err)
        except error.URLError as err:
            return str(err)     
