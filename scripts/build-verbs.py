#!/usr/bin/env python3
"""Builds src/data/verbs-data.json with 500 verbs across ~38 situational categories.

Vol I (100 verbs) is preserved exactly as-is; Vols II–V (400 new verbs) are
appended below with hand-written American-IPA pronunciations and Spanish
glosses. Field order matches the schema:  i, ip, sp, p, pi, [pSp], pp, ppi,
[ppSp], g, gi, t, ti
"""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "src" / "data" / "verbs-data.json"


def v(i, ip, sp, p, pi, pp, ppi, g, gi, t, ti, *, pSp=None, ppSp=None):
    """One verb record. pSp/ppSp are speech-overrides for TTS homographs."""
    out = {"i": i, "ip": ip, "sp": sp, "p": p, "pi": pi}
    if pSp is not None:
        out["pSp"] = pSp
    out["pp"] = pp
    out["ppi"] = ppi
    if ppSp is not None:
        out["ppSp"] = ppSp
    out["g"] = g
    out["gi"] = gi
    out["t"] = t
    out["ti"] = ti
    return out


# ----------------------------------------------------------------------------
# VOL II  — 100 verbs, 9 categorías
# ----------------------------------------------------------------------------

vol2 = [
    {"id": "amplio", "name": "Verbos de Uso Amplio", "icon": "◆", "verbs": [
        v("look",     "/lʊk/",         "mirar",                "looked",   "/lʊkt/",       "looked",   "/lʊkt/",       "looking",   "/ˈlʊkɪŋ/",     "looks",    "/lʊks/"),
        v("use",      "/juːz/",        "usar",                 "used",     "/juːzd/",      "used",     "/juːzd/",      "using",     "/ˈjuːzɪŋ/",    "uses",     "/ˈjuːzɪz/"),
        v("become",   "/bɪˈkʌm/",      "convertirse / volverse","became",  "/bɪˈkeɪm/",    "become",   "/bɪˈkʌm/",     "becoming",  "/bɪˈkʌmɪŋ/",   "becomes",  "/bɪˈkʌmz/"),
        v("seem",     "/siːm/",        "parecer",              "seemed",   "/siːmd/",      "seemed",   "/siːmd/",      "seeming",   "/ˈsiːmɪŋ/",    "seems",    "/siːmz/"),
        v("begin",    "/bɪˈɡɪn/",      "empezar / comenzar",   "began",    "/bɪˈɡæn/",     "begun",    "/bɪˈɡʌn/",     "beginning", "/bɪˈɡɪnɪŋ/",   "begins",   "/bɪˈɡɪnz/"),
        v("show",     "/ʃoʊ/",         "mostrar",              "showed",   "/ʃoʊd/",       "shown",    "/ʃoʊn/",       "showing",   "/ˈʃoʊɪŋ/",     "shows",    "/ʃoʊz/"),
        v("happen",   "/ˈhæpən/",      "suceder / ocurrir",    "happened", "/ˈhæpənd/",    "happened", "/ˈhæpənd/",    "happening", "/ˈhæpənɪŋ/",   "happens",  "/ˈhæpənz/"),
        v("provide",  "/prəˈvaɪd/",    "proveer / brindar",    "provided", "/prəˈvaɪdɪd/", "provided", "/prəˈvaɪdɪd/", "providing", "/prəˈvaɪdɪŋ/", "provides", "/prəˈvaɪdz/"),
        v("include",  "/ɪnˈkluːd/",    "incluir",              "included", "/ɪnˈkluːdɪd/", "included", "/ɪnˈkluːdɪd/", "including", "/ɪnˈkluːdɪŋ/", "includes", "/ɪnˈkluːdz/"),
        v("continue", "/kənˈtɪnjuː/",  "continuar",            "continued","/kənˈtɪnjuːd/","continued","/kənˈtɪnjuːd/","continuing","/kənˈtɪnjuːɪŋ/","continues","/kənˈtɪnjuːz/"),
        v("change",   "/tʃeɪndʒ/",     "cambiar",              "changed",  "/tʃeɪndʒd/",   "changed",  "/tʃeɪndʒd/",   "changing",  "/ˈtʃeɪndʒɪŋ/", "changes",  "/ˈtʃeɪndʒɪz/"),
        v("stop",     "/stɒp/",        "parar / detener",      "stopped",  "/stɒpt/",      "stopped",  "/stɒpt/",      "stopping",  "/ˈstɒpɪŋ/",    "stops",    "/stɒps/"),
        v("create",   "/kriˈeɪt/",     "crear",                "created",  "/kriˈeɪtɪd/",  "created",  "/kriˈeɪtɪd/",  "creating",  "/kriˈeɪtɪŋ/",  "creates",  "/kriˈeɪts/"),
        v("add",      "/æd/",          "agregar / añadir",     "added",    "/ˈædɪd/",      "added",    "/ˈædɪd/",      "adding",    "/ˈædɪŋ/",      "adds",     "/ædz/"),
        v("watch",    "/wɒtʃ/",        "ver / observar",       "watched",  "/wɒtʃt/",      "watched",  "/wɒtʃt/",      "watching",  "/ˈwɒtʃɪŋ/",    "watches",  "/ˈwɒtʃɪz/"),
    ]},
    {"id": "negocios", "name": "Negocios y Dinero", "icon": "$", "verbs": [
        v("buy",      "/baɪ/",         "comprar",              "bought",   "/bɔːt/",       "bought",   "/bɔːt/",       "buying",    "/ˈbaɪɪŋ/",     "buys",     "/baɪz/"),
        v("sell",     "/sɛl/",         "vender",               "sold",     "/soʊld/",      "sold",     "/soʊld/",      "selling",   "/ˈsɛlɪŋ/",     "sells",    "/sɛlz/"),
        v("pay",      "/peɪ/",         "pagar",                "paid",     "/peɪd/",       "paid",     "/peɪd/",       "paying",    "/ˈpeɪɪŋ/",     "pays",     "/peɪz/"),
        v("earn",     "/ɜːrn/",        "ganar (dinero)",       "earned",   "/ɜːrnd/",      "earned",   "/ɜːrnd/",      "earning",   "/ˈɜːrnɪŋ/",    "earns",    "/ɜːrnz/"),
        v("spend",    "/spɛnd/",       "gastar",               "spent",    "/spɛnt/",      "spent",    "/spɛnt/",      "spending",  "/ˈspɛndɪŋ/",   "spends",   "/spɛndz/"),
        v("save",     "/seɪv/",        "ahorrar / guardar",    "saved",    "/seɪvd/",      "saved",    "/seɪvd/",      "saving",    "/ˈseɪvɪŋ/",    "saves",    "/seɪvz/"),
        v("cost",     "/kɒst/",        "costar",               "cost",     "/kɒst/",       "cost",     "/kɒst/",       "costing",   "/ˈkɒstɪŋ/",    "costs",    "/kɒsts/"),
        v("owe",      "/oʊ/",          "deber (dinero)",       "owed",     "/oʊd/",        "owed",     "/oʊd/",        "owing",     "/ˈoʊɪŋ/",      "owes",     "/oʊz/"),
        v("borrow",   "/ˈbɒroʊ/",      "pedir prestado",       "borrowed", "/ˈbɒroʊd/",    "borrowed", "/ˈbɒroʊd/",    "borrowing", "/ˈbɒroʊɪŋ/",   "borrows",  "/ˈbɒroʊz/"),
        v("lend",     "/lɛnd/",        "prestar",              "lent",     "/lɛnt/",       "lent",     "/lɛnt/",       "lending",   "/ˈlɛndɪŋ/",    "lends",    "/lɛndz/"),
        v("afford",   "/əˈfɔːrd/",     "permitirse",           "afforded", "/əˈfɔːrdɪd/",  "afforded", "/əˈfɔːrdɪd/",  "affording", "/əˈfɔːrdɪŋ/",  "affords",  "/əˈfɔːrdz/"),
        v("invest",   "/ɪnˈvɛst/",     "invertir",             "invested", "/ɪnˈvɛstɪd/",  "invested", "/ɪnˈvɛstɪd/",  "investing", "/ɪnˈvɛstɪŋ/",  "invests",  "/ɪnˈvɛsts/"),
    ]},
    {"id": "salud", "name": "Salud y Cuerpo", "icon": "✚", "verbs": [
        v("breathe",  "/briːð/",       "respirar",             "breathed", "/briːðd/",     "breathed", "/briːðd/",     "breathing", "/ˈbriːðɪŋ/",   "breathes", "/briːðz/"),
        v("exercise", "/ˈɛksərsaɪz/",  "ejercitarse",          "exercised","/ˈɛksərsaɪzd/","exercised","/ˈɛksərsaɪzd/","exercising","/ˈɛksərsaɪzɪŋ/","exercises","/ˈɛksərsaɪzɪz/"),
        v("rest",     "/rɛst/",        "descansar",            "rested",   "/ˈrɛstɪd/",    "rested",   "/ˈrɛstɪd/",    "resting",   "/ˈrɛstɪŋ/",    "rests",    "/rɛsts/"),
        v("recover",  "/rɪˈkʌvər/",    "recuperarse",          "recovered","/rɪˈkʌvərd/",  "recovered","/rɪˈkʌvərd/",  "recovering","/rɪˈkʌvərɪŋ/", "recovers", "/rɪˈkʌvərz/"),
        v("hurt",     "/hɜːrt/",       "doler / lastimar",     "hurt",     "/hɜːrt/",      "hurt",     "/hɜːrt/",      "hurting",   "/ˈhɜːrtɪŋ/",   "hurts",    "/hɜːrts/"),
        v("heal",     "/hiːl/",        "sanar / curar",        "healed",   "/hiːld/",      "healed",   "/hiːld/",      "healing",   "/ˈhiːlɪŋ/",    "heals",    "/hiːlz/"),
        v("suffer",   "/ˈsʌfər/",      "sufrir",               "suffered", "/ˈsʌfərd/",    "suffered", "/ˈsʌfərd/",    "suffering", "/ˈsʌfərɪŋ/",   "suffers",  "/ˈsʌfərz/"),
        v("die",      "/daɪ/",         "morir",                "died",     "/daɪd/",       "died",     "/daɪd/",       "dying",     "/ˈdaɪɪŋ/",     "dies",     "/daɪz/"),
        v("cough",    "/kɒf/",         "toser",                "coughed",  "/kɒft/",       "coughed",  "/kɒft/",       "coughing",  "/ˈkɒfɪŋ/",     "coughs",   "/kɒfs/"),
        v("swallow",  "/ˈswɒloʊ/",     "tragar",               "swallowed","/ˈswɒloʊd/",   "swallowed","/ˈswɒloʊd/",   "swallowing","/ˈswɒloʊɪŋ/",  "swallows", "/ˈswɒloʊz/"),
        v("relax",    "/rɪˈlæks/",     "relajarse",            "relaxed",  "/rɪˈlækst/",   "relaxed",  "/rɪˈlækst/",   "relaxing",  "/rɪˈlæksɪŋ/",  "relaxes",  "/rɪˈlæksɪz/"),
        v("wake",     "/weɪk/",        "despertar",            "woke",     "/woʊk/",       "woken",    "/ˈwoʊkən/",    "waking",    "/ˈweɪkɪŋ/",    "wakes",    "/weɪks/"),
    ]},
    {"id": "cocina-comida", "name": "Cocina y Comida", "icon": "♨", "verbs": [
        v("boil",     "/bɔɪl/",        "hervir",               "boiled",   "/bɔɪld/",      "boiled",   "/bɔɪld/",      "boiling",   "/ˈbɔɪlɪŋ/",    "boils",    "/bɔɪlz/"),
        v("fry",      "/fraɪ/",        "freír",                "fried",    "/fraɪd/",      "fried",    "/fraɪd/",      "frying",    "/ˈfraɪɪŋ/",    "fries",    "/fraɪz/"),
        v("bake",     "/beɪk/",        "hornear",              "baked",    "/beɪkt/",      "baked",    "/beɪkt/",      "baking",    "/ˈbeɪkɪŋ/",    "bakes",    "/beɪks/"),
        v("mix",      "/mɪks/",        "mezclar",              "mixed",    "/mɪkst/",      "mixed",    "/mɪkst/",      "mixing",    "/ˈmɪksɪŋ/",    "mixes",    "/ˈmɪksɪz/"),
        v("stir",     "/stɜːr/",       "remover / revolver",   "stirred",  "/stɜːrd/",     "stirred",  "/stɜːrd/",     "stirring",  "/ˈstɜːrɪŋ/",   "stirs",    "/stɜːrz/"),
        v("pour",     "/pɔːr/",        "verter / servir",      "poured",   "/pɔːrd/",      "poured",   "/pɔːrd/",      "pouring",   "/ˈpɔːrɪŋ/",    "pours",    "/pɔːrz/"),
        v("slice",    "/slaɪs/",       "rebanar",              "sliced",   "/slaɪst/",     "sliced",   "/slaɪst/",     "slicing",   "/ˈslaɪsɪŋ/",   "slices",   "/ˈslaɪsɪz/"),
        v("peel",     "/piːl/",        "pelar",                "peeled",   "/piːld/",      "peeled",   "/piːld/",      "peeling",   "/ˈpiːlɪŋ/",    "peels",    "/piːlz/"),
        v("serve",    "/sɜːrv/",       "servir",               "served",   "/sɜːrvd/",     "served",   "/sɜːrvd/",     "serving",   "/ˈsɜːrvɪŋ/",   "serves",   "/sɜːrvz/"),
        v("taste",    "/teɪst/",       "probar / saborear",    "tasted",   "/ˈteɪstɪd/",   "tasted",   "/ˈteɪstɪd/",   "tasting",   "/ˈteɪstɪŋ/",   "tastes",   "/teɪsts/"),
    ]},
    {"id": "tecnologia", "name": "Tecnología", "icon": "⌨", "verbs": [
        v("click",    "/klɪk/",        "hacer clic",           "clicked",  "/klɪkt/",      "clicked",  "/klɪkt/",      "clicking",  "/ˈklɪkɪŋ/",    "clicks",   "/klɪks/"),
        v("type",     "/taɪp/",        "teclear",              "typed",    "/taɪpt/",      "typed",    "/taɪpt/",      "typing",    "/ˈtaɪpɪŋ/",    "types",    "/taɪps/"),
        v("download", "/ˈdaʊnloʊd/",   "descargar",            "downloaded","/ˈdaʊnloʊdɪd/","downloaded","/ˈdaʊnloʊdɪd/","downloading","/ˈdaʊnloʊdɪŋ/","downloads","/ˈdaʊnloʊdz/"),
        v("upload",   "/ˈʌploʊd/",     "subir (archivo)",      "uploaded", "/ˈʌploʊdɪd/",  "uploaded", "/ˈʌploʊdɪd/",  "uploading", "/ˈʌploʊdɪŋ/",  "uploads",  "/ˈʌploʊdz/"),
        v("install",  "/ɪnˈstɔːl/",    "instalar",             "installed","/ɪnˈstɔːld/",  "installed","/ɪnˈstɔːld/",  "installing","/ɪnˈstɔːlɪŋ/", "installs", "/ɪnˈstɔːlz/"),
        v("update",   "/ʌpˈdeɪt/",     "actualizar",           "updated",  "/ʌpˈdeɪtɪd/",  "updated",  "/ʌpˈdeɪtɪd/",  "updating",  "/ʌpˈdeɪtɪŋ/",  "updates",  "/ʌpˈdeɪts/"),
        v("delete",   "/dɪˈliːt/",     "eliminar / borrar",    "deleted",  "/dɪˈliːtɪd/",  "deleted",  "/dɪˈliːtɪd/",  "deleting",  "/dɪˈliːtɪŋ/",  "deletes",  "/dɪˈliːts/"),
        v("search",   "/sɜːrtʃ/",      "buscar",               "searched", "/sɜːrtʃt/",    "searched", "/sɜːrtʃt/",    "searching", "/ˈsɜːrtʃɪŋ/",  "searches", "/ˈsɜːrtʃɪz/"),
        v("connect",  "/kəˈnɛkt/",     "conectar",             "connected","/kəˈnɛktɪd/",  "connected","/kəˈnɛktɪd/",  "connecting","/kəˈnɛktɪŋ/",  "connects", "/kəˈnɛkts/"),
        v("share",    "/ʃɛər/",        "compartir",            "shared",   "/ʃɛərd/",      "shared",   "/ʃɛərd/",      "sharing",   "/ˈʃɛərɪŋ/",    "shares",   "/ʃɛərz/"),
    ]},
    {"id": "relaciones", "name": "Relaciones y Sociedad", "icon": "♥", "verbs": [
        v("marry",    "/ˈmæri/",       "casarse",              "married",  "/ˈmærid/",     "married",  "/ˈmærid/",     "marrying",  "/ˈmæriɪŋ/",    "marries",  "/ˈmæriz/"),
        v("hug",      "/hʌɡ/",         "abrazar",              "hugged",   "/hʌɡd/",       "hugged",   "/hʌɡd/",       "hugging",   "/ˈhʌɡɪŋ/",     "hugs",     "/hʌɡz/"),
        v("kiss",     "/kɪs/",         "besar",                "kissed",   "/kɪst/",       "kissed",   "/kɪst/",       "kissing",   "/ˈkɪsɪŋ/",     "kisses",   "/ˈkɪsɪz/"),
        v("fight",    "/faɪt/",        "pelear",               "fought",   "/fɔːt/",       "fought",   "/fɔːt/",       "fighting",  "/ˈfaɪtɪŋ/",    "fights",   "/faɪts/"),
        v("argue",    "/ˈɑːrɡjuː/",    "discutir",             "argued",   "/ˈɑːrɡjuːd/",  "argued",   "/ˈɑːrɡjuːd/",  "arguing",   "/ˈɑːrɡjuːɪŋ/", "argues",   "/ˈɑːrɡjuːz/"),
        v("forgive",  "/fərˈɡɪv/",     "perdonar",             "forgave",  "/fərˈɡeɪv/",   "forgiven", "/fərˈɡɪvən/",  "forgiving", "/fərˈɡɪvɪŋ/",  "forgives", "/fərˈɡɪvz/"),
        v("trust",    "/trʌst/",       "confiar",              "trusted",  "/ˈtrʌstɪd/",   "trusted",  "/ˈtrʌstɪd/",   "trusting",  "/ˈtrʌstɪŋ/",   "trusts",   "/trʌsts/"),
        v("promise",  "/ˈprɒmɪs/",     "prometer",             "promised", "/ˈprɒmɪst/",   "promised", "/ˈprɒmɪst/",   "promising", "/ˈprɒmɪsɪŋ/",  "promises", "/ˈprɒmɪsɪz/"),
        v("introduce","/ɪntrəˈdjuːs/", "presentar (a alguien)","introduced","/ɪntrəˈdjuːst/","introduced","/ɪntrəˈdjuːst/","introducing","/ɪntrəˈdjuːsɪŋ/","introduces","/ɪntrəˈdjuːsɪz/"),
        v("thank",    "/θæŋk/",        "agradecer",            "thanked",  "/θæŋkt/",      "thanked",  "/θæŋkt/",      "thanking",  "/ˈθæŋkɪŋ/",    "thanks",   "/θæŋks/"),
        v("apologize","/əˈpɒlədʒaɪz/", "disculparse",          "apologized","/əˈpɒlədʒaɪzd/","apologized","/əˈpɒlədʒaɪzd/","apologizing","/əˈpɒlədʒaɪzɪŋ/","apologizes","/əˈpɒlədʒaɪzɪz/"),
        v("invite",   "/ɪnˈvaɪt/",     "invitar",              "invited",  "/ɪnˈvaɪtɪd/",  "invited",  "/ɪnˈvaɪtɪd/",  "inviting",  "/ɪnˈvaɪtɪŋ/",  "invites",  "/ɪnˈvaɪts/"),
        v("visit",    "/ˈvɪzɪt/",      "visitar",              "visited",  "/ˈvɪzɪtɪd/",   "visited",  "/ˈvɪzɪtɪd/",   "visiting",  "/ˈvɪzɪtɪŋ/",   "visits",   "/ˈvɪzɪts/"),
    ]},
    {"id": "deportes", "name": "Deportes y Ocio", "icon": "♪", "verbs": [
        v("play",     "/pleɪ/",        "jugar / tocar",        "played",   "/pleɪd/",      "played",   "/pleɪd/",      "playing",   "/ˈpleɪɪŋ/",    "plays",    "/pleɪz/"),
        v("win",      "/wɪn/",         "ganar (juego)",        "won",      "/wʌn/",        "won",      "/wʌn/",        "winning",   "/ˈwɪnɪŋ/",     "wins",     "/wɪnz/"),
        v("compete",  "/kəmˈpiːt/",    "competir",             "competed", "/kəmˈpiːtɪd/", "competed", "/kəmˈpiːtɪd/", "competing", "/kəmˈpiːtɪŋ/", "competes", "/kəmˈpiːts/"),
        v("train",    "/treɪn/",       "entrenar",             "trained",  "/treɪnd/",     "trained",  "/treɪnd/",     "training",  "/ˈtreɪnɪŋ/",   "trains",   "/treɪnz/"),
        v("dance",    "/dæns/",        "bailar",               "danced",   "/dænst/",      "danced",   "/dænst/",      "dancing",   "/ˈdænsɪŋ/",    "dances",   "/ˈdænsɪz/"),
        v("sing",     "/sɪŋ/",         "cantar",               "sang",     "/sæŋ/",        "sung",     "/sʌŋ/",        "singing",   "/ˈsɪŋɪŋ/",     "sings",    "/sɪŋz/"),
        v("draw",     "/drɔː/",        "dibujar",              "drew",     "/druː/",       "drawn",    "/drɔːn/",      "drawing",   "/ˈdrɔːɪŋ/",    "draws",    "/drɔːz/"),
        v("paint",    "/peɪnt/",       "pintar",               "painted",  "/ˈpeɪntɪd/",   "painted",  "/ˈpeɪntɪd/",   "painting",  "/ˈpeɪntɪŋ/",   "paints",   "/peɪnts/"),
        v("swim",     "/swɪm/",        "nadar",                "swam",     "/swæm/",       "swum",     "/swʌm/",       "swimming",  "/ˈswɪmɪŋ/",    "swims",    "/swɪmz/"),
        v("ride",     "/raɪd/",        "montar / cabalgar",    "rode",     "/roʊd/",       "ridden",   "/ˈrɪdən/",     "riding",    "/ˈraɪdɪŋ/",    "rides",    "/raɪdz/"),
        v("jump",     "/dʒʌmp/",       "saltar",               "jumped",   "/dʒʌmpt/",     "jumped",   "/dʒʌmpt/",     "jumping",   "/ˈdʒʌmpɪŋ/",   "jumps",    "/dʒʌmps/"),
        v("climb",    "/klaɪm/",       "escalar / trepar",     "climbed",  "/klaɪmd/",     "climbed",  "/klaɪmd/",     "climbing",  "/ˈklaɪmɪŋ/",   "climbs",   "/klaɪmz/"),
    ]},
    {"id": "naturaleza", "name": "Naturaleza y Clima", "icon": "❀", "verbs": [
        v("rain",     "/reɪn/",        "llover",               "rained",   "/reɪnd/",      "rained",   "/reɪnd/",      "raining",   "/ˈreɪnɪŋ/",    "rains",    "/reɪnz/"),
        v("snow",     "/snoʊ/",        "nevar",                "snowed",   "/snoʊd/",      "snowed",   "/snoʊd/",      "snowing",   "/ˈsnoʊɪŋ/",    "snows",    "/snoʊz/"),
        v("shine",    "/ʃaɪn/",        "brillar",              "shone",    "/ʃoʊn/",       "shone",    "/ʃoʊn/",       "shining",   "/ˈʃaɪnɪŋ/",    "shines",   "/ʃaɪnz/"),
        v("grow",     "/ɡroʊ/",        "crecer / cultivar",    "grew",     "/ɡruː/",       "grown",    "/ɡroʊn/",      "growing",   "/ˈɡroʊɪŋ/",    "grows",    "/ɡroʊz/"),
        v("freeze",   "/friːz/",       "congelar",             "froze",    "/froʊz/",      "frozen",   "/ˈfroʊzən/",   "freezing",  "/ˈfriːzɪŋ/",   "freezes",  "/ˈfriːzɪz/"),
        v("melt",     "/mɛlt/",        "derretir",             "melted",   "/ˈmɛltɪd/",    "melted",   "/ˈmɛltɪd/",    "melting",   "/ˈmɛltɪŋ/",    "melts",    "/mɛlts/"),
        v("blow",     "/bloʊ/",        "soplar",               "blew",     "/bluː/",       "blown",    "/bloʊn/",      "blowing",   "/ˈbloʊɪŋ/",    "blows",    "/bloʊz/"),
    ]},
    {"id": "reparacion", "name": "Reparación y Construcción", "icon": "⚒", "verbs": [
        v("fix",      "/fɪks/",        "arreglar",             "fixed",    "/fɪkst/",      "fixed",    "/fɪkst/",      "fixing",    "/ˈfɪksɪŋ/",    "fixes",    "/ˈfɪksɪz/"),
        v("repair",   "/rɪˈpɛər/",     "reparar",              "repaired", "/rɪˈpɛərd/",   "repaired", "/rɪˈpɛərd/",   "repairing", "/rɪˈpɛərɪŋ/",  "repairs",  "/rɪˈpɛərz/"),
        v("replace",  "/rɪˈpleɪs/",    "reemplazar",           "replaced", "/rɪˈpleɪst/",  "replaced", "/rɪˈpleɪst/",  "replacing", "/rɪˈpleɪsɪŋ/", "replaces", "/rɪˈpleɪsɪz/"),
        v("design",   "/dɪˈzaɪn/",     "diseñar",              "designed", "/dɪˈzaɪnd/",   "designed", "/dɪˈzaɪnd/",   "designing", "/dɪˈzaɪnɪŋ/",  "designs",  "/dɪˈzaɪnz/"),
        v("measure",  "/ˈmɛʒər/",      "medir",                "measured", "/ˈmɛʒərd/",    "measured", "/ˈmɛʒərd/",    "measuring", "/ˈmɛʒərɪŋ/",   "measures", "/ˈmɛʒərz/"),
        v("check",    "/tʃɛk/",        "revisar / verificar",  "checked",  "/tʃɛkt/",      "checked",  "/tʃɛkt/",      "checking",  "/ˈtʃɛkɪŋ/",    "checks",   "/tʃɛks/"),
        v("test",     "/tɛst/",        "probar / poner a prueba","tested", "/ˈtɛstɪd/",    "tested",   "/ˈtɛstɪd/",    "testing",   "/ˈtɛstɪŋ/",    "tests",    "/tɛsts/"),
        v("adjust",   "/əˈdʒʌst/",     "ajustar",              "adjusted", "/əˈdʒʌstɪd/",  "adjusted", "/əˈdʒʌstɪd/",  "adjusting", "/əˈdʒʌstɪŋ/",  "adjusts",  "/əˈdʒʌsts/"),
        v("assemble", "/əˈsɛmbəl/",    "ensamblar / armar",    "assembled","/əˈsɛmbəld/",  "assembled","/əˈsɛmbəld/",  "assembling","/əˈsɛmbəlɪŋ/", "assembles","/əˈsɛmbəlz/"),
    ]},
]


