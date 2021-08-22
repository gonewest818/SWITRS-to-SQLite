MOVEMENT_PRECEDING = {
    "A": "stopped",
    "B": "proceeding straight",
    "C": "ran off road",
    "D": "making right turn",
    "E": "making left turn",
    "F": "making u-turn",
    "G": "backing",
    "H": "slowing/stopping",
    "I": "passing other vehicle",
    "J": "changing lanes",
    "K": "parking maneuver",
    "L": "entering traffic",
    "M": "other unsafe turning",
    "N": "crossed into opposing lane",
    "O": "parked",
    "P": "merging",
    "Q": "traveling wrong way",
    "R": "other",
}

STATEWIDE_VEHICLE_TYPE = {
    "A": "passenger car",
    "B": "passenger car with trailer",
    "C": "motorcycle or scooter",
    "D": "pickup or panel truck",
    "E": "pickup or panel truck with trailer",
    "F": "truck or truck tractor",
    "G": "truck or truck tractor with trailer",
    "H": "schoolbus",
    "I": "other bus",
    "J": "emergency vehicle",
    "K": "highway construction equipment",
    "L": "bicycle",
    "M": "other vehicle",
    "N": "pedestrian",
    "O": "moped",
}

DEGREE_OF_INJURY = {
    "0": "no injury",
    "1": "killed",
    "2": "severe injury",
    "3": "other visible injury",
    "4": "complaint of pain",
}

PARTY_TYPE = {
    "1": "driver",
    "2": "pedestrian",
    "3": "parked vehicle",
    "4": "bicyclist",
    "5": "other",
}

SEX = {
    "M": "male",
    "F": "female",
}

WEATHER = {
    "A": "clear",
    "B": "cloudy",
    "C": "raining",
    "D": "snowing",
    "E": "fog",
    "F": "other",
    "G": "wind",
}

CHP_BEAT_TYPE = {
    "0": "not chp",
    "1": "interstate",
    "2": "us highway",
    "3": "state route",
    "4": "county road line",
    "5": "county road area",
    "6": "us highway",
    "7": "state route",
    "8": "county road line",
    "9": "county road area",
    "10": "safety services program",
    "S": "safety services program",
    "11": "administrative",
    "A": "administrative",
}

COLLISION_TYPE = {
    "A": "head-on",
    "B": "sideswipe",
    "C": "rear end",
    "D": "broadside",
    "E": "hit object",
    "F": "overturned",
    "G": "pedestrian",
    "H": "other",
}

INVOLVED_WITH = {
    "A": "non-collision",
    "B": "pedestrian",
    "C": "other motor vehicle",
    "D": "motor vehicle on other roadway",
    "E": "parked motor vehicle",
    "F": "train",
    "G": "bicycle",
    "H": "animal",
    "I": "fixed object",
    "J": "other object",
}

PEDESTRIAN_ACTION = {
    "A": "no pedestrian involved",
    "B": "crossing in intersection crosswalk",
    "C": "crossing non-intersection crosswalk",
    "D": "crossing not in crosswalk",
    "E": "in road",
    "F": "not in road",
    "G": "using school bus",
}

DIRECTION = {
    "N": "north",
    "E": "east",
    "S": "south",
    "W": "west",
}

LOCATION_TYPE = {
    "H": "highway",
    "I": "intersection",
    "R": "ramp",
}

CHP_BEAT_CLASS = {
    "1": "chp primary",
    "2": "chp other",
    "0": "not chp",
}

HIT_AND_RUN = {
    "F": "felony",
    "M": "misdemeanor",
    "N": "not hit and run",
}

ROAD_SURFACE = {
    "A": "dry",
    "B": "wet",
    "C": "snowy",
    "D": "slippery",
}

ROAD_CONDITION = {
    "A": "holes",
    "B": "loose material",
    "C": "obstruction",
    "D": "construction",
    "E": "reduced width",
    "F": "flooded",
    "G": "other",
    "H": "normal",
}

