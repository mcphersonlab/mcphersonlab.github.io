# Conference data shared between conferences.qmd and index.qmd
# Update this file to modify conference information

from datetime import datetime

conferences = [
    {
        "name": "Staphylococcal Diseases Gordon Research Conference",
        "location": "Waterville Valley, NH, USA",
        "lat": 43.9815,
        "lon": -71.5078,
        "start_date": "2027-08-08",
        "end_date": "2027-08-13",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "2027 abstract dates TBD; check GRC website",
        "type": "Conference",
        "url": "https://www.grc.org/staphylococcal-diseases-conference/2027/",
        "projects": [
            "https://github.com/mcphersonlab/amr-staphylococcus-aureus"
        ]
    },
    {
        "name": "ClostPath Biennial",
        "location": "Paris, France (2027 TBD)",
        "lat": 48.8566,
        "lon": 2.3522,
        "start_date": "2027-09-01",
        "end_date": "2027-09-04",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "2027 dates and location TBD (biennial); map shows 2025 host city",
        "type": "Conference",
        "url": "https://www.clostpath2025.conferences-pasteur.org/",
        "projects": [
            "https://github.com/mcphersonlab/clostridioides_atlas",
            "https://github.com/mcphersonlab/mgx-cdi-peds"
        ]
    },
    {
        "name": "Peggy Lillis Foundation National C. diff Summit",
        "location": "Washington, DC",
        "lat": 38.9072,
        "lon": -77.0369,
        "start_date": "2026-04-13",
        "end_date": "2026-04-13",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "",
        "type": "Symposium",
        "url": "https://cdiff.org/event/summit26/",
        "projects": [
            "https://github.com/mcphersonlab/tx-cdi",
            "https://github.com/mcphersonlab/mgx-clostridioides-difficile",
            "https://github.com/mcphersonlab/clostridioides_atlas",
            "https://github.com/mcphersonlab/mgx-cdi-peds",
            "https://github.com/mcphersonlab/roi-cdi"
        ]
    },
    {
        "name": "BPS Annual",
        "location": "Manchester, UK",
        "lat": 53.4808,
        "lon": -2.2426,
        "start_date": "2026-12-08",
        "end_date": "2026-12-10",
        "abstract_open": "2026-04-01",
        "abstract_close": "2026-09-01",
        "abstract_note": "See BPS website for abstract dates and details",
        "type": "Conference",
        "url": "https://www.bps.ac.uk/events",
        "projects": [
            "https://github.com/mcphersonlab/structure-function-pharmacology",
            "https://github.com/mcphersonlab/SpaceTime",
            "https://github.com/mcphersonlab/pcol-biofilm-rifamycins"
        ]
    },
    {
        "name": "TMC AMR",
        "location": "Houston, TX",
        "lat": 29.711,
        "lon": -95.3981,
        "start_date": "2027-01-13",
        "end_date": "2027-01-15",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "10th Annual; 2027 dates TBD (typically mid-January)",
        "type": "Conference",
        "url": "https://www.tmc.edu/events/",
        "projects": [
            "https://github.com/mcphersonlab/mgx-cdi-vre",
            "https://github.com/mcphersonlab/amr-enterococcus-faecium",
            "https://github.com/mcphersonlab/amr-env-food",
            "https://github.com/mcphersonlab/amr-env-water",
            "https://github.com/mcphersonlab/cost-amr"
        ]
    },
    {
        "name": "IMARI Annual",
        "location": "Las Vegas, NV",
        "lat": 36.1699,
        "lon": -115.1398,
        "start_date": "2027-01-27",
        "end_date": "2027-01-29",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "2027 dates TBD; check IMARI website",
        "type": "Conference",
        "url": "https://imari.org",
        "projects": [
            "https://github.com/mcphersonlab/ai-amr",
            "https://github.com/mcphersonlab/amr-acinetobacter-baumannii",
            "https://github.com/mcphersonlab/amr-candida-auris",
            "https://github.com/mcphersonlab/amr-env-food",
            "https://github.com/mcphersonlab/amr-env-water"
        ]
    },
    {
        "name": "BSAC and GARDP Antimicrobial Chemotherapy Conference",
        "location": "Online",
        "lat": 51.5074,
        "lon": -0.1278,
        "start_date": "2027-02-03",
        "end_date": "2027-02-04",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "2027 dates TBD; free online conference",
        "type": "Conference",
        "url": "https://acc-conference.com/",
        "projects": [
            "https://github.com/mcphersonlab/mgx-abx-healthy",
            "https://github.com/mcphersonlab/abx-iv-mgx-mbx-imm",
            "https://github.com/mcphersonlab/amr-env-food"
        ]
    },
    {
        "name": "AAAS Annual",
        "location": "Chicago, IL",
        "lat": 41.8827,
        "lon": -87.6233,
        "start_date": "2027-02-18",
        "end_date": "2027-02-20",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "Abstract dates TBD; check AAAS website",
        "type": "Conference",
        "url": "https://meetings.aaas.org/",
        "projects": [
            "https://github.com/mcphersonlab/mgx-immunol-regulatory-t-cells",
            "https://github.com/mcphersonlab/mgx-mbx-colorectal-cancer",
            "https://github.com/mcphersonlab/mgx-mbx-glp-1",
            "https://github.com/mcphersonlab/EarthEpi",
            "https://github.com/mcphersonlab/StormPath",
            "https://github.com/mcphersonlab/DigitalTwin-Society-Health",
            "https://github.com/mcphersonlab/env-mgx-pd"
        ]
    },
    {
        "name": "CSIRO AMR Summit",
        "location": "Sydney, Australia",
        "lat": -33.8688,
        "lon": 151.2093,
        "start_date": "2027-02-17",
        "end_date": "2027-02-19",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "2027 dates TBD; invitation-only event",
        "type": "Conference",
        "url": "https://www.csiro.au/en/about/challenges-missions/antimicrobial-resistance/amr-summit",
        "projects": [
            "https://github.com/mcphersonlab/ai-amr",
            "https://github.com/mcphersonlab/cost-amr",
            "https://github.com/mcphersonlab/amr-env-food",
            "https://github.com/mcphersonlab/amr-env-water"
        ]
    },
    {
        "name": "Biophysical Society Annual",
        "location": "Philadelphia, PA",
        "lat": 39.9526,
        "lon": -75.1652,
        "start_date": "2027-02-20",
        "end_date": "2027-02-24",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "Abstract dates TBD; see Biophysical Society website for updates",
        "type": "Conference",
        "url": "https://www.biophysics.org/upcoming-annual-meetings",
        "projects": [
            "https://github.com/mcphersonlab/biophysics-proteins-as-complex-machines-of-physics",
            "https://github.com/mcphersonlab/ai-structural-biology",
            "https://github.com/mcphersonlab/namd-adk",
            "https://github.com/mcphersonlab/phys-hiv-lenacapavir",
            "https://github.com/mcphersonlab/SpaceTime"
        ]
    },
    {
        "name": "CROI Annual",
        "location": "San Diego, CA",
        "lat": 32.7157,
        "lon": -117.1611,
        "start_date": "2027-03-21",
        "end_date": "2027-03-24",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "Abstract dates TBD; check CROI website",
        "type": "Conference",
        "url": "https://www.croiconference.org/",
        "projects": [
            "https://github.com/mcphersonlab/amr-hiv",
            "https://github.com/mcphersonlab/epi-hbv",
            "https://github.com/mcphersonlab/phys-hiv-lenacapavir",
            "https://github.com/mcphersonlab/pcol-vcddmde-hbv"
        ]
    },
    {
        "name": "ASBMB Annual",
        "location": "Washington, DC",
        "lat": 38.9072,
        "lon": -77.0369,
        "start_date": "2026-03-07",
        "end_date": "2026-03-10",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.asbmb.org/annual-meeting",
        "projects": [
            "https://github.com/mcphersonlab/structure-function-pharmacology",
            "https://github.com/mcphersonlab/namd-adk",
            "https://github.com/mcphersonlab/SpaceTime",
            "https://github.com/mcphersonlab/pcol-biofilm-rifamycins"
        ]
    },
    {
        "name": "EMBL AI and Biology",
        "location": "EMBL Heidelberg and Online",
        "lat": 49.3988,
        "lon": 8.6724,
        "start_date": "2026-03-10",
        "end_date": "2026-03-13",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.embl.org/about/info/course-and-conference-office/events/ees26-02/",
        "projects": [
            "https://github.com/mcphersonlab/ai-structural-biology",
            "https://github.com/mcphersonlab/ai-amr",
            "https://github.com/mcphersonlab/ai-microbiome-transmission",
            "https://github.com/mcphersonlab/ai-forecast-pharmacology"
        ]
    },
    {
        "name": "ESCMID Annual",
        "location": "Munich, Germany",
        "lat": 48.1371,
        "lon": 11.5761,
        "start_date": "2026-04-17",
        "end_date": "2026-04-21",
        "abstract_open": "2025-10-15",
        "abstract_close": "2025-11-26",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.escmid.org/congress-events/escmid-global/",
        "projects": [
            "https://github.com/mcphersonlab/amr-klebsiella-pneumoniae",
            "https://github.com/mcphersonlab/amr-env-food",
            "https://github.com/mcphersonlab/amr-env-water",
            "https://github.com/mcphersonlab/tx-cuti",
            "https://github.com/mcphersonlab/DOOR-STEP"
        ]
    },
    {
        "name": "TSHP/GCSHP Annual Seminar",
        "location": "Galveston, TX",
        "lat": 29.3013,
        "lon": -94.7977,
        "start_date": "2026-04-24",
        "end_date": "2026-04-26",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://tshp.org/mpage/as26",
        "projects": [
            "https://github.com/mcphersonlab/tx-staph-bacteremia",
            "https://github.com/mcphersonlab/practice",
            "https://github.com/mcphersonlab/PharmacyEducation",
            "https://github.com/mcphersonlab/tx-cdi",
            "https://github.com/mcphersonlab/tx-cap",
            "https://github.com/mcphersonlab/tx-uuti",
            "https://github.com/mcphersonlab/tx-cuti"
        ]
    },
    {
        "name": "Houston C diff & Microbiome Conference",
        "location": "Houston, TX",
        "lat": 29.7191,
        "lon": -95.3881,
        "start_date": "2026-04-30",
        "end_date": "2026-04-30",
        "abstract_open": "2026-02-14",
        "abstract_close": "2026-03-31",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.uh.edu/pharmacy/news-and-events/events/houston-cdiff-and-microbiome-conference/",
        "projects": [
            "https://github.com/mcphersonlab/mgx-clostridioides-difficile",
            "https://github.com/mcphersonlab/mgx-mbx-abx-cdi",
            "https://github.com/mcphersonlab/clostridioides_atlas",
            "https://github.com/mcphersonlab/mgx-cdi-peds",
            "https://github.com/mcphersonlab/roi-cdi",
            "https://github.com/mcphersonlab/tx-cdi"
        ]
    },
    {
        "name": "MAD-ID (SIDP)",
        "location": "Orlando, Florida",
        "lat": 28.5383,
        "lon": -81.3792,
        "start_date": "2026-05-14",
        "end_date": "2026-05-17",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "See conference website for abstract dates and details",
        "type": "Conference",
        "url": "https://www.mad-id.org/annual-meeting-1",
        "projects": [
            "https://github.com/mcphersonlab/practice",
            "https://github.com/mcphersonlab/tx-staph-bacteremia",
            "https://github.com/mcphersonlab/tx-cdi",
            "https://github.com/mcphersonlab/tx-cap",
            "https://github.com/mcphersonlab/tx-uuti",
            "https://github.com/mcphersonlab/tx-cuti"
        ]
    },
    {
        "name": "ASPET Annual",
        "location": "Minneapolis, MN",
        "lat": 44.9778,
        "lon": -93.265,
        "start_date": "2026-05-17",
        "end_date": "2026-05-20",
        "abstract_open": "2025-09-22",
        "abstract_close": "2025-12-04",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.aspet.org/aspet/meetings-awards",
        "projects": [
            "https://github.com/mcphersonlab/SpaceTime",
            "https://github.com/mcphersonlab/pcol-biofilm-rifamycins",
            "https://github.com/mcphersonlab/structure-function-pharmacology",
            "https://github.com/mcphersonlab/practice"
        ]
    },
    {
        "name": "ISPOR Annual",
        "location": "Philadelphia, PA",
        "lat": 39.9526,
        "lon": -75.1652,
        "start_date": "2026-05-17",
        "end_date": "2026-05-20",
        "abstract_open": "2025-10-31",
        "abstract_close": "2026-01-09",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.ispor.org/conferences-education",
        "projects": [
            "https://github.com/mcphersonlab/roi-pipeline-antimicrobial",
            "https://github.com/mcphersonlab/cost-amr",
            "https://github.com/mcphersonlab/roi-cdi",
            "https://github.com/mcphersonlab/DOOR-STEP",
            "https://github.com/mcphersonlab/epi-hbv"
        ]
    },
    {
        "name": "ASM Microbe",
        "location": "Washington, DC",
        "lat": 38.9072,
        "lon": -77.0369,
        "start_date": "2026-06-11",
        "end_date": "2026-06-15",
        "abstract_open": "2025-10-15",
        "abstract_close": "2026-01-21",
        "abstract_note": "Travel awards: Oct 15 - Dec 2, 2025; Abstracts: Dec 2, 2025 - Jan 21, 2026",
        "type": "Conference",
        "url": "https://asm.org/events/asm-microbe",
        "projects": [
            "https://github.com/mcphersonlab/ai-microbiome-transmission",
            "https://github.com/mcphersonlab/MicroSCOPE",
            "https://github.com/mcphersonlab/amr-env-food",
            "https://github.com/mcphersonlab/amr-env-water",
            "https://github.com/mcphersonlab/env-tx-ocean",
            "https://github.com/mcphersonlab/mgx-cap",
            "https://github.com/mcphersonlab/clostridioides_atlas"
        ]
    },
    {
        "name": "Anaerobe Biennial",
        "location": "New York, NY, USA",
        "lat": 40.7306,
        "lon": -73.9352,
        "start_date": "2026-07-07",
        "end_date": "2026-07-10",
        "abstract_open": "2025-10-23",
        "abstract_close": "2026-02-01",
        "abstract_note": "Oral: Jan 1, 2026; Poster: Feb 1, 2026",
        "type": "Conference",
        "url": "http://www.anaerobe.org/2026/",
        "projects": [
            "https://github.com/mcphersonlab/amr-clostridioides-difficile",
            "https://github.com/mcphersonlab/clostridioides_atlas",
            "https://github.com/mcphersonlab/mgx-clostridioides-difficile",
            "https://github.com/mcphersonlab/mgx-cdi-peds"
        ]
    },
    {
        "name": "IUPHAR Annual",
        "location": "Melbourne, Australia",
        "lat": -37.8136,
        "lon": 144.9631,
        "start_date": "2026-07-12",
        "end_date": "2026-07-17",
        "abstract_open": "2025-02-01",
        "abstract_close": "2025-09-15",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.iuphar.org/",
        "projects": [
            "https://github.com/mcphersonlab/structure-function-pharmacology",
            "https://github.com/mcphersonlab/ai-forecast-pharmacology",
            "https://github.com/mcphersonlab/SpaceTime",
            "https://github.com/mcphersonlab/pcol-biofilm-rifamycins",
            "https://github.com/mcphersonlab/pcol-vcddmde-hbv"
        ]
    },
    {
        "name": "AACP Pharmacy Education",
        "location": "Grapevine, TX",
        "lat": 32.9342,
        "lon": -97.0781,
        "start_date": "2026-07-18",
        "end_date": "2026-07-21",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.aacp.org/events/annual-meetings",
        "projects": [
            "https://github.com/mcphersonlab/PharmacyEducation",
            "https://github.com/mcphersonlab/pharm-comm-ai",
            "https://github.com/mcphersonlab/practice",
            "https://github.com/mcphersonlab/immune-izapp"
        ]
    },
    {
        "name": "Conference on Beneficial Microbes",
        "location": "Madison, WI",
        "lat": 43.0731,
        "lon": -89.4012,
        "start_date": "2026-07-19",
        "end_date": "2026-07-23",
        "abstract_open": "2026-02-01",
        "abstract_close": "2026-04-08",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://conferences.union.wisc.edu/microbes/",
        "projects": [
            "https://github.com/mcphersonlab/MicrobiomeHUES",
            "https://github.com/mcphersonlab/env-mgx-pd",
            "https://github.com/mcphersonlab/abx-iv-mgx-mbx-imm"
        ]
    },
    {
        "name": "ASV Annual",
        "location": "Minneapolis, MN",
        "lat": 44.9778,
        "lon": -93.265,
        "start_date": "2026-07-27",
        "end_date": "2026-07-30",
        "abstract_open": "2025-12-01",
        "abstract_close": "2026-02-01",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.asv.org/annual-meeting",
        "projects": [
            "https://github.com/mcphersonlab/ai-forecast-influenza",
            "https://github.com/mcphersonlab/epi-hbv"
        ]
    },
    {
        "name": "STI Prevention Conference",
        "location": "TBD",
        "lat": 33.749,
        "lon": -84.388,
        "start_date": "2026-09-01",
        "end_date": "2026-09-01",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "2026 dates and location to be announced",
        "type": "Conference",
        "url": "https://stipreventionconference.org/",
        "projects": [
            "https://github.com/mcphersonlab/amr-neisseria-gonorrhoeae",
            "https://github.com/mcphersonlab/amr-hiv",
            "https://github.com/mcphersonlab/epi-hbv"
        ]
    },
    {
        "name": "The 9th International C. difficile Symposium (ICDS)",
        "location": "Bled, Slovenia",
        "lat": 46.3683,
        "lon": 14.1146,
        "start_date": "2026-09-08",
        "end_date": "2026-09-10",
        "abstract_open": "2026-03-10",
        "abstract_close": "2026-05-15",
        "abstract_note": "",
        "type": "Symposium",
        "url": "https://www.icds.si/",
        "projects": [
            "https://github.com/mcphersonlab/tx-cdi",
            "https://github.com/mcphersonlab/roi-cdi",
            "https://github.com/mcphersonlab/clostridioides_atlas",
            "https://github.com/mcphersonlab/mgx-clostridioides-difficile",
            "https://github.com/mcphersonlab/amr-clostridioides-difficile",
            "https://github.com/mcphersonlab/mgx-cdi-peds"
        ]
    },
    {
        "name": "MSGERC Biennial",
        "location": "Denver, CO",
        "lat": 39.7392,
        "lon": -104.9903,
        "start_date": "2026-09-09",
        "end_date": "2026-09-11",
        "abstract_open": "2026-04-01",
        "abstract_close": "2026-07-31",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://msgerc.org/2026-biennial-meeting/",
        "projects": [
            "https://github.com/mcphersonlab/amr-aspergillus-fumigatus",
            "https://github.com/mcphersonlab/amr-lomentospora-prolificans",
            "https://github.com/mcphersonlab/amr-candida-auris"
        ]
    },
    {
        "name": "Rice AI in Health",
        "location": "Houston, TX",
        "lat": 29.7174,
        "lon": -95.4018,
        "start_date": "2026-09-14",
        "end_date": "2026-09-17",
        "abstract_open": "",
        "abstract_close": "",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.aihealthconference.com/",
        "projects": [
            "https://github.com/mcphersonlab/DigitalTwin-Society-Health",
            "https://github.com/mcphersonlab/ai-amr",
            "https://github.com/mcphersonlab/ai-microbiome-transmission",
            "https://github.com/mcphersonlab/pharm-comm-ai"
        ]
    },
    {
        "name": "ESCV Annual",
        "location": "Porto, Portugal",
        "lat": 41.1579,
        "lon": -8.6291,
        "start_date": "2026-09-16",
        "end_date": "2026-09-19",
        "abstract_open": "2026-02-02",
        "abstract_close": "2026-05-11",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://escv.eu/calendar-events/",
        "projects": [
            "https://github.com/mcphersonlab/mgx-virome",
            "https://github.com/mcphersonlab/epi-hbv",
            "https://github.com/mcphersonlab/phys-hiv-lenacapavir"
        ]
    },
    {
        "name": "Global AMR Innovators' Conference (GAMRIC)",
        "location": "Lisbon, Portugal",
        "lat": 38.7223,
        "lon": -9.1393,
        "start_date": "2026-09-22",
        "end_date": "2026-09-24",
        "abstract_open": "2026-03-10",
        "abstract_close": "2026-03-31",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.gamric.org/",
        "projects": [
            "https://github.com/mcphersonlab/cost-amr",
            "https://github.com/mcphersonlab/amr-env-food",
            "https://github.com/mcphersonlab/amr-env-water",
            "https://github.com/mcphersonlab/roi-pipeline-antimicrobial"
        ]
    },
    {
        "name": "North American Cystic Fibrosis (CF) Conference",
        "location": "Atlanta, Georgia",
        "lat": 33.749,
        "lon": -84.388,
        "start_date": "2026-10-07",
        "end_date": "2026-10-10",
        "abstract_open": "2026-03-17",
        "abstract_close": "2026-04-17",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.nacfconference.org/",
        "projects": [
            "https://github.com/mcphersonlab/amr-pseudomonas-aeruginosa",
            "https://github.com/mcphersonlab/MoTrPAC_plus_CF",
            "https://github.com/mcphersonlab/mgx-cap"
        ]
    },
    {
        "name": "IDSA IDWeek",
        "location": "Washington, DC",
        "lat": 38.9072,
        "lon": -77.0369,
        "start_date": "2026-10-21",
        "end_date": "2026-10-24",
        "abstract_open": "2026-02-18",
        "abstract_close": "2026-04-30",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.idweek.org/",
        "projects": [
            "https://github.com/mcphersonlab/tx-cap",
            "https://github.com/mcphersonlab/tx-uuti",
            "https://github.com/mcphersonlab/mgx-cap",
            "https://github.com/mcphersonlab/tx-cuti",
            "https://github.com/mcphersonlab/immune-izapp",
            "https://github.com/mcphersonlab/DOOR-STEP",
            "https://github.com/mcphersonlab/mgx-cdi-vre"
        ]
    },
    {
        "name": "ASHP Midyear",
        "location": "Orlando, FL",
        "lat": 28.4158,
        "lon": -81.2989,
        "start_date": "2026-12-06",
        "end_date": "2026-12-09",
        "abstract_open": "2026-05-30",
        "abstract_close": "2026-10-01",
        "abstract_note": "",
        "type": "Conference",
        "url": "https://www.ashp.org/meetings-and-conferences/midyear-clinical-meeting-and-exhibition",
        "projects": [
            "https://github.com/mcphersonlab/tx-staph-bacteremia",
            "https://github.com/mcphersonlab/practice",
            "https://github.com/mcphersonlab/PharmacyEducation",
            "https://github.com/mcphersonlab/tx-cdi",
            "https://github.com/mcphersonlab/tx-cap",
            "https://github.com/mcphersonlab/tx-uuti",
            "https://github.com/mcphersonlab/tx-cuti"
        ]
    }
]


def normalize_conference_url(url):
    return (url or "").rstrip("/")


def _format_conference_date(date_str, conference_name, field_name):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y")
    except ValueError as exc:
        raise ValueError(
            f"Invalid {field_name} date {date_str!r} for conference {conference_name!r} in research/_conferences_data.py"
        ) from exc


def format_conference_abstract_deadline(conference):
    if conference.get("abstract_open") and conference.get("abstract_close"):
        open_date = _format_conference_date(conference["abstract_open"], conference["name"], "abstract_open")
        close_date = _format_conference_date(conference["abstract_close"], conference["name"], "abstract_close")
        return f"{open_date} - {close_date}"
    if conference.get("abstract_close"):
        return _format_conference_date(conference["abstract_close"], conference["name"], "abstract_close")
    if conference.get("abstract_open"):
        return _format_conference_date(conference["abstract_open"], conference["name"], "abstract_open")
    return "TBD"


conference_abstract_deadlines = {
    normalize_conference_url(conf.get("url", "")): {
        "name": conf["name"],
        "abstract_display": format_conference_abstract_deadline(conf),
    }
    for conf in conferences
    if conf.get("url")
}