# ----------------------------------------------------------------------------
# VOL III  — 100 verbs, 10 categorías
# ----------------------------------------------------------------------------

vol3 = [
    {"id": "estudios-academia", "name": "Estudios y Academia", "icon": "✎", "verbs": [
        v("research", "/rɪˈsɜːrtʃ/",   "investigar",           "researched","/rɪˈsɜːrtʃt/", "researched","/rɪˈsɜːrtʃt/","researching","/rɪˈsɜːrtʃɪŋ/","researches","/rɪˈsɜːrtʃɪz/"),
        v("analyze",  "/ˈænəlaɪz/",    "analizar",             "analyzed", "/ˈænəlaɪzd/",  "analyzed", "/ˈænəlaɪzd/",  "analyzing", "/ˈænəlaɪzɪŋ/", "analyzes", "/ˈænəlaɪzɪz/"),
        v("summarize","/ˈsʌməraɪz/",   "resumir",              "summarized","/ˈsʌməraɪzd/", "summarized","/ˈsʌməraɪzd/","summarizing","/ˈsʌməraɪzɪŋ/","summarizes","/ˈsʌməraɪzɪz/"),
        v("memorize", "/ˈmɛməraɪz/",   "memorizar",            "memorized","/ˈmɛməraɪzd/", "memorized","/ˈmɛməraɪzd/", "memorizing","/ˈmɛməraɪzɪŋ/","memorizes","/ˈmɛməraɪzɪz/"),
        v("review",   "/rɪˈvjuː/",     "repasar / reseñar",    "reviewed", "/rɪˈvjuːd/",   "reviewed", "/rɪˈvjuːd/",   "reviewing", "/rɪˈvjuːɪŋ/",  "reviews",  "/rɪˈvjuːz/"),
        v("translate","/trænzˈleɪt/",  "traducir",             "translated","/trænzˈleɪtɪd/","translated","/trænzˈleɪtɪd/","translating","/trænzˈleɪtɪŋ/","translates","/trænzˈleɪts/"),
        v("define",   "/dɪˈfaɪn/",     "definir",              "defined",  "/dɪˈfaɪnd/",   "defined",  "/dɪˈfaɪnd/",   "defining",  "/dɪˈfaɪnɪŋ/",  "defines",  "/dɪˈfaɪnz/"),
        v("debate",   "/dɪˈbeɪt/",     "debatir",              "debated",  "/dɪˈbeɪtɪd/",  "debated",  "/dɪˈbeɪtɪd/",  "debating",  "/dɪˈbeɪtɪŋ/",  "debates",  "/dɪˈbeɪts/"),
        v("present",  "/prɪˈzɛnt/",    "presentar (exponer)",  "presented","/prɪˈzɛntɪd/", "presented","/prɪˈzɛntɪd/", "presenting","/prɪˈzɛntɪŋ/", "presents", "/prɪˈzɛnts/"),
        v("graduate", "/ˈɡrædʒueɪt/",  "graduarse",            "graduated","/ˈɡrædʒueɪtɪd/","graduated","/ˈɡrædʒueɪtɪd/","graduating","/ˈɡrædʒueɪtɪŋ/","graduates","/ˈɡrædʒueɪts/"),
        v("cite",     "/saɪt/",        "citar (fuente)",       "cited",    "/ˈsaɪtɪd/",    "cited",    "/ˈsaɪtɪd/",    "citing",    "/ˈsaɪtɪŋ/",    "cites",    "/saɪts/"),
        v("quote",    "/kwoʊt/",       "citar (palabras)",     "quoted",   "/ˈkwoʊtɪd/",   "quoted",   "/ˈkwoʊtɪd/",   "quoting",   "/ˈkwoʊtɪŋ/",   "quotes",   "/kwoʊts/"),
    ]},
    {"id": "transporte", "name": "Transporte y Conducción", "icon": "⇆", "verbs": [
        v("park",     "/pɑːrk/",       "estacionar",           "parked",   "/pɑːrkt/",     "parked",   "/pɑːrkt/",     "parking",   "/ˈpɑːrkɪŋ/",   "parks",    "/pɑːrks/"),
        v("brake",    "/breɪk/",       "frenar",               "braked",   "/breɪkt/",     "braked",   "/breɪkt/",     "braking",   "/ˈbreɪkɪŋ/",   "brakes",   "/breɪks/"),
        v("accelerate","/əkˈsɛləreɪt/","acelerar",             "accelerated","/əkˈsɛləreɪtɪd/","accelerated","/əkˈsɛləreɪtɪd/","accelerating","/əkˈsɛləreɪtɪŋ/","accelerates","/əkˈsɛləreɪts/"),
        v("steer",    "/stɪər/",       "conducir / dirigir",   "steered",  "/stɪərd/",     "steered",  "/stɪərd/",     "steering",  "/ˈstɪərɪŋ/",   "steers",   "/stɪərz/"),
        v("refuel",   "/riːˈfjuːəl/",  "recargar combustible", "refueled", "/riːˈfjuːəld/","refueled", "/riːˈfjuːəld/","refueling", "/riːˈfjuːəlɪŋ/","refuels",  "/riːˈfjuːəlz/"),
        v("board",    "/bɔːrd/",       "abordar",              "boarded",  "/ˈbɔːrdɪd/",   "boarded",  "/ˈbɔːrdɪd/",   "boarding",  "/ˈbɔːrdɪŋ/",   "boards",   "/bɔːrdz/"),
        v("depart",   "/dɪˈpɑːrt/",    "partir / salir",       "departed", "/dɪˈpɑːrtɪd/", "departed", "/dɪˈpɑːrtɪd/", "departing", "/dɪˈpɑːrtɪŋ/", "departs",  "/dɪˈpɑːrts/"),
        v("navigate", "/ˈnævɪɡeɪt/",   "navegar / orientarse", "navigated","/ˈnævɪɡeɪtɪd/","navigated","/ˈnævɪɡeɪtɪd/","navigating","/ˈnævɪɡeɪtɪŋ/","navigates","/ˈnævɪɡeɪts/"),
        v("transport","/trænˈspɔːrt/", "transportar",          "transported","/trænˈspɔːrtɪd/","transported","/trænˈspɔːrtɪd/","transporting","/trænˈspɔːrtɪŋ/","transports","/trænˈspɔːrts/"),
        v("ship",     "/ʃɪp/",         "enviar / despachar",   "shipped",  "/ʃɪpt/",       "shipped",  "/ʃɪpt/",       "shipping",  "/ˈʃɪpɪŋ/",     "ships",    "/ʃɪps/"),
    ]},
    {"id": "moda-vestir", "name": "Moda y Vestimenta", "icon": "✂", "verbs": [
        v("wear",     "/wɛər/",        "llevar puesto",        "wore",     "/wɔːr/",       "worn",     "/wɔːrn/",      "wearing",   "/ˈwɛərɪŋ/",    "wears",    "/wɛərz/"),
        v("dress",    "/drɛs/",        "vestir(se)",           "dressed",  "/drɛst/",      "dressed",  "/drɛst/",      "dressing",  "/ˈdrɛsɪŋ/",    "dresses",  "/ˈdrɛsɪz/"),
        v("button",   "/ˈbʌtən/",      "abotonar",             "buttoned", "/ˈbʌtənd/",    "buttoned", "/ˈbʌtənd/",    "buttoning", "/ˈbʌtənɪŋ/",   "buttons",  "/ˈbʌtənz/"),
        v("zip",      "/zɪp/",         "subir cremallera",     "zipped",   "/zɪpt/",       "zipped",   "/zɪpt/",       "zipping",   "/ˈzɪpɪŋ/",     "zips",     "/zɪps/"),
        v("fold",     "/foʊld/",       "doblar",               "folded",   "/ˈfoʊldɪd/",   "folded",   "/ˈfoʊldɪd/",   "folding",   "/ˈfoʊldɪŋ/",   "folds",    "/foʊldz/"),
        v("iron",     "/ˈaɪərn/",      "planchar",             "ironed",   "/ˈaɪərnd/",    "ironed",   "/ˈaɪərnd/",    "ironing",   "/ˈaɪərnɪŋ/",   "irons",    "/ˈaɪərnz/"),
        v("sew",      "/soʊ/",         "coser",                "sewed",    "/soʊd/",       "sewn",     "/soʊn/",       "sewing",    "/ˈsoʊɪŋ/",     "sews",     "/soʊz/"),
        v("knit",     "/nɪt/",         "tejer",                "knitted",  "/ˈnɪtɪd/",     "knitted",  "/ˈnɪtɪd/",     "knitting",  "/ˈnɪtɪŋ/",     "knits",    "/nɪts/"),
        v("comb",     "/koʊm/",        "peinar",               "combed",   "/koʊmd/",      "combed",   "/koʊmd/",      "combing",   "/ˈkoʊmɪŋ/",    "combs",    "/koʊmz/"),
        v("brush",    "/brʌʃ/",        "cepillar",             "brushed",  "/brʌʃt/",      "brushed",  "/brʌʃt/",      "brushing",  "/ˈbrʌʃɪŋ/",    "brushes",  "/ˈbrʌʃɪz/"),
    ]},
    {"id": "arte-musica", "name": "Arte y Música", "icon": "♬", "verbs": [
        v("perform",  "/pərˈfɔːrm/",   "actuar / interpretar", "performed","/pərˈfɔːrmd/", "performed","/pərˈfɔːrmd/", "performing","/pərˈfɔːrmɪŋ/","performs", "/pərˈfɔːrmz/"),
        v("compose",  "/kəmˈpoʊz/",    "componer",             "composed", "/kəmˈpoʊzd/",  "composed", "/kəmˈpoʊzd/",  "composing", "/kəmˈpoʊzɪŋ/", "composes", "/kəmˈpoʊzɪz/"),
        v("record",   "/rɪˈkɔːrd/",    "grabar",               "recorded", "/rɪˈkɔːrdɪd/", "recorded", "/rɪˈkɔːrdɪd/", "recording", "/rɪˈkɔːrdɪŋ/", "records",  "/rɪˈkɔːrdz/"),
        v("conduct",  "/kənˈdʌkt/",    "dirigir (orquesta)",   "conducted","/kənˈdʌktɪd/", "conducted","/kənˈdʌktɪd/", "conducting","/kənˈdʌktɪŋ/", "conducts", "/kənˈdʌkts/"),
        v("sketch",   "/skɛtʃ/",       "esbozar / bocetar",    "sketched", "/skɛtʃt/",     "sketched", "/skɛtʃt/",     "sketching", "/ˈskɛtʃɪŋ/",   "sketches", "/ˈskɛtʃɪz/"),
        v("illustrate","/ˈɪləstreɪt/", "ilustrar",             "illustrated","/ˈɪləstreɪtɪd/","illustrated","/ˈɪləstreɪtɪd/","illustrating","/ˈɪləstreɪtɪŋ/","illustrates","/ˈɪləstreɪts/"),
        v("sculpt",   "/skʌlpt/",      "esculpir",             "sculpted", "/ˈskʌlptɪd/",  "sculpted", "/ˈskʌlptɪd/",  "sculpting", "/ˈskʌlptɪŋ/",  "sculpts",  "/skʌlpts/"),
        v("photograph","/ˈfoʊtəɡræf/", "fotografiar",          "photographed","/ˈfoʊtəɡræft/","photographed","/ˈfoʊtəɡræft/","photographing","/ˈfoʊtəɡræfɪŋ/","photographs","/ˈfoʊtəɡræfs/"),
        v("edit",     "/ˈɛdɪt/",       "editar",               "edited",   "/ˈɛdɪtɪd/",    "edited",   "/ˈɛdɪtɪd/",    "editing",   "/ˈɛdɪtɪŋ/",    "edits",    "/ˈɛdɪts/"),
        v("exhibit",  "/ɪɡˈzɪbɪt/",    "exhibir",              "exhibited","/ɪɡˈzɪbɪtɪd/", "exhibited","/ɪɡˈzɪbɪtɪd/", "exhibiting","/ɪɡˈzɪbɪtɪŋ/", "exhibits", "/ɪɡˈzɪbɪts/"),
    ]},
    {"id": "ley-justicia", "name": "Ley y Justicia", "icon": "⚖", "verbs": [
        v("sue",      "/suː/",         "demandar",             "sued",     "/suːd/",       "sued",     "/suːd/",       "suing",     "/ˈsuːɪŋ/",     "sues",     "/suːz/"),
        v("accuse",   "/əˈkjuːz/",     "acusar",               "accused",  "/əˈkjuːzd/",   "accused",  "/əˈkjuːzd/",   "accusing",  "/əˈkjuːzɪŋ/",  "accuses",  "/əˈkjuːzɪz/"),
        v("defend",   "/dɪˈfɛnd/",     "defender",             "defended", "/dɪˈfɛndɪd/",  "defended", "/dɪˈfɛndɪd/",  "defending", "/dɪˈfɛndɪŋ/",  "defends",  "/dɪˈfɛndz/"),
        v("judge",    "/dʒʌdʒ/",       "juzgar",               "judged",   "/dʒʌdʒd/",     "judged",   "/dʒʌdʒd/",     "judging",   "/ˈdʒʌdʒɪŋ/",   "judges",   "/ˈdʒʌdʒɪz/"),
        v("sentence", "/ˈsɛntəns/",    "sentenciar",           "sentenced","/ˈsɛntənst/",  "sentenced","/ˈsɛntənst/",  "sentencing","/ˈsɛntənsɪŋ/", "sentences","/ˈsɛntənsɪz/"),
        v("arrest",   "/əˈrɛst/",      "arrestar",             "arrested", "/əˈrɛstɪd/",   "arrested", "/əˈrɛstɪd/",   "arresting", "/əˈrɛstɪŋ/",   "arrests",  "/əˈrɛsts/"),
        v("swear",    "/swɛər/",       "jurar",                "swore",    "/swɔːr/",      "sworn",    "/swɔːrn/",     "swearing",  "/ˈswɛərɪŋ/",   "swears",   "/swɛərz/"),
        v("testify",  "/ˈtɛstɪfaɪ/",   "testificar",           "testified","/ˈtɛstɪfaɪd/", "testified","/ˈtɛstɪfaɪd/", "testifying","/ˈtɛstɪfaɪɪŋ/","testifies","/ˈtɛstɪfaɪz/"),
        v("appeal",   "/əˈpiːl/",      "apelar",               "appealed", "/əˈpiːld/",    "appealed", "/əˈpiːld/",    "appealing", "/əˈpiːlɪŋ/",   "appeals",  "/əˈpiːlz/"),
        v("convict",  "/kənˈvɪkt/",    "condenar / declarar culpable","convicted","/kənˈvɪktɪd/","convicted","/kənˈvɪktɪd/","convicting","/kənˈvɪktɪŋ/","convicts","/kənˈvɪkts/"),
    ]},
    {"id": "politica-civica", "name": "Política y Civismo", "icon": "✪", "verbs": [
        v("vote",     "/voʊt/",        "votar",                "voted",    "/ˈvoʊtɪd/",    "voted",    "/ˈvoʊtɪd/",    "voting",    "/ˈvoʊtɪŋ/",    "votes",    "/voʊts/"),
        v("elect",    "/ɪˈlɛkt/",      "elegir (votar)",       "elected",  "/ɪˈlɛktɪd/",   "elected",  "/ɪˈlɛktɪd/",   "electing",  "/ɪˈlɛktɪŋ/",   "elects",   "/ɪˈlɛkts/"),
        v("govern",   "/ˈɡʌvərn/",     "gobernar",             "governed", "/ˈɡʌvərnd/",   "governed", "/ˈɡʌvərnd/",   "governing", "/ˈɡʌvərnɪŋ/",  "governs",  "/ˈɡʌvərnz/"),
        v("protest",  "/prəˈtɛst/",    "protestar",            "protested","/prəˈtɛstɪd/", "protested","/prəˈtɛstɪd/", "protesting","/prəˈtɛstɪŋ/", "protests", "/prəˈtɛsts/"),
        v("negotiate","/nɪˈɡoʊʃieɪt/", "negociar",             "negotiated","/nɪˈɡoʊʃieɪtɪd/","negotiated","/nɪˈɡoʊʃieɪtɪd/","negotiating","/nɪˈɡoʊʃieɪtɪŋ/","negotiates","/nɪˈɡoʊʃieɪts/"),
        v("sign",     "/saɪn/",        "firmar",               "signed",   "/saɪnd/",      "signed",   "/saɪnd/",      "signing",   "/ˈsaɪnɪŋ/",    "signs",    "/saɪnz/"),
        v("declare",  "/dɪˈklɛər/",    "declarar",             "declared", "/dɪˈklɛərd/",  "declared", "/dɪˈklɛərd/",  "declaring", "/dɪˈklɛərɪŋ/", "declares", "/dɪˈklɛərz/"),
        v("regulate", "/ˈrɛɡjəleɪt/",  "regular",              "regulated","/ˈrɛɡjəleɪtɪd/","regulated","/ˈrɛɡjəleɪtɪd/","regulating","/ˈrɛɡjəleɪtɪŋ/","regulates","/ˈrɛɡjəleɪts/"),
        v("support",  "/səˈpɔːrt/",    "apoyar",               "supported","/səˈpɔːrtɪd/", "supported","/səˈpɔːrtɪd/", "supporting","/səˈpɔːrtɪŋ/", "supports", "/səˈpɔːrts/"),
        v("oppose",   "/əˈpoʊz/",      "oponerse",             "opposed",  "/əˈpoʊzd/",    "opposed",  "/əˈpoʊzd/",    "opposing",  "/əˈpoʊzɪŋ/",   "opposes",  "/əˈpoʊzɪz/"),
    ]},
    {"id": "ciencia", "name": "Ciencia e Investigación", "icon": "⚛", "verbs": [
        v("observe",  "/əbˈzɜːrv/",    "observar",             "observed", "/əbˈzɜːrvd/",  "observed", "/əbˈzɜːrvd/",  "observing", "/əbˈzɜːrvɪŋ/", "observes", "/əbˈzɜːrvz/"),
        v("experiment","/ɪkˈspɛrɪmənt/","experimentar",        "experimented","/ɪkˈspɛrɪmɛntɪd/","experimented","/ɪkˈspɛrɪmɛntɪd/","experimenting","/ɪkˈspɛrɪmɛntɪŋ/","experiments","/ɪkˈspɛrɪmənts/"),
        v("calculate","/ˈkælkjəleɪt/", "calcular",             "calculated","/ˈkælkjəleɪtɪd/","calculated","/ˈkælkjəleɪtɪd/","calculating","/ˈkælkjəleɪtɪŋ/","calculates","/ˈkælkjəleɪts/"),
        v("predict",  "/prɪˈdɪkt/",    "predecir",             "predicted","/prɪˈdɪktɪd/", "predicted","/prɪˈdɪktɪd/", "predicting","/prɪˈdɪktɪŋ/", "predicts", "/prɪˈdɪkts/"),
        v("classify", "/ˈklæsɪfaɪ/",   "clasificar",           "classified","/ˈklæsɪfaɪd/","classified","/ˈklæsɪfaɪd/","classifying","/ˈklæsɪfaɪɪŋ/","classifies","/ˈklæsɪfaɪz/"),
        v("document", "/ˈdɒkjəmɛnt/",  "documentar",           "documented","/ˈdɒkjəmɛntɪd/","documented","/ˈdɒkjəmɛntɪd/","documenting","/ˈdɒkjəmɛntɪŋ/","documents","/ˈdɒkjəmənts/"),
        v("discover", "/dɪˈskʌvər/",   "descubrir",            "discovered","/dɪˈskʌvərd/", "discovered","/dɪˈskʌvərd/","discovering","/dɪˈskʌvərɪŋ/","discovers","/dɪˈskʌvərz/"),
        v("prove",    "/pruːv/",       "probar / demostrar",   "proved",   "/pruːvd/",     "proven",   "/ˈpruːvən/",   "proving",   "/ˈpruːvɪŋ/",   "proves",   "/pruːvz/"),
        v("simulate", "/ˈsɪmjəleɪt/",  "simular",              "simulated","/ˈsɪmjəleɪtɪd/","simulated","/ˈsɪmjəleɪtɪd/","simulating","/ˈsɪmjəleɪtɪŋ/","simulates","/ˈsɪmjəleɪts/"),
        v("deduce",   "/dɪˈduːs/",     "deducir",              "deduced",  "/dɪˈduːst/",   "deduced",  "/dɪˈduːst/",   "deducing",  "/dɪˈduːsɪŋ/",  "deduces",  "/dɪˈduːsɪz/"),
    ]},
    {"id": "ambiente", "name": "Medio Ambiente", "icon": "❦", "verbs": [
        v("pollute",  "/pəˈluːt/",     "contaminar",           "polluted", "/pəˈluːtɪd/",  "polluted", "/pəˈluːtɪd/",  "polluting", "/pəˈluːtɪŋ/",  "pollutes", "/pəˈluːts/"),
        v("recycle",  "/riːˈsaɪkəl/",  "reciclar",             "recycled", "/riːˈsaɪkəld/","recycled", "/riːˈsaɪkəld/","recycling", "/riːˈsaɪklɪŋ/","recycles", "/riːˈsaɪkəlz/"),
        v("conserve", "/kənˈsɜːrv/",   "conservar",            "conserved","/kənˈsɜːrvd/", "conserved","/kənˈsɜːrvd/", "conserving","/kənˈsɜːrvɪŋ/","conserves","/kənˈsɜːrvz/"),
        v("plant",    "/plænt/",       "plantar / sembrar",    "planted",  "/ˈplæntɪd/",   "planted",  "/ˈplæntɪd/",   "planting",  "/ˈplæntɪŋ/",   "plants",   "/plænts/"),
        v("cultivate","/ˈkʌltɪveɪt/",  "cultivar",             "cultivated","/ˈkʌltɪveɪtɪd/","cultivated","/ˈkʌltɪveɪtɪd/","cultivating","/ˈkʌltɪveɪtɪŋ/","cultivates","/ˈkʌltɪveɪts/"),
        v("harvest",  "/ˈhɑːrvɪst/",   "cosechar",             "harvested","/ˈhɑːrvɪstɪd/","harvested","/ˈhɑːrvɪstɪd/","harvesting","/ˈhɑːrvɪstɪŋ/","harvests", "/ˈhɑːrvɪsts/"),
        v("sustain",  "/səˈsteɪn/",    "sostener / mantener",  "sustained","/səˈsteɪnd/",  "sustained","/səˈsteɪnd/",  "sustaining","/səˈsteɪnɪŋ/", "sustains", "/səˈsteɪnz/"),
        v("restore",  "/rɪˈstɔːr/",    "restaurar",            "restored", "/rɪˈstɔːrd/",  "restored", "/rɪˈstɔːrd/",  "restoring", "/rɪˈstɔːrɪŋ/", "restores", "/rɪˈstɔːrz/"),
    ]},
    {"id": "crianza", "name": "Crianza y Cuidado", "icon": "✿", "verbs": [
        v("bathe",    "/beɪð/",        "bañar(se)",            "bathed",   "/beɪðd/",      "bathed",   "/beɪðd/",      "bathing",   "/ˈbeɪðɪŋ/",    "bathes",   "/beɪðz/"),
        v("nurse",    "/nɜːrs/",       "amamantar / cuidar",   "nursed",   "/nɜːrst/",     "nursed",   "/nɜːrst/",     "nursing",   "/ˈnɜːrsɪŋ/",   "nurses",   "/ˈnɜːrsɪz/"),
        v("rock",     "/rɒk/",         "mecer",                "rocked",   "/rɒkt/",       "rocked",   "/rɒkt/",       "rocking",   "/ˈrɒkɪŋ/",     "rocks",    "/rɒks/"),
        v("comfort",  "/ˈkʌmfərt/",    "consolar",             "comforted","/ˈkʌmfərtɪd/", "comforted","/ˈkʌmfərtɪd/", "comforting","/ˈkʌmfərtɪŋ/", "comforts", "/ˈkʌmfərts/"),
        v("soothe",   "/suːð/",        "calmar / apaciguar",   "soothed",  "/suːðd/",      "soothed",  "/suːðd/",      "soothing",  "/ˈsuːðɪŋ/",    "soothes",  "/suːðz/"),
        v("raise",    "/reɪz/",        "criar / levantar",     "raised",   "/reɪzd/",      "raised",   "/reɪzd/",      "raising",   "/ˈreɪzɪŋ/",    "raises",   "/ˈreɪzɪz/"),
        v("scold",    "/skoʊld/",      "regañar",              "scolded",  "/ˈskoʊldɪd/",  "scolded",  "/ˈskoʊldɪd/",  "scolding",  "/ˈskoʊldɪŋ/",  "scolds",   "/skoʊldz/"),
        v("praise",   "/preɪz/",       "elogiar",              "praised",  "/preɪzd/",     "praised",  "/preɪzd/",     "praising",  "/ˈpreɪzɪŋ/",   "praises",  "/ˈpreɪzɪz/"),
        v("feed",     "/fiːd/",        "alimentar",            "fed",      "/fɛd/",        "fed",      "/fɛd/",        "feeding",   "/ˈfiːdɪŋ/",    "feeds",    "/fiːdz/"),
        v("hush",     "/hʌʃ/",         "callar / silenciar",   "hushed",   "/hʌʃt/",       "hushed",   "/hʌʃt/",       "hushing",   "/ˈhʌʃɪŋ/",     "hushes",   "/ˈhʌʃɪz/"),
    ]},
    {"id": "emergencias", "name": "Emergencias y Seguridad", "icon": "⚠", "verbs": [
        v("rescue",   "/ˈrɛskjuː/",    "rescatar",             "rescued",  "/ˈrɛskjuːd/",  "rescued",  "/ˈrɛskjuːd/",  "rescuing",  "/ˈrɛskjuːɪŋ/", "rescues",  "/ˈrɛskjuːz/"),
        v("alert",    "/əˈlɜːrt/",     "alertar",              "alerted",  "/əˈlɜːrtɪd/",  "alerted",  "/əˈlɜːrtɪd/",  "alerting",  "/əˈlɜːrtɪŋ/",  "alerts",   "/əˈlɜːrts/"),
        v("warn",     "/wɔːrn/",       "advertir",             "warned",   "/wɔːrnd/",     "warned",   "/wɔːrnd/",     "warning",   "/ˈwɔːrnɪŋ/",   "warns",    "/wɔːrnz/"),
        v("protect",  "/prəˈtɛkt/",    "proteger",             "protected","/prəˈtɛktɪd/", "protected","/prəˈtɛktɪd/", "protecting","/prəˈtɛktɪŋ/", "protects", "/prəˈtɛkts/"),
        v("evacuate", "/ɪˈvækjueɪt/",  "evacuar",              "evacuated","/ɪˈvækjueɪtɪd/","evacuated","/ɪˈvækjueɪtɪd/","evacuating","/ɪˈvækjueɪtɪŋ/","evacuates","/ɪˈvækjueɪts/"),
        v("escape",   "/ɪˈskeɪp/",     "escapar",              "escaped",  "/ɪˈskeɪpt/",   "escaped",  "/ɪˈskeɪpt/",   "escaping",  "/ɪˈskeɪpɪŋ/",  "escapes",  "/ɪˈskeɪps/"),
        v("survive",  "/sərˈvaɪv/",    "sobrevivir",           "survived", "/sərˈvaɪvd/",  "survived", "/sərˈvaɪvd/",  "surviving", "/sərˈvaɪvɪŋ/", "survives", "/sərˈvaɪvz/"),
        v("shelter",  "/ˈʃɛltər/",     "refugiar",             "sheltered","/ˈʃɛltərd/",   "sheltered","/ˈʃɛltərd/",   "sheltering","/ˈʃɛltərɪŋ/",  "shelters", "/ˈʃɛltərz/"),
        v("ban",      "/bæn/",         "prohibir",             "banned",   "/bænd/",       "banned",   "/bænd/",       "banning",   "/ˈbænɪŋ/",     "bans",     "/bænz/"),
        v("defuse",   "/diːˈfjuːz/",   "desactivar / calmar",  "defused",  "/diːˈfjuːzd/", "defused",  "/diːˈfjuːzd/", "defusing",  "/diːˈfjuːzɪŋ/","defuses",  "/diːˈfjuːzɪz/"),
    ]},
]