LIGHTING = {
    "A": "daylight",
    "B": "dusk or dawn",
    "C": "dark with street lights",
    "D": "dark with no street lights",
    "E": "dark with street lights not functioning",
}

CONTROL_DEVICE = {
    "A": "functioning",
    "B": "not functioning",
    "C": "obscured",
    "D": "none",
}

SIDE_OF_HIGHWAY = {
    "N": "northbound",
    "S": "southbound",
    "E": "eastbound",
    "W": "westbound",
}

PRIMARY_COLLISION_FACTOR = {
    "A": "vehicle code violation",
    "B": "other improper driving",
    "C": "other than driver",
    "D": "unknown",
    "E": "fell asleep",
}

PCF_VIOLATION_CODE = {
    "B": "business",
    "C": "vehicle",
    "H": "city health",
    "I": "city ordinance",
    "O": "county ordinance",
    "P": "penal",
    "S": "streets",
    "W": "welfare",
}

RACE = {
    "A": "asian",
    "B": "black",
    "H": "hispanic",
    "O": "other",
    "W": "white",
}

COLLISION_SEVERITY = {
    "0": "property damage only",
    "1": "fatal",
    "2": "severe injury",
    "3": "other injury",
    "4": "pain",
}

PCF_VIOLATION_CATEGORY = {
    "00": "unknown",
    "01": "dui",
    "02": "impeding traffic",
    "03": "speeding",
    "04": "following too closely",
    "05": "wrong side of road",
    "06": "improper passing",
    "07": "unsafe lane change",
    "08": "improper turning",
    "09": "automobile right of way",
    "10": "pedestrian right of way",
    "11": "pedestrian violation",
    "12": "traffic signals and signs",
    "13": "hazardous parking",
    "14": "lights",
    "15": "brakes",
    "16": "other equipment",
    "17": "other hazardous violation",
    "18": "other than driver (or pedestrian)",
    "21": "unsafe starting or backing",
    "22": "other improper driving",
    "23": "pedestrian dui",
    "24": "fell asleep",
}

COUNTIES = {
    "01": "alameda",
    "02": "alpine",
    "03": "amador",
    "04": "butte",
    "05": "calaveras",
    "06": "colusa",
    "07": "contra costa",
    "08": "del norte",
    "09": "el dorado",
    "10": "fresno",
    "11": "glenn",
    "12": "humboldt",
    "13": "imperial",
    "14": "inyo",
    "15": "kern",
    "16": "kings",
    "17": "lake",
    "18": "lassen",
    "19": "los angeles",
    "20": "madera",
    "21": "marin",
    "22": "mariposa",
    "23": "mendocino",
    "24": "merced",
    "25": "modoc",
    "26": "mono",
    "27": "monterey",
    "28": "napa",
    "29": "nevada",
    "30": "orange",
    "31": "placer",
    "32": "plumas",
    "33": "riverside",
    "34": "sacramento",
    "35": "san benito",
    "36": "san bernardino",
    "37": "san diego",
    "38": "san francisco",
    "39": "san joaquin",
    "40": "san luis obispo",
    "41": "san mateo",
    "42": "santa barbara",
    "43": "santa clara",
    "44": "santa cruz",
    "45": "shasta",
    "46": "sierra",
    "47": "siskiyou",
    "48": "solano",
    "49": "sonoma",
    "50": "stanislaus",
    "51": "sutter",
    "52": "tehama",
    "53": "trinity",
    "54": "tulare",
    "55": "tuolumne",
    "56": "ventura",
    "57": "yolo",
    "58": "yuba",
}

