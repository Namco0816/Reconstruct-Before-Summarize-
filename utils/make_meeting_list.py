import os

ami_meeting_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/ami") if f.split(".")[-1] == "da"]))
# ami_meeting_list = ["ES2005c"]
icsi_meeting_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/icsi") if f.split(".")[-1] == "da"]))

ami_zh_meeting_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/ami_zh") if f.split(".")[-2] == "da"]))

ami_reference_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/ami_zh") if f.split(".")[1:] == ["ducref", "abstract", "zh"]]))
ami_actions_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/ami_zh") if f.split(".")[1:] == ["ducref", "actions", "zh"]]))
ami_decisions_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/ami_zh") if f.split(".")[1:] == ["ducref", "decisions", "zh"]]))
ami_problems_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/ami_zh") if f.split(".")[1:] == ["ducref", "problems", "zh"]]))

icsi_reference_list = list(set([ f.split(".")[0] for f in os.listdir("resources/data/meeting/icsi") if f.split(".")[1:] == ["ducref", "abstract"]]))
icsi_test_set = [
    'Bed004',
    'Bed009',
    'Bed016',
    'Bmr005',
    'Bmr019',
    'Bro018'
]

icsi_eval_set = [
    'Bed003',
    'Bed017',
    'Bed012',
    'Bed013',
    'Bmr014',
    'Bmr015',
    'Bmr020',
    'Bmr003',
    'Bro025',
    'Bro026',
    'Bro027',
]
icsi_train_set = [
    'Bed008',
    'Bed011',
    'Bmr018',
    'Bed015',
    'Bed010',
    'Bro024',
    'Bmr007',
    'Bed005',
    'Bmr006',
    'Bed002',
    'Bro023',
    'Bmr013',
    'Bed014',
    "Bdb001",
    "Bmr009",
    'Bed006',
    "Bmr010",
    "Bmr011",
    "Bmr012",
    "Bmr016",
    "Bmr023",
    "Bmr024",
    "Bmr025",
    "Bmr026",
    "Bmr027",
    "Bro003",
    "Bro004",
    "Bro005",
    "Bro007",
    "Bro008",
    "Bro010",
    "Bro011",
    "Bro012",
    "Bro013",
    "Bro014",
    "Bro016",
    "Bro017",
    "Bro019",
    "Bro021",
    "Bro022",
    "Bro028",
    "Buw001",
]


ami_eval_set = [
    "ES2003a",
    "ES2003b",
    "ES2003c",
    "ES2003d",
    "ES2011a",
    "ES2011b",
    "ES2011c",
    "ES2011d",
    "IS1008a",
    "IS1008b",
    "IS1008c",
    "IS1008d",
    "TS3004a",
    "TS3004b",
    "TS3004c",
    "TS3004d",
    "TS3006a",
    "TS3006b",
    "TS3006c",
    "TS3006d",
]

ami_test_set = [
    "ES2004a",
    "ES2004b",
    "ES2004c",
    "ES2004d",
    "ES2014a",
    "ES2014b",
    "ES2014c",
    "ES2014d",
    "IS1009a",
    "IS1009b",
    "IS1009c",
    "IS1009d",
    "TS3003a",
    "TS3003b",
    "TS3003c",
    "TS3003d",
    "TS3007a",
    "TS3007b",
    "TS3007c",
    "TS3007d",
]

ami_train_set = [
    "ES2002a",
    "ES2002b",
    "ES2002c",
    "ES2002d",
    "ES2005a",
    "ES2005b",
    "ES2005c",
    "ES2005d",
    "ES2006a",
    "ES2006b",
    "ES2006c",
    "ES2006d",
    "ES2007a",
    "ES2007b",
    "ES2007c",
    "ES2007d",
    "ES2008a",
    "ES2008b",
    "ES2008c",
    "ES2008d",
    "ES2009a",
    "ES2009b",
    "ES2009c",
    "ES2009d",
    "ES2010a",
    "ES2010b",
    "ES2010c",
    "ES2010d",
    "ES2012a",
    "ES2012b",
    "ES2012c",
    "ES2012d",
    "ES2013a",
    "ES2013b",
    "ES2013c",
    "ES2013d",
    "ES2015a",
    "ES2015b",
    "ES2015c",
    "ES2015d",
    "ES2016a",
    "ES2016b",
    "ES2016c",
    "ES2016d",
    "IS1000a",
    "IS1000b",
    "IS1000c",
    "IS1000d",
    "IS1001a",
    "IS1001b",
    "IS1001c",
    "IS1001d",
    "IS1002b",
    "IS1002c",
    "IS1002d",
    "IS1003a",
    "IS1003b",
    "IS1003c",
    "IS1003d",
    "IS1004a",
    "IS1004b",
    "IS1004c",
    "IS1004d",
    "IS1005a",
    "IS1005b",
    "IS1005c",
    "IS1006a",
    "IS1006b",
    "IS1006c",
    "IS1006d",
    "IS1007a",
    "IS1007b",
    "IS1007c",
    "IS1007d",
    "TS3005a",
    "TS3005b",
    "TS3005c",
    "TS3005d",
    "TS3008a",
    "TS3008b",
    "TS3008c",
    "TS3008d",
    "TS3009a",
    "TS3009b",
    "TS3009c",
    "TS3009d",
    "TS3010a",
    "TS3010b",
    "TS3010c",
    "TS3010d",
    "TS3011a",
    "TS3011b",
    "TS3011c",
    "TS3011d",
    "TS3012a",
    "TS3012b",
    "TS3012d",
]
