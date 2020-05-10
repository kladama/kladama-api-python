# Kladama API for Python

![Master Build](https://github.com/plexilar/kladama-api-python/workflows/Build/badge.svg?branch=master)

Python API for Kladama Services Integration

## How to install it

You can install the API through PIP

```shell script
pip install kladama-api
```

## How to start using it

First, you must to authenticate through a <em>API Token</em> that must be provided to you. This authentication process returns a session object that must be used to create a `Context` object.

```python
# retrieve all areas of interest by user

import kladama as kld

env = kld.Environments().prod
api_token = '<your provided token>'
session = kld.authenticate(env, api_token)

query = kld.Query().aoi.by_user('<your user>')
aois = kld.Context(session).get(query)
for aoi in aois:
    print(aoi.name, '-', aoi.description, 'in', aoi.link)
```

## How to create an area of interest

```python
# create a periodic subscription

import kladama as kld

env = kld.Environments().prod
api_token = '<your provided token>'
session = kld.authenticate(env, api_token)

operation = kld.Operations()\
    .create_aoi\
    .set_user('<your user>')\
    .set_aoi_id('<aoi id>')\
    .set_name("Test AOI")\
    .set_category("Test")\
    .set_features({
        "type": "FeatureCollection",
        "name": "Test AoI",
        "features": {
            "type": "Feature",
            "properties": {
                "id": "5b8c9e286e63b329cf764c61",
                "name": "field-1",
                "geometry": {
                    "type": "MultiPolygon",
                    "coordinates": [
                        [
                            [
                                [-60.675417,-21.854207],
                                [-60.675394,-21.855348],
                                [-60.669532,-21.858799],
                                [-60.656133,-21.85887],
                                [-60.656118,-21.854208],
                                [-60.675417,-21.854207]
                            ]
                        ]
                    ]
                },
            }
        }
    })

response = kld.Context(session).execute(operation)
if not isinstance(response, kld.Success):
    print(response.__str__())
```

## How to create a subscription

```python
# create a periodic subscription

import kladama as kld

env = kld.Environments().prod
api_token = '<your provided token>'
session = kld.authenticate(env, api_token)

operation = kld.Operations()\
    .create_periodic_subsc\
    .set_user('<your user>')\
    .set_variable_name('ecmwf-era5-2m-ar-max-temp')\
    .set_variable_source_name('ECMWF')\
    .set_spatial_operation_name('mean')\
    .set_aoi_name('<aoi name>')

response = kld.Context(session).execute(operation)
if isinstance(response, kld.Success):
    code = response.result['code'] # the code is the id of the subscription
else:
    print(response.__str__())
```
