# Python dictionary of ISO 3166-1-alpha-2 codes, as per publicly available data on official ISO site in July 2015.
# Available under MIT license
# Dimitris Karagkasidis, https://github.com/pageflt

continents = {
    "LA": "latin_america",
    "SA": "south_america",
    "CA": "central_america",
    "AS": "asia",
    "OC": "australia",
    "AF": "africa",
    "EU": "europe",
    # "AN": "antarctica"
}

world_iso = {
    "africa": {
        "DZ": "algeria",
        "AO": "angola",
        "BJ": "benin",
        "BW": "botswana",
        "BF": "burkina-faso",
        "BI": "burundi",
        "CM": "cameroon",
        # canary-islands    # Island
        # "CV": "cape-verde", # Island
        "CF": "central-african-republic",
        "TD": "chad",
        # "KM": "comores", # Island
        "CG": "congo-brazzaville",
        "CD": "congo-democratic-republic",
        "DJ": "djibouti",
        "EG": "egypt",
        "GQ": "equatorial-guinea",
        "ER": "eritrea",
        "ET": "ethiopia",
        "GA": "gabon",
        "GH": "ghana",
        "GW": "guinea-bissau",  # No Data
        "GN": "guinea",
        "CI": "ivory-coast",
        "KE": "kenya",
        "LS": "lesotho",
        "LR": "liberia",
        "LY": "libya",
        "MG": "madagascar",
        "MW": "malawi",
        "ML": "mali",
        "MR": "mauritania",
        # "MU": "mauritius", Island
        "MA": "morocco",
        "MZ": "mozambique",
        "NA": "namibia",
        "NE": "niger",
        "NG": "nigeria",
        "RW": "rwanda",
        # saint-helena-ascension-and-tristan-da-cunha
        # "ST": "sao-tome-and-principe", #Island
        "SN": "senegal",
        "GM": "gambia",
        # "SC": "seychelles", #Island
        "SL": "sierra-leone",
        "SO": "somalia",  # No Data
        # south-africa-and-lesotho
        "ZA": "south-africa",
        "SS": "south-sudan",
        "SD": "sudan",
        "SZ": "swaziland",
        "TZ": "tanzania",
        "TG": "togo",
        "TN": "tunisia",
        "UG": "uganda",
        "ZM": "zambia",
        "ZW": "zimbabwe",
        "EH": "western-sahara",
    },
    "asia": {
        "AF": "afghanistan",
        "AM": "armenia",
        "AZ": "azerbaijan",
        "BH": "bahrain",
        "BD": "bangladesh",
        "BT": "bhutan",
        # "IO": "british indian ocean territory",
        # "BN": "brunei darussalam", # merged with MY
        "KH": "cambodia",
        "CN": "china",
        # "CX": "christmas island",
        # "CC": "cocos (keeling) islands",
        "CY": "cyprus",
        "GE": "georgia",
        "HK": "hong kong",
        "IN": "india",
        "ID": "indonesia",
        "IR": "iran",
        "IQ": "iraq",
        "IL": "israel",
        "JP": "japan",
        "JO": "jordan",
        "KZ": "kazakhstan",
        "KP": "north-korea",
        "KR": "south-korea",
        "KW": "kuwait",
        "KG": "kyrgyzstan",
        "LA": "lao-people's-democratic-republic",
        "LB": "lebanon",
        "MO": "macao",
        "MY": "malaysia",
        "SG": "singapore",
        "BN": "brunei",
        # "MV": "maldives",  # Island
        "MN": "mongolia",
        "MM": "myanmar",
        "NP": "nepal",
        "OM": "oman",
        "PK": "pakistan",
        "PS": "palestine",
        "PH": "philippines",
        "QA": "qatar",
        "SA": "saudi-arabia",
        "SG": "singapore",  # merged with MY
        "LK": "sri-lanka",
        "SY": "syria",
        "TW": "taiwan",
        "TJ": "tajikistan",
        "TH": "thailand",
        "TM": "turkmenistan",
        "AE": "united-arab-emirates",
        "UZ": "uzbekistan",
        "VN": "vietnam",
        "YE": "yemen",
    },
    "australia": {
        # "AS": "american-oceania",  # Island
        "AU": "australia",
        # "CK": "cook islands",  # Island
        # "FJ": "fiji",  # Island
        # "PF": "french-polynesia",  # Island
        # "GU": "guam",  # Island
        # "KI": "kiribati",  # Island
        # "MH": "marshall islands",  # Island
        # "FM": "micronesia",  # Island
        # "NR": "nauru",  # Island
        "NC": "new-caledonia",
        "NZ": "new-zealand",
        # "NU": "niue",  # Island
        # "NF": "norfolk island",  # Island
        # "MP": "northern mariana islands",
        # "PW": "palau",  # Island
        "PG": "papua-new-guinea",
        # "WS": "samoa",  # Island
        # "SB": "solomon islands",
        # "TK": "tokelau",  # Island
        # "TO": "tonga",  # Island
        # "TV": "tuvalu",  # Island
        # "VU": "vanuatu",  # Island
        # "WF": "wallis-et-futuna",  # Island
    },
    "europe": {
        "AL": "albania",
        "AD": "andorra",
        "AT": "austria",
        "BY": "belarus",
        "BE": "belgium",
        "BA": "bosnia-herzegovina",
        "BG": "bulgaria",
        "HR": "croatia",
        "CZ": "czech-republic",
        "DK": "denmark",
        "EE": "estonia",
        # "FO": "faroe islands",
        "FI": "finland",
        "FR": "france",
        "DE": "germany",
        # "GI": "gibraltar", Island ?
        "GR": "greece",
        # "GG": "guernsey", Island
        "HU": "hungary",
        "IS": "iceland",
        "IE": "ireland-and-northern-ireland",
        # "IM": "isle of man",
        "IT": "italy",
        # "JE": "jersey",
        "LV": "latvia",
        "LI": "liechtenstein",
        "LT": "lithuania",
        "LU": "luxembourg",
        "MK": "macedonia",
        "MT": "malta",
        "MD": "moldova",
        "MC": "monaco",
        "ME": "montenegro",
        "NL": "netherlands",
        "NO": "norway",
        "PL": "poland",
        "PT": "portugal",
        "RO": "romania",
        "RU": "russia",
        # "SM": "san-marino",
        "RS": "serbia",
        "SK": "slovakia",
        "SI": "slovenia",
        "ES": "spain",
        # "SJ": "svalbard-and-jan-mayen",
        "SE": "sweden",
        "CH": "switzerland",
        "UA": "ukraine",
        "GB": "great-britain",
        "TR": "turkey",
    },
    "north_america": {
        "CA": "canada",
        "GL": "greenland",
        "MX": "mexico",
        "US": "united states",
    },
    "latin_america": {
        "AR": "argentina",
        "BO": "bolivia",
        "BR": "brazil",
        "CL": "chile",
        "CO": "colombia",
        "EC": "ecuador",
        "GF": "french-guyane",
        "GY": "guyane",
        "PE": "peru",
        "PY": "paraguay",
        "SR": "suriname",
        "UY": "uruguay",
        "VE": "venezuela",
    },
    "central_america": {
        "BZ": "belize",
        "CR": "costa-rica",
        "HN": "honduras",
        "GT": "guatemala",
        "NI": "nicaragua",
        "PA": "panama",
        "SV": "el-salvador",
    },
}

