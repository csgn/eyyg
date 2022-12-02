/*
+------------------+----------------+--------------+-------+
| request_endpoint | request_status | request_time | count |
|------------------+----------------+--------------+-------|
| /usr             | 200            | 2019-12-31   | 2     |
| /usr             | 303            | 2019-12-31   | 1     |
| /usr             | 304            | 2019-12-31   | 3     |
| /usr             | 403            | 2019-12-31   | 3     |
| /usr             | 404            | 2019-12-31   | 1     |
| /usr             | 500            | 2019-12-31   | 1     |
| /usr             | 502            | 2019-12-31   | 1     |
| /usr             | 200            | 2020-01-01   | 4     |
| /usr             | 303            | 2020-01-01   | 6     |
| /usr             | 304            | 2020-01-01   | 7     |
| /usr             | 403            | 2020-01-01   | 4     |
| /usr             | 404            | 2020-01-01   | 5     |
| /usr             | 500            | 2020-01-01   | 7     |
| /usr             | 502            | 2020-01-01   | 4     |
| /usr             | 200            | 2020-01-02   | 1     |
| /usr             | 303            | 2020-01-02   | 6     |
| /usr             | 304            | 2020-01-02   | 3     |
| /usr             | 403            | 2020-01-02   | 6     |
| /usr             | 404            | 2020-01-02   | 7     |
| /usr             | 500            | 2020-01-02   | 4     |
*/

select request_endpoint
		,request_status
		,request_time::timestamp::date
		,count(*)
from serverlog
where request_endpoint = '/usr' and request_method = 'PUT'
group by request_endpoint
		  ,request_status
		  ,request_time::timestamp::date 
order by 3;

