from datetime import timedelta

from feast import (
    FeatureView,
    Field,
)
from feast.types import Float32

from data_sources import *
from entities import *

driver_hourly_stats_view = FeatureView(
    name="driver_hourly_stats",
    description="Hourly driver conversion and acceptance-rate features",
    tags={
    "production": "True",
    "domain": "mobility",
    "managed_by": "feast_ci",
    "ci_test": "v1",
},
    owner="panrui1998110@gmail.com",
    entities=[driver],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
    ],
    online=True,
    source=driver_stats
)