CHP_VEHICLE_TYPE = {
    "01": "passenger car, station",
    "02": "motorcycle",
    "03": "motor driven",
    "04": "bicycle",
    "05": "motorized bicycle",
    "06": "all terrain vehicle",
    "07": "sport utility vehicle",
    "08": "mini-vans",
    "09": "paratransit",
    "10": "tour bus",
    "11": "other commercial",
    "12": "non-commercial bus",
    "13": "school bus public type i",
    "14": "school bus public type ii",
    "15": "school bus private type i",
    "16": "school bus private type ii",
    "17": "school bus contractual type i",
    "18": "school bus contractual type ii",
    "19": "general public paratransit",
    "20": "public transit authority",
    "21": "two axle tank truck",
    "22": "pickups & panels",
    "23": "pickup w/camper",
    "24": "three axle tank truck",
    "25": "truck tractor",
    "26": "two axle truck",
    "27": "three or more axle truck",
    "28": "semi tank trailer",
    "29": "pull tank trailer",
    "30": "two tank trailer",
    "31": "semi",
    "32": "pull",
    "33": "two trailers (includes semi & pull)",
    "34": "boat",
    "35": "utility",
    "36": "trailer coach",
    "37": "extralegal permit load",
    "38": "pole, pipe, or logging dolly",
    "39": "three trailers",
    "40": "federally legal semi",
    "41": "ambulance",
    "42": "dune buggy",
    "43": "fire truck",
    "44": "fork lift",
    "45": "hwy. construction equip.",
    "46": "implement of husbandry",
    "47": "motor home",
    "48": "police car",
    "49": "police motorcycle",
    "50": "mobile equipment",
    "51": "farm labor vehicle (certified)",
    "52": "federally legal double combo over 75 feet",
    "53": "fifth wheel travel trailer",
    "54": "container chassis",
    "55": "two-axle tow truck",
    "56": "three-axle tow truck",
    "57": "farm labor vehicle",
    "58": "farm labor transporter",
    "59": "motor home > 40 feet",
    "60": "pedestrian",
    "61": "second or additional enforcement action(s)",
    "62": "passengers",
    "63": "youth bus",
    "64": "school pupil activity bus type i",
    "65": "school pupil activity bus type ii",
    "71": "passenger car, station wagon, jeep: hazardous material",
    "72": "pickups and panels: hazardous material",
    "73": "pickup and camper: hazardous material",
    "75": "truck tractor: hazardous material",
    "76": "two-axle truck: hazardous material",
    "77": "three or more axle truck: hazardous material",
    "78": "two-axle tank truck: hazardous material",
    "79": "three-axle tank truck: hazardous material",
    "81": "passenger car, station wagon, jeep: hazardous waste or hazardous waste/material combination",
    "82": "pickups and panels: hazardous waste or hazardous waste/material combination",
    "83": "pickup and camper: hazardous waste or hazardous waste/material combination",
    "85": "truck tractor: hazardous waste or hazardous waste/material combination",
    "86": "two-axle truck: hazardous waste or hazardous waste/material combination",
    "87": "three or more axle truck: hazardous waste or hazardous waste/material combination",
    "88": "two-axle tank truck: hazardous waste or hazardous waste/material combination",
    "89": "three-axle tank truck: hazardous waste or hazardous waste/material combination",
    "94": "go-ped, zip electric scooter, motoboard",
    "95": "misc. non-motor vehicle",
    "96": "misc. motor vehicle (snowmobile, golf cart)",
    "97": "low speed vehicle",
    "98": "emergency vehicle (on emergency run)",
    "99": "unknown hit and run vehicle involvement",
}

CELLPHONE_USE_TYPE = {
    'B': "cellphone in use",
    'C': "cellphone not in use",
    'D': "no cellphone/unknown",
    '1': "cellphone in use (handheld)",
    '2': "cellphone in use (hands-free)",
    '3': "cellphone not in use",
}

SOBRIETY = {
    'A': 'had not been drinking',
    'B': 'had been drinking, under influence',
    'C': 'had been drinking, not under influence',
    'D': 'had been drinking, impairment unknown',
    'G': 'impairment unknown',
    'H': 'not applicable',
}

DRUG = {
    'E': 'under drug influence',
    'F': 'impairment - physical',
    'H': 'not applicable',
    'I': 'sleepy/fatigued',
}
