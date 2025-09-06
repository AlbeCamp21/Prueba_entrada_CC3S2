# Prueba_entrada_CC3S2

**2.3. Git: FF vs rebase vs cherry-pick**

El merge fast forward (FF) nos permite integrar cambios de una rama a otra, avanzando el puntero sin crear un commit adicional. Por otro lado, el rebase reescribe el historial para aplicar los cambios sobre el commit más reciente, esto nos ayuda a tener un historial lineal. Por último, cherry-pick nos permite copiar un commit específico de otra rama y pasarlo a otra, siendo útil en casos donde solo se quiera aplicar ciertos cambios, sin la necesidad de mezclar todos los commits.

**3.2. Prueba API con curl y jq**

El encabezado Content-Type devuelto por el servidor fue:

```
HTTP/2 200
date: Sat, 06 Sep 2025 20:19:36 GMT
content-type: application/json; charset=utf-8
content-length: 292
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=3ig47BLk4aWJ8v22zg2M17sbo1vj3uV1ZqjkVvzqABE%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1754033457"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=3ig47BLk4aWJ8v22zg2M17sbo1vj3uV1ZqjkVvzqABE%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1754033457"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1754033466
age: 21226
cf-cache-status: HIT
cf-ray: 97b0a988afe5c084-EZE
alt-svc: h3=":443"; ma=86400
```
