from __future__ import annotations
from .environment import MurfEnvironment
from enum import Enum

class MurfRegion(Enum):
    DEFAULT = "default"
    GLOBAL = "global"
    US_EAST = "us-east"
    US_WEST = "us-west"
    EU_CENTRAL = "eu-central"
    IN = "in"
    JP = "jp"
    AU = "au"
    KR = "kr"
    ME = "me"
    SA_EAST = "sa-east"
    UK = "uk"
    CA = "ca"

global_environment = MurfEnvironment(
    base="https://global.api.murf.ai",
    production="wss://global.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

us_east_environment = MurfEnvironment(
    base="https://us-east.api.murf.ai",
    production="wss://us-east.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

us_west_environment = MurfEnvironment(
    base="https://us-west.api.murf.ai",
    production="wss://us-west.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

eu_central_environment = MurfEnvironment(
    base="https://eu-central.api.murf.ai",
    production="wss://eu-central.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

in_environment = MurfEnvironment(
    base="https://in.api.murf.ai",
    production="wss://in.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

jp_environment = MurfEnvironment(
    base="https://jp.api.murf.ai",
    production="wss://jp.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

au_environment = MurfEnvironment(
    base="https://au.api.murf.ai",
    production="wss://au.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

kr_environment = MurfEnvironment(
    base="https://kr.api.murf.ai",
    production="wss://kr.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

me_environment = MurfEnvironment(
    base="https://me.api.murf.ai",
    production="wss://me.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

sa_east_environment = MurfEnvironment(
    base="https://sa-east.api.murf.ai",
    production="wss://sa-east.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

uk_environment = MurfEnvironment(
    base="https://uk.api.murf.ai",
    production="wss://uk.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)

ca_environment = MurfEnvironment(
    base="https://ca.api.murf.ai",
    production="wss://ca.api.murf.ai/v1/speech",
    global_router="https://global.api.murf.ai",
    us_east="https://us-east.api.murf.ai",
    us_west="https://us-west.api.murf.ai",
    india="https://in.api.murf.ai",
    canada="https://ca.api.murf.ai",
    south_korea="https://kr.api.murf.ai",
    uae="https://me.api.murf.ai",
    japan="https://jp.api.murf.ai",
    australia="https://au.api.murf.ai",
    eu_central="https://eu-central.api.murf.ai",
    uk="https://uk.api.murf.ai",
    south_america="https://sa-east.api.murf.ai"
)


region_environment_map = {
    MurfRegion.DEFAULT: MurfEnvironment.DEFAULT,
    MurfRegion.GLOBAL: global_environment,
    MurfRegion.US_EAST: us_east_environment,
    MurfRegion.US_WEST: us_west_environment,
    MurfRegion.EU_CENTRAL: eu_central_environment,
    MurfRegion.IN: in_environment,
    MurfRegion.JP: jp_environment,
    MurfRegion.AU: au_environment,
    MurfRegion.KR: kr_environment,
    MurfRegion.ME: me_environment,
    MurfRegion.SA_EAST: sa_east_environment,
    MurfRegion.UK: uk_environment,
    MurfRegion.CA: ca_environment,
}