# Based on: https://waml.org/waml-information-bulletin/46-3/index-to-lc-g-schedule/1-world/
continent_regions = {
    # SCANDANAVIAN REGION
    "SCR": ["DK", "NO", "SE", "FI", "IS"],  
    # EASTREN EUROPIAN REGION
    "EER": ["BY", "BU", "CZ", "RU", "SK", "UA", "GB", "LT", "LV", "EE"],
    # CENTRAL EUROPIAN REGION
    "CER": ["AT", "CH", "CZ", "DE", "HU", "PL", "SK"],
    # BALKAN PENISULAN REGION
    "BPR": ["AL","AN","BA","BG","GR","HR","MD","MT","RO","SL","RS","ME","MK"],
    # WESTREN EUROPE
    "WER": ["FR", "BE", "GB", "IE", "LU", "MC", "NL"],
    # SOUTHERN EUROPAIN REGION
    "SER": ["ES", "IT", "PT"],  
    # African regions
    "NAR": ["EG", "DZ", "LY", "MA", "SD", "SS"],  # NORTHERN AFRICAN REGION
    # WESTREN AFRICAN REGION
    "WAR": ["MR","ML","NE","NG","BJ","BF","TG","GH","CI","LR","SL","GN","GM","SL",],
    # CENTRAL AFRICAN REGION
    "CAR": ["TD", "CF", "CM", "GQ", "GA", "CD", "CG", "AO"],
    # EASTREN AFRICAN REGION
    "EAR": ["ET", "UG", "KE", "RW", "BI", "TZ", "MZ", "DJ", "MG"],
    # SOUTHERN AFRICAN REGION
    "SAR": ["MW", "ZM", "ZW", "BW", "NA", "SZ", "LS", "ZA"],
    # Asian regions (XNC is missing for nothern cyprus)
    "WAS": ["TR","AM","AZ","BH","CY","GE","IQ","IL-PL","JO","KW","LB","OM","PS","QA","SA","SY","AE","YE"],
    # FAR EASTREN AISIAN REGION
    "FEAR": ["JP", "KP", "KR", "CN", "TW", "CN", "MN"],
    # SOUTHEASTREN AISIAN REGION
    "SEAR": ["LA", "TH", "KH", "VN", "PH", "MYSGBN", "ID"],
    "CAR": ["KZ", "KG", "UZ", "TM", "TJ"],  # CENTRAL AISIAN REGION
    # SOUTHERN AISIAN REGION
    "SAR": ["MM", "BD", "BT", "NP", "IN", "LK", "PK", "AF"],
    # MIDDLE EASTREN ASIAN REGION
    "MEAR": ["TR", "SY", "IQ", "IR", "JO", "IL", "AE", "YE"],
    # American continent regions
    "NACR": ["CA", "GL", "MX", "US"],  # NORTHREN AMERCIAN CONTINENT REGION
    # SOUTHERN LATIN AMERICAL REGION
    "LACR": ["AR", "BO", "BR", "CL", "CO", "EC", "PE", "SR", "UY", "VE"],
    "CACR": ["BZ", "GT", "SV", "HN", "NI", "CR"],  # CENTRAL AMERICAN REGION
    # Customized test set
    "TEST": ["NG", "NE", "SL", "MA"],
}


