



## sub-api

1. 查询子账户的列表 subs

```json
{
	"code": "A10000",
	"data": [{
		"subId": "CA648855168502206464",
		"bussType": "spot",
		"state": "Frozen",
		"subAccount": "001",
		"subIdentify": "001"
	}, {
		"subId": "CA648855702269333504",
		"bussType": "spot",
		"state": "Frozen",
		"subAccount": "002",
		"subIdentify": "002"
	}, {
		"subId": "CA648856083527372801",
		"bussType": "spot",
		"state": "Frozen",
		"subAccount": "004",
		"subIdentify": "004"
	}, {
		"subId": "CA648856083527372800",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "003",
		"subIdentify": "003"
	}, {
		"subId": "CA649259408953446400",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "122aaaaa",
		"subIdentify": "1222"
	}, {
		"subId": "CA649266767897563136",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "12222223a",
		"subIdentify": "11111111"
	}, {
		"subId": "CA649266767893368832",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "aaaaaa111",
		"subIdentify": "s1222211234567890-oiuytrewqqwweertyy12345678901234"
	}, {
		"subId": "CA649551759336804352",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "1211111aa",
		"subIdentify": "12"
	}, {
		"subId": "CA649579834980175872",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "122222aa",
		"subIdentify": "1"
	}, {
		"subId": "CA649579834955010048",
		"bussType": "spot",
		"state": "Normal",
		"subAccount": "00000005a",
		"subIdentify": "12312322222222222222222222"
	}],
	"message": "Success"
}
```

2. 查询子账户的余额

/v1/account/subs/' + subId + '/balance

```json
{
    "code":"A10000",
    "data":[
        {
            "balance":7.22,
            "currency":"BTC"
        },
        {
            "balance":328.9,
            "currency":"EOS"
        },
        {
            "balance":28,
            "currency":"BCH"
        },
        {
            "balance":199.72,
            "currency":"BRL"
        }
    ],
    "message":"Success"
}
```

3. 子账户转账'CA648856083527372800'

  subId = 'CA648856083527372800'
        assetCode = 'BTC'
        transferAmount = '0.51'
        transferType = 'master-transfer-out'

```json
{'code': 'A10000', 'data': 39, 'message': 'Success'}
```


4. 子账户转账列表
```json
{
	"code": "A10000",
	"data": [{
		"subId": "CA648855702269333504",
		"amount": 9.32,
		"currency": "BTC",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 111,
		"currency": "EOS",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 220.0,
		"currency": "EOS",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 100.0,
		"currency": "BRL",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 103.22,
		"currency": "BRL",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 103.22,
		"currency": "BRL",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 3.5,
		"currency": "BRL",
		"state": "success",
		"type": "master-transfer-in"
	}, {
		"subId": "CA648855702269333504",
		"amount": 2.1,
		"currency": "EOS",
		"state": "success",
		"type": "master-transfer-in"
	}, {
		"subId": "CA648855702269333504",
		"amount": 2.1,
		"currency": "BTC",
		"state": "success",
		"type": "master-transfer-in"
	}, {
		"subId": "CA648855702269333504",
		"amount": 30.0,
		"currency": "BCH",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648855702269333504",
		"amount": 2,
		"currency": "BCH",
		"state": "success",
		"type": "master-transfer-in"
	}, {
		"subId": "CA648856083527372801",
		"amount": 30.0,
		"currency": "BRL",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648856083527372800",
		"amount": 1,
		"currency": "BTC",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA649259408953446400",
		"amount": 1.2,
		"currency": "BTC",
		"state": "success",
		"type": "master-transfer-out"
	}, {
		"subId": "CA648856083527372800",
		"amount": 1,
		"currency": "BTC",
		"state": "success",
		"type": "master-transfer-out"
	}],
	"message": "Success"
}

```