# ----------------------------------------------------------------------------
# VOL IV  — 100 verbs, 11 categorías
# ----------------------------------------------------------------------------

vol4 = [
    {"id": "cambio-transformacion", "name": "Cambio y Transformación", "icon": "↻", "verbs": [
        v("evolve",   "/ɪˈvɒlv/",      "evolucionar",          "evolved",  "/ɪˈvɒlvd/",    "evolved",  "/ɪˈvɒlvd/",    "evolving",  "/ɪˈvɒlvɪŋ/",   "evolves",  "/ɪˈvɒlvz/"),
        v("adapt",    "/əˈdæpt/",      "adaptar(se)",          "adapted",  "/əˈdæptɪd/",   "adapted",  "/əˈdæptɪd/",   "adapting",  "/əˈdæptɪŋ/",   "adapts",   "/əˈdæpts/"),
        v("transform","/trænsˈfɔːrm/", "transformar",          "transformed","/trænsˈfɔːrmd/","transformed","/trænsˈfɔːrmd/","transforming","/trænsˈfɔːrmɪŋ/","transforms","/trænsˈfɔːrmz/"),
        v("reform",   "/rɪˈfɔːrm/",    "reformar",             "reformed", "/rɪˈfɔːrmd/",  "reformed", "/rɪˈfɔːrmd/",  "reforming", "/rɪˈfɔːrmɪŋ/", "reforms",  "/rɪˈfɔːrmz/"),
        v("switch",   "/swɪtʃ/",       "cambiar / intercambiar","switched","/swɪtʃt/",     "switched", "/swɪtʃt/",     "switching", "/ˈswɪtʃɪŋ/",   "switches", "/ˈswɪtʃɪz/"),
        v("modify",   "/ˈmɒdɪfaɪ/",    "modificar",            "modified", "/ˈmɒdɪfaɪd/",  "modified", "/ˈmɒdɪfaɪd/",  "modifying", "/ˈmɒdɪfaɪɪŋ/", "modifies", "/ˈmɒdɪfaɪz/"),
        v("alter",    "/ˈɔːltər/",     "alterar / modificar",  "altered",  "/ˈɔːltərd/",   "altered",  "/ˈɔːltərd/",   "altering",  "/ˈɔːltərɪŋ/",  "alters",   "/ˈɔːltərz/"),
        v("develop",  "/dɪˈvɛləp/",    "desarrollar",          "developed","/dɪˈvɛləpt/",  "developed","/dɪˈvɛləpt/",  "developing","/dɪˈvɛləpɪŋ/", "develops", "/dɪˈvɛləps/"),
        v("emerge",   "/ɪˈmɜːrdʒ/",    "emerger / surgir",     "emerged",  "/ɪˈmɜːrdʒd/",  "emerged",  "/ɪˈmɜːrdʒd/",  "emerging",  "/ɪˈmɜːrdʒɪŋ/", "emerges",  "/ɪˈmɜːrdʒɪz/"),
        v("expand",   "/ɪkˈspænd/",    "expandir",             "expanded", "/ɪkˈspændɪd/", "expanded", "/ɪkˈspændɪd/", "expanding", "/ɪkˈspændɪŋ/", "expands",  "/ɪkˈspændz/"),
    ]},
    {"id": "analisis-decision", "name": "Análisis y Decisión", "icon": "✦", "verbs": [
        v("conclude", "/kənˈkluːd/",   "concluir",             "concluded","/kənˈkluːdɪd/","concluded","/kənˈkluːdɪd/","concluding","/kənˈkluːdɪŋ/","concludes","/kənˈkluːdz/"),
        v("evaluate", "/ɪˈvæljueɪt/",  "evaluar",              "evaluated","/ɪˈvæljueɪtɪd/","evaluated","/ɪˈvæljueɪtɪd/","evaluating","/ɪˈvæljueɪtɪŋ/","evaluates","/ɪˈvæljueɪts/"),
        v("compare",  "/kəmˈpɛər/",    "comparar",             "compared", "/kəmˈpɛərd/",  "compared", "/kəmˈpɛərd/",  "comparing", "/kəmˈpɛərɪŋ/", "compares", "/kəmˈpɛərz/"),
        v("contrast", "/kənˈtræst/",   "contrastar",           "contrasted","/kənˈtræstɪd/","contrasted","/kənˈtræstɪd/","contrasting","/kənˈtræstɪŋ/","contrasts","/kənˈtræsts/"),
        v("prioritize","/praɪˈɔːrɪtaɪz/","priorizar",          "prioritized","/praɪˈɔːrɪtaɪzd/","prioritized","/praɪˈɔːrɪtaɪzd/","prioritizing","/praɪˈɔːrɪtaɪzɪŋ/","prioritizes","/praɪˈɔːrɪtaɪzɪz/"),
        v("consider", "/kənˈsɪdər/",   "considerar",           "considered","/kənˈsɪdərd/", "considered","/kənˈsɪdərd/","considering","/kənˈsɪdərɪŋ/","considers","/kənˈsɪdərz/"),
        v("weigh",    "/weɪ/",         "pesar / sopesar",      "weighed",  "/weɪd/",       "weighed",  "/weɪd/",       "weighing",  "/ˈweɪɪŋ/",     "weighs",   "/weɪz/"),
        v("doubt",    "/daʊt/",        "dudar",                "doubted",  "/ˈdaʊtɪd/",    "doubted",  "/ˈdaʊtɪd/",    "doubting",  "/ˈdaʊtɪŋ/",    "doubts",   "/daʊts/"),
        v("assume",   "/əˈsuːm/",      "asumir / suponer",     "assumed",  "/əˈsuːmd/",    "assumed",  "/əˈsuːmd/",    "assuming",  "/əˈsuːmɪŋ/",   "assumes",  "/əˈsuːmz/"),
        v("hesitate", "/ˈhɛzɪteɪt/",   "dudar / vacilar",      "hesitated","/ˈhɛzɪteɪtɪd/","hesitated","/ˈhɛzɪteɪtɪd/","hesitating","/ˈhɛzɪteɪtɪŋ/","hesitates","/ˈhɛzɪteɪts/"),
    ]},
    {"id": "comprar-consumir", "name": "Comprar y Consumir", "icon": "♢", "verbs": [
        v("order",    "/ˈɔːrdər/",     "ordenar / pedir",      "ordered",  "/ˈɔːrdərd/",   "ordered",  "/ˈɔːrdərd/",   "ordering",  "/ˈɔːrdərɪŋ/",  "orders",   "/ˈɔːrdərz/"),
        v("refund",   "/rɪˈfʌnd/",     "reembolsar",           "refunded", "/rɪˈfʌndɪd/",  "refunded", "/rɪˈfʌndɪd/",  "refunding", "/rɪˈfʌndɪŋ/",  "refunds",  "/rɪˈfʌndz/"),
        v("exchange", "/ɪksˈtʃeɪndʒ/", "intercambiar / cambiar","exchanged","/ɪksˈtʃeɪndʒd/","exchanged","/ɪksˈtʃeɪndʒd/","exchanging","/ɪksˈtʃeɪndʒɪŋ/","exchanges","/ɪksˈtʃeɪndʒɪz/"),
        v("claim",    "/kleɪm/",       "reclamar",             "claimed",  "/kleɪmd/",     "claimed",  "/kleɪmd/",     "claiming",  "/ˈkleɪmɪŋ/",   "claims",   "/kleɪmz/"),
        v("deliver",  "/dɪˈlɪvər/",    "entregar",             "delivered","/dɪˈlɪvərd/",  "delivered","/dɪˈlɪvərd/",  "delivering","/dɪˈlɪvərɪŋ/", "delivers", "/dɪˈlɪvərz/"),
        v("package",  "/ˈpækɪdʒ/",     "empacar",              "packaged", "/ˈpækɪdʒd/",   "packaged", "/ˈpækɪdʒd/",   "packaging", "/ˈpækɪdʒɪŋ/",  "packages", "/ˈpækɪdʒɪz/"),
        v("gift",     "/ɡɪft/",        "regalar",              "gifted",   "/ˈɡɪftɪd/",    "gifted",   "/ˈɡɪftɪd/",    "gifting",   "/ˈɡɪftɪŋ/",    "gifts",    "/ɡɪfts/"),
        v("bargain",  "/ˈbɑːrɡɪn/",    "negociar / regatear",  "bargained","/ˈbɑːrɡɪnd/",  "bargained","/ˈbɑːrɡɪnd/",  "bargaining","/ˈbɑːrɡɪnɪŋ/", "bargains", "/ˈbɑːrɡɪnz/"),
        v("browse",   "/braʊz/",       "navegar / curiosear",  "browsed",  "/braʊzd/",     "browsed",  "/braʊzd/",     "browsing",  "/ˈbraʊzɪŋ/",   "browses",  "/ˈbraʊzɪz/"),
        v("purchase", "/ˈpɜːrtʃəs/",   "adquirir / comprar",   "purchased","/ˈpɜːrtʃəst/", "purchased","/ˈpɜːrtʃəst/", "purchasing","/ˈpɜːrtʃəsɪŋ/","purchases","/ˈpɜːrtʃəsɪz/"),
    ]},
    {"id": "liderazgo-gestion", "name": "Liderazgo y Gestión", "icon": "★", "verbs": [
        v("lead",     "/liːd/",        "liderar / encabezar",  "led",      "/lɛd/",        "led",      "/lɛd/",        "leading",   "/ˈliːdɪŋ/",    "leads",    "/liːdz/", pSp="led", ppSp="led"),
        v("supervise","/ˈsuːpərvaɪz/", "supervisar",           "supervised","/ˈsuːpərvaɪzd/","supervised","/ˈsuːpərvaɪzd/","supervising","/ˈsuːpərvaɪzɪŋ/","supervises","/ˈsuːpərvaɪzɪz/"),
        v("mentor",   "/ˈmɛntɔːr/",    "asesorar / mentorear", "mentored", "/ˈmɛntɔːrd/",  "mentored", "/ˈmɛntɔːrd/",  "mentoring", "/ˈmɛntɔːrɪŋ/", "mentors",  "/ˈmɛntɔːrz/"),
        v("delegate", "/ˈdɛlɪɡeɪt/",   "delegar",              "delegated","/ˈdɛlɪɡeɪtɪd/","delegated","/ˈdɛlɪɡeɪtɪd/","delegating","/ˈdɛlɪɡeɪtɪŋ/","delegates","/ˈdɛlɪɡeɪts/"),
        v("direct",   "/dɪˈrɛkt/",     "dirigir",              "directed", "/dɪˈrɛktɪd/",  "directed", "/dɪˈrɛktɪd/",  "directing", "/dɪˈrɛktɪŋ/",  "directs",  "/dɪˈrɛkts/"),
        v("motivate", "/ˈmoʊtɪveɪt/",  "motivar",              "motivated","/ˈmoʊtɪveɪtɪd/","motivated","/ˈmoʊtɪveɪtɪd/","motivating","/ˈmoʊtɪveɪtɪŋ/","motivates","/ˈmoʊtɪveɪts/"),
        v("inspire",  "/ɪnˈspaɪər/",   "inspirar",             "inspired", "/ɪnˈspaɪərd/", "inspired", "/ɪnˈspaɪərd/", "inspiring", "/ɪnˈspaɪərɪŋ/","inspires", "/ɪnˈspaɪərz/"),
        v("organize", "/ˈɔːrɡənaɪz/",  "organizar",            "organized","/ˈɔːrɡənaɪzd/","organized","/ˈɔːrɡənaɪzd/","organizing","/ˈɔːrɡənaɪzɪŋ/","organizes","/ˈɔːrɡənaɪzɪz/"),
        v("coordinate","/koʊˈɔːrdɪneɪt/","coordinar",          "coordinated","/koʊˈɔːrdɪneɪtɪd/","coordinated","/koʊˈɔːrdɪneɪtɪd/","coordinating","/koʊˈɔːrdɪneɪtɪŋ/","coordinates","/koʊˈɔːrdɪneɪts/"),
        v("oversee",  "/oʊvərˈsiː/",   "supervisar / vigilar", "oversaw",  "/oʊvərˈsɔː/",  "overseen", "/oʊvərˈsiːn/", "overseeing","/oʊvərˈsiːɪŋ/","oversees", "/oʊvərˈsiːz/"),
    ]},
    {"id": "exito-logro", "name": "Éxito y Logro", "icon": "✯", "verbs": [
        v("succeed",  "/səkˈsiːd/",    "tener éxito",          "succeeded","/səkˈsiːdɪd/", "succeeded","/səkˈsiːdɪd/", "succeeding","/səkˈsiːdɪŋ/", "succeeds", "/səkˈsiːdz/"),
        v("achieve",  "/əˈtʃiːv/",     "lograr",               "achieved", "/əˈtʃiːvd/",   "achieved", "/əˈtʃiːvd/",   "achieving", "/əˈtʃiːvɪŋ/",  "achieves", "/əˈtʃiːvz/"),
        v("accomplish","/əˈkɒmplɪʃ/",  "cumplir / realizar",   "accomplished","/əˈkɒmplɪʃt/","accomplished","/əˈkɒmplɪʃt/","accomplishing","/əˈkɒmplɪʃɪŋ/","accomplishes","/əˈkɒmplɪʃɪz/"),
        v("gain",     "/ɡeɪn/",        "ganar / obtener",      "gained",   "/ɡeɪnd/",      "gained",   "/ɡeɪnd/",      "gaining",   "/ˈɡeɪnɪŋ/",    "gains",    "/ɡeɪnz/"),
        v("overcome", "/oʊvərˈkʌm/",   "superar",              "overcame", "/oʊvərˈkeɪm/", "overcome", "/oʊvərˈkʌm/",  "overcoming","/oʊvərˈkʌmɪŋ/","overcomes","/oʊvərˈkʌmz/"),
        v("master",   "/ˈmæstər/",     "dominar",              "mastered", "/ˈmæstərd/",   "mastered", "/ˈmæstərd/",   "mastering", "/ˈmæstərɪŋ/",  "masters",  "/ˈmæstərz/"),
        v("excel",    "/ɪkˈsɛl/",      "destacar / sobresalir","excelled", "/ɪkˈsɛld/",    "excelled", "/ɪkˈsɛld/",    "excelling", "/ɪkˈsɛlɪŋ/",   "excels",   "/ɪkˈsɛlz/"),
        v("prevail",  "/prɪˈveɪl/",    "prevalecer",           "prevailed","/prɪˈveɪld/",  "prevailed","/prɪˈveɪld/",  "prevailing","/prɪˈveɪlɪŋ/", "prevails", "/prɪˈveɪlz/"),
        v("advance",  "/ədˈvæns/",     "avanzar",              "advanced", "/ədˈvænst/",   "advanced", "/ədˈvænst/",   "advancing", "/ədˈvænsɪŋ/",  "advances", "/ədˈvænsɪz/"),
        v("conquer",  "/ˈkɒŋkər/",     "conquistar",           "conquered","/ˈkɒŋkərd/",   "conquered","/ˈkɒŋkərd/",   "conquering","/ˈkɒŋkərɪŋ/",  "conquers", "/ˈkɒŋkərz/"),
    ]},
    {"id": "fallo-error", "name": "Fallo y Error", "icon": "✗", "verbs": [
        v("fail",     "/feɪl/",        "fallar / fracasar",    "failed",   "/feɪld/",      "failed",   "/feɪld/",      "failing",   "/ˈfeɪlɪŋ/",    "fails",    "/feɪlz/"),
        v("struggle", "/ˈstrʌɡəl/",    "luchar / esforzarse",  "struggled","/ˈstrʌɡəld/",  "struggled","/ˈstrʌɡəld/",  "struggling","/ˈstrʌɡlɪŋ/", "struggles","/ˈstrʌɡəlz/"),
        v("stumble",  "/ˈstʌmbəl/",    "tropezar",             "stumbled", "/ˈstʌmbəld/",  "stumbled", "/ˈstʌmbəld/",  "stumbling", "/ˈstʌmblɪŋ/",  "stumbles", "/ˈstʌmbəlz/"),
        v("slip",     "/slɪp/",        "resbalar",             "slipped",  "/slɪpt/",      "slipped",  "/slɪpt/",      "slipping",  "/ˈslɪpɪŋ/",    "slips",    "/slɪps/"),
        v("falter",   "/ˈfɔːltər/",    "vacilar / titubear",   "faltered", "/ˈfɔːltərd/",  "faltered", "/ˈfɔːltərd/",  "faltering", "/ˈfɔːltərɪŋ/", "falters",  "/ˈfɔːltərz/"),
        v("regret",   "/rɪˈɡrɛt/",     "lamentar",             "regretted","/rɪˈɡrɛtɪd/",  "regretted","/rɪˈɡrɛtɪd/",  "regretting","/rɪˈɡrɛtɪŋ/",  "regrets",  "/rɪˈɡrɛts/"),
        v("mistake",  "/mɪˈsteɪk/",    "equivocarse",          "mistook",  "/mɪˈstʊk/",    "mistaken", "/mɪˈsteɪkən/", "mistaking", "/mɪˈsteɪkɪŋ/", "mistakes", "/mɪˈsteɪks/"),
        v("abandon",  "/əˈbændən/",    "abandonar",            "abandoned","/əˈbændənd/",  "abandoned","/əˈbændənd/",  "abandoning","/əˈbændənɪŋ/","abandons", "/əˈbændənz/"),
    ]},
    {"id": "emocion-corporal", "name": "Expresión Emocional", "icon": "☺", "verbs": [
        v("laugh",    "/læf/",         "reír",                 "laughed",  "/læft/",       "laughed",  "/læft/",       "laughing",  "/ˈlæfɪŋ/",     "laughs",   "/læfs/"),
        v("smile",    "/smaɪl/",       "sonreír",              "smiled",   "/smaɪld/",     "smiled",   "/smaɪld/",     "smiling",   "/ˈsmaɪlɪŋ/",   "smiles",   "/smaɪlz/"),
        v("scream",   "/skriːm/",      "gritar",               "screamed", "/skriːmd/",    "screamed", "/skriːmd/",    "screaming", "/ˈskriːmɪŋ/",  "screams",  "/skriːmz/"),
        v("sob",      "/sɒb/",         "sollozar",             "sobbed",   "/sɒbd/",       "sobbed",   "/sɒbd/",       "sobbing",   "/ˈsɒbɪŋ/",     "sobs",     "/sɒbz/"),
        v("blush",    "/blʌʃ/",        "sonrojarse",           "blushed",  "/blʌʃt/",      "blushed",  "/blʌʃt/",      "blushing",  "/ˈblʌʃɪŋ/",    "blushes",  "/ˈblʌʃɪz/"),
        v("grin",     "/ɡrɪn/",        "sonreír (con dientes)","grinned",  "/ɡrɪnd/",      "grinned",  "/ɡrɪnd/",      "grinning",  "/ˈɡrɪnɪŋ/",    "grins",    "/ɡrɪnz/"),
        v("frown",    "/fraʊn/",       "fruncir el ceño",      "frowned",  "/fraʊnd/",     "frowned",  "/fraʊnd/",     "frowning",  "/ˈfraʊnɪŋ/",   "frowns",   "/fraʊnz/"),
        v("sigh",     "/saɪ/",         "suspirar",             "sighed",   "/saɪd/",       "sighed",   "/saɪd/",       "sighing",   "/ˈsaɪɪŋ/",     "sighs",    "/saɪz/"),
        v("yawn",     "/jɔːn/",        "bostezar",             "yawned",   "/jɔːnd/",      "yawned",   "/jɔːnd/",      "yawning",   "/ˈjɔːnɪŋ/",    "yawns",    "/jɔːnz/"),
        v("weep",     "/wiːp/",        "llorar",               "wept",     "/wɛpt/",       "wept",     "/wɛpt/",       "weeping",   "/ˈwiːpɪŋ/",    "weeps",    "/wiːps/"),
    ]},
    {"id": "accion-rapida", "name": "Acción Rápida", "icon": "»", "verbs": [
        v("rush",     "/rʌʃ/",         "apresurarse",          "rushed",   "/rʌʃt/",       "rushed",   "/rʌʃt/",       "rushing",   "/ˈrʌʃɪŋ/",     "rushes",   "/ˈrʌʃɪz/"),
        v("hurry",    "/ˈhɜːri/",      "darse prisa",          "hurried",  "/ˈhɜːrid/",    "hurried",  "/ˈhɜːrid/",    "hurrying",  "/ˈhɜːriɪŋ/",   "hurries",  "/ˈhɜːriz/"),
        v("dash",     "/dæʃ/",         "lanzarse / correr",    "dashed",   "/dæʃt/",       "dashed",   "/dæʃt/",       "dashing",   "/ˈdæʃɪŋ/",     "dashes",   "/ˈdæʃɪz/"),
        v("lunge",    "/lʌndʒ/",       "lanzarse / abalanzarse","lunged",  "/lʌndʒd/",     "lunged",   "/lʌndʒd/",     "lunging",   "/ˈlʌndʒɪŋ/",   "lunges",   "/ˈlʌndʒɪz/"),
        v("sprint",   "/sprɪnt/",      "esprintar",            "sprinted", "/ˈsprɪntɪd/",  "sprinted", "/ˈsprɪntɪd/",  "sprinting", "/ˈsprɪntɪŋ/",  "sprints",  "/sprɪnts/"),
        v("leap",     "/liːp/",        "saltar / brincar",     "leaped",   "/liːpt/",      "leaped",   "/liːpt/",      "leaping",   "/ˈliːpɪŋ/",    "leaps",    "/liːps/"),
        v("race",     "/reɪs/",        "correr / competir",    "raced",    "/reɪst/",      "raced",    "/reɪst/",      "racing",    "/ˈreɪsɪŋ/",    "races",    "/ˈreɪsɪz/"),
        v("hustle",   "/ˈhʌsəl/",      "darse prisa / trabajar duro","hustled","/ˈhʌsəld/","hustled",  "/ˈhʌsəld/",    "hustling",  "/ˈhʌslɪŋ/",    "hustles",  "/ˈhʌsəlz/"),
    ]},
    {"id": "comunicacion-digital", "name": "Comunicación Digital", "icon": "✉", "verbs": [
        v("post",     "/poʊst/",       "publicar",             "posted",   "/ˈpoʊstɪd/",   "posted",   "/ˈpoʊstɪd/",   "posting",   "/ˈpoʊstɪŋ/",   "posts",    "/poʊsts/"),
        v("comment",  "/ˈkɒmɛnt/",     "comentar",             "commented","/ˈkɒmɛntɪd/",  "commented","/ˈkɒmɛntɪd/",  "commenting","/ˈkɒmɛntɪŋ/", "comments", "/ˈkɒmənts/"),
        v("subscribe","/səbˈskraɪb/",  "suscribirse",          "subscribed","/səbˈskraɪbd/","subscribed","/səbˈskraɪbd/","subscribing","/səbˈskraɪbɪŋ/","subscribes","/səbˈskraɪbz/"),
        v("stream",   "/striːm/",      "transmitir en vivo",   "streamed", "/striːmd/",    "streamed", "/striːmd/",    "streaming", "/ˈstriːmɪŋ/",  "streams",  "/striːmz/"),
        v("message",  "/ˈmɛsɪdʒ/",     "enviar mensaje",       "messaged", "/ˈmɛsɪdʒd/",   "messaged", "/ˈmɛsɪdʒd/",   "messaging", "/ˈmɛsɪdʒɪŋ/",  "messages", "/ˈmɛsɪdʒɪz/"),
        v("tag",      "/tæɡ/",         "etiquetar",            "tagged",   "/tæɡd/",       "tagged",   "/tæɡd/",       "tagging",   "/ˈtæɡɪŋ/",     "tags",     "/tæɡz/"),
        v("mute",     "/mjuːt/",       "silenciar",            "muted",    "/ˈmjuːtɪd/",   "muted",    "/ˈmjuːtɪd/",   "muting",    "/ˈmjuːtɪŋ/",   "mutes",    "/mjuːts/"),
        v("scroll",   "/skroʊl/",      "desplazarse",          "scrolled", "/skroʊld/",    "scrolled", "/skroʊld/",    "scrolling", "/ˈskroʊlɪŋ/",  "scrolls",  "/skroʊlz/"),
    ]},
    {"id": "movimiento-fino", "name": "Movimiento Fino", "icon": "·", "verbs": [
        v("tap",      "/tæp/",         "tocar suavemente",     "tapped",   "/tæpt/",       "tapped",   "/tæpt/",       "tapping",   "/ˈtæpɪŋ/",     "taps",     "/tæps/"),
        v("drag",     "/dræɡ/",        "arrastrar",            "dragged",  "/dræɡd/",      "dragged",  "/dræɡd/",      "dragging",  "/ˈdræɡɪŋ/",    "drags",    "/dræɡz/"),
        v("swipe",    "/swaɪp/",       "deslizar",             "swiped",   "/swaɪpt/",     "swiped",   "/swaɪpt/",     "swiping",   "/ˈswaɪpɪŋ/",   "swipes",   "/swaɪps/"),
        v("hover",    "/ˈhʌvər/",      "flotar / pasar encima","hovered",  "/ˈhʌvərd/",    "hovered",  "/ˈhʌvərd/",    "hovering",  "/ˈhʌvərɪŋ/",   "hovers",   "/ˈhʌvərz/"),
        v("pinch",    "/pɪntʃ/",       "pellizcar",            "pinched",  "/pɪntʃt/",     "pinched",  "/pɪntʃt/",     "pinching",  "/ˈpɪntʃɪŋ/",   "pinches",  "/ˈpɪntʃɪz/"),
        v("zoom",     "/zuːm/",        "ampliar / hacer zoom", "zoomed",   "/zuːmd/",      "zoomed",   "/zuːmd/",      "zooming",   "/ˈzuːmɪŋ/",    "zooms",    "/zuːmz/"),
        v("flick",    "/flɪk/",        "dar un toque rápido",  "flicked",  "/flɪkt/",      "flicked",  "/flɪkt/",      "flicking",  "/ˈflɪkɪŋ/",    "flicks",   "/flɪks/"),
        v("twist",    "/twɪst/",       "torcer / girar",       "twisted",  "/ˈtwɪstɪd/",   "twisted",  "/ˈtwɪstɪd/",   "twisting",  "/ˈtwɪstɪŋ/",   "twists",   "/twɪsts/"),
        v("slide",    "/slaɪd/",       "deslizar",             "slid",     "/slɪd/",       "slid",     "/slɪd/",       "sliding",   "/ˈslaɪdɪŋ/",   "slides",   "/slaɪdz/"),
        v("snap",     "/snæp/",        "chasquear",            "snapped",  "/snæpt/",      "snapped",  "/snæpt/",      "snapping",  "/ˈsnæpɪŋ/",    "snaps",    "/snæps/"),
    ]},
    {"id": "estado-ser", "name": "Estado y Permanencia", "icon": "∞", "verbs": [
        v("exist",    "/ɪɡˈzɪst/",     "existir",              "existed",  "/ɪɡˈzɪstɪd/",  "existed",  "/ɪɡˈzɪstɪd/",  "existing",  "/ɪɡˈzɪstɪŋ/",  "exists",   "/ɪɡˈzɪsts/"),
        v("persist",  "/pərˈsɪst/",    "persistir",            "persisted","/pərˈsɪstɪd/", "persisted","/pərˈsɪstɪd/", "persisting","/pərˈsɪstɪŋ/", "persists", "/pərˈsɪsts/"),
        v("remain",   "/rɪˈmeɪn/",     "permanecer",           "remained", "/rɪˈmeɪnd/",   "remained", "/rɪˈmeɪnd/",   "remaining", "/rɪˈmeɪnɪŋ/",  "remains",  "/rɪˈmeɪnz/"),
        v("last",     "/læst/",        "durar",                "lasted",   "/ˈlæstɪd/",    "lasted",   "/ˈlæstɪd/",    "lasting",   "/ˈlæstɪŋ/",    "lasts",    "/læsts/"),
        v("endure",   "/ɪnˈdjʊər/",    "soportar / aguantar",  "endured",  "/ɪnˈdjʊərd/",  "endured",  "/ɪnˈdjʊərd/",  "enduring",  "/ɪnˈdjʊərɪŋ/", "endures",  "/ɪnˈdjʊərz/"),
        v("vary",     "/ˈvɛəri/",      "variar",               "varied",   "/ˈvɛərid/",    "varied",   "/ˈvɛərid/",    "varying",   "/ˈvɛəriɪŋ/",   "varies",   "/ˈvɛəriz/"),
        v("differ",   "/ˈdɪfər/",      "diferir",              "differed", "/ˈdɪfərd/",    "differed", "/ˈdɪfərd/",    "differing", "/ˈdɪfərɪŋ/",   "differs",  "/ˈdɪfərz/"),
    ]},
]


# ----------------------------------------------------------------------------
# VOL V  — 100 verbs, 11 categorías
# ----------------------------------------------------------------------------

vol5 = [
    {"id": "cognitiva", "name": "Acción Cognitiva", "icon": "✺", "verbs": [
        v("notice",   "/ˈnoʊtɪs/",     "notar / darse cuenta", "noticed",  "/ˈnoʊtɪst/",   "noticed",  "/ˈnoʊtɪst/",   "noticing",  "/ˈnoʊtɪsɪŋ/",  "notices",  "/ˈnoʊtɪsɪz/"),
        v("recognize","/ˈrɛkəɡnaɪz/",  "reconocer",            "recognized","/ˈrɛkəɡnaɪzd/","recognized","/ˈrɛkəɡnaɪzd/","recognizing","/ˈrɛkəɡnaɪzɪŋ/","recognizes","/ˈrɛkəɡnaɪzɪz/"),
        v("recall",   "/rɪˈkɔːl/",     "recordar / evocar",    "recalled", "/rɪˈkɔːld/",   "recalled", "/rɪˈkɔːld/",   "recalling", "/rɪˈkɔːlɪŋ/",  "recalls",  "/rɪˈkɔːlz/"),
        v("identify", "/aɪˈdɛntɪfaɪ/", "identificar",          "identified","/aɪˈdɛntɪfaɪd/","identified","/aɪˈdɛntɪfaɪd/","identifying","/aɪˈdɛntɪfaɪɪŋ/","identifies","/aɪˈdɛntɪfaɪz/"),
        v("distinguish","/dɪˈstɪŋɡwɪʃ/","distinguir",          "distinguished","/dɪˈstɪŋɡwɪʃt/","distinguished","/dɪˈstɪŋɡwɪʃt/","distinguishing","/dɪˈstɪŋɡwɪʃɪŋ/","distinguishes","/dɪˈstɪŋɡwɪʃɪz/"),
        v("perceive", "/pərˈsiːv/",    "percibir",             "perceived","/pərˈsiːvd/",  "perceived","/pərˈsiːvd/",  "perceiving","/pərˈsiːvɪŋ/", "perceives","/pərˈsiːvz/"),
        v("sense",    "/sɛns/",        "sentir / intuir",      "sensed",   "/sɛnst/",      "sensed",   "/sɛnst/",      "sensing",   "/ˈsɛnsɪŋ/",    "senses",   "/ˈsɛnsɪz/"),
        v("grasp",    "/ɡræsp/",       "captar / agarrar",     "grasped",  "/ɡræspt/",     "grasped",  "/ɡræspt/",     "grasping",  "/ˈɡræspɪŋ/",   "grasps",   "/ɡræsps/"),
        v("ponder",   "/ˈpɒndər/",     "reflexionar",          "pondered", "/ˈpɒndərd/",   "pondered", "/ˈpɒndərd/",   "pondering", "/ˈpɒndərɪŋ/",  "ponders",  "/ˈpɒndərz/"),
        v("reflect",  "/rɪˈflɛkt/",    "reflejar / reflexionar","reflected","/rɪˈflɛktɪd/","reflected","/rɪˈflɛktɪd/", "reflecting","/rɪˈflɛktɪŋ/", "reflects", "/rɪˈflɛkts/"),
    ]},
    {"id": "creativa", "name": "Acción Creativa", "icon": "❋", "verbs": [
        v("invent",   "/ɪnˈvɛnt/",     "inventar",             "invented", "/ɪnˈvɛntɪd/",  "invented", "/ɪnˈvɛntɪd/",  "inventing", "/ɪnˈvɛntɪŋ/",  "invents",  "/ɪnˈvɛnts/"),
        v("draft",    "/dræft/",       "redactar / bosquejar", "drafted",  "/ˈdræftɪd/",   "drafted",  "/ˈdræftɪd/",   "drafting",  "/ˈdræftɪŋ/",   "drafts",   "/dræfts/"),
        v("prototype","/ˈproʊtətaɪp/", "prototipar",           "prototyped","/ˈproʊtətaɪpt/","prototyped","/ˈproʊtətaɪpt/","prototyping","/ˈproʊtətaɪpɪŋ/","prototypes","/ˈproʊtətaɪps/"),
        v("brainstorm","/ˈbreɪnstɔːrm/","lluvia de ideas",     "brainstormed","/ˈbreɪnstɔːrmd/","brainstormed","/ˈbreɪnstɔːrmd/","brainstorming","/ˈbreɪnstɔːrmɪŋ/","brainstorms","/ˈbreɪnstɔːrmz/"),
        v("imagine",  "/ɪˈmædʒɪn/",    "imaginar",             "imagined", "/ɪˈmædʒɪnd/",  "imagined", "/ɪˈmædʒɪnd/",  "imagining", "/ɪˈmædʒɪnɪŋ/", "imagines", "/ɪˈmædʒɪnz/"),
        v("dream",    "/driːm/",       "soñar",                "dreamed",  "/driːmd/",     "dreamed",  "/driːmd/",     "dreaming",  "/ˈdriːmɪŋ/",   "dreams",   "/driːmz/"),
        v("envision", "/ɪnˈvɪʒən/",    "visualizar",           "envisioned","/ɪnˈvɪʒənd/", "envisioned","/ɪnˈvɪʒənd/", "envisioning","/ɪnˈvɪʒənɪŋ/","envisions","/ɪnˈvɪʒənz/"),
        v("conceive", "/kənˈsiːv/",    "concebir",             "conceived","/kənˈsiːvd/",  "conceived","/kənˈsiːvd/",  "conceiving","/kənˈsiːvɪŋ/", "conceives","/kənˈsiːvz/"),
        v("devise",   "/dɪˈvaɪz/",     "idear",                "devised",  "/dɪˈvaɪzd/",   "devised",  "/dɪˈvaɪzd/",   "devising",  "/dɪˈvaɪzɪŋ/",  "devises",  "/dɪˈvaɪzɪz/"),
        v("formulate","/ˈfɔːrmjəleɪt/","formular",             "formulated","/ˈfɔːrmjəleɪtɪd/","formulated","/ˈfɔːrmjəleɪtɪd/","formulating","/ˈfɔːrmjəleɪtɪŋ/","formulates","/ˈfɔːrmjəleɪts/"),
    ]},
    {"id": "celebracion", "name": "Celebración y Eventos", "icon": "✧", "verbs": [
        v("celebrate","/ˈsɛlɪbreɪt/",  "celebrar",             "celebrated","/ˈsɛlɪbreɪtɪd/","celebrated","/ˈsɛlɪbreɪtɪd/","celebrating","/ˈsɛlɪbreɪtɪŋ/","celebrates","/ˈsɛlɪbreɪts/"),
        v("attend",   "/əˈtɛnd/",      "asistir",              "attended", "/əˈtɛndɪd/",   "attended", "/əˈtɛndɪd/",   "attending", "/əˈtɛndɪŋ/",   "attends",  "/əˈtɛndz/"),
        v("host",     "/hoʊst/",       "ser anfitrión",        "hosted",   "/ˈhoʊstɪd/",   "hosted",   "/ˈhoʊstɪd/",   "hosting",   "/ˈhoʊstɪŋ/",   "hosts",    "/hoʊsts/"),
        v("greet",    "/ɡriːt/",       "saludar",              "greeted",  "/ˈɡriːtɪd/",   "greeted",  "/ˈɡriːtɪd/",   "greeting",  "/ˈɡriːtɪŋ/",   "greets",   "/ɡriːts/"),
        v("toast",    "/toʊst/",       "brindar",              "toasted",  "/ˈtoʊstɪd/",   "toasted",  "/ˈtoʊstɪd/",   "toasting",  "/ˈtoʊstɪŋ/",   "toasts",   "/toʊsts/"),
        v("gather",   "/ˈɡæðər/",      "reunir(se)",           "gathered", "/ˈɡæðərd/",    "gathered", "/ˈɡæðərd/",    "gathering", "/ˈɡæðərɪŋ/",   "gathers",  "/ˈɡæðərz/"),
        v("cheer",    "/tʃɪər/",       "vitorear / animar",    "cheered",  "/tʃɪərd/",     "cheered",  "/tʃɪərd/",     "cheering",  "/ˈtʃɪərɪŋ/",   "cheers",   "/tʃɪərz/"),
        v("mingle",   "/ˈmɪŋɡəl/",     "mezclarse / socializar","mingled", "/ˈmɪŋɡəld/",   "mingled",  "/ˈmɪŋɡəld/",   "mingling",  "/ˈmɪŋɡlɪŋ/",   "mingles",  "/ˈmɪŋɡəlz/"),
        v("congratulate","/kənˈɡrætʃəleɪt/","felicitar",       "congratulated","/kənˈɡrætʃəleɪtɪd/","congratulated","/kənˈɡrætʃəleɪtɪd/","congratulating","/kənˈɡrætʃəleɪtɪŋ/","congratulates","/kənˈɡrætʃəleɪts/"),
        v("decorate", "/ˈdɛkəreɪt/",   "decorar",              "decorated","/ˈdɛkəreɪtɪd/","decorated","/ˈdɛkəreɪtɪd/","decorating","/ˈdɛkəreɪtɪŋ/","decorates","/ˈdɛkəreɪts/"),
    ]},
    {"id": "promesas-confianza", "name": "Promesas y Confianza", "icon": "✠", "verbs": [
        v("bet",      "/bɛt/",         "apostar",              "bet",      "/bɛt/",        "bet",      "/bɛt/",        "betting",   "/ˈbɛtɪŋ/",     "bets",     "/bɛts/"),
        v("pledge",   "/plɛdʒ/",       "comprometerse",        "pledged",  "/plɛdʒd/",     "pledged",  "/plɛdʒd/",     "pledging",  "/ˈplɛdʒɪŋ/",   "pledges",  "/ˈplɛdʒɪz/"),
        v("commit",   "/kəˈmɪt/",      "comprometerse",        "committed","/kəˈmɪtɪd/",   "committed","/kəˈmɪtɪd/",   "committing","/kəˈmɪtɪŋ/",   "commits",  "/kəˈmɪts/"),
        v("vow",      "/vaʊ/",         "jurar / prometer",     "vowed",    "/vaʊd/",       "vowed",    "/vaʊd/",       "vowing",    "/ˈvaʊɪŋ/",     "vows",     "/vaʊz/"),
        v("betray",   "/bɪˈtreɪ/",     "traicionar",           "betrayed", "/bɪˈtreɪd/",   "betrayed", "/bɪˈtreɪd/",   "betraying", "/bɪˈtreɪɪŋ/",  "betrays",  "/bɪˈtreɪz/"),
        v("deceive",  "/dɪˈsiːv/",     "engañar",              "deceived", "/dɪˈsiːvd/",   "deceived", "/dɪˈsiːvd/",   "deceiving", "/dɪˈsiːvɪŋ/",  "deceives", "/dɪˈsiːvz/"),
        v("confide",  "/kənˈfaɪd/",    "confiar (un secreto)", "confided", "/kənˈfaɪdɪd/", "confided", "/kənˈfaɪdɪd/", "confiding", "/kənˈfaɪdɪŋ/", "confides", "/kənˈfaɪdz/"),
        v("rely",     "/rɪˈlaɪ/",      "depender / contar con","relied",   "/rɪˈlaɪd/",    "relied",   "/rɪˈlaɪd/",    "relying",   "/rɪˈlaɪɪŋ/",   "relies",   "/rɪˈlaɪz/"),
        v("depend",   "/dɪˈpɛnd/",     "depender",             "depended", "/dɪˈpɛndɪd/",  "depended", "/dɪˈpɛndɪd/",  "depending", "/dɪˈpɛndɪŋ/",  "depends",  "/dɪˈpɛndz/"),
        v("lie",      "/laɪ/",         "mentir",               "lied",     "/laɪd/",       "lied",     "/laɪd/",       "lying",     "/ˈlaɪɪŋ/",     "lies",     "/laɪz/"),
    ]},
    {"id": "fuerza-fisica", "name": "Acción de Fuerza", "icon": "✊", "verbs": [
        v("grab",     "/ɡræb/",        "agarrar",              "grabbed",  "/ɡræbd/",      "grabbed",  "/ɡræbd/",      "grabbing",  "/ˈɡræbɪŋ/",    "grabs",    "/ɡræbz/"),
        v("grip",     "/ɡrɪp/",        "sujetar firmemente",   "gripped",  "/ɡrɪpt/",      "gripped",  "/ɡrɪpt/",      "gripping",  "/ˈɡrɪpɪŋ/",    "grips",    "/ɡrɪps/"),
        v("squeeze",  "/skwiːz/",      "apretar / exprimir",   "squeezed", "/skwiːzd/",    "squeezed", "/skwiːzd/",    "squeezing", "/ˈskwiːzɪŋ/",  "squeezes", "/ˈskwiːzɪz/"),
        v("snatch",   "/snætʃ/",       "arrebatar",            "snatched", "/snætʃt/",     "snatched", "/snætʃt/",     "snatching", "/ˈsnætʃɪŋ/",   "snatches", "/ˈsnætʃɪz/"),
        v("smash",    "/smæʃ/",        "estrellar / romper",   "smashed",  "/smæʃt/",      "smashed",  "/smæʃt/",      "smashing",  "/ˈsmæʃɪŋ/",    "smashes",  "/ˈsmæʃɪz/"),
        v("crush",    "/krʌʃ/",        "aplastar",             "crushed",  "/krʌʃt/",      "crushed",  "/krʌʃt/",      "crushing",  "/ˈkrʌʃɪŋ/",    "crushes",  "/ˈkrʌʃɪz/"),
        v("slam",     "/slæm/",        "azotar / golpear",     "slammed",  "/slæmd/",      "slammed",  "/slæmd/",      "slamming",  "/ˈslæmɪŋ/",    "slams",    "/slæmz/"),
        v("wrestle",  "/ˈrɛsəl/",      "luchar (cuerpo)",      "wrestled", "/ˈrɛsəld/",    "wrestled", "/ˈrɛsəld/",    "wrestling", "/ˈrɛslɪŋ/",    "wrestles", "/ˈrɛsəlz/"),
    ]},
    {"id": "limpieza", "name": "Limpieza", "icon": "♨", "verbs": [
        v("rinse",    "/rɪns/",        "enjuagar",             "rinsed",   "/rɪnst/",      "rinsed",   "/rɪnst/",      "rinsing",   "/ˈrɪnsɪŋ/",    "rinses",   "/ˈrɪnsɪz/"),
        v("scrub",    "/skrʌb/",       "fregar",               "scrubbed", "/skrʌbd/",     "scrubbed", "/skrʌbd/",     "scrubbing", "/ˈskrʌbɪŋ/",   "scrubs",   "/skrʌbz/"),
        v("sweep",    "/swiːp/",       "barrer",               "swept",    "/swɛpt/",      "swept",    "/swɛpt/",      "sweeping",  "/ˈswiːpɪŋ/",   "sweeps",   "/swiːps/"),
        v("mop",      "/mɒp/",         "trapear",              "mopped",   "/mɒpt/",       "mopped",   "/mɒpt/",       "mopping",   "/ˈmɒpɪŋ/",     "mops",     "/mɒps/"),
        v("vacuum",   "/ˈvækjuːm/",    "aspirar",              "vacuumed", "/ˈvækjuːmd/",  "vacuumed", "/ˈvækjuːmd/",  "vacuuming", "/ˈvækjuːmɪŋ/", "vacuums",  "/ˈvækjuːmz/"),
        v("dust",     "/dʌst/",        "quitar el polvo",      "dusted",   "/ˈdʌstɪd/",    "dusted",   "/ˈdʌstɪd/",    "dusting",   "/ˈdʌstɪŋ/",    "dusts",    "/dʌsts/"),
        v("polish",   "/ˈpɒlɪʃ/",      "pulir / lustrar",      "polished", "/ˈpɒlɪʃt/",    "polished", "/ˈpɒlɪʃt/",    "polishing", "/ˈpɒlɪʃɪŋ/",   "polishes", "/ˈpɒlɪʃɪz/"),
        v("scour",    "/ˈskaʊər/",     "fregar enérgicamente", "scoured",  "/ˈskaʊərd/",   "scoured",  "/ˈskaʊərd/",   "scouring",  "/ˈskaʊərɪŋ/",  "scours",   "/ˈskaʊərz/"),
    ]},
    {"id": "ataque-defensa", "name": "Ataque y Defensa", "icon": "⚔", "verbs": [
        v("attack",   "/əˈtæk/",       "atacar",               "attacked", "/əˈtækt/",     "attacked", "/əˈtækt/",     "attacking", "/əˈtækɪŋ/",    "attacks",  "/əˈtæks/"),
        v("shoot",    "/ʃuːt/",        "disparar",             "shot",     "/ʃɒt/",        "shot",     "/ʃɒt/",        "shooting",  "/ˈʃuːtɪŋ/",    "shoots",   "/ʃuːts/"),
        v("stab",     "/stæb/",        "apuñalar",             "stabbed",  "/stæbd/",      "stabbed",  "/stæbd/",      "stabbing",  "/ˈstæbɪŋ/",    "stabs",    "/stæbz/"),
        v("dodge",    "/dɒdʒ/",        "esquivar",             "dodged",   "/dɒdʒd/",      "dodged",   "/dɒdʒd/",      "dodging",   "/ˈdɒdʒɪŋ/",    "dodges",   "/ˈdɒdʒɪz/"),
        v("block",    "/blɒk/",        "bloquear",             "blocked",  "/blɒkt/",      "blocked",  "/blɒkt/",      "blocking",  "/ˈblɒkɪŋ/",    "blocks",   "/blɒks/"),
        v("retreat",  "/rɪˈtriːt/",    "retirarse",            "retreated","/rɪˈtriːtɪd/", "retreated","/rɪˈtriːtɪd/", "retreating","/rɪˈtriːtɪŋ/", "retreats", "/rɪˈtriːts/"),
        v("ambush",   "/ˈæmbʊʃ/",      "emboscar",             "ambushed", "/ˈæmbʊʃt/",    "ambushed", "/ˈæmbʊʃt/",    "ambushing", "/ˈæmbʊʃɪŋ/",   "ambushes", "/ˈæmbʊʃɪz/"),
        v("surrender","/səˈrɛndər/",   "rendirse",             "surrendered","/səˈrɛndərd/","surrendered","/səˈrɛndərd/","surrendering","/səˈrɛndərɪŋ/","surrenders","/səˈrɛndərz/"),
    ]},
    {"id": "negociacion", "name": "Negociación y Acuerdo", "icon": "↔", "verbs": [
        v("persuade", "/pərˈsweɪd/",   "persuadir",            "persuaded","/pərˈsweɪdɪd/","persuaded","/pərˈsweɪdɪd/","persuading","/pərˈsweɪdɪŋ/","persuades","/pərˈsweɪdz/"),
        v("convince", "/kənˈvɪns/",    "convencer",            "convinced","/kənˈvɪnst/",  "convinced","/kənˈvɪnst/",  "convincing","/kənˈvɪnsɪŋ/", "convinces","/kənˈvɪnsɪz/"),
        v("accept",   "/əkˈsɛpt/",     "aceptar",              "accepted", "/əkˈsɛptɪd/",  "accepted", "/əkˈsɛptɪd/",  "accepting", "/əkˈsɛptɪŋ/",  "accepts",  "/əkˈsɛpts/"),
        v("reject",   "/rɪˈdʒɛkt/",    "rechazar",             "rejected", "/rɪˈdʒɛktɪd/", "rejected", "/rɪˈdʒɛktɪd/", "rejecting", "/rɪˈdʒɛktɪŋ/", "rejects",  "/rɪˈdʒɛkts/"),
        v("settle",   "/ˈsɛtəl/",      "resolver / asentarse", "settled",  "/ˈsɛtəld/",    "settled",  "/ˈsɛtəld/",    "settling",  "/ˈsɛtlɪŋ/",    "settles",  "/ˈsɛtəlz/"),
        v("compromise","/ˈkɒmprəmaɪz/","ceder / llegar a acuerdo","compromised","/ˈkɒmprəmaɪzd/","compromised","/ˈkɒmprəmaɪzd/","compromising","/ˈkɒmprəmaɪzɪŋ/","compromises","/ˈkɒmprəmaɪzɪz/"),
        v("demand",   "/dɪˈmænd/",     "exigir",               "demanded", "/dɪˈmændɪd/",  "demanded", "/dɪˈmændɪd/",  "demanding", "/dɪˈmændɪŋ/",  "demands",  "/dɪˈmændz/"),
        v("offer",    "/ˈɒfər/",       "ofrecer",              "offered",  "/ˈɒfərd/",     "offered",  "/ˈɒfərd/",     "offering",  "/ˈɒfərɪŋ/",    "offers",   "/ˈɒfərz/"),
    ]},
    {"id": "expresion-verbal", "name": "Expresión Verbal", "icon": "❝", "verbs": [
        v("criticize","/ˈkrɪtɪsaɪz/",  "criticar",             "criticized","/ˈkrɪtɪsaɪzd/","criticized","/ˈkrɪtɪsaɪzd/","criticizing","/ˈkrɪtɪsaɪzɪŋ/","criticizes","/ˈkrɪtɪsaɪzɪz/"),
        v("mock",     "/mɒk/",         "burlarse",             "mocked",   "/mɒkt/",       "mocked",   "/mɒkt/",       "mocking",   "/ˈmɒkɪŋ/",     "mocks",    "/mɒks/"),
        v("tease",    "/tiːz/",        "molestar / bromear",   "teased",   "/tiːzd/",      "teased",   "/tiːzd/",      "teasing",   "/ˈtiːzɪŋ/",    "teases",   "/ˈtiːzɪz/"),
        v("joke",     "/dʒoʊk/",       "bromear",              "joked",    "/dʒoʊkt/",     "joked",    "/dʒoʊkt/",     "joking",    "/ˈdʒoʊkɪŋ/",   "jokes",    "/dʒoʊks/"),
        v("complain", "/kəmˈpleɪn/",   "quejarse",             "complained","/kəmˈpleɪnd/", "complained","/kəmˈpleɪnd/","complaining","/kəmˈpleɪnɪŋ/","complains","/kəmˈpleɪnz/"),
        v("gossip",   "/ˈɡɒsɪp/",      "chismear",             "gossiped", "/ˈɡɒsɪpt/",    "gossiped", "/ˈɡɒsɪpt/",    "gossiping", "/ˈɡɒsɪpɪŋ/",   "gossips",  "/ˈɡɒsɪps/"),
        v("whisper",  "/ˈwɪspər/",     "susurrar",             "whispered","/ˈwɪspərd/",   "whispered","/ˈwɪspərd/",   "whispering","/ˈwɪspərɪŋ/", "whispers", "/ˈwɪspərz/"),
        v("shout",    "/ʃaʊt/",        "gritar",               "shouted",  "/ˈʃaʊtɪd/",    "shouted",  "/ˈʃaʊtɪd/",    "shouting",  "/ˈʃaʊtɪŋ/",    "shouts",   "/ʃaʊts/"),
        v("mumble",   "/ˈmʌmbəl/",     "murmurar",             "mumbled",  "/ˈmʌmbəld/",   "mumbled",  "/ˈmʌmbəld/",   "mumbling",  "/ˈmʌmblɪŋ/",   "mumbles",  "/ˈmʌmbəlz/"),
        v("stutter",  "/ˈstʌtər/",     "tartamudear",          "stuttered","/ˈstʌtərd/",   "stuttered","/ˈstʌtərd/",   "stuttering","/ˈstʌtərɪŋ/", "stutters", "/ˈstʌtərz/"),
    ]},
    {"id": "cuerpo-extra", "name": "Gestos Corporales", "icon": "✋", "verbs": [
        v("blink",    "/blɪŋk/",       "parpadear",            "blinked",  "/blɪŋkt/",     "blinked",  "/blɪŋkt/",     "blinking",  "/ˈblɪŋkɪŋ/",   "blinks",   "/blɪŋks/"),
        v("wink",     "/wɪŋk/",        "guiñar el ojo",        "winked",   "/wɪŋkt/",      "winked",   "/wɪŋkt/",      "winking",   "/ˈwɪŋkɪŋ/",    "winks",    "/wɪŋks/"),
        v("sniff",    "/snɪf/",        "olfatear",             "sniffed",  "/snɪft/",      "sniffed",  "/snɪft/",      "sniffing",  "/ˈsnɪfɪŋ/",    "sniffs",   "/snɪfs/"),
        v("scratch",  "/skrætʃ/",      "rascar",               "scratched","/skrætʃt/",    "scratched","/skrætʃt/",    "scratching","/ˈskrætʃɪŋ/", "scratches","/ˈskrætʃɪz/"),
        v("nod",      "/nɒd/",         "asentir con la cabeza","nodded",   "/ˈnɒdɪd/",     "nodded",   "/ˈnɒdɪd/",     "nodding",   "/ˈnɒdɪŋ/",     "nods",     "/nɒdz/"),
        v("shrug",    "/ʃrʌɡ/",        "encogerse de hombros", "shrugged", "/ʃrʌɡd/",      "shrugged", "/ʃrʌɡd/",      "shrugging", "/ˈʃrʌɡɪŋ/",    "shrugs",   "/ʃrʌɡz/"),
        v("stretch",  "/strɛtʃ/",      "estirar",              "stretched","/strɛtʃt/",    "stretched","/strɛtʃt/",    "stretching","/ˈstrɛtʃɪŋ/", "stretches","/ˈstrɛtʃɪz/"),
        v("exhale",   "/ɛksˈheɪl/",    "exhalar",              "exhaled",  "/ɛksˈheɪld/",  "exhaled",  "/ɛksˈheɪld/",  "exhaling",  "/ɛksˈheɪlɪŋ/", "exhales",  "/ɛksˈheɪlz/"),
    ]},
    {"id": "clima-natural", "name": "Fenómenos Naturales", "icon": "☂", "verbs": [
        v("drizzle",  "/ˈdrɪzəl/",     "lloviznar",            "drizzled", "/ˈdrɪzəld/",   "drizzled", "/ˈdrɪzəld/",   "drizzling", "/ˈdrɪzlɪŋ/",   "drizzles", "/ˈdrɪzəlz/"),
        v("hail",     "/heɪl/",        "granizar",             "hailed",   "/heɪld/",      "hailed",   "/heɪld/",      "hailing",   "/ˈheɪlɪŋ/",    "hails",    "/heɪlz/"),
        v("thunder",  "/ˈθʌndər/",     "tronar",               "thundered","/ˈθʌndərd/",   "thundered","/ˈθʌndərd/",   "thundering","/ˈθʌndərɪŋ/", "thunders", "/ˈθʌndərz/"),
        v("flood",    "/flʌd/",        "inundar",              "flooded",  "/ˈflʌdɪd/",    "flooded",  "/ˈflʌdɪd/",    "flooding",  "/ˈflʌdɪŋ/",    "floods",   "/flʌdz/"),
        v("drift",    "/drɪft/",       "ir a la deriva",       "drifted",  "/ˈdrɪftɪd/",   "drifted",  "/ˈdrɪftɪd/",   "drifting",  "/ˈdrɪftɪŋ/",   "drifts",   "/drɪfts/"),
        v("sprout",   "/spraʊt/",      "brotar",               "sprouted", "/ˈspraʊtɪd/",  "sprouted", "/ˈspraʊtɪd/",  "sprouting", "/ˈspraʊtɪŋ/",  "sprouts",  "/spraʊts/"),
        v("bloom",    "/bluːm/",       "florecer",             "bloomed",  "/bluːmd/",     "bloomed",  "/bluːmd/",     "blooming",  "/ˈbluːmɪŋ/",   "blooms",   "/bluːmz/"),
        v("wilt",     "/wɪlt/",        "marchitarse",          "wilted",   "/ˈwɪltɪd/",    "wilted",   "/ˈwɪltɪd/",    "wilting",   "/ˈwɪltɪŋ/",    "wilts",    "/wɪlts/"),
        v("hatch",    "/hætʃ/",        "eclosionar",           "hatched",  "/hætʃt/",      "hatched",  "/hætʃt/",      "hatching",  "/ˈhætʃɪŋ/",    "hatches",  "/ˈhætʃɪz/"),
        v("swarm",    "/swɔːrm/",      "enjambrar",            "swarmed",  "/swɔːrmd/",    "swarmed",  "/swɔːrmd/",    "swarming",  "/ˈswɔːrmɪŋ/",  "swarms",   "/swɔːrmz/"),
    ]},
]


# ----------------------------------------------------------------------------
# Build, validate, write
# ----------------------------------------------------------------------------

def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    existing_ids = {c["id"] for c in data["categories"]}

    new_categories = vol2 + vol3 + vol4 + vol5

    # Sanity: no duplicate category ids vs existing
    for cat in new_categories:
        if cat["id"] in existing_ids:
            raise SystemExit(f"Duplicate category id: {cat['id']}")

    # Sanity: each category 7..17 verbs
    for cat in new_categories:
        n = len(cat["verbs"])
        if not (7 <= n <= 17):
            raise SystemExit(f"Category {cat['id']} has {n} verbs (must be 7-17)")

    # Append, then check verb-level uniqueness across the whole corpus
    data["categories"].extend(new_categories)
    seen: dict[str, str] = {}
    for cat in data["categories"]:
        for verb in cat["verbs"]:
            key = verb["i"]
            if key in seen:
                raise SystemExit(f"Duplicate verb '{key}' in {cat['id']} (also in {seen[key]})")
            seen[key] = cat["id"]

    total = sum(len(c["verbs"]) for c in data["categories"])
    print(f"Total categories: {len(data['categories'])}")
    print(f"Total verbs:      {total}")

    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {DATA_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
